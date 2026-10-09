"""Branch receipts, current presence and campaign prices for struct3-b."""
import copy
import unittest

from tests.story_fixture import fresh_story
from tools import rrt_verify as verify
from storylines import areelu_trickster as areelu, areelu_afterlogue as afterlogue


class StructuralRoundThreeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = verify.Model(cls.story)
        cls.scenes = cls.model.by_id

    def state(self, chapter, flags=(), finances=2000):
        state = verify.SimState(chapter, 0)
        state.flags.update(flags)
        if "trickster" in state.flags:
            state.flags.add("trickster.ever")
        state.crusade_resources = {"Finances": finances}
        verify.sim_complete(self.model, state)
        return state

    def play(self, sid, state, selected):
        scene = self.scenes[sid]
        node = scene["Nodes"][0]
        path = []
        scratch = copy.deepcopy(state)
        for _ in range(50):
            scratch.flags.update(node.get("EnterSet", []))
            available = [i for i, answer in enumerate(node["Choices"])
                         if verify.sim_choice_available(answer, scratch)]
            self.assertTrue(available, (sid, node["Id"]))
            index = selected.get(node["Id"], available[0])
            choice = node["Choices"][index]
            self.assertTrue(verify.sim_choice_available(choice, scratch), (sid, node["Id"], index))
            # Build the explicit traversal with a scratch state. The public
            # simulator applies each debit and durable receipt to the real state.
            path.append(choice)
            scratch.flags.update(choice["Set"])
            if choice.get("Crusade"):
                resource = choice["Crusade"]["Resource"]
                scratch.crusade_resources[resource] += choice["Crusade"]["Amount"]
            verify.sim_complete(self.model, scratch)
            if choice["Abort"] or choice["Next"] is None:
                break
            node = self.model.nodes[sid][choice["Next"]]
        else:
            self.fail("unexpected cycle")
        return verify.sim_play(self.model, scene, state, set(), (0, path))

    @staticmethod
    def visible(paragraph, state):
        return (set(paragraph.get("Requires", [])) <= state.flags
                and not set(paragraph.get("Forbids", [])) & state.flags
                and all(set(group) & state.flags for group in paragraph.get("AnyGroups", [])))

    def test_oath_victim_receipts_and_later_loss_in_both_endings(self):
        p = "camellia.trickster."
        histories = {
            "nurah": {"nurah.trickster.returned", "nurah.dead_camellia"},
            "soana": {"soana.trickster.returned", "soana.killed_by_camellia"},
            "kaylessa": {"kaylessa.trickster.returned", "kaylessa.camellia_killed"},
        }
        for suffix in ("", "_camp"):
            for woman, history in histories.items():
                with self.subTest(suffix=suffix, woman=woman):
                    state = self.state(5, {"trickster", *history})
                    root = self.model.nodes[p + "kills_answered.oath" + suffix]["start"]
                    index = next(i for i, c in enumerate(root["Choices"])
                                 if c["Next"] == woman and verify.sim_choice_available(c, state))
                    self.assertTrue(self.play(p + "kills_answered.oath" + suffix, state,
                                              {"start": index, "ask": 0}))
                    self.assertIn(p + "oath_loophole", state.flags)
                    self.assertEqual({p + "oath_victim." + woman},
                                     state.flags & {p + "oath_victim." + w for w in histories})
                    verify.sim_complete(self.model, state)
                    for ending in ("kept", "commit"):
                        paras = self.model.nodes[p + "epilogue." + ending]["page"]["Paragraphs"]
                        living = next(x for x in paras if p + "oath_victim.available" in x["Requires"])
                        self.assertTrue(self.visible(living, state))
                        # Historical return and unrelated available victims survive
                        # the selected woman's later epoch loss.
                        lost = copy.deepcopy(state)
                        lost.flags.add(woman + ".epoch_unavailable")
                        for other, other_history in histories.items():
                            if other != woman:
                                lost.flags.update(other_history)
                        verify.sim_complete(self.model, lost)
                        self.assertFalse(self.visible(living, lost))
                        self.assertIn(next(iter(history)), lost.flags)
                        lost_readers = [x for x in paras if p + "oath_victim." + woman in x["Requires"]
                                        and woman + ".present_now" in x["Forbids"]]
                        self.assertEqual(1, sum(self.visible(x, lost) for x in lost_readers))

    def test_legacy_anonymous_oath_does_not_infer_any_living_victim(self):
        p = "camellia.trickster."
        state = self.state(6, {"trickster", p + "oath_loophole",
                              "nurah.trickster.returned", "nurah.dead_camellia"})
        for ending in ("kept", "commit"):
            paras = self.model.nodes[p + "epilogue." + ending]["page"]["Paragraphs"]
            living = next(x for x in paras if p + "oath_victim.available" in x["Requires"])
            self.assertFalse(self.visible(living, state))
            historical = [x for x in paras if p + "oath_victim.recorded" in x["Forbids"]]
            self.assertEqual(1, sum(self.visible(x, state) for x in historical))

    def test_burned_kept_and_filed_accounts_after_cloud(self):
        sid = areelu.P + "report.promise"
        variants = self.story["NativeEpilogueEdits"][afterlogue.CUE_0004]
        def matches(groups, flags):
            return any(all((f[1:] not in flags) if f.startswith("!") else f in flags for f in g)
                       for g in groups)
        for choice, departure in ((1, True), (2, False), (3, False), (4, True)):
            state = self.state(6, {"trickster", areelu.STRUCK, areelu.WAGERED,
                                   areelu.BET, "sacrifice", "ending.trickster", areelu.COMMITTED})
            self.assertTrue(self.play(sid, state, {"start": 0, "confront": choice, "why": 1}))
            self.assertEqual(departure, areelu.REPORT_DEPARTED in state.flags)
            afterword = self.scenes[areelu.P + "report.afterword"]["Nodes"][0]["Choices"]
            self.assertEqual(not departure, verify.sim_choice_available(afterword[0], state))
            self.assertTrue(verify.sim_choice_available(afterword[1], state))
            candidates = [variants, *variants.get("Variants", [])]
            selected = [v["Replacement"] for v in candidates if matches(v["When"], state.flags)]
            self.assertEqual([afterlogue.LINE_DEPARTED if departure else afterlogue.LINE_SPARED], selected)

    def test_experiments_charge_before_witness_and_preserve_independent_refusal(self):
        for kind, price in (("convicts", 500), ("graft", 300)):
            key = areelu.EXPERIMENT + kind
            scene = self.scenes[key]
            self.assertIn(areelu.CELL_LIST, scene["AnswerLists"])
            self.assertEqual(areelu.CELL_RETURN, scene["NativeReturnCue"])
            poor = self.state(5, {"trickster"}, price - 1)
            self.assertFalse(verify.sim_choice_available(scene["Nodes"][0]["Choices"][0], poor))
            for choice, receipt, paid in ((0, "paid", price), (1, "refused", 0)):
                state = self.state(5, {"trickster"})
                self.assertTrue(self.play(key, state, {"start": choice}))
                self.assertEqual(2000 - paid, state.crusade_resources["Finances"])
                self.assertIn(key + "." + receipt, state.flags)
                self.assertIn(key + ".witnessed", state.flags)
                later = self.scenes[key + ".outcome"]
                self.assertFalse(verify.sim_available(self.model, later, state))
                state.hour = 48
                verify.sim_complete(self.model, state)
                self.assertTrue(verify.sim_available(self.model, later, state))
                funded = copy.deepcopy(state)
                self.assertTrue(self.play(key + ".outcome", funded, {"account": 0}))
                self.assertIn(key + ".batch_funded", funded.flags)
                self.assertEqual(2000 - paid - price, funded.crusade_resources["Finances"])
                self.assertTrue(self.play(key + ".outcome", state, {"account": 1}))
                self.assertIn(key + ".outcome_read", state.flags)
                self.assertIn(key + ".batch_refused", state.flags)
                report = areelu.P + "report." + ("commission" if kind == "graft" else kind)
                report_choices = self.model.nodes[report]["start"]["Choices"]
                self.assertEqual(choice == 0, verify.sim_choice_available(report_choices[0], state))
                refusal_index = 3 if kind == "convicts" else 2
                self.assertEqual(choice == 1, verify.sim_choice_available(report_choices[refusal_index], state))
                paras = self.model.nodes[report]["start"]["Paragraphs"]
                self.assertTrue(any(self.visible(x, state) and key + "." + receipt in x["Requires"]
                                    for x in paras))
            abandoned = self.state(5, {"trickster"})
            self.assertFalse(self.play(key, abandoned, {"start": 2}))
            self.assertNotIn(key + ".witnessed", abandoned.flags)
            self.assertEqual(2000, abandoned.crusade_resources["Finances"])


if __name__ == "__main__":
    unittest.main()
