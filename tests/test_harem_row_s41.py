"""S41: earned channels, evidence outcomes and protected hostile continuity."""
import copy
from tests.story_fixture import fresh_story
import unittest

from storylines import household_pair_iomedae_areelu as pair
from tools import rrt_verify as rules
from tools.harem_schedule_lint import delayed_clock_errors

class ReconstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)
        cls.scenes = {s["Id"]: s for s in cls.model.scenes if s["Id"].startswith(pair.PREFIX)}

    def state(self, step, **extra):
        state = rules.SimState(5, 200)
        state.flags.update(["trickster", "trickster.now", "trickster.ever", "chapter_later",
                            "trickster.foresight.accepted", "household.started", "household.table.kept", "iomedae.committed",
                            "iomedae.trickster.disputation.called", "iomedae.trickster.disputed",
                            "iomedae.trickster.first_spoken", "iomedae.banner_in_hand",
                            "areelu.trickster.wager_struck", "areelu.trickster.lens_held"])
        if step == "reconstruction":
            state.flags.add(pair.P("open.ready"))
            state.times[pair.P("open.ready")] = 100
        elif step == "repair":
            state.flags.add(pair.P("reconstruction.unsettled"))
            state.times[pair.P("reconstruction.unsettled")] = 100
        state.flags.update(extra.get("flags", []))
        rules.sim_complete(self.model, state)
        return state

    def available(self, step, state):
        rules.sim_complete(self.model, state)
        return rules.sim_available(self.model, self.scenes[pair.P(step)], state)

    def test_ch5_wager_and_channel_matrix(self):
        for step in ("open", "reconstruction", "repair"):
            with self.subTest(step=step):
                state = self.state(step)
                self.assertTrue(self.available(step, state))
                self.assertNotIn("areelu.committed", state.flags)
                for missing in ("trickster.foresight.accepted", "trickster",
                                "iomedae.trickster.first_spoken"):
                    blocked = copy.deepcopy(state)
                    blocked.flags.discard(missing)
                    self.assertFalse(self.available(step, blocked), missing)
                lost = copy.deepcopy(state)
                lost.flags.discard("iomedae.banner_in_hand")
                lost.flags.add("iz.sock_raised")
                self.assertFalse(self.available(step, lost))
                lost.flags.add("iomedae.trickster.order_banner")
                self.assertTrue(self.available(step, lost))
                for participant in self.scenes[pair.P(step)]["Participants"]:
                    closed = copy.deepcopy(state)
                    closed.flags.add(self.story["Relationships"][participant]["ClosedFlag"])
                    self.assertFalse(self.available(step, closed))

    def test_claimant_alone_and_lens_not_projector(self):
        for step in ("open", "reconstruction", "repair"):
            state = self.state(step)
            state.flags.discard("areelu.trickster.lens_held")
            self.assertEqual(self.available(step, state), step == "open")
            state.flags.discard("areelu.trickster.wager_struck")
            self.assertEqual(self.available(step, state), step == "open")
        for step in ("reconstruction", "repair"):
            state = self.state(step)
            # No fabricated destruction key: the native projector has no
            # S41 reader. The earned lens works without its laboratory cue.
            self.assertNotIn("areelu.one_must_burn", state.flags)
            scene = self.scenes[pair.P(step)]
            self.assertTrue(all("projector" not in f for f in scene["Requires"] + scene["Forbids"]))
            self.assertTrue(self.available(step, state))
            for loss in self.story["Relationships"]["areelu"]["UnavailableFlags"]:
                absent = copy.deepcopy(state)
                absent.flags.add(loss)
                self.assertFalse(self.available(step, absent), loss)

    def test_clock_refusal_replay_and_rest_allowance(self):
        for step, clock in (("reconstruction", "open.ready"), ("repair", "reconstruction.unsettled")):
            state = self.state(step)
            state.times[pair.P(clock)] = 153
            self.assertFalse(self.available(step, state))
            state.hour += 1
            self.assertTrue(self.available(step, state))
            # Save/reload retains the deed clock and spent allowance.
            loaded = copy.deepcopy(state)
            loaded.rest_spent["household.protected"] = 2
            self.assertFalse(self.available(step, loaded))
            loaded.rest_spent.clear()
            loaded.flags.add(pair.P(step + ".seen"))
            self.assertFalse(self.available(step, loaded))
            refused = self.state(step, flags=[pair.P("permanent_refusal")])
            self.assertFalse(self.available(step, refused))
            self.assertEqual(delayed_clock_errors(self.scenes[pair.P(step)], self.story), [])

    def test_terminals_have_exact_costs_and_evidence(self):
        expected = {
            ("open", "kept"): {"open.seen", "open.ready", "known.case_bundle"},
            ("open", "burned"): {"open.seen", "open.records_burned", "known.case_bundle", "permanent_refusal"},
            ("reconstruction", "originals"): {"reconstruction.seen", "proof.originals_collated",
                                             "cost.commander_evening_spent", *pair.ACCOUNT_COSTS},
            ("reconstruction", "families"): {"reconstruction.seen", "proof.families_identified",
                                            "cost.commander_contacts_exposed", *pair.ACCOUNT_COSTS},
            ("reconstruction", "rejected"): {"reconstruction.seen", "reconstruction.unsettled", "unsettled",
                                            "cost.commander_false_apology"},
            ("repair", "restored"): {"repair.seen", "proof.index_restored", "cost.commander_evening_spent",
                                    "cost.commander_edit_exposed", *pair.ACCOUNT_COSTS},
            ("repair", "refused"): {"repair.seen", "repair.declined", "permanent_refusal"},
        }
        for (step, node_id), flags in expected.items():
            node = next(n for n in self.scenes[pair.P(step)]["Nodes"] if n["Id"] == node_id)
            self.assertEqual(set(node["Choices"][0]["Set"]), {pair.P(f) for f in flags})
            if "account.delivered" in flags:
                for name in ("K-17", "Odran Vesk", "K-22", "Tervan Sorn", "K-31", "Talaran Dorn", "unknown"):
                    self.assertIn(name, node["Text"])

    def test_fixed_hostility_and_independent_obligations(self):
        for step in ("reconstruction", "repair"):
            state = self.state(step, flags=["iomedae.harem.enmity.areelu", "areelu.harem.enmity.iomedae"])
            self.assertTrue(self.available(step, state))
        for scene in self.scenes.values():
            for node in scene["Nodes"]:
                self.assertFalse(node.get("Paragraphs"))
                for choice in node["Choices"]:
                    self.assertFalse(choice.get("Check"))
                    self.assertTrue(all(f.startswith(pair.PREFIX) for f in choice["Set"]))
                    if choice.get("Abort"):
                        self.assertFalse(choice["Set"])
                    for flag in choice["Set"]:
                        self.assertFalse(any(token in flag for token in (".attitude.", ".enmity.", ".stance.",
                                                                         ".reconciled.", ".closed", ".committed")))
            self.assertEqual(scene["HouseholdCategory"], "protected")
            self.assertFalse(scene.get("ForbidOverrides"))

    def play(self, step, state, index):
        scene = self.scenes[pair.P(step)]
        self.assertTrue(self.available(step, state))
        nodes = {n["Id"]: n for n in scene["Nodes"]}
        choice = nodes["start"]["Choices"][index]
        path = [choice]
        while choice["Next"]:
            self.assertFalse(choice["Set"], "Publish only after the evidence and reactions")
            choice = nodes[choice["Next"]]["Choices"][0]
            path.append(choice)
        return rules.sim_play(self.model, scene, state, {"committed": set(), "closed": set()}, plan=(0, path))

    def test_evidence_walks_and_false_record_correction(self):
        for approach in (0, 1):
            state = self.state("open")
            self.assertTrue(self.play("open", state, 0))
            state.rest_spent.clear()
            state.hour += 47
            self.assertFalse(self.available("reconstruction", state))
            state.hour += 1
            self.assertTrue(self.play("reconstruction", state, approach))
            self.assertIn(pair.P("account.delivered"), state.flags)
            self.assertNotIn(pair.P("reconstruction.unsettled"), state.flags)
            self.assertFalse(self.available("repair", state))
            self.assertEqual(state.rest_spent["household.protected"], 1)
        for final_choice in (0, 1):
            state = self.state("reconstruction")
            self.assertTrue(self.play("reconstruction", state, 2))
            self.assertNotIn(pair.P("account.delivered"), state.flags)
            state.hour += 48
            state.rest_spent.clear()
            self.assertTrue(self.play("repair", state, final_choice))
            self.assertEqual(pair.P("account.delivered") in state.flags, final_choice == 0)
            self.assertEqual(pair.P("permanent_refusal") in state.flags, final_choice == 1)
            self.assertFalse(self.available("repair", copy.deepcopy(state)))
        state = self.state("open")
        self.assertTrue(self.play("open", state, 1))
        state.hour += 48
        state.rest_spent.clear()
        self.assertFalse(self.available("reconstruction", state))

    def test_abort_has_no_saved_effect_or_charge(self):
        for step, index in (("open", 2), ("reconstruction", 3), ("repair", 2)):
            state = self.state(step)
            before = copy.deepcopy(state)
            self.assertFalse(self.play(step, state, index))
            self.assertEqual(state.rest_spent, before.rest_spent)
            self.assertEqual(state.times, before.times)
            self.assertEqual(state.flags, before.flags)


if __name__ == "__main__":
    unittest.main()
