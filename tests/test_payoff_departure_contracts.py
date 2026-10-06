"""Eng3-ab contract mutations against the generated export (no extra export)."""
import copy
import json
from pathlib import Path
import unittest

from tools import departure_lint, payoff_lint

ROOT = Path(__file__).resolve().parents[1]


class ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from tests.story_fixture import fresh_story
        cls.story = fresh_story()

    def test_stance_receipt_cannot_be_dropped_from_ending_or_last_call(self):
        for fragment in ("epilogue", "lastcall.page"):
            story = copy.deepcopy(self.story)
            contract, surface = next((c, s) for c in payoff_lint.contracts()["stance_guards"]
                                     for s in c["surfaces"] if fragment in s[0]
                                     and any("exclusive_chosen" in k for k in c["requires"]))
            sid, nid, index = surface
            node = next(n for s in story["Scenes"] if s["Id"] == sid for n in s["Nodes"] if n["Id"] == nid)
            node["Paragraphs"][index]["Requires"].remove(next(k for k in contract["requires"] if "exclusive_chosen" in k))
            self.assertTrue(any(sid in error and "stance" in error for error in payoff_lint.check(story)))

    def test_new_stance_paragraph_cannot_bypass_inventory(self):
        story = copy.deepcopy(self.story)
        scene = next(s for s in story["Scenes"] if s["Id"] == "soana.lastcall.page")
        scene["Nodes"][0].setdefault("Paragraphs", []).append({
            "Text": "Unclassified", "Requires": ["soana.partner.exclusive_chosen"]})
        self.assertTrue(any("unclassified stance payoff" in error for error in payoff_lint.check(story)))

    def test_mixed_ordinary_late_paragraph_keeps_earned_alternatives(self):
        story = copy.deepcopy(self.story)
        scene = next(s for s in story["Scenes"] if s["Id"] == "areelu.trickster.finale.prior_lien")
        paragraph = scene["Nodes"][0]["Paragraphs"][0]
        group = ["areelu.payoff.ordinary", "areelu.trickster.late_committed"]
        self.assertIn(group, paragraph["AnyGroups"])
        paragraph["AnyGroups"].remove(group)
        self.assertTrue(any(scene["Id"] in error for error in payoff_lint.check(story)))

    def test_integrated_acceptance_effects_cannot_disappear(self):
        story = copy.deepcopy(self.story)
        producer = next(p for p in payoff_lint.contracts()["routes"]["soana"]["producers"] if "effects" in p)
        node = next(n for s in story["Scenes"] if s["Id"] == producer["scene"]
                    for n in s["Nodes"] if n["Id"] == producer["node"])
        node["Choices"][producer["choice"]]["Set"] = []
        self.assertTrue(any("altered integrated acceptance receipts" in error for error in payoff_lint.check(story)))

    def test_mixed_refusal_page_gates_only_the_romantic_choices(self):
        story = copy.deepcopy(self.story)
        scene = next(s for s in story["Scenes"] if s["Id"] == "arsinoe.trickster.late.commit")
        self.assertNotIn("arsinoe.trickster.late_committed", scene["Requires"])
        choices = scene["Nodes"][0]["Choices"]
        self.assertIn("arsinoe.trickster.late_committed", choices[0]["Requires"])
        self.assertIn("arsinoe.trickster.late_committed", choices[1]["Requires"])
        self.assertEqual(["arsinoe.trickster.late_declined"], choices[2]["Requires"])
        choices[0]["Requires"].remove("arsinoe.trickster.late_committed")
        self.assertTrue(any(scene["Id"] in error for error in payoff_lint.check(story)))

    def test_inventory(self):
        self.assertEqual([], departure_lint.check(self.story))
        self.assertEqual([], payoff_lint.check(self.story))

    def test_native_selector_cannot_drop_final_replacement_gates(self):
        story = copy.deepcopy(self.story)
        target, spec = next((key, spec) for key, spec in story["NativeEpilogueEdits"].items()
                            if any(".payoff." in key for key in spec["When"][0]))
        spec["When"][0] = [key for key in spec["When"][0]
                            if ".payoff." not in key and not key.endswith(".present_now")]
        self.assertTrue(any(target in error for error in payoff_lint.check(story)))
        self.assertTrue(any(target in error for error in departure_lint.check(story)))

    def test_earlier_yes_does_not_override_later_future_terms(self):
        story = copy.deepcopy(self.story)
        story["DerivedForbids"]["arsinoe.trickster.late_committed"].remove("arsinoe.future_spoken")
        self.assertTrue(any("future_spoken" in e for e in payoff_lint.check(story)))

    def test_each_womans_presence_requires_current_availability(self):
        for woman, contract in departure_lint.contracts()["women"].items():
            surface = next(iter(contract["surfaces"]), None)
            if not surface:
                continue
            with self.subTest(woman=woman):
                story = copy.deepcopy(self.story)
                scene = next(s for s in story["Scenes"] if s["Id"] == surface["scene"])
                key = woman + (".reachable_by_letter" if surface.get("letter") else ".present_now")
                scene["Requires"].remove(key)
                self.assertTrue(any(surface["scene"] in e for e in departure_lint.check(story)))

    def test_ordinary_acceptance_cannot_be_its_own_revoker(self):
        story = copy.deepcopy(self.story)
        story["DerivedForbids"]["arsinoe.payoff.ordinary"].append("arsinoe.future_spoken")
        self.assertTrue(any("earned arm also forbids" in e for e in payoff_lint.check(story)))

    def test_late_sword_does_not_earn_an_iz_song(self):
        story = copy.deepcopy(self.story)
        scene = next(s for s in story["Scenes"] if s["Id"] == "yaniel.lastcall.page")
        scene["Nodes"][0]["Paragraphs"][3]["Requires"].remove("yaniel.radiance_sang")
        self.assertTrue(any("yaniel.lastcall.page" in e for e in payoff_lint.check(story)))

    def test_new_scenes_cannot_bypass_departure_inventory(self):
        story = copy.deepcopy(self.story)
        story["Scenes"].append({"Id": "yaniel.new_unclassified_visit", "Relationship": "yaniel"})
        self.assertTrue(any("new_unclassified_visit" in e for e in departure_lint.check(story)))
        story["Scenes"].append({"Id": "minachiv.new_unclassified_pair", "Relationship": "minagho_chivarro"})
        self.assertTrue(any("new_unclassified_pair" in e for e in departure_lint.check(story)))

    def test_correspondence_cannot_use_a_historical_return_directly(self):
        story = copy.deepcopy(self.story)
        story["Derived"]["melazmera.reachable_by_letter"].append(["melazmera.trickster.returned"])
        self.assertTrue(any("uncontracted correspondence" in e for e in departure_lint.check(story)))

    def test_native_coda_keeps_its_earned_native_alternative(self):
        story = copy.deepcopy(self.story)
        page = next(s for s in story["Scenes"] if s["Id"] == "wenduag.lastcall.page")
        self.assertIn("wenduag.payoff.partner", page["Requires"])
        self.assertIn(["wenduag.romance_finished.latched"], story["Derived"]["wenduag.payoff.partner"])

    def test_ledger_receipt_cannot_be_dropped(self):
        story = copy.deepcopy(self.story)
        entry = next(e for e in story["Books"]["trickster.ledger"]["Entries"] if e["Id"] == "owed.terendelev")
        entry["Requires"].remove("terendelev.payoff.debt")
        self.assertTrue(any("owed.terendelev" in e for e in payoff_lint.check(story)))

    def test_secondary_commitment_cannot_bypass_the_shared_guest_seat(self):
        story = copy.deepcopy(self.story)
        key = "nocticula.harem.eligible"
        story["Derived"][key] = [["noct.acq.renewed_agreement"]]
        self.assertTrue(any(key in e for e in payoff_lint.check(story)))

    def test_coffin_return_requires_an_observed_death(self):
        story = copy.deepcopy(self.story)
        story["Derived"]["camellia.trickster.coffin_life"][0].remove("camellia.trickster.death_observed")
        self.assertTrue(any("coffin_life" in e for e in payoff_lint.check(story)))

    def test_return_qualifier_cannot_replace_its_actual_event_source(self):
        story = copy.deepcopy(self.story)
        story["DepartureEpochs"]["camellia"]["ReturnTriggers"] = {}
        self.assertTrue(any("earned return event sources" in e for e in departure_lint.check(story)))

    def test_an_earlier_death_cannot_unlock_a_current_coffin_producer(self):
        story = copy.deepcopy(self.story)
        scene = next(s for s in story["Scenes"] if s["Id"] == "camellia.trickster.killed.third_night")
        scene["Requires"].remove("camellia.dead")
        self.assertTrue(any(scene["Id"] in e for e in payoff_lint.check(story)))
