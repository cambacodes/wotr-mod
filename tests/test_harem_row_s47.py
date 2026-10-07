"""S47 save references, current channels, irreversible outcomes and pause safety."""
import copy
import json
from pathlib import Path
import unittest

from storylines.harem_rows import s47
from tools import rrt_verify


class S47Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads((Path(__file__).resolve().parents[1] / "development/Story.json").read_text(encoding="utf-8-sig"))
        cls.model = rrt_verify.Model(cls.story)
        cls.by_id = cls.model.by_id

    def state(self, *extra):
        state = rrt_verify.SimState(5, 1000)
        state.flags.update(("trickster", "trickster.foresight.accepted", "trickster.foresight.cost.promise",
                            "yaniel.freed.latched", "yaniel.trickster.returned", "yaniel.areelu_unmasked",
                            "areelu.trickster.primed", s47.P + "proof.ready", *extra))
        rrt_verify.sim_complete(self.model, state)
        return state

    def test_native_projection_does_not_require_romance_or_bodily_seat(self):
        body = self.by_id[s47.P + "inspection"]
        self.assertEqual(body["AnswerLists"], [s47.HOST])
        self.assertEqual(body["NativeReturnCue"], s47.RETURN)
        self.assertFalse(body.get("Participants"))
        self.assertFalse(body.get("TableHosted"))
        self.assertFalse(body.get("Remote"))  # native projection, not a rest letter
        self.assertEqual(body["RestAllowance"], "household.protected")
        self.assertEqual((body["MinChapter"], body["MaxChapter"]), (5, 5))
        self.assertTrue(all(n["Speaker"] == "conversant" for n in body["Nodes"]))
        self.assertNotIn("areelu.committed", body["Requires"])
        self.assertTrue(rrt_verify.sim_available(self.model, body, self.state()))

    def test_current_channel_loss_and_unearned_gates(self):
        body = self.by_id[s47.P + "inspection"]
        for loss in (s47.DESTROYED, "areelu.closed", "areelu.dead_fight", "yaniel.closed",
                     "yaniel.killed.latched", "yaniel.trickster.left_free", "trickster.failed"):
            with self.subTest(loss=loss):
                self.assertFalse(rrt_verify.sim_available(self.model, body, self.state(loss)))
        for missing in ("trickster", "trickster.foresight.accepted", "yaniel.freed.latched",
                        "yaniel.trickster.returned", "areelu.trickster.primed", s47.P + "proof.ready"):
            with self.subTest(missing=missing):
                state = self.state()
                state.flags.discard(missing)
                # Recompute derived gates from scratch, not from stale closure.
                for key in self.story.get("Derived", {}):
                    state.flags.discard(key)
                rrt_verify.sim_complete(self.model, state)
                self.assertFalse(rrt_verify.sim_available(self.model, body, state))

    def test_earlier_return_never_overrides_a_later_loss(self):
        body = self.by_id[s47.P + "inspection"]
        for rel in ("yaniel", "areelu"):
            with self.subTest(woman=rel):
                state = self.state()
                state.times["yaniel.trickster.returned"] = 100
                loss = rel + ".returned_actor_lost"
                state.flags.add(loss)
                state.times[loss] = 900
                # Main supplies the compiled epoch result; sim_complete does
                # not replay the runtime loss-observation inventory itself.
                state.flags.add(rel + ".epoch_unavailable")
                rrt_verify.sim_complete(self.model, state)
                self.assertFalse(rrt_verify.sim_available(self.model, body, state))
        state = self.state()
        state.chapter = 6
        self.assertFalse(rrt_verify.sim_available(self.model, body, state))

    def test_all_paths_pause_without_writes_or_native_effects(self):
        body = self.by_id[s47.P + "inspection"]
        for node in body["Nodes"]:
            with self.subTest(node=node["Id"]):
                pauses = [c for c in node["Choices"] if c.get("Abort")]
                self.assertEqual(len(pauses), 1)
                pause = pauses[0]
                self.assertFalse(pause.get("Set"))
                for field in ("Next", "NativeNext", "Check", "Crusade", "RemoveItem", "Revive", "StartEtude"):
                    self.assertFalse(pause.get(field))
                for choice in node["Choices"]:
                    if choice.get("Next"):
                        self.assertFalse(choice.get("Set"))

    def test_four_terminal_outcomes_are_permanent_and_distinct(self):
        body = self.by_id[s47.P + "inspection"]
        results = {n["Id"]: n["Choices"][0] for n in body["Nodes"] if n["Id"] in ("undertaking", "retained", "unsettled", "declined")}
        for name, choice in results.items():
            flags = choice["Set"]
            with self.subTest(result=name):
                self.assertIn(s47.P + "inspection.seen", flags)
                self.assertFalse(choice.get("Next"))
                self.assertFalse(any("reconciled" in f or "enmity" in f or "committed" in f for f in flags))
                self.assertFalse(rrt_verify.sim_available(self.model, body, self.state(*flags)))
                for receipt in ("proof.quest_done", "face.excluded", "original.returned", "cost.areelu_specific_guise", "cost.commander_reconnaissance"):
                    self.assertEqual(s47.P + receipt in flags, name == "undertaking")
        self.assertIn(s47.P + "mandate.broken", results["retained"]["Set"])

    def test_committed_and_spent_beat_have_one_commission(self):
        commission = self.by_id[s47.P + "commission"]
        for history in ("yaniel.committed", s47.BEAT):
            with self.subTest(history=history):
                self.assertTrue(rrt_verify.sim_available(self.model, commission, self.state(history)))
                self.assertTrue(rrt_verify.sim_available(self.model, commission,
                                self.state(history, "areelu.closed", s47.DESTROYED)))
                for receipt in ("proof.ready", "commission.declined"):
                    self.assertFalse(rrt_verify.sim_available(self.model, commission,
                                     self.state(history, s47.P + "commission.seen", s47.P + receipt)))
        self.assertFalse(rrt_verify.sim_available(self.model, commission, self.state()))
        beat = self.by_id[s47.BEAT]
        for id in ("end", "end_refused", "end_unknown"):
            node = next(n for n in beat["Nodes"] if n["Id"] == id)
            self.assertEqual(len(node["Choices"]), 3)
            self.assertEqual(node["Choices"][0]["Next"], "robbed")
            self.assertEqual(node["Choices"][1]["Next"], "bite")
            self.assertEqual(node["Choices"][2]["Next"], "household_face_request")
        request = next(n for n in beat["Nodes"] if n["Id"] == "household_face_request")
        self.assertIn(s47.BEAT, request["Choices"][0]["Set"])
        self.assertIn(s47.BEAT, request["Choices"][1]["Set"])
        self.assertEqual(request["Choices"][2]["Set"], [])

    def test_registration_is_idempotent_and_readers_stay_in_permitted_hosts(self):
        from storylines import yaniel_walls, lastcall_ledger, lastcall_partners
        payload = {"Scenes": []}
        s47.register(payload, payload["Scenes"], {})
        before = copy.deepcopy((payload, yaniel_walls.SCENES, lastcall_ledger.EXTRA_ENTRIES, lastcall_partners.PARTNERS))
        s47.register(payload, payload["Scenes"], {})
        self.assertEqual(before, (payload, yaniel_walls.SCENES, lastcall_ledger.EXTRA_ENTRIES, lastcall_partners.PARTNERS))
        self.assertEqual(self.story["SeenCues"][s47.DESTROYED], ["591acfaf8500cc94aa7a8918db767d43"])
        self.assertEqual(self.story["DerivedOpenRoutes"][s47.P + "contact.open"], ["areelu", "yaniel"])
        for body in self.story["Scenes"]:
            for node in body["Nodes"]:
                for para in node.get("Paragraphs", []):
                    if any(flag.startswith(s47.P) for flag in para.get("Requires", [])):
                        self.assertTrue(body.get("Owner", "").endswith("Epilogue"), body["Id"])


if __name__ == "__main__":
    unittest.main()
