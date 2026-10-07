"""S25 deed paths, retirement, attendance, clocks and save-safe registration."""
import copy
import json
from pathlib import Path
import unittest

from storylines import household
from storylines.harem_rows import s25
from tools import harem_schedule_lint, rrt_verify, savecompat

ROOT = Path(__file__).resolve().parents[1]


class S25Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads((ROOT / "development/Story.json").read_text(encoding="utf-8-sig"))
        cls.payload = copy.deepcopy(cls.base)
        cls.entries_before = copy.deepcopy(household.ENTRIES)
        s25.register(cls.payload, cls.payload["Scenes"], cls.payload["Etudes"])
        cls.rows = {s["Id"].removeprefix(s25.P): rrt_verify.norm_scene(s)
                    for s in cls.payload["Scenes"] if s["Id"].startswith(s25.P)}
        # Exercise the real availability oracle on this row, without enumerating
        # every unrelated route's dialogue graph for each pair acceptance walk.
        cls.model = rrt_verify.Model(dict(
            Scenes=list(cls.rows.values()), Relationships={r: cls.payload["Relationships"][r]
                                                          for r in (*s25.PAIR, "household")},
            RestAllowances=cls.payload["RestAllowances"],
            Derived={key: value for key, value in cls.payload["Derived"].items() if key.startswith(s25.P)}))

    def state(self, step, extra=(), hour=1000):
        state = rrt_verify.SimState(5, hour)
        state.flags.update(self.rows[step]["Requires"])
        state.flags.update(extra)
        return state

    def walk(self, step, index, success=True):
        body = self.rows[step]
        nodes = {n["Id"]: n for n in body["Nodes"]}
        node, flags, visited = "start", set(), []
        while node:
            visited.append(node)
            choices = nodes[node]["Choices"]
            self.assertTrue(choices)
            answer = choices[index if node == "start" else 0]
            self.assertEqual(answer["Requires"], [])
            self.assertEqual(answer["Forbids"], [])
            flags.update(answer["Set"])
            if answer["Abort"]:
                return flags, visited, True
            if answer.get("Check"):
                node = answer["Check"]["Success" if success else "Failure"]
            else:
                node = answer["Next"]
        return flags, visited, False

    def test_primary_and_retry_publish_only_after_both_answers(self):
        for step, root in (("settle", 0), ("settle", 1), ("retry", 0)):
            writes, visited, aborted = self.walk(step, root)
            self.assertFalse(aborted)
            self.assertIn("answer", visited)
            self.assertEqual(visited[-1], "vellexia")
            self.assertEqual(writes, set(s25.flags(step + ".seen", step + ".kept", *s25.RESPECT,
                                                  "cost.commander.clearing_time")))
        failed, _, _ = self.walk("settle", 0, success=False)
        self.assertIn(s25.P + "settle.failed", failed)
        self.assertNotIn(s25.P + "display.answer_kept", failed)
        failed, _, _ = self.walk("retry", 1)
        self.assertIn(s25.P + "retry.failed", failed)
        for step, index in (("settle", 2), ("retry", 2)):
            writes, _, _ = self.walk(step, index)
            self.assertEqual(writes, set(s25.flags(step + ".seen", step + ".declined")))

    def test_every_abort_is_effect_free_and_roots_keep_indices(self):
        counts = dict(settle=4, retry=4, company=3, desire=3, choice=5, morning=2)
        for step, count in counts.items():
            self.assertEqual(len(self.rows[step]["Nodes"][0]["Choices"]), count)
            writes, visited, aborted = self.walk(step, count - 1)
            self.assertTrue(aborted)
            self.assertEqual(writes, set())
            self.assertEqual(visited, ["start"])

    def test_current_body_page_path_and_visit_guards(self):
        body = self.rows["settle"]
        state = self.state("settle")
        self.assertTrue(rrt_verify.sim_available(self.model, body, state))
        for missing in ("trickster", "foresight.page_taken", "household.stance_eligible",
                        "household.table.kept", "camellia.present_now", "vellexia.present_now",
                        "vellexia.trickster.in_person"):
            absent = copy.deepcopy(state)
            absent.flags.remove(missing)
            absent.flags.update(("trickster.ever", "shyka.met", "vellexia.trickster.returned"))
            self.assertFalse(rrt_verify.sim_available(self.model, body, absent), missing)
        for lost in s25.EXCLUSIONS:
            absent = copy.deepcopy(state)
            absent.flags.update((lost, "vellexia.trickster.returned", "camellia.trickster.returned"))
            self.assertFalse(rrt_verify.sim_available(self.model, body, absent), lost)
        for chapter in (3, 4, 6):
            state.chapter = chapter
            self.assertFalse(rrt_verify.sim_available(self.model, body, state))

    def test_retry_clock_refusal_and_allowance_are_independent(self):
        state = self.state("retry")
        body = self.rows["retry"]
        state.times[s25.P + "settle.failed"] = 952
        self.assertTrue(rrt_verify.sim_available(self.model, body, state))
        state.hour = 999
        self.assertFalse(rrt_verify.sim_available(self.model, body, state))
        state.hour = 1000
        state.rest_spent["household.protected"] = 2
        self.assertFalse(rrt_verify.sim_available(self.model, body, state))
        state.rest_spent.clear()
        for terminal in ("retry.seen", "settle.kept", "settle.declined"):
            blocked = copy.deepcopy(state)
            blocked.flags.add(s25.P + terminal)
            self.assertFalse(rrt_verify.sim_available(self.model, body, blocked))

    def test_optional_sequence_remains_blocked_even_with_every_deed(self):
        for step in ("company", "desire", "choice", "morning"):
            body = self.rows[step]
            state = self.state(step, s25.flags("settle.kept", "retry.kept", *s25.LOVER))
            self.assertFalse(rrt_verify.sim_available(self.model, body, state))
            self.assertIn(s25.P + "ready", body["Forbids"])
            self.assertTrue(body["ManualOnly"])
            self.assertEqual(body["Kind"], "event")
            self.assertFalse(body.get("InteractionHub"))
            for woman in s25.PAIR:
                self.assertIn(woman + ".present_now", body["Requires"])
        self.assertEqual(self.rows["company"]["RequiresAnyGroups"], [list(s25.flags("settle.kept", "retry.kept"))])
        self.assertEqual([self.rows[s]["DelayHours"] for s in ("company", "desire", "choice", "morning")], [48, 48, 48, 8])
        self.assertEqual([s for s, body in self.rows.items() if body.get("HouseholdArcStart")], ["company"])

    def test_optional_personal_answers_and_empty_filled_slot_have_identical_flow(self):
        writes, visited, _ = self.walk("choice", 0)
        self.assertEqual(visited, ["start", "camellia_answer", "vellexia_answer", "mutual", "explicit.1", "after"])
        self.assertEqual(writes, set(s25.flags("choice.seen", "choice.both_yes", "choice.room_cleared")))
        slot = next(n for n in self.rows["choice"]["Nodes"] if n["Id"] == "explicit.1")
        self.assertEqual(slot["Choices"][0]["Set"], [])
        original = slot["Text"]
        try:
            slot["Text"] = "User-supplied interval."
            self.assertEqual(self.walk("choice", 0), (writes, visited, False))
        finally:
            slot["Text"] = original
        for index, terminal in ((1, "choice.camellia_no"), (2, "choice.vellexia_no"), (3, "choice.friends_only")):
            writes, visited, _ = self.walk("choice", index)
            self.assertEqual(writes, set(s25.flags("choice.seen", terminal)))
            self.assertNotIn("explicit.1", visited)
        for step in ("company", "desire"):
            writes, _, _ = self.walk(step, 1)
            self.assertEqual(writes, set(s25.flags(step + ".seen", step + ".declined")))

    def test_stage_deeds_cannot_be_replaced_by_slot_or_invitation(self):
        stages = rrt_verify.Model(dict(Scenes=[], Derived={key: value for key, value in self.payload["Derived"].items()
                                                          if key.startswith(s25.P)}))
        for woman in s25.PAIR:
            key = s25.P + woman + ".lover"
            expected = set(s25.flags(*s25.LOVER))
            self.assertEqual(set(self.payload["Derived"][key][0]), expected)
            for missing in expected:
                state = rrt_verify.SimState(5, 1000)
                state.flags.update(expected - {missing})
                rrt_verify.sim_complete(stages, state)
                self.assertNotIn(key, state.flags)
        writes = {f for body in self.rows.values() for node in body["Nodes"] for answer in node["Choices"] for f in answer["Set"]}
        self.assertFalse(writes.intersection(self.payload["Derived"]))
        self.assertTrue(all(f.startswith(s25.P) for f in writes))
        self.assertFalse(any("enmity" in f or "reconciled" in f or "committed" in f or "closed" in f for f in writes))

    def test_registration_savecompat_clocks_consumers_and_existing_data(self):
        self.assertEqual(len(self.rows), 6)
        self.assertEqual(household.ENTRIES, self.entries_before)
        payload = copy.deepcopy(self.payload)
        s25.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(payload, self.payload)
        self.assertEqual(self.payload["Scenes"][:len(self.base["Scenes"])], self.base["Scenes"])
        self.assertEqual(self.payload["Books"], self.base["Books"])
        self.assertEqual(savecompat.check(self.payload), [])
        for body in self.rows.values():
            self.assertEqual(harem_schedule_lint.delayed_clock_errors(body, self.payload), [])
            self.assertEqual(self.payload["ForesightConsumers"][body["Id"]], "foresight.page_taken")
            for a, b in (s25.PAIR, s25.PAIR[::-1]):
                self.assertEqual(body["ForbidOverrides"][household.enmity(a, b)], a + ".harem.reconciled." + b)
                self.assertIn(household.enmity(a, b), self.payload["PendingHooks"])
                self.assertIn(a + ".harem.reconciled." + b, self.payload["PendingHooks"])


if __name__ == "__main__":
    unittest.main()
