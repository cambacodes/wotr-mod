"""S03a chronological walks, actual attendance and one applied interval."""
import copy
import unittest

from story_fixture import fresh_story
from storylines.harem_rows import s03a
from tools import departure_lint, payoff_lint, rrt_verify as verify, savecompat, text_structure_lint


class ShieldBench(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = fresh_story()
        cls.model = verify.Model(cls.payload)

    def row(self, step):
        return self.model.by_id[s03a.p(step)]

    def state(self, step="company", chapter=5):
        state = verify.SimState(chapter, 1000)
        state.flags.update(self.row(step)["Requires"])
        for woman in s03a.PAIR:
            state.flags.update(self.payload["SeatWomen"][woman]["Requires"])
            state.flags.update(self.model.composites[woman + ".harem.eligible"][0])
        return state

    def walk(self, step, path, flags=()):
        state = self.state(step)
        state.flags.update(flags)
        if "arueshalae.changed" in state.flags or "arueshalae.ward_held" in state.flags:
            state.flags.add(s03a.p("choice.offer_ready"))
        nodes = {node["Id"]: node for node in self.row(step)["Nodes"]}
        current = nodes["start"]
        written, removed = [], []
        for index in path:
            choice = current["Choices"][index]
            self.assertTrue(verify.sim_choice_available(choice, state), (step, current["Id"], index))
            written.extend(choice["Set"])
            state.flags.update(choice["Set"])
            if choice.get("RemoveItem"):
                removed.append(choice["RemoveItem"])
                state.flags.discard("arueshalae.ward_held")
            if choice["Abort"] or choice["Next"] is None:
                return written, removed, choice["Abort"]
            current = nodes[choice["Next"]]
        self.fail("unfinished walk: " + step)

    def test_structural_save_and_surface_contracts(self):
        self.assertEqual(verify.validate(self.model), [])
        self.assertEqual(savecompat.check(self.payload), [])
        self.assertEqual(payoff_lint.check(self.payload), [])
        self.assertEqual(departure_lint.check(self.payload), [])

    def test_all_speaker_switches_pass_the_actual_text_lint(self):
        for step in s03a.STEPS:
            for node in self.row(step)["Nodes"]:
                hard, review = text_structure_lint.spans(node["Text"], node["Speaker"])
                self.assertEqual((hard, review), ([], []), (step, node["Id"]))

    def test_append_only_idempotent_and_no_foreign_writes(self):
        payload = copy.deepcopy(self.payload)
        owned = {s03a.p(step) for step in s03a.STEPS}
        payload["Scenes"][:] = [s for s in payload["Scenes"] if s["Id"] not in owned]
        original = copy.deepcopy(payload["Scenes"])
        self.assertTrue(any(s["Id"] == s03a.p("fallen.settle") for s in original))
        s03a.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(payload["Scenes"][:len(original)], original)
        self.assertEqual([s["Id"] for s in payload["Scenes"][len(original):]], [s03a.p(x) for x in s03a.STEPS])
        registered = copy.deepcopy(payload)
        s03a.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(payload, registered)
        for step in s03a.STEPS:
            row = self.row(step)
            self.assertEqual(self.payload["ForesightConsumers"][row["Id"]], "foresight.page_taken")
            self.assertEqual(row["RestAllowance"], "household.pair")
            self.assertEqual(row["Participants"], list(s03a.PAIR))
            self.assertEqual(row["ParticipantWomen"], list(s03a.PAIR))
            self.assertEqual(row["HouseholdArcStart"], step == "company")
            self.assertFalse(row.get("AnswerLists"))
            for node in row["Nodes"]:
                self.assertFalse(node.get("Paragraphs"))
                for choice in node["Choices"]:
                    self.assertTrue(all(f.startswith(s03a.PREFIX) for f in choice["Set"]))

    def test_indexed_completed_deeds_and_abort(self):
        for step, path, result in (("company", [0, 0, 0], "kept"),
                                   ("desire", [0, 0, 0, 0], "named"),
                                   ("morning", [0, 0, 0], "done")):
            self.assertEqual(self.walk(step, path)[:2], (list(s03a.OUTCOMES[step, result]), []))
        for step in s03a.STEPS:
            self.assertEqual(self.walk(step, [1 if step == "morning" else 2]), ([], [], True))
        for step in s03a.STEPS[:3]:
            self.assertEqual(self.walk(step, [1, 0]), (list(s03a.OUTCOMES[step, "declined"]), [], False))

    def test_release_and_warded_mutual_choice(self):
        written, removed, _ = self.walk("choice", [0, 0, 0, 0, 0, 0], ["arueshalae.changed"])
        self.assertEqual(written, list(s03a.OUTCOMES["choice", "kept_safe"]))
        self.assertEqual(removed, [])
        written, removed, _ = self.walk("choice", [0, 0, 1, 0, 0, 0, 0], ["arueshalae.ward_held"])
        self.assertEqual(set(written), set(s03a.OUTCOMES["choice", "kept_warded"]))
        self.assertEqual(removed, [s03a.SCROLL])
        self.assertEqual(written.count(s03a.p("choice.ward_spent")), 2)  # application + exhaustive terminal
        self.assertEqual(self.walk("choice", [0, 1, 0, 0], ["arueshalae.changed"])[0], list(s03a.OUTCOMES["choice", "declined"]))
        self.assertEqual(self.walk("choice", [0, 0, 2, 0, 0], ["arueshalae.changed"])[0], list(s03a.OUTCOMES["choice", "declined"]))
        for path in ([0, 1, 0, 0], [0, 0, 2, 0, 0]):
            self.assertEqual(self.walk("choice", path, ["arueshalae.ward_held"])[1], [])

    def test_every_contact_page_has_an_exit_without_scroll(self):
        state = self.state("choice")
        state.flags.add(s03a.p("choice.ward_spent"))
        for node in self.row("choice")["Nodes"]:
            choices = [c for c in node["Choices"] if verify.sim_choice_available(c, state)]
            self.assertTrue(choices, node["Id"])
        answer = next(n for n in self.row("choice")["Nodes"] if n["Id"] == "arueshalae_yes")
        self.assertFalse(verify.sim_choice_available(answer["Choices"][0], state))
        self.assertFalse(verify.sim_choice_available(answer["Choices"][1], state))
        root = self.row("choice")["Nodes"][0]
        self.assertFalse(verify.sim_choice_available(root["Choices"][0], state))
        for node_id in ("arueshalae_yes", "ward_application"):
            node = next(n for n in self.row("choice")["Nodes"] if n["Id"] == node_id)
            defer = node["Choices"][-1]
            self.assertTrue(verify.sim_choice_available(defer, state))
            self.assertTrue(defer["Abort"])
            self.assertEqual(defer["Set"], [])
        self.assertEqual(self.payload["Derived"][s03a.p("choice.offer_ready")],
                         [["arueshalae.changed"], ["arueshalae.ward_held"]])

    def test_page_path_current_branch_and_attendance(self):
        for step in s03a.STEPS:
            row, state = self.row(step), self.state(step)
            self.assertTrue(verify.sim_available(self.model, row, state), step)
            for key in ("trickster", "trickster.now", "foresight.page_taken", "arueshalae.redeemed",
                        "seelah.present_now", "arueshalae.present_now", s03a.p("arueshalae_body")):
                state.flags.remove(key)
                state.flags.update(["shyka.met", "trickster.ever", "arueshalae.trickster.returned"])
                self.assertFalse(verify.sim_available(self.model, row, state), (step, key))
                state.flags.add(key)
            for loss in ("seelah.closed", "arueshalae.closed", "arueshalae.corrupted",
                         "seelah.epoch_unavailable", "arueshalae.epoch_unavailable",
                         "arueshalae_dead", "arueshalae.evil_dead", "arueshalae.kicked_out",
                         "arueshalae.kicked_out_evil", "seelah.returned_actor_lost", "trickster.failed"):
                state.flags.add(loss)
                self.assertFalse(verify.sim_available(self.model, row, state), (step, loss))
                state.flags.remove(loss)
            for chapter in (4, 6):
                state.chapter = chapter
                self.assertFalse(verify.sim_available(self.model, row, state))
        state = verify.SimState(5, 1000)
        state.flags.update(["arueshalae.changed", "arueshalae.trickster.returned"])
        verify.sim_complete(self.model, state)
        self.assertNotIn(s03a.p("arueshalae_body"), state.flags)
        state.flags.add("arueshalae.recruited_drezen")
        verify.sim_complete(self.model, state)
        self.assertIn(s03a.p("arueshalae_body"), state.flags)

    def test_clock_allowance_enmity_and_survival(self):
        for step, prior, hours in (("desire", "company.kept", 48), ("choice", "desire.named", 48),
                                   ("morning", "choice.both_yes", 8)):
            row, state = self.row(step), self.state(step)
            state.times[s03a.p(prior)] = 1000
            state.hour = 1000 + hours - 1
            self.assertFalse(verify.sim_available(self.model, row, state))
            state.hour += 1
            self.assertTrue(verify.sim_available(self.model, row, state))
            state.rest_spent["household.pair"] = 1
            self.assertFalse(verify.sim_available(self.model, row, state))
            state.rest_spent.clear()
            state.flags.add("sacrifice")
            self.assertFalse(verify.sim_available(self.model, row, state))
            state.flags.add("trickster.commander_back")
            self.assertTrue(verify.sim_available(self.model, row, state))
            for a, b in (s03a.PAIR, s03a.PAIR[::-1]):
                key = a + ".harem.enmity." + b
                state.flags.add(key)
                self.assertFalse(verify.sim_available(self.model, row, state))
                state.flags.add(a + ".harem.reconciled." + b)
                self.assertTrue(verify.sim_available(self.model, row, state))
                state.flags.remove(key)
        for chapter in (3, 5):
            key = "household.cap.ch%d.arcs" % chapter
            if key in self.payload["Counts"]:
                self.assertIn(s03a.p("company.seen"), self.payload["Counts"][key]["Of"])
                self.assertIn(key, self.row("company")["Forbids"])
                for step in s03a.STEPS[1:]:
                    self.assertNotIn(key, self.row(step)["Forbids"])


if __name__ == "__main__":
    unittest.main()
