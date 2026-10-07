"""Text ownership enforcement must ignore all gameplay metadata."""
import contextlib
import copy
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools import voice_lock_lint as lint


def sample():
    return {"Scenes": [{"Id": "route.scene", "Nodes": [
        {"Id": "start", "Text": "Anevia's café — {n}wait.{/n}",
         "Paragraphs": [{"Text": "Conditional prose", "Requires": ["earned"]}],
         "Choices": [{"Text": "Stay", "Next": "end"}, {"Text": "Leave"}]},
        {"Id": "end", "Text": "Goodbye", "Choices": []}]}]}


def manifest(story):
    return {"locked": {"route.scene": {"owner": "claude", "since": "abc123",
                                       "text_sha": lint.text_sha(story["Scenes"][0])}}}


class VoiceLockTests(unittest.TestCase):
    def run_lint(self, story, data, *args, owner="", context=("codex/gates", "Fix gates")):
        with tempfile.TemporaryDirectory(prefix="rrt-voice-lock-") as directory:
            story_path, lock_path = Path(directory) / "Story.json", Path(directory) / "locks.json"
            story_path.write_text(json.dumps(story, ensure_ascii=False), encoding="utf-8")
            lock_path.write_text(json.dumps(data, ensure_ascii=False) + "\n", encoding="utf-8", newline="\r\n")
            with patch.dict("os.environ", {"RRT_VOICE_OWNER": owner}), \
                    patch.object(lint, "git_context", return_value=context), \
                    contextlib.redirect_stdout(io.StringIO()):
                result = lint.main(["--story", str(story_path), "--locks", str(lock_path), *args])
            raw = lock_path.read_bytes()
            return result, json.loads(raw), raw

    def test_empty_initial_inventory_and_unchanged_lock_pass(self):
        lint.validate_locks(json.loads(lint.LOCKS.read_text(encoding="utf-8")))
        for data in ({"locked": {}}, manifest(sample())):
            self.assertEqual(0, self.run_lint(sample(), data, "--strict")[0])

    def test_hash_serialization_is_stable_utf8(self):
        expected = [["Anevia's café — {n}wait.{/n}", ["Conditional prose"], ["Stay", "Leave"]],
                    ["Goodbye", [], []]]
        payload = json.dumps(expected, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        self.assertEqual(hashlib.sha256(payload).hexdigest(), lint.text_sha(sample()["Scenes"][0]))

    def test_each_text_surface_is_protected(self):
        for surface in ("node", "paragraph", "choice"):
            with self.subTest(surface=surface):
                story = sample()
                node = story["Scenes"][0]["Nodes"][0]
                target = {"node": node, "paragraph": node["Paragraphs"][0], "choice": node["Choices"][0]}[surface]
                target["Text"] += " changed"
                self.assertEqual(1, self.run_lint(story, manifest(sample()), "--strict")[0])

    def test_metadata_changes_do_not_trip_lint(self):
        story = sample()
        scene = story["Scenes"][0]
        node = scene["Nodes"][0]
        for target in (scene, node, node["Paragraphs"][0], *node["Choices"]):
            target.update(Requires=["new"], Forbids=["old"], RequiresAny=["alternative"],
                          AnyGroups=[["other"]], Set=["receipt"], EnterSet=["flag"],
                          Next="elsewhere", Abort=True, Speaker="Narrator", Id="changed.id")
        scene["Id"] = "route.scene"
        story["Derived"] = {"new": [["earned"]]}
        self.assertEqual(0, self.run_lint(story, manifest(sample()), "--strict")[0])

    def test_boundaries_and_order_are_hashed(self):
        original = sample()["Scenes"][0]
        changed = copy.deepcopy(original)
        changed["Nodes"][0]["Choices"].reverse()
        self.assertNotEqual(lint.text_sha(original), lint.text_sha(changed))
        # Joining raw strings would fail to distinguish these two texts.
        a = {"Nodes": [{"Text": "ab", "Choices": [{"Text": "c"}]}]}
        b = {"Nodes": [{"Text": "a", "Choices": [{"Text": "bc"}]}]}
        self.assertNotEqual(lint.text_sha(a), lint.text_sha(b))

    def test_missing_and_duplicate_targets_fail_even_for_voice_jobs(self):
        for scenes in ([], sample()["Scenes"] * 2):
            self.assertEqual(1, self.run_lint({"Scenes": scenes}, manifest(sample()), "--strict",
                                            context=("claude/voice-anevia", ""))[0])

    def test_voice_job_classification(self):
        for branch, message in (("claude/voice-anevia", ""), ("claude/pol-anevia", ""),
                                ("claude/polish-anevia", ""), ("integration", "Claude voice: Anevia"),
                                ("integration", "Polish Anevia\nCo-Authored-By: Claude Opus")):
            self.assertTrue(lint.claude_voice_job(branch, message), (branch, message))
        for branch, message in (("claude/gates", ""), ("claude/voicelock", "Add lint"),
                                ("claude/voice-lock-lint", ""), ("claude/tools/voice-anevia", ""),
                                ("codex/voice-anevia", ""), ("integration", "Fix gates\nCo-Authored-By: Claude Opus"),
                                ("integration", "Add voice lock lint\nCo-Authored-By: Claude Opus"),
                                ("integration", "Change voice")):
            self.assertFalse(lint.claude_voice_job(branch, message), (branch, message))

    def test_authorized_voice_job_passes_without_refreshing_hash(self):
        story, data = sample(), manifest(sample())
        story["Scenes"][0]["Nodes"][0]["Text"] += " rewritten"
        for context in (("claude/voice-anevia", ""), ("integration", "Claude voice rewrite")):
            code, after, _ = self.run_lint(story, data, "--strict", context=context)
            self.assertEqual(0, code)
            self.assertEqual(data, after)

    def test_report_mode_and_env_alone_do_not_refresh(self):
        story, data = sample(), manifest(sample())
        story["Scenes"][0]["Nodes"][0]["Text"] += " rewritten"
        self.assertEqual(0, self.run_lint(story, data)[0])
        code, after, _ = self.run_lint(story, data, "--strict", owner="claude")
        self.assertEqual(1, code)
        self.assertEqual(data, after)

    def test_update_requires_owner_even_on_voice_branch(self):
        data = manifest(sample())
        code, after, _ = self.run_lint(sample(), data, "--update", context=("claude/voice-anevia", ""))
        self.assertEqual(1, code)
        self.assertEqual(data, after)

    def test_update_preserves_provenance_crlf_and_only_existing_locks(self):
        story, data = sample(), manifest(sample())
        story["Scenes"][0]["Nodes"][0]["Text"] += " rewritten"
        story["Scenes"].append({"Id": "unlocked", "Nodes": [{"Text": "Other prose"}]})
        code, after, raw = self.run_lint(story, data, "--strict", "--update", owner="claude")
        self.assertEqual(0, code)
        self.assertEqual({"route.scene"}, set(after["locked"]))
        lock = after["locked"]["route.scene"]
        self.assertEqual(("claude", "abc123"), (lock["owner"], lock["since"]))
        self.assertEqual(lint.text_sha(story["Scenes"][0]), lock["text_sha"])
        self.assertNotIn(b"\n", raw.replace(b"\r\n", b""))
        self.assertEqual(0, self.run_lint(story, after, "--strict")[0])

    def test_invalid_manifest_and_missing_update_target_never_write(self):
        data = manifest(sample())
        invalid = copy.deepcopy(data)
        invalid["locked"]["route.scene"]["text_sha"] = "bad hash"
        for story, locks in ((sample(), invalid), ({"Scenes": []}, data)):
            code, after, _ = self.run_lint(story, locks, "--update", owner="claude")
            self.assertEqual(1, code)
            self.assertEqual(locks, after)


if __name__ == "__main__":
    unittest.main()
