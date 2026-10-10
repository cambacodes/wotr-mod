"""Mutation proofs for the stale outcome and loan contracts repaired by test-rot."""
import copy
import json
import unittest

from story_format import c, n, scene
from tools.crossroute_checks import late_commitment
from tools.crossroute_checks.common import Proof, blocks, verify
from tools.lastcall_entitlement_lint import CONTRACTS, history_errors


class TestRotContractTests(unittest.TestCase):
    def test_refusal_exemption_never_exempts_a_commitment_producer(self):
        for route, sid, nid in (
            ("kiana", "kiana.trickster.epilogue.commit", "partner_resolved_refuse"),
            ("kiana", "kiana.trickster.epilogue.commit", "partner_resolved_stop"),
            ("herrax", "herrax.trickster.epilogue.after_hours.invitation", "declined"),
        ):
            with self.subTest(scene=sid, node=nid):
                payload = dict(
                    Scenes=[scene(sid, "Refusal", "Epilogue", 6, "", [
                        n(nid, "Narrator", "The invitation was refused.", c())
                    ], requires=(route + ".trickster.late_committed",), Relationship=route)],
                    Relationships={route: dict(StartedFlag=route + ".started", ClosedFlag=route + ".closed",
                                               CommittedFlag=route + ".committed")})

                def findings(data):
                    model = verify.Model(data)
                    return late_commitment.check(model, list(blocks(model)), Proof(model))

                # The separate acceptance graph is omitted here. Inspect the
                # reward verdict at the repaired scene/node address.
                self.assertFalse(any(diagnostics["subject"] == route for diagnostics in findings(payload)))
                mutant = copy.deepcopy(payload)
                mutant["Scenes"][0]["Nodes"][0]["Choices"][0]["Set"] = [route + ".committed"]
                self.assertTrue(any(diagnostics["subject"] == route for diagnostics in findings(mutant)))

    def test_collecting_a_wager_cannot_settle_the_separate_luck_loan(self):
        contracts = json.loads(CONTRACTS.read_text(encoding="utf-8"))
        key = "chadali.lastcall.luck_due"
        loan_contract = {"surfaces": [], "derived_forbids": {key: contracts["derived_forbids"][key]}}
        control = dict(Scenes=[], DerivedForbids={key: ["chadali.fortunes.loan_returned"]})
        self.assertEqual([], history_errors(control, loan_contract))
        for exclusions in ([], ["chadali.fortunes.loan_returned", "chadali.wagers.luck_lost"]):
            with self.subTest(exclusions=exclusions):
                mutant = dict(Scenes=[], DerivedForbids={key: exclusions})
                self.assertTrue(any(key in error for error in history_errors(mutant, loan_contract)))


if __name__ == "__main__":
    unittest.main()
