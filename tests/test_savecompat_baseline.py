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
    def test_merge_b10_stance_exits_keep_saved_indices_and_continue_ids(self):
        from tests.story_fixture import fresh_story
        scenes = {s["Id"]: s for s in fresh_story()["Scenes"]}
        for sid, nid, index in (
            ("anevia.trickster.gone.commit", "answer", 17),
            ("anevia.trickster.gone.second_ask", "price", 15),
            ("anevia.trickster.gone.fetched_commit", "answer", 17),
            ("anevia.trickster.gone.fetched_second_ask", "price", 15),
            ("kiana.trickster.late_question", "partner_secret", 2),
            ("kiana.trickster.late_question_letter", "partner_secret", 2),
            ("kiana.trickster.late_question", "partner_refuse", 1),
            ("kiana.trickster.late_question_letter", "partner_refuse", 1),
            ("soana.trickster.returned.terms", "partner_secret_bind", 1),
            ("soana.trickster.returned.terms", "partner_secret_bind_clay", 1),
            ("soana.trickster.returned.second_ask", "partner_secret_price", 2),
            ("soana.trickster.missed.bowl", "partner_secret_terms", 1),
            ("soana.trickster.missed.second_ask", "partner_secret_start", 1),
        ):
            node = next(n for n in scenes[sid]["Nodes"] if n["Id"] == nid)
            answer = node["Choices"][index]
            self.assertTrue(answer["Abort"], (sid, nid, index))
            self.assertEqual(answer["Forbids"], ["trickster.now"])
            self.assertEqual(answer["Set"], [])
        for sid in ("soana.trickster.epilogue.commit", "soana.trickster.epilogue.luck_late"):
            for nid in ("partner_share_start", "partner_secret_start"):
                node = next(n for n in scenes[sid]["Nodes"] if n["Id"] == nid)
                # Integration commit 219bcbe gave these newly authored stance
                # continuations their own IDs; the old page exit stays inert.
                self.assertEqual(savecompat.choice_identities(scenes[sid], node)[0]["GuidFor"],
                                 "answer.%s.%s.accept" % (sid, nid))
                self.assertTrue(node["Choices"][0]["Set"])

    def test_generated_story_keeps_frozen_save_references(self):
        # The gate supplies its fresh export; standalone runs build isolated source.
        from tests.story_fixture import fresh_story
        failures = savecompat.check(fresh_story())
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
        from tests.story_fixture import fresh_story
        ids = [scene["Id"] for scene in fresh_story()["Scenes"]]
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


CHAPLAIN_PREFIX = "nidalynn.trickster."
CHAPLAIN_PRAYED = CHAPLAIN_PREFIX + "chaplain_prayed"
CHAPLAIN_SENT_AWAY = CHAPLAIN_PREFIX + "chaplain_sent_away"


def chaplain_available(item, flags):
    return (set(item["Requires"]) <= flags
            and not set(item["Forbids"]) & flags
            and all(set(group) & flags for group in item.get("AnyGroups", [])))


class NidalynnChaplainTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from tests.story_fixture import fresh_story
        cls.story = fresh_story()
        cls.scene = next(scene for scene in cls.story["Scenes"]
                         if scene["Id"] == CHAPLAIN_PREFIX + "kiln.the_chaplain")
        cls.nodes = {node["Id"]: node for node in cls.scene["Nodes"]}

    def test_all_three_paths_record_only_the_played_outcome(self):
        for index, target in enumerate(("hers", "pray", "leave")):
            with self.subTest(target=target):
                self.assertEqual(self.nodes["want"]["Choices"][index]["Next"], target)
                flags = set()
                node_id = target
                visited = []
                while node_id:
                    self.assertNotIn(node_id, visited)
                    visited.append(node_id)
                    choices = self.nodes[node_id]["Choices"]
                    self.assertEqual(len(choices), 1)
                    choice = choices[0]
                    self.assertTrue(chaplain_available(choice, flags))
                    flags.update(choice["Set"])
                    if node_id == "prayer":
                        self.assertNotIn(CHAPLAIN_PRAYED, flags)
                    if node_id in ("after_prayer", "leave"):
                        self.assertEqual(flags & {CHAPLAIN_PRAYED, CHAPLAIN_SENT_AWAY},
                                         {CHAPLAIN_SENT_AWAY} if target == "leave" else {CHAPLAIN_PRAYED})
                    node_id = choice["Next"]
                self.assertEqual(flags & {CHAPLAIN_PRAYED, CHAPLAIN_SENT_AWAY},
                                 {CHAPLAIN_SENT_AWAY} if target == "leave" else {CHAPLAIN_PRAYED})
                self.assertEqual("prayer" in visited, target != "leave")
                self.assertEqual(self.nodes["end"]["Choices"][0]["Set"], [])

    def test_either_outcome_blocks_repeating_the_visit(self):
        flags = set(self.scene["Requires"])
        self.assertTrue(chaplain_available(self.scene, flags))
        for outcome in (CHAPLAIN_PRAYED, CHAPLAIN_SENT_AWAY):
            with self.subTest(outcome=outcome):
                self.assertFalse(chaplain_available(self.scene, flags | {outcome}))

    def test_report_readers_cover_both_outcomes_but_not_an_unplayed_visit(self):
        reports = [paragraph for scene in self.story["Scenes"]
                   if scene["Id"].startswith(CHAPLAIN_PREFIX + "epilogue.")
                   for node in scene["Nodes"]
                   for paragraph in node.get("Paragraphs", [])
                   if CHAPLAIN_PRAYED in paragraph["Requires"]
                   or any(CHAPLAIN_PRAYED in group for group in paragraph.get("AnyGroups", []))]
        self.assertTrue(reports)
        for paragraph in reports:
            self.assertFalse(chaplain_available(paragraph, set()))
            self.assertTrue(chaplain_available(paragraph, {CHAPLAIN_PRAYED}))
            self.assertTrue(chaplain_available(paragraph, {CHAPLAIN_SENT_AWAY}))




