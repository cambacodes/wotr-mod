"""eng7-l13: mutation coverage for earned history and assembled rewards."""
import copy
import unittest
from tests.structure import without_prose
from unittest.mock import patch

from expansion import make_expansion
from storylines import earned_outcomes
from tools.crossroute_checks import late_commitment
from tools.crossroute_checks.common import Proof, blocks, verify
from tools.lastcall_entitlement_lint import errors as entitlement_errors


def findings(payload):
    model = verify.Model(copy.deepcopy(payload))
    return late_commitment.check(model, list(blocks(model)), Proof(model))



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class EarnedOutcomeGeneratorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        integrate = earned_outcomes.integrate

        def capture(payload, **options):
            # Observe this pass at its real assembly seam. Later appenders need
            # the ending nodes it supplies, so disabling it breaks the build.
            cls.before = copy.deepcopy(payload)
            integrate(payload, **options)

        with patch.object(earned_outcomes, "integrate", side_effect=capture) as observed:
            cls.after = make_expansion()
        if observed.call_count != 1:
            raise AssertionError("Expected one earned-outcome integration pass")

    def test_generator_does_not_mutate_shared_authoring_constants(self):
        # A shallow export may share every nested dictionary with its author.
        source = copy.deepcopy(self.before)
        shallow_export = dict(source)
        earned_outcomes.integrate(shallow_export)
        self.assertEqual(without_prose(source), without_prose(self.before))

    def test_every_reward_has_live_proof(self):
        self.assertEqual(findings(self.after), [])

    def test_non_romance_page_receipt_keeps_its_paid_terminal(self):
        scene = next(s for s in self.after['Scenes'] if s['Id'] == 'trickster.foresight.page')
        gate = next(n for n in scene['Nodes'] if n['Id'] == 'g_gate')
        self.assertEqual([(c['Set'], c['Abort'], c['Next']) for c in gate['Choices']],
                         [(['trickster.foresight.gate_fire'], False, None)])

    def test_framework_exception_cannot_hide_a_romantic_producer(self):
        payload = copy.deepcopy(self.before)
        scene = next(s for s in payload["Scenes"] if s["Id"] == "trickster.foresight.page")
        gate = next(n for n in scene["Nodes"] if n["Id"] == "g_gate")
        saved_answer(gate["Choices"], 0)["Set"].append("trickster.foresight.first_night")
        # Give the framework a real closure producer before the new reward.
        # Its shipped closed key has no producer, so clearing entry conditions
        # alone would still correctly prove that an ordinary run cannot close it.
        saved_answer(scene["Nodes"][0]["Choices"], 0)["Set"].append("trickster.foresight.closed")
        self.assertTrue(any(f["scene"] == scene["Id"] for f in findings(payload)))

    def test_raw_terms_need_acceptance_and_late_refusal_revokes_it(self):
        model = verify.Model(copy.deepcopy(self.after))
        state = verify.SimState(6, 1000)
        state.flags.update({"chapter_later", "trickster", "trickster.ever",
                            "dorgelinda.trickster.methods_heard"})
        verify.sim_complete(model, state)
        self.assertNotIn("dorgelinda.trickster.late_committed", state.flags)
        state.flags.add("dorgelinda.committed")
        verify.sim_complete(model, state)
        self.assertIn("dorgelinda.trickster.late_committed", state.flags)
        state.flags.add("dorgelinda.trickster.declined")
        verify.sim_complete(model, state)
        self.assertNotIn("dorgelinda.trickster.late_committed", state.flags)

    def test_existing_late_refusal_override_remains_an_earned_road(self):
        model = verify.Model(copy.deepcopy(self.after))
        for courted in (False, True):
            with self.subTest(courted=courted):
                state = verify.SimState(6, 1000)
                state.flags.update({"chapter_later", "trickster", "trickster.ever",
                                    "chadali.started", "chadali.trickster.declined"})
                if courted:
                    state.flags.add("chadali.trickster.courted")
                verify.sim_complete(model, state)
                self.assertNotIn("chadali.trickster.late_committed", state.flags)
                state.flags.add("council.debrief_motion")
                verify.sim_complete(model, state)
                self.assertIn("chadali.trickster.hall_sealed", state.flags)
                self.assertEqual(courted, "chadali.trickster.late_committed" in state.flags)
                if not courted:
                    state.flags.add("chadali.trickster.courted")
                    verify.sim_complete(model, state)
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
        choice = saved_answer(next(n for n in scene["Nodes"] if n["Id"] == "torches")["Choices"], 0)
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
            self.assertIn("mielarah.trickster.cost.meant", saved_answer(node["Choices"], 0)["Set"])

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

    def test_historical_prose_exemption_cannot_hide_a_new_producer(self):
        payload = copy.deepcopy(self.before)
        scene = next(s for s in payload["Scenes"] if s["Id"] == "noct.ending_death")
        saved_answer(scene["Nodes"][0]["Choices"], 0)["Set"].append(payload["Relationships"]["nocticula"]["CommittedFlag"])
        self.assertTrue(any(f["scene"] == scene["Id"] and f["slot"] == "choice[0]" for f in findings(payload)))

    def test_earned_return_and_ordinary_path_remain_valid(self):
        model = verify.Model(copy.deepcopy(self.after))
        state = verify.SimState(6, 1000)
        state.flags.update({"chapter_later", "chapter.six", "trickster", "trickster.ever",
                            "devarra.trickster.tested"})
        verify.sim_complete(model, state)
        self.assertNotIn("devarra.trickster.late_committed", state.flags)
        state.flags.add("devarra.trickster.late_accepted")
        verify.sim_complete(model, state)
        self.assertNotIn("devarra.trickster.late_committed", state.flags)
        state.flags.add("devarra.committed")
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

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        scene = next(s for s in self.after['Scenes'] if s['Id'] == 'trickster.foresight.page')
        choice = next(n for n in scene['Nodes'] if n['Id'] == 'g_gate')['Choices'][0]
        with patch.dict(choice, Set=[]):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_non_romance_page_receipt_keeps_its_paid_terminal()


if __name__ == "__main__":
    unittest.main()
