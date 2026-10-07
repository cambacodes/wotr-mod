"""S42 acceptance walks against the assembled base plus the isolated row."""
import copy
import json
from pathlib import Path
import unittest

from storylines.harem_rows import s42
from tools import rrt_verify as rules, savecompat

ROOT = Path(__file__).resolve().parents[1]


class RowS42(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads((ROOT / "development/Story.json").read_text(encoding="utf-8-sig"))
        cls.story = copy.deepcopy(cls.base)
        s42.register(cls.story, cls.story["Scenes"], cls.story["Etudes"])
        cls.model = rules.Model(cls.story)
        cls.rows = {step: cls.model.by_id[s42.P + step] for step in ("settle", "retry")}

    def state(self, step="settle", hour=100):
        state = rules.SimState(5, hour)
        state.flags.update(self.rows[step]["Requires"])
        state.times.update({flag: 0 for flag in state.flags})
        return state

    def available(self, step, state):
        return rules.sim_available(self.model, self.rows[step], state)

    def commit(self, step, node, state):
        choice = next(n for n in self.rows[step]["Nodes"] if n["Id"] == node)["Choices"][0]
        self.assertTrue(rules.sim_choice_available(choice, state))
        state.flags.update(choice["Set"] + [s42.P + step])
        state.times.update({flag: state.hour for flag in choice["Set"] + [s42.P + step]})
        state.rest_spent["household.protected"] = state.rest_spent.get("household.protected", 0) + 1

    def test_required_guards_and_current_losses_on_both_entries(self):
        for step in self.rows:
            initial = self.state(step)
            self.assertTrue(self.available(step, initial))
            for flag in self.rows[step]["Requires"]:
                state = copy.deepcopy(initial)
                state.flags.remove(flag)
                self.assertFalse(self.available(step, state), (step, flag))
            for flag in self.rows[step]["Forbids"]:
                state = copy.deepcopy(initial)
                state.flags.add(flag)
                if self.rows[step]["ForbidOverrides"].get(flag) in state.flags:
                    state.flags.remove(self.rows[step]["ForbidOverrides"][flag])
                self.assertFalse(self.available(step, state), (step, flag))
            for flag, override in s42.OVERRIDES.items():
                state = copy.deepcopy(initial)
                state.flags.update((flag, override))
                self.assertTrue(self.available(step, state), (step, flag))
                state.flags.add(flag.split(".")[0] + ".epoch_unavailable")
                self.assertFalse(self.available(step, state))
            state = copy.deepcopy(initial)
            state.flags.update(("kaylessa.camellia_killed", "kaylessa.trickster.returned"))
            self.assertFalse(self.available(step, state))
            state = copy.deepcopy(initial)
            state.rest_spent["household.protected"] = 2
            self.assertFalse(self.available(step, state))
            for chapter in (3, 4, 6):
                state = copy.deepcopy(initial)
                state.chapter = chapter
                self.assertFalse(self.available(step, state))

    def test_check_and_all_aborts_have_no_writes_or_native_effects(self):
        choice = self.rows["settle"]["Nodes"][0]["Choices"][0]
        self.assertEqual(choice["Check"], dict(Skill="SkillThievery", DC=28, Success="landed", Failure="missed"))
        self.assertEqual(choice["Set"], [])
        for row in self.rows.values():
            for node in row["Nodes"]:
                abort = node["Choices"][-1]
                self.assertTrue(abort["Abort"])
                self.assertEqual(abort["Set"], [])
                self.assertIsNone(abort["Next"])
                self.assertFalse(any(abort.get(key) for key in
                                     ("NativeNext", "Revive", "Crusade", "RemoveItem", "StartEtude", "Alignment")))
            for node in row["Nodes"]:
                for choice in node["Choices"]:
                    self.assertTrue(all(flag.startswith(s42.P) for flag in choice["Set"]))
                    self.assertFalse(any(word in flag for flag in choice["Set"]
                                         for word in (".enmity.", ".attitude.", ".closed", ".reconciled.", ".committed")))

    def test_success_costs_and_deeds_and_save_reload(self):
        for node in ("landed", "carried"):
            state = self.state()
            self.commit("settle", node, state)
            state = copy.deepcopy(state)  # restored flags/timestamps/allowance
            self.assertFalse(self.available("settle", state))
            self.assertFalse(self.available("retry", state))
            self.assertTrue(all(s42.P + f in state.flags for f in s42.SUCCESS))
            self.assertEqual(s42.P + "cost.commander_evening" in state.flags, node == "carried")
            self.assertNotIn(s42.P + "exposure_unsettled", state.flags)

    def test_pending_retry_clock_refusal_and_success(self):
        state = self.state()
        self.commit("settle", "missed", state)
        state.hour = 147
        self.assertFalse(self.available("retry", state))
        state.hour = 148
        self.assertTrue(self.available("retry", state))
        self.assertNotIn(s42.P + "exposure_unsettled", state.flags)
        for node in ("sealed", "refused"):
            loaded = copy.deepcopy(state)
            self.commit("retry", node, loaded)
            self.assertIn(s42.P + "settle.failed", loaded.flags)
            self.assertEqual(s42.P + "exposure_unsettled" in loaded.flags, node == "refused")
            self.assertFalse(self.available("retry", loaded))
            self.assertEqual(loaded.rest_spent["household.protected"], 2)
        state = self.state()
        self.commit("settle", "declined", state)
        self.assertIn(s42.P + "exposure_unsettled", state.flags)
        self.assertFalse(self.available("retry", state))

    def test_enmity_override_preserves_history_and_reader_priority(self):
        for a, b in (s42.PAIR, tuple(reversed(s42.PAIR))):
            state = self.state("retry")
            edge = a + ".harem.enmity." + b
            state.flags.add(edge)
            self.assertFalse(self.available("retry", state))
            state.flags.add(a + ".harem.reconciled." + b)
            self.assertTrue(self.available("retry", state))
            self.commit("retry", "sealed", state)
            self.assertIn(edge, state.flags)
        entry = next(e for e in self.story["Books"]["trickster.ledger"]["Entries"] if e["Id"] == s42.P + "notes")
        pending = entry["Lines"][0]
        self.assertEqual(pending["Forbids"], [s42.P + "retry.seen", s42.P + "exposure_unsettled"])

    def test_registration_is_idempotent_and_save_compatible(self):
        story = copy.deepcopy(self.story)
        before = copy.deepcopy(story)
        s42.register(story, story["Scenes"], story["Etudes"])
        self.assertEqual(story, before)
        self.assertEqual(savecompat.check(story), [])
        old = next(s for s in self.base["Scenes"] if s["Id"] == "kaylessa.clearing.where_i_was_meant_to_die")
        new = next(s for s in story["Scenes"] if s["Id"] == old["Id"])
        for original, current in zip(old["Nodes"][0]["Choices"], new["Nodes"][0]["Choices"]):
            self.assertEqual(original["Next"], current["Next"])
            self.assertEqual(original["Set"], current["Set"])
        self.assertFalse(any(n.get("Paragraphs") for s in self.rows.values() for n in s["Nodes"]))


if __name__ == "__main__":
    unittest.main()
