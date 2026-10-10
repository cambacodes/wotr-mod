"""J02 controller histories and exhaustive approved producer census."""
import copy
import hashlib
import json
from pathlib import Path
import unittest
from tests.structure import without_prose
from unittest.mock import patch

from tests.story_fixture import fresh_story
from tests.harem_row_walk import walk
from storylines.harem_rows import zz_contract_controller as controller
from storylines.harem_rows import s03a, s10, s20, s21, s29, s30
from tools import contract_j02_census, rrt_verify as rules, savecompat

ROOT = Path(__file__).resolve().parents[1]


class ContractJ02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)
        cls.data = controller.policy()

    def state(self, *flags):
        state = rules.SimState(5, 1000)
        state.flags.update(flags)
        state.crusade_resources = dict(Finances=10000, Materials=10000, Favors=10000)
        rules.sim_complete(self.model, state)
        return state

    def publish(self, scene_id, node_id, state, incident):
        node = next(n for n in self.model.by_id[scene_id]["Nodes"] if n["Id"] == node_id)
        available = [c for c in node["Choices"] if incident in c["Set"]
                     and rules.sim_choice_available(c, state)]
        answer, = available
        state.flags.update(answer["Set"])
        rules.sim_complete(self.model, state)
        return answer

    def test_manifest_accounts_for_exact_frozen_hook_identity(self):
        manifest = contract_j02_census.census(self.story)
        names = [row["hook"] for row in manifest["rows"]]
        self.assertEqual(sorted(names), sorted(self.data['hooks']))
        self.assertEqual(len(names), len(set(names)))
        self.assertTrue(all(row.get("reason") for row in manifest["rows"]
                            if row["status"] == "legitimately-inert"))
        breach = next(r for r in manifest["rows"] if r["hook"].endswith("boundary.breached"))
        self.assertEqual(breach["status"], "produced")
        self.assertTrue(all(t["scene"].endswith("debt_repayment") for t in breach["terminals"]))
        self.assertNotIn("foresight.page_taken", names)

    def test_first_final_failure_survives_later_failure_and_reconciliation(self):
        # The named faith refusal records Seelah's first target. A different
        # earlier target, even reconciled, makes it an incident-only terminal.
        sid = "household.pair.seelah_camellia.settle"
        incident = "household.pair.seelah_camellia.permanent_refusal"
        edge = "seelah.harem.enmity.camellia"
        state = self.state()
        self.publish(sid, "refused", state, incident)
        self.assertIn(edge, state.flags)
        self.assertIn("seelah.harem.stance.tolerated", state.flags)
        state = self.state("seelah.harem.enmity.areelu", "seelah.harem.reconciled.areelu")
        chosen = self.publish(sid, "refused", state, incident)
        self.assertNotIn(edge, state.flags)
        self.assertNotIn("seelah.harem.stance.tolerated", chosen["Set"])
        self.assertIn("seelah.harem.enmity.areelu", state.flags)

    def test_saved_first_failure_is_not_replaced_by_later_actual_arueshalae_failure(self):
        first = "arueshalae.harem.enmity.nocticula"
        state = self.state()
        # S08's current prototype has no final refusal publication; establish
        # its exact approved historical key as a saved earlier incident.
        state.flags.add(first)
        rules.sim_complete(self.model, state)
        sid = "household.pair.arueshalae_vellexia.retry.good"
        if sid not in self.model.by_id:
            sid = "household.pair.arueshalae_vellexia.retry"
        incident = "household.pair.arueshalae_vellexia.retry.failed"
        scene = self.model.by_id[sid]
        node = next(n for n in scene["Nodes"] if any(incident in c["Set"] for c in n["Choices"]))
        choice = self.publish(sid, node["Id"], state, incident)
        self.assertNotIn("arueshalae.harem.enmity.vellexia", choice["Set"])
        self.assertNotIn("arueshalae.harem.enmity.vellexia", state.flags)
        self.assertIn(incident, state.flags)
        # Its matching prior receipt does not release the historical slot.
        state.flags.add("arueshalae.harem.reconciled.nocticula")
        rules.sim_complete(self.model, state)
        self.assertIn("arueshalae.harem.enmity_any", state.flags)

    def test_failed_first_attempt_retry_success_and_abort_never_create_enmity(self):
        for prefix in ("household.pair.vellexia_shamira.",
                       "household.pair.arueshalae_minagho.",
                       "household.pair.arueshalae_vellexia."):
            state = self.state(prefix + "settle.failed")
            self.assertFalse(any(".harem.enmity." in f for f in state.flags))
            candidates = [s for s in self.model.scenes if s["Id"].startswith(prefix + "retry")]
            self.assertTrue(candidates)
            outcomes = walk(self, self.model, candidates[0], state)
            success = [s for s in outcomes if prefix + "retry.done" in s.flags
                       or prefix + "retry.kept" in s.flags]
            self.assertTrue(success)
            for done in success:
                rules.sim_complete(self.model, done)
                self.assertIn(prefix + "settle.failed", done.flags)
                self.assertFalse(any(".harem.enmity." in f for f in done.flags))
            aborts = [s for s in outcomes if prefix + "retry.seen" not in s.flags]
            self.assertTrue(aborts)
            for aborted in aborts:
                self.assertFalse(aborted.rest_spent)
                self.assertFalse(any(".harem.enmity." in f for f in aborted.flags))

    def claimant_rows(self):
        # Every emitted wrapper shares its row's exact final input.
        for pair, incident, edge, claimant in (
            ("kaylessa_camellia", "exposure_unsettled",
             "kaylessa.harem.enmity.camellia", "kaylessa"),
            ("kaylessa_anevia", "trail_unsettled",
             "kaylessa.harem.enmity.w.anevia", "kaylessa"),
            ("shamira_arueshalae", "claim.unsettled",
             "arueshalae.harem.enmity.shamira", "arueshalae"),
        ):
            prefix = "household.pair." + pair + "."
            for scene in self.model.scenes:
                if scene["Id"].startswith(prefix + "settle"):
                    suffix = scene["Id"][len(prefix + "settle"):]
                    yield prefix, scene, self.model.by_id[prefix + "retry" + suffix], prefix + incident, edge, claimant

    def test_claimant_addendum_covers_every_wrapper_and_exact_terminal(self):
        rows = list(self.claimant_rows())
        self.assertEqual({settle["Id"] for _, settle, _, _, _, _ in rows}, {
            "household.pair.kaylessa_camellia.settle",
            "household.pair.kaylessa_anevia.settle.pair",
            "household.pair.kaylessa_anevia.settle.solo",
            "household.pair.shamira_arueshalae.settle.good",
            "household.pair.shamira_arueshalae.settle.evil",
        })
        for prefix, _, _, incident, edge, claimant in rows:
            rule = next(r for r in self.data["failures"] if r["prefix"] == prefix)
            self.assertEqual(rule["terminal"], [incident])
            self.assertEqual(rule["enmity"], edge)
            self.assertEqual(rule["stance"], claimant + ".harem.stance.tolerated")
        for row in ("S42", "S43", "S44"):
            disposition = next(d for d in self.data["dispositions"] if d["rows"] == row)
            self.assertEqual(disposition["status"], "supported")

    def test_claimant_failed_first_attempt_then_success_or_abort_has_no_enmity(self):
        for prefix, settle, retry, incident, edge, claimant in self.claimant_rows():
            with self.subTest(scene=settle["Id"]):
                first = walk(self, self.model, settle, self.state())
                pending = [s for s in first if prefix + "settle.failed" in s.flags]
                self.assertTrue(pending)
                for failed in pending:
                    rules.sim_complete(self.model, failed)
                    self.assertNotIn(incident, failed.flags)
                    self.assertFalse(any(".harem.enmity." in f for f in failed.flags))
                    outcomes = walk(self, self.model, retry, failed)
                    successes = [s for s in outcomes if prefix + "retry.done" in s.flags]
                    aborts = [s for s in outcomes if prefix + "retry.seen" not in s.flags]
                    self.assertTrue(successes)
                    self.assertTrue(aborts)
                    for done in successes + aborts:
                        rules.sim_complete(self.model, done)
                        self.assertIn(prefix + "settle.failed", done.flags)
                        self.assertNotIn(incident, done.flags)
                        self.assertNotIn(claimant + ".harem.stance.tolerated", done.flags)
                        self.assertFalse(any(".harem.enmity." in f for f in done.flags))
                    for aborted in aborts:
                        self.assertEqual(aborted.rest_spent, failed.rest_spent)

    def test_claimant_final_refusal_publishes_only_approved_woman_edge(self):
        for prefix, settle, retry, incident, edge, claimant in self.claimant_rows():
            first = walk(self, self.model, settle, self.state())
            pending = next(s for s in first if prefix + "settle.failed" in s.flags)
            rules.sim_complete(self.model, pending)
            for scene, incoming in ((settle, self.state()), (retry, pending)):
                with self.subTest(scene=scene["Id"]):
                    finals = [s for s in walk(self, self.model, scene, incoming)
                              if incident in s.flags]
                    self.assertTrue(finals)
                    for final in finals:
                        rules.sim_complete(self.model, final)
                        self.assertEqual({f for f in final.flags if ".harem.enmity." in f}, {edge})
                        self.assertIn(claimant + ".harem.stance.tolerated", final.flags)
                        self.assertIn(controller.owner(edge), final.flags)
                        self.assertNotIn("household.controller.anevia.enmity_any", final.flags)
                        self.assertNotIn("household.controller.irabeth.enmity_any", final.flags)

    def test_claimant_first_target_survives_final_refusal_even_after_receipt(self):
        for prefix, settle, retry, incident, edge, claimant in self.claimant_rows():
            old = ("kaylessa.harem.enmity.w.anevia"
                   if edge == "kaylessa.harem.enmity.camellia"
                   else "kaylessa.harem.enmity.camellia"
                   if claimant == "kaylessa"
                   else "arueshalae.harem.enmity.nocticula")
            for reconciled in (False, True):
                for scene in (settle, retry):
                    with self.subTest(scene=scene["Id"], reconciled=reconciled):
                        state = self.state(old, prefix + "settle.failed",
                                           *([controller._receipt(old)] if reconciled else []))
                        finals = [s for s in walk(self, self.model, scene, state)
                                  if incident in s.flags]
                        self.assertTrue(finals)
                        for final in finals:
                            rules.sim_complete(self.model, final)
                            self.assertEqual({f for f in final.flags if ".harem.enmity." in f}, {old})
                            self.assertNotIn(claimant + ".harem.stance.tolerated", final.flags)

    def test_qualified_minagho_failure_does_not_infect_chivarro(self):
        prefix = "household.pair.arueshalae_minagho."
        scene = next(s for s in self.model.scenes if s["Id"].startswith(prefix + "retry"))
        incident = prefix + "retry.failed"
        node = next(n for n in scene["Nodes"] if any(incident in c["Set"] for c in n["Choices"]))
        state = self.state()
        self.publish(scene["Id"], node["Id"], state, incident)
        self.assertIn("minagho_chivarro.harem.enmity.minagho.arueshalae", state.flags)
        self.assertIn("minagho_chivarro.harem.stance.minagho.tolerated", state.flags)
        for alias in self.data["aliases"]:
            self.assertNotIn(alias, state.flags)
        self.assertFalse(any("enmity.chivarro." in f for f in state.flags))
        pair = self.state("tirabade.harem.enmity.anevia.kaylessa")
        solo = self.state("anevia.harem.enmity.kaylessa")
        for state in (pair, solo):
            self.assertIn("household.controller.anevia.enmity_any", state.flags)
            self.assertNotIn("household.controller.irabeth.enmity_any", state.flags)

    def test_alliance_stages_need_every_actual_deed_and_cost_and_have_no_lovers(self):
        for row, pair, receipts in (
            (s10, ("seelah", "nenio"), s10.ANSWERED[1:]),
            (s21, s21.PAIR, s21.KEPT[1:]),
            (s29, s29.PAIR, s29.HELPED[1:]),
            (s30, ("eliandra", "targona"), s30.ANSWERED[1:]),
        ):
            for a, b in (pair, pair[::-1]):
                key = a + ".harem.attitude." + b + ".friend"
                self.assertIn(key, self.state(*receipts).flags)
                for missing in receipts:
                    self.assertNotIn(key, self.state(*(f for f in receipts if f != missing)).flags)
                for stage in ("rival", "respect", "lover"):
                    self.assertNotIn(a + ".harem.attitude." + b + "." + stage, self.story["Derived"])
                self.assertNotIn(key, self.state(*receipts, a + ".harem.enmity." + b).flags)
            prefix = row.PREFIX if hasattr(row, "PREFIX") else row.P
            for scene in self.model.scenes:
                if scene["Id"].startswith(prefix):
                    self.assertFalse(any(".harem.attitude." in f for f in scene["Requires"]))
                    self.assertIn("foresight.page_taken", scene["Requires"])
                    self.assertIn("household.table.kept", scene["Requires"])

    def test_jannah_offer_postponement_and_unknown_are_not_her_actual_answer(self):
        for outcome in s20.OUTCOMES:
            state = self.state(s20.ACCOUNT, outcome)
            self.assertEqual("seelah.harem.attitude.jannah.friend" in state.flags,
                             outcome.endswith(".herself"))

    def test_fall_selects_current_directional_stage_without_erasing_earned_history(self):
        key = "seelah.harem.attitude.arueshalae.lover"
        love = self.story["Derived"][key][1]
        native = "arueshalae.recruited_drezen"
        self.assertIn(key, self.state(*love, native).flags)
        for missing in love:
            proof = [] if missing == "arueshalae.redeemed" else [native]
            self.assertNotIn(key, self.state(*(f for f in love if f != missing), *proof).flags)
        respect = "seelah.harem.attitude.arueshalae.respect"
        hearing = self.story["Derived"][respect][0]
        state = self.state(*love, *hearing, native, "arueshalae.fallen",
                           "household.pair.seelah_arueshalae.fallen.settle.seen")
        self.assertNotIn(key, state.flags)
        self.assertNotIn("seelah.harem.attitude.arueshalae.friend", state.flags)
        self.assertIn(respect, state.flags)
        self.assertNotIn("seelah.harem.attitude.arueshalae.rival", state.flags)
        self.assertIn("arueshalae.harem.attitude.seelah.rival", state.flags)
        self.assertNotIn("arueshalae.harem.attitude.seelah.respect", state.flags)
        self.assertTrue(set(love) <= state.flags)

    def test_s36_receipt_needs_exact_old_target_and_full_replacement_not_pending_failure(self):
        receipt = "hepzamirah.harem.reconciled.melazmera"
        inputs = self.story["Derived"][receipt][0]
        self.assertIn(receipt, self.state(*inputs).flags)
        for missing in inputs:
            self.assertNotIn(receipt, self.state(*(f for f in inputs if f != missing)).flags)
        pending = self.state("household.pair.melazmera_hepzamirah.diversion.failed")
        self.assertNotIn("hepzamirah.harem.enmity.melazmera", pending.flags)
        self.assertEqual([receipt], [f for f in self.data["hooks"] if ".reconciled." in f
                                    and f in self.story["Derived"]])

    def test_no_clock_allocation_or_text_rewrite_and_registration_is_idempotent(self):
        self.assertEqual(savecompat.check(self.story), [])
        before = copy.deepcopy(self.story)
        controller.register(before, before["Scenes"], before["Etudes"])
        self.assertEqual(without_prose(before), without_prose(self.story), "Controller registration must be idempotent")
        for key in self.story["Derived"]:
            if ".harem.attitude." in key:
                self.assertNotIn(key, self.story.get("Latches", {}))

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        from contextlib import ExitStack
        with ExitStack() as changes:
            for scene in self.story['Scenes']:
                for node in scene['Nodes']:
                    for choice in node['Choices']:
                        if any(f.endswith('boundary.breached') for f in choice['Set']):
                            changes.enter_context(patch.dict(choice, Set=[f for f in choice['Set'] if not f.endswith('boundary.breached')]))
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_manifest_accounts_for_exact_frozen_hook_identity()


if __name__ == "__main__":
    unittest.main()
