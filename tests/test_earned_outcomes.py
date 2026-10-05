"""eng7-l13: mutation and save-shape coverage for the final generator pass."""
import copy
import unittest
from unittest.mock import patch

from expansion import make_expansion
from storylines import earned_outcomes
from tools.crossroute_checks import late_commitment
from tools.crossroute_checks.common import Proof, blocks, verify
from tools.lastcall_entitlement_lint import errors as entitlement_errors


def findings(payload):
    model = verify.Model(copy.deepcopy(payload))
    return late_commitment.check(model, list(blocks(model)), Proof(model))


class EarnedOutcomeGeneratorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch.object(earned_outcomes, "integrate"):
            cls.before = make_expansion()
        cls.after = copy.deepcopy(cls.before)
        earned_outcomes.integrate(cls.after)

    def test_generator_does_not_mutate_shared_authoring_constants(self):
        # A shallow export may share every nested dictionary with its author.
        source = copy.deepcopy(self.before)
        shallow_export = dict(source)
        earned_outcomes.integrate(shallow_export)
        self.assertEqual(source, self.before)

    def test_every_reward_has_live_proof(self):
        self.assertGreater(len(findings(self.before)), 1000)
        self.assertEqual(findings(self.after), [])

    def test_non_romance_page_receipt_keeps_its_paid_terminal(self):
        scene = next(s for s in self.after["Scenes"] if s["Id"] == "trickster.foresight.page")
        gate = next(n for n in scene["Nodes"] if n["Id"] == "g_gate")
        self.assertEqual(len(gate["Choices"]), 1)
        self.assertEqual(gate["Choices"][0]["Set"], ["trickster.foresight.gate_fire"])
        self.assertFalse(gate["Choices"][0]["Abort"])

    def test_framework_exception_cannot_hide_a_romantic_producer(self):
        payload = copy.deepcopy(self.before)
        scene = next(s for s in payload["Scenes"] if s["Id"] == "trickster.foresight.page")
        gate = next(n for n in scene["Nodes"] if n["Id"] == "g_gate")
        gate["Choices"][0]["Set"].append("trickster.foresight.first_night")
        # Give the framework a real closure producer before the new reward.
        # Its shipped closed key has no producer, so clearing entry conditions
        # alone would still correctly prove that an ordinary run cannot close it.
        scene["Nodes"][0]["Choices"][0]["Set"].append("trickster.foresight.closed")
        self.assertTrue(any(f["scene"] == scene["Id"] for f in findings(payload)))

    def test_scene_nodes_answers_and_targets_preserved(self):
        self.assertEqual(list(self.before["Relationships"]), list(self.after["Relationships"]))
        self.assertEqual([s["Id"] for s in self.before["Scenes"]], [s["Id"] for s in self.after["Scenes"]])
        for old, new in zip(self.before["Scenes"], self.after["Scenes"]):
            self.assertEqual([n["Id"] for n in old["Nodes"]], [n["Id"] for n in new["Nodes"]])
            for a, b in zip(old["Nodes"], new["Nodes"]):
                self.assertEqual(a["Text"], b["Text"])
                self.assertGreaterEqual(len(b["Choices"]), len(a["Choices"]))
                for previous, current in zip(a["Choices"], b["Choices"]):
                    for field in ("Text", "Next", "Check", "Abort", "NativeNext", "Revive"):
                        self.assertEqual(previous.get(field), current.get(field), (old["Id"], a["Id"], field))

    def test_raw_terms_late_pages_also_supply_their_existing_refusal(self):
        model = verify.Model(copy.deepcopy(self.after))
        state = verify.SimState(6, 1000)
        state.flags.update({"chapter_later", "trickster", "dorgelinda.trickster.methods_heard"})
        verify.sim_complete(model, state)
        self.assertIn("dorgelinda.trickster.late_committed", state.flags)
        state.flags.add("dorgelinda.trickster.declined")
        verify.sim_complete(model, state)
        self.assertNotIn("dorgelinda.trickster.late_committed", state.flags)
        self.assertNotIn("dorgelinda.harem.eligible", state.flags)

    def test_existing_late_refusal_override_remains_an_earned_road(self):
        model = verify.Model(copy.deepcopy(self.after))
        state = verify.SimState(6, 1000)
        state.flags.update({"chapter_later", "trickster", "chadali.started", "chadali.trickster.declined"})
        verify.sim_complete(model, state)
        self.assertNotIn("chadali.trickster.late_committed", state.flags)
        state.flags.add("council.debrief_motion")
        verify.sim_complete(model, state)
        self.assertIn("chadali.trickster.hall_sealed", state.flags)
        self.assertIn("chadali.trickster.late_committed", state.flags)

    def test_late_producer_mutation_fails_even_with_guarded_pages(self):
        payload = copy.deepcopy(self.after)
        key = "devarra.trickster.late_committed"
        payload["Derived"][key][0].remove("devarra.outcome.route_open")
        self.assertTrue(any(f["route"] == "devarra" and f["subject"] == "late-entitlement"
                            for f in findings(payload)))

    def test_removing_live_path_guard_reopens_the_reported_defect(self):
        payload = copy.deepcopy(self.after)
        scene = next(s for s in payload["Scenes"] if s["Id"] == "iomedae.trickster.disputation")
        choice = next(n for n in scene["Nodes"] if n["Id"] == "torches")["Choices"][0]
        # Earlier lanes may already prove current power at scene entry.
        self.assertTrue("trickster.now" in scene["Requires"] or "trickster.now" in choice["Requires"])
        scene["Requires"] = [k for k in scene["Requires"] if k != "trickster.now"]
        choice["Requires"] = [k for k in choice["Requires"] if k != "trickster.now"]
        self.assertTrue(any(f["scene"] == scene["Id"] and f["subject"] == "current-path" for f in findings(payload)))

    def test_removing_mandatory_response_guard_is_detected(self):
        payload = copy.deepcopy(self.after)
        for scene in payload["Scenes"]:
            if scene["Id"] == "jannah.circle.your_part":
                for node in scene["Nodes"]:
                    for choice in node["Choices"]:
                        if choice.get("Next") == "not_you_want":
                            choice["Requires"].remove("jannah.outcome.eligible")
        self.assertTrue(any(f["scene"] == "jannah.circle.your_part" and f["subject"] == "refusal/control" for f in findings(payload)))

    def test_mielarah_discovery_records_existing_consequence_in_both_markets(self):
        for sid in ("mielarah.deck.market", "mielarah.deck.market.arcade"):
            scene = next(s for s in self.after["Scenes"] if s["Id"] == sid)
            node = next(n for n in scene["Nodes"] if n["Id"] == "worked_out")
            self.assertIn("mielarah.trickster.cost.meant", node["Choices"][0]["Set"])

    def test_lastcall_parity_and_mutation(self):
        self.assertEqual(entitlement_errors(self.after), [])
        payload = copy.deepcopy(self.after)
        payload["Derived"]["nenio.lastcall.callable"][0][0] = "nenio.trickster.cost.name_filed"
        self.assertTrue(any("nenio.lastcall.callable" in error for error in entitlement_errors(payload)))

    def test_lastcall_rewrite_preserves_unconditional_and_staked_paragraphs(self):
        payload = copy.deepcopy(self.before)
        page = next(s for s in payload["Scenes"] if s["Id"] == "nenio.lastcall.page")
        paragraphs = page["Nodes"][0]["Paragraphs"]
        plain = {"Text": "{n}The morning wind turns the page.{/n}"}
        stake = {"Text": "{n}The paid name is still gone.{/n}",
                 "Requires": ["nenio.trickster.cost.name_filed"]}
        paragraphs.extend([plain, stake])
        earned_outcomes.normalize_lastcall(payload, lambda route: route + ".outcome.route_open")
        self.assertEqual(plain["Requires"], [])
        self.assertEqual(stake["Requires"], ["nenio.trickster.name_gone"])
        self.assertEqual(entitlement_errors(payload), [])

    def test_historical_prose_exemption_cannot_hide_a_new_producer(self):
        payload = copy.deepcopy(self.before)
        scene = next(s for s in payload["Scenes"] if s["Id"] == "noct.ending_death")
        scene["Nodes"][0]["Choices"][0]["Set"].append(payload["Relationships"]["nocticula"]["CommittedFlag"])
        self.assertTrue(any(f["scene"] == scene["Id"] and f["slot"] == "choice[0]" for f in findings(payload)))

    def test_earned_return_and_ordinary_path_remain_valid(self):
        model = verify.Model(copy.deepcopy(self.after))
        state = verify.SimState(5, 1000)
        state.flags.update({"chapter_later", "trickster", "trickster.ever", "devarra.trickster.tested"})
        verify.sim_complete(model, state)
        self.assertIn("devarra.trickster.late_committed", state.flags)
        # Main.State supplies the built-in inhuman aggregate from native Swarm.
        state.flags.update({"swarm", "inhuman"})
        verify.sim_complete(model, state)
        self.assertNotIn("devarra.trickster.late_committed", state.flags)
        state.flags.difference_update({"swarm", "inhuman"})
        state.flags.update({"devarra.dead_lair", "devarra.trickster.returned"})
        verify.sim_complete(model, state)
        self.assertIn("devarra.trickster.late_committed", state.flags)
        state.flags = {"chapter_later", "arsinoe.committed", "arsinoe.romance_kept"}
        verify.sim_complete(model, state)
        self.assertIn("arsinoe.outcome.route_open", state.flags)


if __name__ == "__main__":
    unittest.main()
