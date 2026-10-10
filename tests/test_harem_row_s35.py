"""S35 acceptance walks against the final engine's availability rules."""
import copy
import json
from pathlib import Path
import unittest
from tests.story_fixture import fresh_story, row_registration_fixture

from storylines.harem_rows import s35
from storylines import foresight
from tools import rrt_verify as rules
from tools import savecompat, harem_schedule_lint


class S35Tests(unittest.TestCase):
    @staticmethod
    def register_row(payload):
        before = dict(foresight.CONSUMERS)
        try:
            s35.register(payload, payload["Scenes"], payload["Etudes"])
        finally:
            foresight.CONSUMERS.clear()
            foresight.CONSUMERS.update(before)

    @classmethod
    def setUpClass(cls):
        cls.base = row_registration_fixture(s35)
        cls.story = copy.deepcopy(cls.base)
        cls.register_row(cls.story)
        cls.model = rules.Model(cls.story)
        cls.audit = cls.model.by_id[s35.PREFIX + "audit"]
        cls.retry = cls.model.by_id[s35.PREFIX + "retry"]

    def state(self, hour=200):
        state = rules.SimState(5, hour)
        state.flags.update([
            "trickster", "trickster.foresight.accepted", "trickster.foresight.cost.promise",
            "household.table.kept", "nurah.meeting_arrived", "nurah.meeting_accepted",
            "nurah.complete", "nurah.copies_settled", "nurah.ending_partners",
            "arsinoe.committed", "arsinoe.continuation_kept", "arsinoe.campaign_lover",
            "arsinoe.shared_terms", "arsinoe.future_spoken",
        ])
        rules.sim_complete(self.model, state)
        return state

    def root(self, body):
        return body["Nodes"][0]["Choices"]

    def publish(self, body, node_id, state):
        node = next(n for n in body["Nodes"] if n["Id"] == node_id)
        self.assertEqual(len(node["Choices"]), 1)
        choice = node["Choices"][0]
        self.assertTrue(rules.sim_choice_available(choice, state))
        self.assertFalse(choice.get("Abort"))
        state.flags.update(choice["Set"])
        state.times.update({flag: state.hour for flag in choice["Set"]})
        rules.sim_complete(self.model, state)

    def test_registration_is_append_only_idempotent_and_does_not_mutate_existing_content(self):
        payload = copy.deepcopy(self.base)
        old = copy.deepcopy(payload["Scenes"])
        missing = {s["Id"] for s in s35.SCENES} - {s["Id"] for s in old}
        self.register_row(payload)
        self.register_row(payload)
        self.assertEqual(payload["Scenes"][:len(old)], old)
        self.assertEqual(len(payload["Scenes"]), len(old) + len(missing))
        self.assertEqual(sum(e["Id"] == "seating.arsinoe_nurah.audit"
                             for e in payload["Books"]["trickster.ledger"]["Entries"]), 1)
        old_entry = next(e for e in self.base["Books"]["trickster.ledger"]["Entries"]
                         if e["Id"] == "seating.arsinoe.nurah")
        gated = next(e for e in payload["Books"]["trickster.ledger"]["Entries"]
                     if e["Id"] == old_entry["Id"])
        self.assertEqual(gated["Text"], old_entry["Text"])
        self.assertEqual(gated["Lines"], old_entry["Lines"])
        self.assertIn(s35.PREFIX + "audit.seen", gated["Forbids"])
        for row in s35.SCENES:
            self.assertEqual(payload["ForesightConsumers"][row["Id"]], "foresight.page_taken")
        self.assertEqual(savecompat.check(payload), [])

    def test_assembled_row_passes_structural_validation(self):
        self.assertEqual([e for e in rules.validate(self.model) if s35.PREFIX in e], [])

    def test_earned_page_current_path_chapter_and_body_are_required(self):
        self.assertTrue(rules.sim_available(self.model, self.audit, self.state()))
        for removed in ("trickster", "trickster.foresight.accepted",
                        "nurah.complete", "arsinoe.committed"):
            with self.subTest(removed=removed):
                state = self.state()
                state.flags.remove(removed)
                rules.sim_complete(self.model, state)
                self.assertFalse(rules.sim_available(self.model, self.audit, state))
        for chapter in (3, 4, 6):
            state = self.state()
            state.chapter = chapter
            self.assertFalse(rules.sim_available(self.model, self.audit, state))
        state = self.state()
        state.flags.remove("nurah.meeting_arrived")
        state.flags.update(["nurah.correspondence_available", "nurah.trickster.returned",
                            "nurah.trickster.released"])
        rules.sim_complete(self.model, state)
        self.assertTrue(rules.sim_available(self.model, self.audit, state))
        state.flags.remove("nurah.complete")
        rules.sim_complete(self.model, state)
        self.assertFalse(rules.sim_available(self.model, self.audit, state))

    def test_closures_later_losses_prison_and_route_blocks_survive_old_returns(self):
        for blocked in ("nurah.closed", "arsinoe.closed", "nurah.parent_lich",
                        "nurah.epoch_unavailable", "arsinoe.epoch_unavailable", "inhuman",
                        "arsinoe.victims_revived", "swarm", "true_lich", "trickster.failed",
                        "fool_king.gone", "nurah.meeting_withdrawn", "nurah.meeting_declined",
                        "sacrifice"):
            for body in (self.audit, self.retry):
                with self.subTest(blocked=blocked, scene=body["Id"]):
                    state = self.state()
                    state.flags.update([blocked, "nurah.trickster.returned", "nurah.trickster.released",
                                        *s35.flags("audit.failed")])
                    state.times[s35.PREFIX + "audit.failed"] = 100
                    rules.sim_complete(self.model, state)
                    self.assertFalse(rules.sim_available(self.model, body, state))
        for body in (self.audit, self.retry):
            state = self.state()
            state.flags.update(["nurah.prison", *s35.flags("audit.failed")])
            state.times[s35.PREFIX + "audit.failed"] = 100
            self.assertFalse(rules.sim_available(self.model, body, state))
            state.flags.add("nurah.trickster.released")
            rules.sim_complete(self.model, state)
            self.assertTrue(rules.sim_available(self.model, body, state))
        for death in ("nurah.dead_drezen", "nurah.dead_camellia", "nurah.killing_mechanism"):
            state = self.state()
            state.flags.add(death)
            rules.sim_complete(self.model, state)
            self.assertFalse(rules.sim_available(self.model, self.audit, state))

    def test_outcome_choices_publish_each_womans_deed_without_attitude_or_romance_writes(self):
        for node_id, method in (("audit_held", "audit"), ("lien_held", "lien"), ("word_held", "word")):
            state = self.state()
            self.publish(self.audit, node_id, state)
            self.assertTrue(set(s35.held("audit", method)) <= state.flags)
            self.assertFalse(rules.sim_available(self.model, self.audit, state))
            self.assertFalse(rules.sim_available(self.model, self.retry, state))
            self.assertEqual({f for f in state.flags if f.startswith(s35.PREFIX + "method.")},
                             {s35.PREFIX + "method." + method})
        for body in (self.audit, self.retry):
            for node in body["Nodes"]:
                for choice in node["Choices"]:
                    for flag in choice.get("Set", []):
                        self.assertTrue(flag.startswith((s35.PREFIX, "trickster.wmt.use.", "household.wmt.debt.")))
                    self.assertIsNone(choice.get("Crusade"))
                    self.assertIsNone(choice.get("StartEtude"))
                    self.assertIsNone(choice.get("RemoveItem"))

    def test_check_lien_and_word_have_concrete_producers_and_preserve_debts(self):
        root = self.root(self.audit)
        self.assertEqual(root[0]["Check"], dict(Skill="SkillKnowledgeWorld", DC=30,
                                              Success="audit_held", Failure="missed", CommanderOnly=True))
        state = self.state()
        self.assertFalse(rules.sim_choice_available(root[1], state))
        state.flags.add(s35.LIEN)
        self.assertTrue(rules.sim_choice_available(root[1], state))
        self.publish(self.audit, "lien_held", state)
        self.assertIn(s35.LIEN, state.flags)
        producers = [choice for body in self.base["Scenes"] for node in body["Nodes"]
                     for choice in node["Choices"] if s35.LIEN in choice.get("Set", [])]
        self.assertTrue(producers)
        self.assertEqual(root[2]["Set"], ["trickster.wmt.use.arsinoe_nurah", "household.wmt.debt.arsinoe_nurah"])
        state = self.state()
        for index in range(3):
            state.flags.add("trickster.wmt.use.test%d" % index)
        rules.sim_complete(self.model, state)
        self.assertFalse(rules.sim_choice_available(root[2], state))
        self.assertTrue(rules.sim_choice_available(root[0], state))
        self.assertTrue(rules.sim_choice_available(root[3], state))

    def test_failed_audit_has_one_timestamped_protected_retry_and_no_new_check_or_price(self):
        state = self.state(hour=100)
        self.publish(self.audit, "missed", state)
        for hour, expected in ((100, False), (147, False), (148, True)):
            state.hour = hour
            self.assertEqual(rules.sim_available(self.model, self.retry, state), expected)
        self.publish(self.retry, "audit_held", state)
        self.assertFalse(rules.sim_available(self.model, self.retry, copy.deepcopy(state)))
        self.assertFalse(rules.sim_available(self.model, self.audit, copy.deepcopy(state)))
        self.assertEqual(harem_schedule_lint.delayed_clock_errors(self.retry, self.story), [])
        self.assertFalse(any(c.get("Check") for n in self.retry["Nodes"] for c in n["Choices"]))
        for body in (self.audit, self.retry):
            self.assertEqual(body["RestAllowance"], "household.protected")
            self.assertEqual(body["HouseholdCategory"], "protected")
            self.assertFalse(body.get("HouseholdArcStart"))
        state = self.state()
        state.rest_spent["household.protected"] = self.story["RestAllowances"]["household.protected"]
        self.assertFalse(rules.sim_available(self.model, self.audit, state))

    def test_refusal_and_abort_keep_every_page_selectable_and_do_not_close_a_romance(self):
        for body in (self.audit, self.retry):
            root = self.root(body)
            self.assertTrue(root[-1]["Abort"])
            self.assertEqual(root[-1]["Set"], [])
            self.assertIsNone(root[-1]["Next"])
            state = self.state()
            self.publish(body, "refused", state)
            self.assertFalse(rules.sim_available(self.model, self.audit, state))
            self.assertFalse(rules.sim_available(self.model, self.retry, state))
            self.assertNotIn("nurah.closed", state.flags)
            self.assertNotIn("arsinoe.closed", state.flags)
            for node in body["Nodes"]:
                self.assertTrue(any(rules.sim_choice_available(c, state) for c in node["Choices"]))

    def test_first_wins_enmity_is_guarded_and_never_overwritten_by_retry(self):
        for woman, other in (s35.WOMEN, s35.WOMEN[::-1]):
            enmity = woman + ".harem.enmity." + other
            reconciled = woman + ".harem.reconciled." + other
            for body in (self.audit, self.retry):
                self.assertEqual(body["ForbidOverrides"][enmity], reconciled)
                state = self.state()
                state.flags.update([enmity, *s35.flags("audit.failed")])
                state.times[s35.PREFIX + "audit.failed"] = 100
                self.assertFalse(rules.sim_available(self.model, body, state))
                state.flags.add(reconciled)
                self.assertTrue(rules.sim_available(self.model, body, state))
            self.publish(self.retry, "audit_held", state)
            self.assertIn(enmity, state.flags)
            self.assertIn(reconciled, state.flags)

    def test_readers_are_history_only_and_select_exactly_one_actual_method(self):
        entry = s35.ledger_entry()
        for method in ("audit", "lien", "word"):
            state = self.state()
            self.publish(self.audit, method + "_held", state)
            state.flags.update(["nurah.closed", "arsinoe.closed", "sacrifice"])
            lines = [line for line in entry["Lines"] if rules.sim_choice_available(line, state)]
            self.assertEqual(len(lines), 1)
            self.assertIn(s35.PREFIX + "method." + method, lines[0]["Requires"])
        self.assertFalse(any(n.get("Paragraphs") for b in s35.SCENES for n in b["Nodes"]))


if __name__ == "__main__":
    unittest.main()
