"""S09 progression against the assembled runtime model; no generated-file edits."""
import copy
import unittest

from tests.story_fixture import fresh_story
from storylines.harem_rows import s09
from tools import rrt_verify as rules
from tools.intimacy_contract_lint import walks
from tools.harem_schedule_lint import delayed_clock_errors
from tests.harem_row_walk import walk


class S09Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)
        cls.rows = {s["Id"]: s for s in cls.model.scenes if s["Id"].startswith(s09.PREFIX)}

    def state(self, evil=True, hour=1000):
        state = rules.SimState(5, hour)
        state.flags.update(("trickster", "trickster.now", "availability.observed", "household.table.kept",
                            "trickster.foresight.accepted", "trickster.foresight.cost.promise",
                            "wenduag.committed", "arueshalae.committed", "wenduag.in_party",
                            "arueshalae.recruited_drezen", "arueshalae.native_alive",
                            "wenduag.trickster.proved", "wenduag.trickster.gate_seen",
                            "wenduag.trickster.claim.given", "arueshalae.trickster.terms"))
        state.flags.add("arueshalae.evil_recruited" if evil else "arueshalae.changed")
        rules.sim_complete(self.model, state)
        return state

    def scene(self, suffix):
        return self.rows[s09.p(suffix)]

    def finish(self, state, suffix, node="plotted"):
        scene = self.scene(suffix)
        choice = next(n for n in scene["Nodes"] if n["Id"] == node)["Choices"][0]
        state.flags.update(choice["Set"])
        for flag in choice["Set"]:
            state.times[flag] = state.hour
        rules.sim_complete(self.model, state)

    def test_registration_is_idempotent_and_ids_are_unique(self):
        from storylines import household
        s09.register({}, [], {})
        s09.register({}, [], {})
        ids = [s["Id"] for s in household.ENTRIES if s["Id"].startswith(s09.PREFIX)]
        self.assertEqual(len(ids), 8)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), set(self.rows))

    def test_unknown_and_corruption_precedence_and_paid_page(self):
        state = self.state(False)
        self.assertTrue(rules.sim_available(self.model, self.scene("settle.good"), state))
        state.flags.add("arueshalae.evil_recruited")
        rules.sim_complete(self.model, state)
        self.assertFalse(rules.sim_available(self.model, self.scene("settle.good"), state))
        self.assertTrue(rules.sim_available(self.model, self.scene("settle.evil"), state))
        for key in ("arueshalae.changed", "arueshalae.evil_recruited", "arueshalae.recruited_drezen"):
            state.flags.discard(key)
        rules.sim_complete(self.model, state)
        self.assertFalse(any(rules.sim_available(self.model, self.scene("settle." + b), state) for b in ("good", "evil")))
        for removed in ("trickster", "trickster.foresight.accepted"):
            state = self.state()
            state.flags.discard(removed)
            rules.sim_complete(self.model, state)
            self.assertFalse(rules.sim_available(self.model, self.scene("settle.evil"), state))

    def test_one_personality_operation_and_48_hour_retry(self):
        state = self.state(False)
        self.finish(state, "settle.good")
        state.flags.add("arueshalae.evil_recruited")
        rules.sim_complete(self.model, state)
        self.assertFalse(rules.sim_available(self.model, self.scene("settle.evil"), state))
        self.assertFalse(rules.sim_available(self.model, self.scene("friend_wenduag"), state))
        for evil, branch in ((True, "evil"), (False, "good")):
            state = self.state(evil)
            self.finish(state, "settle." + branch, "blind")
            state.hour += 47
            self.assertFalse(rules.sim_available(self.model, self.scene("retry." + branch), state))
            state.hour += 1
            self.assertTrue(rules.sim_available(self.model, self.scene("retry." + branch), state))
            self.finish(state, "retry." + branch)
            self.assertFalse(rules.sim_available(self.model, self.scene("retry." + branch), state))

    def test_romance_and_presence_alone_do_not_supply_a_body(self):
        for evil, native in ((True, "arueshalae.evil_recruited"), (False, "arueshalae.native_alive")):
            state = self.state(evil)
            scene = self.scene("settle.evil" if evil else "settle.good")
            self.assertTrue(rules.sim_available(self.model, scene, state))
            state.flags.discard(native)
            # Keep the personality classification from a historical solo outcome.
            state.flags.add("arueshalae.trickster.fallen.house_call" if evil else "arueshalae.changed")
            rules.sim_complete(self.model, state)
            self.assertIn("arueshalae.present_now", state.flags)
            self.assertFalse(rules.sim_available(self.model, scene, state))
        state = self.state()
        state.flags.discard("wenduag.in_party")
        rules.sim_complete(self.model, state)
        self.assertIn("wenduag.present_now", state.flags)
        self.assertFalse(rules.sim_available(self.model, self.scene("settle.evil"), state))

    def test_deeds_elapsed_time_mutual_answers_and_morning(self):
        state = self.state()
        self.finish(state, "settle.evil")
        for step in ("friend_wenduag", "friend_arueshalae"):
            state.hour += 47
            self.assertFalse(rules.sim_available(self.model, self.scene(step), state))
            state.hour += 1
            self.assertTrue(rules.sim_available(self.model, self.scene(step), state))
            self.finish(state, step, "her")
        state.hour += 48
        self.assertTrue(rules.sim_available(self.model, self.scene("choice"), state))
        for receipt in s09.flags(*s09.FRIEND_W, *s09.FRIEND_A):
            lost = copy.deepcopy(state)
            lost.flags.discard(receipt)
            rules.sim_complete(self.model, lost)
            self.assertFalse(rules.sim_available(self.model, self.scene("choice"), lost))
        self.assertNotIn("wenduag.harem.attitude.arueshalae.lover", state.flags)
        # The direct terminal helper does not execute intermediate ward removal.
        state.flags.update(s09.flags("cost.ward_scroll", "ward.applied_wenduag"))
        self.finish(state, "choice", "after")
        self.assertIn("wenduag.harem.attitude.arueshalae.lover", state.flags)
        self.assertIn("arueshalae.harem.attitude.wenduag.lover", state.flags)
        state.hour += 7
        self.assertFalse(rules.sim_available(self.model, self.scene("morning"), state))
        state.hour += 1
        self.assertTrue(rules.sim_available(self.model, self.scene("morning"), state))

    def test_later_loss_or_closure_blocks_every_step_and_old_return_does_not_help(self):
        for scene in self.rows.values():
            for loss in ("wenduag.closed", "arueshalae.closed", "wenduag.q3_sent_away",
                         "arueshalae.kicked_out_evil", "wenduag.epoch_unavailable", "arueshalae.epoch_unavailable"):
                state = self.state(scene["Id"].endswith("evil") or not scene["Id"].endswith("good"))
                state.flags.update(scene["Requires"])
                self.assertTrue(rules.sim_available(self.model, scene, state), scene["Id"])
                state.flags.update((loss, "wenduag.trickster.returned", "arueshalae.trickster.returned"))
                self.assertFalse(rules.sim_available(self.model, scene, state), (scene["Id"], loss))
            self.assertFalse(scene.get("ContactUnit"))
            self.assertIn(s09.p("body.wenduag"), scene["Requires"])
            self.assertTrue(any(key.startswith(s09.p("body.arueshalae.")) for key in scene["Requires"]))

    def test_scroll_is_spent_on_wenduag_no_abort_after_spend_and_slot_is_inert(self):
        scene = self.scene("choice")
        nodes = {n["Id"]: n for n in scene["Nodes"]}
        choice = nodes["protection"]["Choices"][0]
        self.assertEqual(choice["RemoveItem"], s09.SCROLL)
        self.assertEqual(set(choice["Set"]), set(s09.flags("cost.ward_scroll", "ward.applied_wenduag")))
        state = self.state()
        state.flags.add("arueshalae.trickster.fallen.warded")
        self.assertFalse(rules.sim_choice_available(choice, state))
        self.assertTrue(rules.sim_choice_available(nodes["protection"]["Choices"][1], state))
        state.flags.add("arueshalae.ward_held")
        self.assertTrue(rules.sim_choice_available(choice, state))
        slot = nodes[s09.p("choice.explicit.1")]
        self.assertEqual(slot["Choices"][0]["Next"], "after")
        self.assertEqual(slot["Choices"][0]["Set"], [])
        paths = list(walks(scene, set(s09.LIVE) | set(s09.flags("ward.applied_wenduag")), "threshold"))
        self.assertEqual(len(paths), 1)
        self.assertIn("after", paths[0][0])
        for node in ("threshold", s09.p("choice.explicit.1"), "after"):
            self.assertFalse(any(c["Abort"] for c in nodes[node]["Choices"]))

    def test_optional_choice_walk_requires_fresh_ward_and_preserves_solo_bonds(self):
        state = self.state()
        self.finish(state, "settle.evil")
        for step in ("friend_wenduag", "friend_arueshalae"):
            state.hour += 48
            self.finish(state, step, "her")
        state.hour += 48
        scene = self.scene("choice")
        self.assertTrue(rules.sim_available(self.model, scene, state))
        for fresh_ward in (False, True):
            ready = copy.deepcopy(state)
            ready.flags.add("arueshalae.trickster.fallen.warded")
            if fresh_ward:
                ready.flags.add("arueshalae.ward_held")
            outcomes = walk(self, self.model, scene, ready)
            lovers = [outcome for outcome in outcomes if s09.p("choice.both_yes") in outcome.flags]
            self.assertEqual(len(lovers), int(fresh_ward))
            for outcome in outcomes:
                rules.sim_complete(self.model, outcome)
                self.assertIn("wenduag.committed", outcome.flags)
                self.assertIn("arueshalae.committed", outcome.flags)
                mutual = s09.p("choice.both_yes") in outcome.flags
                for a, b in (s09.PAIR, tuple(reversed(s09.PAIR))):
                    self.assertEqual(a + ".harem.attitude." + b + ".lover" in outcome.flags, mutual)
                if mutual:
                    self.assertIn(s09.p("ward.applied_wenduag"), outcome.flags)
                    self.assertIn(s09.p("cost.ward_scroll"), outcome.flags)
                    self.assertEqual(outcome.rest_spent["household.pair"], 1)
                    for receipt in ("deed.wenduag_desire_answer", "deed.arueshalae_desire_answer",
                                    "cost.ward_scroll", "ward.applied_wenduag"):
                        missing = copy.deepcopy(outcome)
                        missing.flags.remove(s09.p(receipt))
                        rules.sim_complete(self.model, missing)
                        self.assertNotIn("wenduag.harem.attitude.arueshalae.lover", missing.flags)
                        self.assertNotIn("arueshalae.harem.attitude.wenduag.lover", missing.flags)
                else:
                    self.assertNotIn(s09.p("ward.applied_wenduag"), outcome.flags)
                    if s09.p("choice.declined") in outcome.flags:
                        outcome.hour += 8
                        self.assertFalse(rules.sim_available(self.model, self.scene("morning"), outcome))

    def test_all_optional_entries_require_current_page_path_and_bodies(self):
        state = self.state()
        self.finish(state, "settle.evil")
        for step, node, hours in (("friend_wenduag", "her", 48),
                                  ("friend_arueshalae", "her", 48),
                                  ("choice", "after", 48), ("morning", "kept", 8)):
            state.hour += hours
            scene = self.scene(step)
            self.assertTrue(rules.sim_available(self.model, scene, state))
            for removed in ("trickster", "trickster.foresight.accepted", "household.table.kept",
                            "wenduag.in_party", "arueshalae.evil_recruited"):
                missing = copy.deepcopy(state)
                missing.flags.remove(removed)
                rules.sim_complete(self.model, missing)
                self.assertFalse(rules.sim_available(self.model, scene, missing), (step, removed))
            for loss in ("wenduag.q3_killed", "arueshalae.evil_dead"):
                lost = copy.deepcopy(state)
                lost.flags.add(loss)
                rules.sim_complete(self.model, lost)
                self.assertFalse(rules.sim_available(self.model, scene, lost), (step, loss))
            self.finish(state, step, node)

    def test_optional_start_needs_actual_base_respect_deeds(self):
        state = self.state()
        self.finish(state, "settle.evil")
        state.hour += 48
        for receipt in s09.RESPECT:
            missing = copy.deepcopy(state)
            missing.flags.remove(s09.p(receipt))
            rules.sim_complete(self.model, missing)
            self.assertFalse(rules.sim_available(self.model, self.scene("friend_wenduag"), missing))

    def test_refusal_abort_allowances_enmity_and_clock_contracts(self):
        for suffix, scene in self.rows.items():
            self.assertEqual(delayed_clock_errors(scene, self.story), [], suffix)
            protected = ".settle." in suffix or ".retry." in suffix
            self.assertEqual(scene["RestAllowance"], "household.protected" if protected else "household.pair")
            self.assertEqual(scene["HouseholdArcStart"], suffix.endswith("friend_wenduag"))
            self.assertEqual(scene["HouseholdArc"], s09.PREFIX.rstrip('.'))
            root = scene["Nodes"][0]
            abort = root["Choices"][-1]
            self.assertTrue(abort["Abort"])
            self.assertEqual(abort["Set"], [])
            state = self.state(not suffix.endswith("good"))
            state.flags.update(scene["Requires"])
            state.flags.add("wenduag.harem.enmity.arueshalae")
            self.assertFalse(rules.sim_available(self.model, scene, state))
            state.flags.add("wenduag.harem.reconciled.arueshalae")
            self.assertTrue(rules.sim_available(self.model, scene, state))
            state.rest_spent[scene["RestAllowance"]] = 2 if protected else 1
            self.assertFalse(rules.sim_available(self.model, scene, state))
        effects = [f for s in self.rows.values() for n in s["Nodes"] for c in n["Choices"] for f in c["Set"]]
        self.assertTrue(all(f.startswith(s09.PREFIX) for f in effects))


if __name__ == "__main__":
    unittest.main()
