"""Performed receipts and earned Drezen continuation for Eritrice's round-two situations."""
import copy
import subprocess
import types
import unittest

from storylines import eritrice_council as council
from storylines import eritrice_minutes as minutes
from storylines import eritrice_trickster as route
from tools import rrt_verify as verify


class EritriceRoundTwoTests(unittest.TestCase):
    def setUp(self):
        self.payload = {"Scenes": copy.deepcopy(route.SCENES + minutes.SCENES + council.SCENES),
                        "Relationships": {"eritrice": copy.deepcopy(route.RELATIONSHIP)}}
        route.integrate(self.payload)
        minutes.integrate(self.payload)
        council.integrate(self.payload)
        self.scenes = {s["Id"]: s for s in self.payload["Scenes"]}

    def play(self, sid, flags, selected):
        """Follow actual selectable answers; never match a different branch by terminal flags."""
        scene = self.scenes[sid]
        state = set(flags)
        node = scene["Nodes"][0]
        for _ in range(30):
            state.update(node.get("EnterSet", []))
            answers = [(i, c) for i, c in enumerate(node["Choices"])
                       if set(c["Requires"]) <= state and not set(c["Forbids"]) & state]
            self.assertTrue(answers, (sid, node["Id"], state))
            desired = selected.get(node["Id"])
            if desired is not None:
                answer = next((c for i, c in answers if i == desired), None)
                self.assertIsNotNone(answer, (sid, node["Id"], desired))
            else:
                answer = answers[0][1]
            state.update(answer["Set"])
            if answer["Abort"]:
                return state
            if answer["Next"] is None:
                state.add(sid)
                return state
            node = self.node(sid, answer["Next"])
        self.fail("Unexpected cycle in " + sid)

    def test_performed_hearing_walks_and_abandoned_offer_keep_distinct_results(self):
        base = {"trickster.ever", "eritrice.started", minutes.POINT_ONE}
        receipts = {council.K + s for s in ("alichino_handled", "argued_own_case", "chair_recused")}
        for caught in (False, True):
            for approach, witness_index, receipt in (
                (0, 0, "alichino_handled"), (1, 1, "argued_own_case"), (2, 2, "chair_recused"),
            ):
                initial = base | ({route.CAUGHT} if caught else set())
                promised = self.play(council.EXPEL, initial, {"rule": approach})
                self.assertFalse(promised & receipts)
                performed = self.play(council.HEARING, promised, {"witness": witness_index, "offer": 0})
                self.assertEqual(performed & receipts, {council.K + receipt})
                self.assertIn(council.HEARING, performed)
            promised = self.play(council.EXPEL, base, {"rule": 0})
            abandoned = self.play(council.HEARING, promised, {"witness": 0, "offer": 1})
            self.assertFalse(abandoned & receipts)
            self.assertIn(council.PENDING, abandoned)

    def test_selected_apology_and_late_answers_supply_only_their_own_receipts(self):
        for threat, ruling in ((True, "ruling"), (False, "ruling_betrayal")):
            initial = {"trickster", "trickster.ever", route.LATCHED}
            if threat:
                initial.add(route.THREAT)
            arranged = self.play(route.P + "fought.tabled", initial, {ruling: 0})
            self.assertNotIn(route.APOLOGISED, arranged)
            self.assertNotIn(route.RETURNED, arranged)
            spoken = self.play(route.VISIT, arranged, {})
            self.assertIn(route.APOLOGISED, spoken)
            self.assertIn(route.RETURNED, spoken)
        for choice in range(3):
            result = self.play(route.P + "epilogue.commit", {"trickster.ever", route.STARTED}, {"page": choice})
            self.assertEqual(route.P + "late_accepted" in result, choice == 0)

    def node(self, scene, node):
        return next(n for n in self.scenes[scene]["Nodes"] if n["Id"] == node)

    def test_hearing_receipts_follow_actions_not_preparation(self):
        request = council.EXPEL
        hearing = council.HEARING
        for node, intention, receipt, action in (
            ("trick", "withdrawal_planned", "alichino_handled", "signed"),
            ("argue", "defense_planned", "argued_own_case", "defense"),
            ("recuse", "recusal_planned", "chair_recused", "recusal"),
        ):
            answer = self.node(request, node)["Choices"][0]
            self.assertEqual(answer["Set"], [council.K + intention])
            self.assertNotIn(council.K + receipt, answer["Set"])
            self.assertEqual(self.node(hearing, action)["Choices"][0]["Set"], [council.K + receipt])
        self.assertIn(hearing, self.scenes[council.K + "the_motion_to_expel_voted"]["Requires"])
        self.assertEqual(self.node(hearing, "offer")["Choices"][1]["Next"], "unfinished")
        self.assertEqual(self.node(hearing, "unfinished")["Choices"][0]["Set"], [council.PENDING])

    def test_apology_payment_arranges_only_then_spoken_action_returns(self):
        for node in ("ruling", "ruling_betrayal"):
            payment = self.node(route.P + "fought.tabled", node)["Choices"][0]
            self.assertEqual(payment["Crusade"]["Amount"], -200)
            self.assertIn(route.P + "apology_arranged", payment["Set"])
            self.assertNotIn(route.APOLOGISED, payment["Set"])
            self.assertNotIn(route.RETURNED, payment["Set"])
        spoken = self.node(route.VISIT, "apology")["Choices"][0]
        self.assertEqual(spoken["Set"], [route.RETURNED, route.APOLOGISED])
        self.assertEqual(self.scenes[route.VISIT]["ContactUnit"], route.UNIT)
        self.assertTrue(self.scenes[route.VISIT]["TricksterDevice"])
        self.assertEqual(self.payload["Presences"]["eritrice.presence"]["Dialog"], "hub")

    def test_extraction_blocks_all_preparation_siblings_without_pain_question(self):
        self.assertEqual(self.payload["SeenCues"][minutes.EXTRACTED], ["f4a908e91c5c447418fa52ddc589184f"])
        model = verify.Model(self.payload)
        before = verify.SimState(5, 5000)
        before.flags.update(("trickster.ever", "eritrice.started", minutes.POINT_ONE,
                             minutes.CONVENING, minutes.ESSENCE, "council.cauldron_given"))
        for sid in (minutes.ESSENCE, council.EVE, council.K + "a_lie_for_the_chair"):
            self.assertIn(minutes.EXTRACTED, self.scenes[sid]["Forbids"])
            self.assertIn("council.debrief_motion", self.scenes[sid]["Forbids"])
            self.assertIn("council.walked_out", self.scenes[sid]["Forbids"])
            after = copy.deepcopy(before)
            after.flags.add(minutes.EXTRACTED)
            self.assertFalse(verify.sim_available(model, model.by_id[sid], after))
        report = self.scenes[minutes.M + "extraction_account"]
        self.assertIn(minutes.URGED, report["Requires"])
        self.assertIn(minutes.EXTRACTED, report["Requires"])
        self.assertNotIn(minutes.ESSENCE_GIVEN, report["Requires"])

    def test_first_night_and_repeat_have_distinct_mornings_and_slots(self):
        self.assertIn(minutes.M + "night", self.scenes[minutes.RECORD]["Requires"])
        self.assertNotIn(minutes.ADJOURNED, self.scenes[minutes.RECORD]["Requires"])
        self.assertEqual(self.node(minutes.ADJOURNED, "cut")["Choices"][0]["Next"], minutes.ADJOURNED + ".explicit.1")
        self.assertEqual(self.node(council.TWICE, "carried")["Choices"][0]["Next"], council.TWICE + ".explicit.1")
        morning = self.scenes[council.K + "second_morning"]
        self.assertIn(council.K + "twice_nightly_carried", morning["Requires"])
        for sid in (minutes.ADJOURNED, minutes.RECORD, council.TWICE):
            hub = self.scenes[sid + ".drezen"]
            self.assertIn(route.VISIT, hub["Requires"])
            self.assertIn(sid, hub["Forbids"])
            self.assertEqual(hub["ContactUnit"], route.UNIT)
            self.assertTrue(any(sid in c["Set"] for n in hub["Nodes"] for c in n["Choices"] if c["Next"] is None))

    def test_late_acceptance_is_her_aye_and_legacy_exits_are_preserved(self):
        old = types.ModuleType("eritrice_before")
        source = subprocess.check_output(["git", "show", "HEAD:storylines/eritrice_trickster.py"])
        exec(compile(source, "eritrice_before.py", "exec"), old.__dict__)
        sid = route.P + "epilogue.commit"
        baseline = next(s for s in old.SCENES if s["Id"] == sid)
        current = self.scenes[sid]
        self.assertEqual([n["Id"] for n in baseline["Nodes"]], [n["Id"] for n in current["Nodes"]])
        for before, after in zip(baseline["Nodes"], current["Nodes"]):
            self.assertEqual(before["Choices"], after["Choices"])
        self.assertEqual(self.node(sid, "aye")["EnterSet"], [route.P + "late_accepted"])
        for node in ("nay", "silence"):
            self.assertNotIn("EnterSet", self.node(sid, node))
        self.assertIn(sid + ".explicit.1", [p.get("Id") for p in self.node(sid, "aye")["Paragraphs"]])


if __name__ == "__main__":
    unittest.main()
