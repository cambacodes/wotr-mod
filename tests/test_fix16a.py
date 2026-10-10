"""fix16a: scoped fixture checks retain full-build delivery enforcement."""
import copy
import unittest

from storylines import areelu_trickster, earned_presence
from tests.test_engine_q5 import ReturnInProgressTests
from tests.story_fixture import fresh_story
from tools import earned_presence_lint, hub_attachment_lint


class ScopeAndDepartureTests(unittest.TestCase):
    def test_local_presence_fixture_does_not_waive_full_delivery_inventory(self):
        story = ReturnInProgressTests().story()
        self.assertEqual([], earned_presence_lint.producer_presence_errors(story, relationships={"aranka"}))
        self.assertTrue(any("missing registered scene" in e
                            for e in earned_presence_lint.producer_presence_errors(story)))
        bad = copy.deepcopy(story)
        bad["Scenes"][0]["Requires"] = ["trickster.ever"]
        self.assertTrue(any(e.startswith("T7") for e in
                            earned_presence_lint.producer_presence_errors(bad, relationships={"aranka"})))

    def test_postwar_report_receipt_does_not_exempt_campaign_departures(self):
        receipt = areelu_trickster.REPORT_DEPARTED
        story = dict(Relationships={"areelu": dict(UnavailableFlags=[])},
                     Scenes=[dict(Id="areelu.report", Relationship="areelu", Nodes=[
                         dict(Id="burn", Choices=[dict(Set=[receipt])])])])
        self.assertTrue(earned_presence.DEPARTURE_EXEMPTIONS[("areelu", receipt)].strip())
        self.assertEqual([], earned_presence_lint.producer_presence_errors(story, relationships={"areelu"}))
        story["Scenes"][0]["Nodes"][0]["Choices"][0]["Set"].append("areelu.gone")
        errors = earned_presence_lint.producer_presence_errors(story, relationships={"areelu"})
        self.assertEqual(1, len(errors), errors)
        self.assertIn("departure areelu.gone", errors[0])
        afterword = next(s for s in areelu_trickster.SCENES if s["Id"] == "areelu.trickster.report.afterword")
        self.assertIn(receipt, afterword["Nodes"][0]["Choices"][0]["Forbids"])


class FoundationTests(unittest.TestCase):
    def test_complete_fixture_keeps_nominated_delivery_foundations(self):
        story = fresh_story()
        ids = {s["Id"] for s in story["Scenes"]}
        self.assertIn("household.ensemble.ch5.arrows", ids)
        self.assertIn("household.docket.gesmerha_jerribeth.account", ids)
        self.assertIn("household.pair.arueshalae_vellexia.settle.good", ids)
        self.assertEqual([], hub_attachment_lint.gameplay_entry_lint(story))
        for sid in ("household.ensemble.ch5.arrows", "household.docket.gesmerha_jerribeth.account"):
            bad = copy.deepcopy(story)
            bad["Scenes"] = [s for s in bad["Scenes"] if s["Id"] != sid]
            self.assertTrue(any(sid + ": missing registered scene" in e
                                for e in hub_attachment_lint.gameplay_entry_lint(bad)))


class ConditionalReturnTests(unittest.TestCase):
    def test_native_life_alternative_cannot_supply_an_unpaid_return(self):
        from tests.test_earned_presence import base
        story = base()
        story['Relationships']['her']['StartedFlag'] = 'her.started'
        story['Derived']['her.present'] = [['her.native_alive'], ['her.returned']]
        story['Derived']['her.native_alive'] = [['chapter_later']]
        story['DerivedForbids'] = {'her.native_alive': ['her.dead']}
        ending = next(s for s in story['Scenes'] if s['Id'] == 'her.ending_together')
        ending['ForbidOverrides']['her.dead'] = 'her.present'
        self.assertFalse(any(e.startswith('T5') for e in earned_presence_lint.check(story)[0]))
        story['DerivedForbids']['her.native_alive'] = []
        self.assertTrue(any(e.startswith('T5') for e in earned_presence_lint.check(story)[0]))
