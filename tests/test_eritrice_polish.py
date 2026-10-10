"""Reviewed Eritrice action receipts, including the staged E14b interjection."""
import copy
import itertools
import unittest
from unittest.mock import patch

from storylines import eritrice_council as council
from storylines import eritrice_minutes as minutes
from storylines import eritrice_trickster as route
from tools import rrt_verify as verify
from tools import text_structure_lint



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class EritricePolishTests(unittest.TestCase):
    def setUp(self):
        self.payload = {
            "Scenes": copy.deepcopy(route.SCENES + minutes.SCENES + council.SCENES),
            "Relationships": {"eritrice": copy.deepcopy(route.RELATIONSHIP)},
            "Etudes": {}, "SeenCues": {},
        }
        council.integrate(self.payload)
        council.integrate_public(self.payload)
        # Reuse the engine's current-path contract; do not add a route gate.
        from expansion import trickster_now_setups
        trickster_now_setups(self.payload)
        self.model = verify.Model(self.payload)
        self.scene = self.model.by_id[council.PUBLIC]
        self.nodes = self.model.nodes[council.PUBLIC]
        self.receipts = {council.LIE_SPOKEN, council.LIE_WITHDRAWN,
                         council.TRUTH_SPOKEN, council.PROTECTION_SPOKEN}

    def world(self, *flags, chapter=5):
        state = verify.SimState(chapter, 5000)
        state.flags.update(flags)
        return state

    @staticmethod
    def choices(node, state):
        return [c for c in node["Choices"] if all(state.has(f) for f in c["Requires"])
                and not any(state.has(f) for f in c["Forbids"])]

    def paths(self, state, node="start", prefix=()):
        answers = self.choices(self.nodes[node], state)
        self.assertTrue(answers, "Page has no selectable answers: " + node)
        for answer in answers:
            next_state = copy.deepcopy(state)
            next_state.flags.update(answer["Set"])
            path = prefix + (answer,)
            if answer["Next"] is None:
                yield path
            else:
                yield from self.paths(next_state, answer["Next"], path)

    def paragraphs(self, flags):
        page = next(s for s in self.payload["Scenes"]
                    if s["Id"] == "eritrice.trickster.epilogue.we_did_meet")["Nodes"][0]
        return {i for i, p in enumerate(page["Paragraphs"])
                if set(p.get("Requires", ())) <= flags
                and not set(p.get("Forbids", ())) & flags
                and all(set(group) & flags for group in p.get("AnyGroups", ()))}

    def test_public_actions_complete_without_rescue_or_native_effects(self):
        cases = ((council.LIED_FOR_HER, {council.LIE_SPOKEN, council.LIE_WITHDRAWN}),
                 (council.PROTECTION_REQUESTED, {council.PROTECTION_SPOKEN}),
                 (council.TRUTH_FOR_CHADALI, {council.TRUTH_SPOKEN}))
        for approach, expected in cases:
            with self.subTest(approach=approach):
                state = self.world("trickster", "trickster.ever", council.K + "a_lie_for_the_chair", approach)
                self.assertTrue(verify.sim_available(self.model, self.scene, state))
                entry, = self.choices(self.nodes["start"], state)
                self.assertIn(entry["Next"], {"promise", "protect", "truth"})
                observed = set()
                for path in self.paths(state):
                    result = copy.deepcopy(state)
                    self.assertTrue(verify.sim_play(self.model, self.scene, result,
                        {"committed": {"eritrice.committed"}, "closed": {"eritrice.closed"}}, ((1, 0, 0, len(path)), list(path))))
                    receipt = result.flags & self.receipts
                    self.assertEqual(len(receipt), 1)
                    observed.update(receipt)
                    self.assertEqual(result.flags - state.flags,
                                     receipt | {council.PUBLIC, "eritrice.started"})
                    self.assertFalse(verify.sim_available(self.model, self.scene, result))
                    for answer in path:
                        self.assertFalse(any(answer.get(field) for field in
                            ("Crusade", "StartEtude", "NativeNext", "Revive", "RemoveItem", "Check")))
                        self.assertFalse(answer["Abort"])
                self.assertEqual(observed, expected)

    def test_every_defensive_mixed_history_has_one_continuation(self):
        approaches = (council.LIED_FOR_HER, council.PROTECTION_REQUESTED, council.TRUTH_FOR_CHADALI)
        for count in range(1, 4):
            for selected in itertools.combinations(approaches, count):
                with self.subTest(selected=selected):
                    answers = self.choices(self.nodes["start"], self.world(*selected))
                    self.assertEqual([a["Next"] for a in answers], ["promise" if council.LIED_FOR_HER in selected
                                     else "protect" if council.PROTECTION_REQUESTED in selected else "truth"])
        self.assertEqual(self.choices(self.nodes["start"], self.world()), [])

    def test_missed_native_opportunity_does_not_reopen_on_return(self):
        base = ("trickster", "trickster.ever", council.K + "a_lie_for_the_chair", council.LIED_FOR_HER)
        for blocker in ("council.walked_out", "council.debrief_motion", minutes.EXTRACTED,
                        "eritrice.essence_given", "eritrice.lost_at_council",
                        "eritrice.closed", "trickster.failed", council.PUBLIC):
            for returned in ((), ("eritrice.trickster.returned",)):
                self.assertFalse(verify.sim_available(self.model, self.scene, self.world(*base, blocker, *returned)))
        for chapter in (3, 4, 6):
            self.assertFalse(verify.sim_available(self.model, self.scene, self.world(*base, chapter=chapter)))
        self.assertFalse(verify.sim_available(self.model, self.scene, self.world(*base[1:])))
        self.assertFalse(verify.sim_available(self.model, self.scene, self.world("trickster", "trickster.ever", council.LIED_FOR_HER)))
        self.assertFalse(verify.sim_available(self.model, self.scene, self.world(*base[:-1])))
        # Selecting either returning native discussion produces no action receipt.
        for native in ("request_immediate_extraction", "discuss_quarrel"):
            state = self.world(*base, native)
            self.assertTrue(verify.sim_available(self.model, self.scene, state))
            self.assertFalse(state.flags & self.receipts)

    def test_pending_and_performed_records_are_distinct(self):
        page = next(s for s in self.payload['Scenes'] if s['Id'] == 'eritrice.trickster.epilogue.we_did_meet')['Nodes'][0]
        for approach, receipt in ((council.LIED_FOR_HER, council.LIE_SPOKEN),
                                  (council.LIED_FOR_HER, council.LIE_WITHDRAWN),
                                  (council.TRUTH_FOR_CHADALI, council.TRUTH_SPOKEN),
                                  (council.PROTECTION_REQUESTED, council.PROTECTION_SPOKEN)):
            pending = [p for p in page['Paragraphs'] if approach in p['Requires'] and receipt in p['Forbids']]
            performed = [p for p in page['Paragraphs'] if receipt in p['Requires']]
            self.assertTrue(pending, approach)
            self.assertTrue(performed, receipt)
            for flags, done in (({approach, 'crossroute.chadali.available'}, False),
                                ({approach, receipt, 'crossroute.chadali.available'}, True)):
                def enabled(p):
                    return set(p['Requires']) <= flags and not set(p['Forbids']) & flags
                self.assertTrue(all(enabled(p) != done for p in pending))
                self.assertTrue(all(enabled(p) == done for p in performed))

    def test_receipts_follow_the_selected_or_rendered_action(self):
        self.assertFalse(self.nodes["start"].get("EnterSet"))
        self.assertTrue(all(not c["Set"] for c in self.nodes["start"]["Choices"]))
        self.assertEqual(saved_answer(self.nodes["promise"]["Choices"], 0)["Set"], [council.LIE_SPOKEN])
        self.assertEqual(saved_answer(self.nodes["promise"]["Choices"], 1)["Set"], [council.LIE_WITHDRAWN])
        self.assertEqual(saved_answer(self.nodes["protect"]["Choices"], 0)["Set"], [council.PROTECTION_SPOKEN])
        self.assertEqual(saved_answer(self.nodes["truth"]["Choices"], 0)["Set"], [council.TRUTH_SPOKEN])
        request = next(s for s in council.SCENES if s["Id"] == council.K + "a_lie_for_the_chair")
        approaches = next(n for n in request["Nodes"] if n["Id"] == "want")["Choices"]
        self.assertEqual([c["Set"] for c in approaches], [[council.LIED_FOR_HER], [council.PROTECTION_REQUESTED], [council.TRUTH_FOR_CHADALI]])

    def test_native_return_speaker_and_player_text_contracts(self):
        self.assertEqual(self.scene["AnswerLists"], ["2e2e6dd9c2bf7d748972de8d5a65b8ad"])
        self.assertTrue(self.scene["ReturnToList"])
        self.assertIsNone(self.scene["NativeReturnCue"])
        self.assertFalse(self.scene.get("ContactUnit"))
        self.assertFalse(self.scene.get("Areas"))
        self.assertEqual(self.scene["DelayHours"], 0)
        self.assertEqual([n["Id"] for n in self.scene["Nodes"]], ["start", "promise", "lie_response", "lie_ruling", "withdraw_response", "protect", "protect_record", "truth", "truth_record"])
        for node in self.scene["Nodes"]:
            if node["Id"] == "lie_response":
                self.assertEqual(node["Speaker"], "Narrator")
            else:
                self.assertEqual(node["SpeakerUnit"], "4a47d14a45ce264408a1c6a33345dd89")
            self.assertFalse(node.get("Paragraphs"))
        self.assertEqual(text_structure_lint.check({"Scenes": council.PUBLIC_SCENES}), {"hard": [], "review": []})
        self.assertEqual(saved_answer(self.nodes["lie_response"]["Choices"], 0)["Next"], "lie_ruling")
        self.assertIsNone(saved_answer(self.nodes["truth_record"]["Choices"], 0)["Next"])

    def test_hook_appends_without_moving_existing_scenes(self):
        baseline = copy.deepcopy(route.SCENES + minutes.SCENES + council.SCENES)
        self.assertEqual([s["Id"] for s in self.payload["Scenes"][:-1]], [s["Id"] for s in baseline])
        self.assertEqual(self.payload["Scenes"][-1]["Id"], council.PUBLIC)

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        with patch.dict(self.nodes['promise']['Choices'][0], Set=[]):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_receipts_follow_the_selected_or_rendered_action()


if __name__ == "__main__":
    unittest.main()
