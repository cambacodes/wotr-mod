"""Round-three counterexamples: real entry histories and borrowed-room staging."""
import copy
import unittest
from unittest.mock import patch

from storylines import eritrice_council as council
from storylines import eritrice_minutes as minutes
from storylines import eritrice_trickster as route
from tests.story_fixture import fresh_story
from tools import rrt_verify as verify


class EritriceRoundThreeTests(unittest.TestCase):
    def setUp(self):
        payload = {"Scenes": copy.deepcopy(route.SCENES + minutes.SCENES + council.SCENES),
                   "Relationships": {"eritrice": copy.deepcopy(route.RELATIONSHIP)}}
        route.integrate(payload)
        minutes.integrate(payload)
        council.integrate(payload)
        self.scenes = {s["Id"]: s for s in payload["Scenes"]}

    def walk(self, sid, flags, picks):
        scene = self.scenes[sid]
        nodes = {n["Id"]: n for n in scene["Nodes"]}
        state = set(flags)
        node = scene["Nodes"][0]
        visited = []
        for _ in range(40):
            state.update(node.get("EnterSet", []))
            visited.append(node["Id"])
            answers = [c for c in node["Choices"] if set(c["Requires"]) <= state
                       and not set(c["Forbids"]) & state]
            self.assertTrue(answers, (sid, node["Id"], state))
            target = picks.get(node["Id"])
            answer = next((c for c in answers if c["Next"] == target), None) if target else next(iter(answers))
            self.assertIsNotNone(answer, (sid, node["Id"], target))
            state.update(answer["Set"])
            if answer["Next"] is None or answer["Abort"]:
                if not answer["Abort"]:
                    state.add(sid)
                return state, visited
            node = nodes[answer["Next"]]
        self.fail("Cycle: " + sid)

    def test_three_entries_recall_only_their_performed_history(self):
        base = {"trickster", "trickster.ever"}
        # Perform the entry scenes rather than inventing the motion receipts.
        hall, _ = self.walk(route.P + "council.motion", base, {"start": "declared"})
        petition, _ = self.walk(route.P + "council.late_motion", base | {"council.debrief_motion"}, {})
        petition, _ = self.walk(route.VISIT, petition, {"open": "friendly"})
        fought, _ = self.walk(route.P + "fought.tabled", base | {route.LATCHED},
                              {"start": "stranger", "stranger": "ruling_betrayal"})
        reconciled, _ = self.walk(route.VISIT, fought, {"open": "apology"})
        self.assertIn(route.APOLOGISED, reconciled)
        for initial, suffix in ((hall, ""), (petition, "_petition"), (reconciled, "_reconciled")):
            flags = initial | {route.STARTED}
            host = ".drezen" if suffix else ""
            with self.subTest(entry=suffix):
                flags, point = self.walk(minutes.POINT_ONE + host, flags,
                    {"rules": "motion" + suffix, "motion" + suffix: "minutes" + suffix})
                flags, _ = self.walk(minutes.CONVENING + host, flags, {})
                flags, quill = self.walk(minutes.QUILL + host, flags,
                    {"held": "hand_honest" if not suffix else "hand" + suffix})
                self.assertIn(minutes.WROTE, flags)
                self.assertIn("motion" + suffix, point)
                self.assertIn("minutes" + suffix, point)
                self.assertIn("hand_honest" if not suffix else "hand" + suffix, quill)
                for other in ("", "_petition", "_reconciled"):
                    if other != suffix:
                        self.assertNotIn("motion" + other, point)
                        self.assertNotIn("hand_honest" if not other else "hand" + other, quill)

    def test_drezen_furniture_remains_local_through_both_mornings(self):
        for sid, scene in self.scenes.items():
            if sid.endswith('.drezen'):
                self.assertEqual(scene['InteractionHub'], 'eritrice.presence')
                self.assertEqual(scene['ContactUnit'], route.UNIT)
                self.assertFalse(scene.get('Remote'))
        for sid in (minutes.ADJOURNED, minutes.RECORD, council.TWICE, council.K + 'second_morning'):
            self.assertIn(sid + '.drezen', self.scenes)

    def test_assembled_proof_has_answers_after_chadali_closure(self):
        payload = fresh_story()
        model = verify.Model(payload)
        scene = next(s for s in payload["Scenes"] if s["Id"] == council.PROOF)
        self.scenes[council.PROOF] = scene
        for orange in (set(), {council.ORANGE}):
            flags = {"trickster.ever", route.STARTED, minutes.POINT_ONE, "chadali.closed"} | orange
            state = verify.SimState(5, 5000)
            state.flags.update(flags)
            verify.sim_complete(model, state)
            self.assertTrue(verify.sim_available(model, model.by_id[council.PROOF], state))
            start = next(n for n in scene["Nodes"] if n["Id"] == "start")
            self.assertTrue(all("chadali.closed" not in c["Forbids"] for c in start["Choices"]))
            for target in ("purse", "speak"):
                self.walk(council.PROOF, state.flags, {"start": target})

    def test_both_third_readings_keep_lastcall_and_refusals_stay_out(self):
        payload = fresh_story()
        model = verify.Model(payload)
        page = model.by_id["eritrice.lastcall.page"]
        self.assertEqual(page["ForbidOverrides"][route.DECLINED], route.COMMITTED)
        for suffix in ("", ".drezen"):
            flags, _ = self.walk(route.P + "council.second_reading" + suffix,
                {"trickster.ever", route.STARTED, minutes.QUILL}, {"start": "refused"})
            self.assertIn(route.DECLINED, flags)
            flags, _ = self.walk(route.P + "council.third_reading" + suffix,
                flags, {"start": "aye"})
            self.assertIn(route.ON_RECORD, flags)
            state = verify.SimState(6, 5000)
            state.flags.update(flags | {"trickster.lastcall.taken", "ending.trickster"})
            verify.sim_complete(model, state)
            self.assertTrue(verify.sim_available(model, page, state), (suffix, page["Requires"]))
            refused = copy.deepcopy(state)
            refused.flags.discard(route.COMMITTED)
            verify.sim_complete(model, refused)
            self.assertFalse(verify.sim_available(model, page, refused))
            closed = copy.deepcopy(state)
            closed.flags.add(route.CLOSED)
            verify.sim_complete(model, closed)
            self.assertFalse(verify.sim_available(model, page, closed))

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        scene = self.scenes[minutes.POINT_ONE]
        choice = next(c for n in scene['Nodes'] if n['Id'] == 'rules'
                      for c in n['Choices'] if c['Next'] == 'motion')
        with patch.dict(choice, Next='motion_petition'):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_three_entries_recall_only_their_performed_history()


if __name__ == "__main__":
    unittest.main()
