"""Save references from the pre-polish user saves must survive every export."""
import copy
import hashlib
import json
import unittest

from tools import savecompat


def sample():
    return {"Scenes": [{"Id": "route.scene", "Owner": "Woman", "Nodes": [
        {"Id": "start", "Choices": [
            {"Id": "first", "Text": "Old words"},
            {"Id": "second", "Text": "Other words"}]},
        {"Id": "end", "Choices": []}]}]}


class SaveCompatibilityTests(unittest.TestCase):
    def test_generated_story_keeps_frozen_save_references(self):
        # Build from source so a stale development export cannot hide a regression.
        from expansion import make_expansion
        failures = savecompat.check(make_expansion())
        self.assertEqual([], failures, "\n".join(failures))

    def test_frozen_revision(self):
        baseline = json.loads(savecompat.BASELINE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(savecompat.BASELINE_REVISION, baseline["Revision"])
        self.assertEqual("b79badabd664b9b7cbf371806a2e28419440d957b8b2ef27507d74fd46456bba",
                         baseline["SourceSHA256"])
        frozen = json.dumps(baseline["Scenes"], ensure_ascii=False, sort_keys=True,
                            separators=(",", ":")).encode("utf-8")
        self.assertEqual("23318cfdb52a16042cd746b8a7ca35c5759b4a537d571b3ee6702f35c7277c2c",
                         hashlib.sha256(frozen).hexdigest())
        self.assertGreater(len(baseline["Scenes"]), 1000)

    def test_additions_and_prose_edits_allowed(self):
        before = sample()
        after = copy.deepcopy(before)
        after["Scenes"][0]["Nodes"][0]["Choices"][0]["Text"] = "Polished words"
        after["Scenes"][0]["Nodes"][0]["Choices"].append({"Text": "New answer"})
        after["Scenes"][0]["Nodes"].append({"Id": "new", "Choices": []})
        after["Scenes"].append({"Id": "new.scene", "Owner": "Woman", "Nodes": []})
        self.assertEqual([], savecompat.check(after, savecompat.inventory(before)))

    def test_loss_shrink_reorder_and_identity_change_fail(self):
        before = sample()
        baseline = savecompat.inventory(before)
        for mutation in ("scene", "node", "shrink", "reorder", "identity"):
            with self.subTest(mutation=mutation):
                after = copy.deepcopy(before)
                nodes = after["Scenes"][0]["Nodes"]
                choices = nodes[0]["Choices"]
                if mutation == "scene":
                    after["Scenes"].clear()
                elif mutation == "node":
                    nodes.pop()
                elif mutation == "shrink":
                    choices.pop()
                elif mutation == "reorder":
                    choices.reverse()
                else:
                    choices[0]["Id"] = "replacement"
                self.assertTrue(savecompat.check(after, baseline))

    def test_legacy_continue_identity_is_not_an_index(self):
        before = sample()
        scene = before["Scenes"][0]
        scene["Owner"] = "Epilogue"
        scene["Nodes"][0]["Choices"] = [{"Text": "Continue"}]
        baseline = savecompat.inventory(before)
        self.assertEqual("answer.route.scene.start.continue",
                         baseline["Scenes"][scene["Id"]]["start"][0]["GuidFor"])
        after = copy.deepcopy(before)
        after["Scenes"][0]["Nodes"][0]["Choices"].append({"Text": "Stay"})
        self.assertTrue(savecompat.check(after, baseline))

    def test_explicit_suffix_preserves_legacy_exit_with_appended_branch(self):
        before = sample()
        scene = before["Scenes"][0]
        scene["Owner"] = "Epilogue"
        scene["Nodes"][0]["Choices"] = [{"Text": "Continue"}]
        baseline = savecompat.inventory(before)
        after = copy.deepcopy(before)
        choices = after["Scenes"][0]["Nodes"][0]["Choices"]
        choices[0].update(Id="continue", Text="Leave")
        choices.append({"Text": "Stay", "Next": "end"})
        self.assertEqual([], savecompat.check(after, baseline))
        choices[0]["Id"] = "replacement"
        self.assertTrue(savecompat.check(after, baseline))

    def test_explicit_legacy_exit_cannot_gain_mechanics(self):
        before = sample()
        before["Scenes"][0]["Owner"] = "Epilogue"
        before["Scenes"][0]["Nodes"][0]["Choices"] = [{"Text": "Continue"}]
        baseline = savecompat.inventory(before)
        for key in savecompat.EXIT_MECHANICS:
            with self.subTest(mechanic=key):
                after = copy.deepcopy(before)
                choices = after["Scenes"][0]["Nodes"][0]["Choices"]
                choices[0].update(Id="continue", **{key: ["changed"]})
                choices.append({"Text": "New stance", "Next": "end"})
                self.assertEqual(["Legacy ending exit mechanics changed: route.scene/start"],
                                 savecompat.check(after, baseline))

    def test_codas_keep_their_original_registration_anchors(self):
        from expansion import make_expansion
        ids = [scene["Id"] for scene in make_expansion()["Scenes"]]
        for anchor, coda, following in (
            ("nenio.trickster.epilogue.scholar", "nenio.lastcall.page", "nenio.trickster.react.sosiel_point_five"),
            ("terendelev.trickster.epilogue.rest", "terendelev.lastcall.page", "terendelev.trickster.react.galfrey.letter_awning"),
        ):
            with self.subTest(coda=coda):
                self.assertEqual(ids.index(anchor) + 1, ids.index(coda))
                self.assertLess(ids.index(coda), ids.index(following))

    def test_inline_host_identity_cannot_disappear(self):
        before = sample()
        before["Scenes"][0].update(ReturnToList=True, AnswerLists=["host.one", "host.two"])
        baseline = savecompat.inventory(before)
        self.assertEqual(["answer.route.scene.host.one.start.0", "answer.route.scene.host.two.start.0"],
                         baseline["Scenes"]["route.scene"]["start"][0]["GuidFor"])
        after = copy.deepcopy(before)
        after["Scenes"][0]["AnswerLists"].pop()
        self.assertTrue(savecompat.check(after, baseline))

    def test_continue_before_has_no_answer_blueprint(self):
        story = sample()
        story["Scenes"][0]["ContinueBefore"] = {"Cue": "native.cue"}
        self.assertEqual([], savecompat.choice_identities(
            story["Scenes"][0], story["Scenes"][0]["Nodes"][0])[0]["GuidFor"])


if __name__ == "__main__":
    unittest.main()
