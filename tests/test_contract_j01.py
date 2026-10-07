"""J01 classification and live-channel regressions against the authored export."""
import copy
import hashlib
import json
from pathlib import Path
import re
import unittest

from tests.story_fixture import fresh_story
from storylines import contract_j01, crossroute_presence
from tools import rrt_verify as rules
from tools.crossroute_checks.common import roster
from tools.crossroute_checks.mention_context import live_mentions
from tools.crossroute_checks.other_woman import native_participation_contexts


class J01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)
        cls.names = roster(cls.model)

    def test_reference_manifest_is_exact_and_never_exempts_new_live_action(self):
        manifest = json.loads(Path("tools/route_packs/plans/j01-reference-contexts.json").read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["contexts"]), 131)
        for entry in manifest["contexts"]:
            scene = self.model.by_id[entry["scene"]]
            slot = entry["slot"]
            if slot in ("Entry", "ReturnText"):
                text = scene[slot]
            else:
                node = next(n for n in scene["Nodes"] if n["Id"] == entry["node"])
                text = node["Text"] if slot == "text" else node["Choices"][int(slot[6:])]["Text"]
            self.assertEqual(hashlib.sha256(text.encode()).hexdigest(), entry["text_sha256"], entry)
            pattern = self.names[entry["woman"]][1]
            self.assertEqual(live_mentions(text, pattern, scene_id=scene["Id"]), [], entry)
            self.assertTrue(live_mentions(text + " " + entry["woman"] + " stands here now.", pattern,
                                          scene_id=scene["Id"]), entry)

    def test_native_professional_guard_preserves_refusal_without_reopening_romance(self):
        story = copy.deepcopy(self.story)
        key = crossroute_presence.availability(story, "arsinoe", "arsinoe")
        model = rules.Model(story)
        state = rules.SimState(5, 100)
        state.flags.update(("arsinoe.closed", "chapter_later", "availability.observed"))
        rules.sim_complete(model, state)
        self.assertIn(key, state.flags)
        self.assertIn("arsinoe.closed", state.flags)
        self.assertNotIn("arsinoe.harem.eligible", state.flags)
        for loss in model.rels["arsinoe"]["UnavailableFlags"]:
            lost = copy.deepcopy(state); lost.flags.add(loss)
            rules.sim_complete(model, lost)
            self.assertNotIn(key, lost.flags, loss)

    def test_summit_native_audience_is_not_nocticula_romance(self):
        story = copy.deepcopy(self.story)
        key = crossroute_presence.availability(story, "nocticula", "nocticula", native_audience=True)
        model = rules.Model(story)
        state = rules.SimState(5, 100)
        state.flags.update(("noct.closed", "chapter_later", "availability.observed"))
        rules.sim_complete(model, state)
        self.assertIn(key, state.flags)
        self.assertNotIn("nocticula.harem.eligible", state.flags)
        self.assertIn("noct.closed", state.flags)
        self.assertNotIn("noct.closed", story.get("DerivedForbids", {}).get(key, []))

    def test_verified_native_recovery_context_is_not_an_unchecked_whole_route_exception(self):
        contexts = native_participation_contexts(self.model)
        self.assertTrue(contexts)
        inherited = {speaker for spec in contexts.values() for speaker in spec["Speakers"]}
        self.assertIn("Arsinoe", inherited)
        self.assertTrue(all(sid.startswith("kiana.") for sid in contexts))
        broken = copy.deepcopy(self.story)
        for spec in broken["NativeEpilogueEdits"].values():
            if spec.get("Replacement") in contexts:
                spec["When"] = [["trickster.ever"]]
            for variant in spec.get("Variants", []):
                if variant.get("Replacement") in contexts:
                    variant["When"] = [["trickster.ever"]]
        self.assertEqual(len(native_participation_contexts(rules.Model(broken))), 0)

    def test_s08_seal_reply_remains_a_channel_and_is_not_emitted_by_j01(self):
        self.assertFalse(any(s["Id"].startswith(contract_j01.S08) for s in self.story["Scenes"]))
        reply = contract_j01.authenticated_reply(
            ["noct.acq.seal_received"], ["noct.closed", "noct.acq.council_fight"])
        scene = dict(ParticipantContacts={"nocticula": reply})
        state = rules.SimState(5, 100)
        state.available_contacts = set()
        state.flags.update(reply["Requires"])
        self.assertTrue(rules.sim_participant_contacts(scene, state))
        for loss in reply["Forbids"]:
            lost = copy.deepcopy(state); lost.flags.add(loss)
            self.assertFalse(rules.sim_participant_contacts(scene, lost), loss)
        state.flags.remove("noct.acq.seal_received")
        self.assertFalse(rules.sim_participant_contacts(scene, state))

    def test_all_emitted_table_and_private_participants_have_declared_contact_types(self):
        for scene in self.story["Scenes"]:
            if not scene.get("Participants") or not (scene.get("InteractionHub") == "household.table"
                                                     or scene.get("PrivateParticipants")):
                continue
            self.assertTrue(scene["ParticipantContacts"], scene["Id"])
            for route in scene["Participants"]:
                women = [w for w in scene.get("ParticipantWomen", [])
                         if self.story["SeatWomen"][w]["Relationship"] == route]
                for woman in women or [route]:
                    self.assertIn(woman, scene["ParticipantContacts"], scene["Id"])

    def test_arueshalae_seat_does_not_import_another_rows_native_recruitment(self):
        body = "household.pair.seelah_arueshalae.arueshalae_body"
        self.assertNotIn(body, self.story["SeatWomen"]["arueshalae"]["Requires"])
        row = self.model.by_id["household.pair.seelah_arueshalae.company"]
        self.assertIn(body, row["Requires"])
        for sid in ("household.pair.galfrey_arueshalae.settle.good",
                    "household.pair.galfrey_arueshalae.settle.evil"):
            scene = self.model.by_id[sid]
            self.assertNotIn(body, scene["Requires"])
            self.assertEqual(scene["ForbidOverrides"]["arueshalae_dead"], "arueshalae.trickster.returned")

    def test_body_witness_cannot_be_redefined_as_a_letter(self):
        payload = copy.deepcopy(self.story)
        scene = next(s for s in payload["Scenes"] if s.get("ContactWitness"))
        scene["ParticipantContacts"]["arueshalae"].update(Kind="letter", Options=[])
        self.assertIn("Current contact witness must be evaluated, never saved: " + scene["Id"],
                      rules.validate(rules.Model(payload)))

    def test_herrax_history_remains_readable_after_the_named_women_leave(self):
        scene = self.model.by_id["herrax.house.predecessor"]
        self.assertNotIn("crossroute.chivarro.unavailable", scene["Forbids"])
        self.assertNotIn("crossroute.minagho.unavailable", scene["Forbids"])
        state = rules.SimState(4, 100)
        state.flags.update(scene["Requires"])
        state.flags.update(("crossroute.chivarro.unavailable", "crossroute.minagho.unavailable",
                            "chivarro.epoch_unavailable", "minagho.epoch_unavailable"))
        self.assertTrue(rules.sim_available(self.model, scene, state))

    def test_ghost_is_not_a_body_and_owned_remote_declarations_survive(self):
        ghost = self.story["Presences"]["hepzamirah.presence.ghost"]["Unit"]
        units = {unit for option in contract_j01.body_options(self.story, "hepzamirah") for unit in option["Units"]}
        self.assertNotIn(ghost, units)
        self.assertIn(self.story["Presences"]["hepzamirah.presence"]["Unit"], units)
        payload = copy.deepcopy(self.story)
        projected = dict(Id="household.pair.eliandra_areelu.inspection", InteractionHub="household.table",
            Participants=["areelu"], ParticipantWomen=[], Requires=[], Forbids=[],
            ParticipantContacts={"areelu": dict(Kind="projection", Requires=["areelu.trickster.lens_held"],
                                               Forbids=["areelu.incinerated"], Options=[])})
        payload["Scenes"].append(projected)
        contract_j01.install(payload)
        current = projected["ParticipantContacts"]["areelu"]
        self.assertEqual(current["Kind"], "projection")
        self.assertIn("areelu.trickster.lens_held", current["Requires"])
        self.assertIn("areelu.incinerated", current["Forbids"])
        self.assertIn("areelu.epoch_unavailable", current["Forbids"])


if __name__ == "__main__":
    unittest.main()