from pathlib import Path
from types import SimpleNamespace

from storylines import (devarra_tower, elyanka_hearse, herrax_house,
                       horzalah_guild, horzalah_trickster, melazmera_hoard)
from tools import prose_pending_lint, slot_brief_lint
from tools.rrt_verify import sim_choice_available

ROOT = Path(__file__).resolve().parents[1]
HOSTS = (
    (herrax_house, "herrax.house.a_night_out", "home", "herrax", 1),
    (herrax_house, "herrax.house.her_rooms", "beside", "herrax", 1),
    (herrax_house, "herrax.house.last_night", "agreed", "herrax", 1),
    (horzalah_guild, "horzalah.trickster.beat.ramparts", "hand", "horzalah", 1),
    (horzalah_guild, "horzalah.trickster.beat.ribbon", "tied", "horzalah", 2),
    (elyanka_hearse, "elyanka.trickster.beat.table", "door2", "elyanka-camilary", 1),
    (elyanka_hearse, "elyanka.trickster.ch6.collateral", "rift2", "elyanka-camilary", 1),
    (melazmera_hoard, "melazmera.trickster.beat.count", "ate", "melazmera", 1),
)


class StructSlotHostTests(unittest.TestCase):
    def test_reachable_continuations_preserve_legacy_terminal_positions(self):
        for module, sid, nid, woman, old_count in HOSTS:
            with self.subTest(scene=sid):
                scene = next(s for s in module.SCENES if s["Id"] == sid)
                host = next(n for n in scene["Nodes"] if n["Id"] == nid)
                slot = sid + ".explicit.1"
                self.assertEqual(old_count + 1, len(host["Choices"]))
                self.assertTrue(all(c["Next"] is None for c in host["Choices"][:old_count]))
                self.assertEqual(slot, host["Choices"][old_count]["Next"])
                path = ROOT / "tools/route_packs/explicit_slots" / woman / (slot + ".json")
                findings, _ = slot_brief_lint.lint([path], {"Scenes": [scene]})
                self.assertEqual([], [f for f in findings if f["severity"] == "hard"])
                disconnected = copy.deepcopy(scene)
                next(n for n in disconnected["Nodes"] if n["Id"] == nid)["Choices"].pop()
                findings, _ = slot_brief_lint.lint([path], {"Scenes": [disconnected]})
                self.assertIn("retired", [f["code"] for f in findings])

    def test_epilogue_appends_after_all_four_existing_paragraphs(self):
        scene = next(s for s in horzalah_trickster.SCENES
                     if s["Id"] == "horzalah.trickster.epilogue.decided")
        page = scene["Nodes"][0]
        self.assertEqual(5, len(page["Paragraphs"]))
        self.assertEqual("horzalah.trickster.epilogue.decided.explicit.1", page["Paragraphs"][4]["Id"])
        self.assertIsNone(page["Choices"][0]["Next"])
        # The registry covers the full export, including route-owned placeholders.
        # A partial host fixture cannot validate unrelated registered targets.
        from tests.story_fixture import fresh_story
        story = fresh_story()
        pending = json.loads((ROOT / "tools/route_packs/plans/prose-pending.json").read_text(encoding="utf-8"))
        self.assertEqual([], prose_pending_lint.check(story, pending, integration=True))
        self.assertTrue(prose_pending_lint.check(story, {"version": 1, "pending": []}, integration=True))

    def test_before_the_end_requires_first_bite_on_flown_branch(self):
        scene = next(s for s in devarra_tower.SCENES if s["Id"] == "devarra.tower.before_the_end")
        climb = next(n for n in scene["Nodes"] if n["Id"] == "climb")
        answer = climb["Choices"][2]
        self.assertEqual("owe_free", answer["Next"])
        flags = {"devarra.trickster.flown"}
        self.assertFalse(sim_choice_available(answer, SimpleNamespace(flags=flags)))
        flags.add("devarra.tower.first_bite")
        self.assertTrue(sim_choice_available(answer, SimpleNamespace(flags=flags)))
        self.assertTrue(sim_choice_available(climb["Choices"][0], SimpleNamespace(flags=set())))


# struct2-05 production witnesses belong to the selected writing gate.
from tests.test_struct2_05 import Structure05Tests


if __name__ == "__main__":
    unittest.main()
