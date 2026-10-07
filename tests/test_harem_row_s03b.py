"""S03b's indexed hearing, current attendance, clock, and save contracts."""
import copy
import unittest

from tests.story_fixture import fresh_story
from storylines.harem_rows import s03b
from tools import harem_schedule_lint, rrt_verify


class FallenHearing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = fresh_story()
        s03b.register(cls.payload, cls.payload["Scenes"], cls.payload["Etudes"])
        cls.model = rrt_verify.Model(cls.payload)

    def row(self, step):
        return self.model.by_id[s03b.p(step)]

    def test_registered_payload_passes_structural_validation(self):
        self.assertEqual(rrt_verify.validate(self.model), [])

    def state(self, step="settle", hour=1000):
        state = rrt_verify.SimState(5, hour)
        state.flags.update(self.row(step)["Requires"])
        # J01's qualified contact contract checks native eligibility inputs
        # and actual actors, rather than accepting a seeded eligibility alias.
        for woman in self.row(step)["ParticipantWomen"]:
            state.flags.update(self.payload["SeatWomen"][woman]["Requires"])
            state.flags.update(self.model.composites[woman + ".harem.eligible"][0])
        state.available_contacts = {
            next(option["Units"][0] for option in contact["Options"]
                 if set(option["Requires"]) <= state.flags
                 and not set(option["Forbids"]) & state.flags)
            for contact in self.row(step)["ParticipantContacts"].values()}
        return state

    def test_registration_is_append_only_and_idempotent(self):
        payload = fresh_story()
        # Also works after the coordinator wires auto-discovery into the build.
        payload["Scenes"][:] = [s for s in payload["Scenes"] if not s["Id"].startswith(s03b.PREFIX)]
        old = copy.deepcopy(payload["Scenes"])
        s03b.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(payload["Scenes"][:len(old)], old)
        self.assertEqual([s["Id"] for s in payload["Scenes"][len(old):]],
                         [s03b.p("settle"), s03b.p("retry")])
        for step in ("settle", "retry"):
            self.assertEqual(payload["ForesightConsumers"][s03b.p(step)], "foresight.page_taken")
        registered = copy.deepcopy(payload)
        s03b.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(payload, registered)

    def test_all_indexed_choices_and_terminals(self):
        for step, targets in (("settle", ["heard", "misheard", "refused", None]),
                              ("retry", ["heard", "refused", None])):
            nodes = {n["Id"]: n for n in self.row(step)["Nodes"]}
            self.assertEqual([c["Next"] for c in nodes["start"]["Choices"]], targets)
            later = nodes["start"]["Choices"][-1]
            self.assertTrue(later["Abort"])
            self.assertEqual(later["Set"], [])
            for target in targets[:-1]:
                choices = nodes[target]["Choices"]
                self.assertEqual(len(choices), 1)
                terminal = choices[0]
                self.assertEqual(terminal["Set"], [s03b.p(s) for s in s03b.OUTCOMES[step][target]])
                self.assertFalse(terminal["Abort"])
                self.assertIsNone(terminal["Next"])
                self.assertTrue(all(flag.startswith(s03b.PREFIX) for flag in terminal["Set"]))

    def test_page_live_path_and_both_current_bodies_are_required(self):
        for step in ("settle", "retry"):
            row = self.row(step)
            state = self.state(step)
            self.assertTrue(rrt_verify.sim_available(self.model, row, state))
            for key in ("trickster", "trickster.now", "foresight.page_taken", "household.stance_eligible",
                        "seelah.harem.eligible", "arueshalae.harem.eligible",
                        "seelah.present_now", "arueshalae.present_now", "arueshalae.corrupted",
                        "arueshalae.evil_recruited", s03b.p("seelah_body")):
                state.flags.remove(key)
                state.flags.update(["trickster.ever", "shyka.met", "seelah.committed", "arueshalae.committed"])
                self.assertFalse(rrt_verify.sim_available(self.model, row, state), (step, key))
                state.flags.add(key)
            for chapter in (3, 4, 6):
                state.chapter = chapter
                self.assertFalse(rrt_verify.sim_available(self.model, row, state))

    def test_body_adapter_distinguishes_current_actor_from_correspondence(self):
        state = rrt_verify.SimState(5, 1000)
        state.flags.update(["seelah.committed", "seelah.trickster.returned"])
        rrt_verify.sim_complete(self.model, state)
        self.assertNotIn(s03b.p("seelah_body"), state.flags)
        state.flags.add("seelah.in_party")
        rrt_verify.sim_complete(self.model, state)
        self.assertIn(s03b.p("seelah_body"), state.flags)
        state.flags.remove("seelah.in_party")
        presence = self.payload["Presences"]["seelah.presence"]
        # Use the existing dismissed-body arm, with all placement conditions.
        state.flags.update(["trickster", "chapter_later", "seelah_gone", "seelah.trickster.primed"])
        for key in presence["Requires"]:
            if key not in self.model.composites:
                state.flags.add(key)
        rrt_verify.sim_complete(self.model, state)
        self.assertIn(s03b.p("seelah_body"), state.flags)
        state.flags.add("seelah.presence.failed")
        rrt_verify.sim_complete(self.model, state)
        self.assertNotIn(s03b.p("seelah_body"), state.flags)

    def test_loss_after_return_closure_and_legacy_arueshalae_deaths_block(self):
        losses = ("seelah.closed", "arueshalae.closed", "seelah.plot_departed",
                  "arueshalae_dead", "arueshalae.evil_dead", "arueshalae.kicked_out",
                  "arueshalae.kicked_out_evil", "seelah.epoch_unavailable",
                  "arueshalae.epoch_unavailable", "seelah.returned_actor_lost",
                  "arueshalae.returned_actor_lost", "trickster.failed", "fool_king.gone")
        for step in ("settle", "retry"):
            for loss in losses:
                state = self.state(step)
                state.flags.update([loss, "seelah.trickster.returned", "arueshalae.trickster.returned"])
                self.assertFalse(rrt_verify.sim_available(self.model, self.row(step), state), (step, loss))

    def test_retry_clock_and_saved_failure_no_duplicate_completion(self):
        row = self.row("retry")
        state = self.state("retry")
        state.times[s03b.p("settle.failed")] = 1000
        for hour, available in ((1047, False), (1048, True)):
            state.hour = hour
            self.assertEqual(rrt_verify.sim_available(self.model, row, state), available)
        for key in ("retry.seen", "settle.done", "unsettled"):
            state.flags.add(s03b.p(key))
            self.assertFalse(rrt_verify.sim_available(self.model, row, state))
            state.flags.remove(s03b.p(key))
        self.assertEqual(harem_schedule_lint.delayed_clock_errors(row, self.payload), [])

    def test_enmity_is_not_overridden_by_a_success_or_higher_stage(self):
        for step in ("settle", "retry"):
            for woman, other in (s03b.PAIR, s03b.PAIR[::-1]):
                state = self.state(step)
                key = woman + ".harem.enmity." + other
                state.flags.update([key, s03b.p("settle.done"), woman + ".harem.attitude." + other + ".lover"])
                self.assertFalse(rrt_verify.sim_available(self.model, self.row(step), state))
                if step == "retry":
                    state.flags.remove(s03b.p("settle.done"))
                state.flags.add(woman + ".harem.reconciled." + other)
                self.assertTrue(rrt_verify.sim_available(self.model, self.row(step), state))

    def test_corruption_wins_without_private_dream_knowledge_or_intimacy(self):
        row = self.row("settle")
        state = self.state()
        state.flags.add("arueshalae.redeemed")
        self.assertTrue(rrt_verify.sim_available(self.model, row, state))
        state.flags.remove("arueshalae.corrupted")
        self.assertFalse(rrt_verify.sim_available(self.model, row, state))
        state.flags.remove("arueshalae.redeemed")
        self.assertFalse(rrt_verify.sim_available(self.model, row, state))
        stages = set(s03b.STAGE_INPUTS)
        self.assertNotIn(("arueshalae", "seelah", "respect"), stages)
        self.assertTrue(all(stage in ("rival", "respect") for _, _, stage in stages))
        for step in ("settle", "retry"):
            row = self.row(step)
            self.assertEqual(row["Participants"], list(s03b.PAIR))
            self.assertEqual(row["RestAllowance"], "household.protected")
            self.assertEqual(row["HouseholdCategory"], "protected")
            self.assertFalse(row.get("HouseholdArcStart"))
            self.assertFalse(row.get("Remote"))
            self.assertFalse(row.get("AnswerLists"))
            self.assertTrue(all(not n.get("Paragraphs") for n in row["Nodes"]))

    def test_protected_allowance_and_commander_survival(self):
        row = self.row("settle")
        state = self.state()
        state.rest_spent["household.protected"] = 2
        self.assertFalse(rrt_verify.sim_available(self.model, row, state))
        state.rest_spent.clear()
        state.flags.add("sacrifice")
        self.assertFalse(rrt_verify.sim_available(self.model, row, state))
        state.flags.add("trickster.commander_back")
        self.assertTrue(rrt_verify.sim_available(self.model, row, state))


if __name__ == "__main__":
    unittest.main()
