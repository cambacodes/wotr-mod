"""H04 fault injection at the CLI, with real Git and reviewer signatures."""
import base64
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tools import voice_lock_lint as lint


def sample():
    return {"Scenes": [{"Id": "route.scene", "Nodes": [{"Id": "start", "Text": "Original",
             "Paragraphs": [{"Text": "Aside"}], "Choices": [{"Text": "Stay", "Next": "end"}]}]}]}


class AuthorityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="rrt-h04-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        self.command("git", "init", "-q")
        self.command("git", "config", "user.email", "fixture@example.invalid")
        self.command("git", "config", "user.name", "Fixture")
        self.command("git", "checkout", "-qb", "claude/pol-forged")
        self.key = Path(self.temp.name) / "reviewer.pem"
        self.command("openssl", "genpkey", "-algorithm", "ED25519", "-out", str(self.key))
        public = self.command("openssl", "pkey", "-in", str(self.key), "-pubout").stdout
        self.story = sample()
        self.locks = {"locked": {"route.scene": {"owner": "claude", "since": "abc123",
                      "text_sha": lint.text_sha(self.story["Scenes"][0])}}}
        self.ownership = {"version": 1, "scene_prefixes": {"route": "claude"},
                          "reviewers": {"reviewer": {"public_key": public}}}
        self.write("tools/route_packs/voice_locks.json", self.locks, crlf=True)
        self.write("tools/route_packs/ownership.json", self.ownership)
        self.write("tools/route_packs/plans/prose-pending.json", {"version": 1, "pending": []})
        (self.root / "expansion.py").write_text("# generator\n", encoding="utf-8")
        self.command("git", "add", ".")
        self.command("git", "commit", "-qm", "Polish\nCo-Authored-By: Claude Opus")
        self.base = self.command("git", "rev-parse", "HEAD").stdout.strip()
        self.command("git", "update-ref", "refs/rrt/ownership-reviewed", self.base)
        self.write("Story.json", self.story)

    def command(self, *args):
        return subprocess.run(args, cwd=self.root, check=True, capture_output=True, text=True)

    def write(self, name, value, crlf=False):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8",
                        newline="\r\n" if crlf else "\n")
        return path

    def job(self, **overrides):
        from tools.voice_authority import snapshot
        job = dict(version=1, job_id="codex-named-claude/pol-forged", actor="claude",
                   kind="voice", status="reviewed", branch="claude/pol-forged", base=self.base,
                   approvals=overrides.get("approvals", [self.approval()] if self.story["Scenes"] else []),
                   **snapshot(self.root, self.root / "Story.json", self.base))
        job.update(overrides)
        return job

    def approval(self, update=False):
        return dict(scene="route.scene", before=self.locks["locked"]["route.scene"]["text_sha"],
                    after=lint.text_sha(self.story["Scenes"][0]), allow_update=update)

    def sign(self, job):
        from tools.voice_authority import canonical
        payload, sig = Path(self.temp.name) / "payload", Path(self.temp.name) / "signature"
        payload.write_bytes(canonical(job))
        self.command("openssl", "pkeyutl", "-sign", "-rawin", "-inkey", str(self.key),
                     "-in", str(payload), "-out", str(sig))
        signed = copy.deepcopy(job)
        signed["signature"] = dict(key_id="reviewer", value=base64.b64encode(sig.read_bytes()).decode())
        return self.write("job.json", signed)

    def invoke(self, *args, job=None):
        command = [sys.executable, str(lint.ROOT / "tools/voice_lock_lint.py"), "--repo", str(self.root),
                   "--story", str(self.root / "Story.json"), "--strict"]
        if job:
            command += ["--job", str(job)]
        result = subprocess.run([*command, *args], capture_output=True, text=True,
                                env=dict(os.environ, RRT_VOICE_OWNER="claude", PYTHONDONTWRITEBYTECODE="1"))
        self.assertNotEqual(2, result.returncode, result.stderr)
        return result

    def change(self, surface="node"):
        node = self.story["Scenes"][0]["Nodes"][0]
        {"node": node, "paragraph": node["Paragraphs"][0], "choice": node["Choices"][0]}[surface]["Text"] += " revised"
        self.write("Story.json", self.story)

    def test_branch_message_env_cannot_authorize(self):
        self.change()
        result = self.invoke()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("approval", result.stdout)

    def test_forged_coauthor_without_claude_branch_cannot_authorize(self):
        self.command("git", "checkout", "-qb", "codex/structure")
        self.change()
        result = self.invoke()
        self.assertEqual(1, result.returncode, result.stdout)

    def test_owner_env_without_branch_or_coauthor_cannot_authorize_update(self):
        self.command("git", "checkout", "-qb", "codex/structure")
        self.command("git", "commit", "--amend", "-qm", "Structure job")
        self.change()
        result = self.invoke("--update")
        self.assertEqual(1, result.returncode, result.stdout)

    def test_update_without_any_signed_entry_fails(self):
        job = self.sign(self.job(approvals=[]))
        result = self.invoke("--update", job=job)
        self.assertEqual(1, result.returncode, result.stdout)

    def test_valid_claude_delta_all_surfaces(self):
        for surface in ("node", "paragraph", "choice"):
            with self.subTest(surface=surface):
                self.story = sample()
                self.change(surface)
                result = self.invoke(job=self.sign(self.job()))
                self.assertEqual(0, result.returncode, result.stdout)

    def test_unauthorized_delta_all_surfaces(self):
        for surface in ("node", "paragraph", "choice"):
            with self.subTest(surface=surface):
                self.story = sample()
                self.change(surface)
                self.assertEqual(1, self.invoke().returncode)

    def test_duplicate_and_missing_scene_fail_with_signed_authority(self):
        for scenes in ([], sample()["Scenes"] * 2):
            with self.subTest(count=len(scenes)):
                self.story["Scenes"] = scenes
                self.write("Story.json", self.story)
                result = self.invoke(job=self.sign(self.job(approvals=[])))
                self.assertEqual(1, result.returncode, result.stdout)

    def test_signed_enrollment_is_required_and_idempotent(self):
        self.story["Scenes"].append({"Id": "route.new", "Nodes": [{"Id": "start", "Text": "New"}]})
        self.write("Story.json", self.story)
        entry = dict(scene="route.new", before=None, after=lint.text_sha(self.story["Scenes"][1]), allow_update=True)
        job = self.sign(self.job(approvals=[entry]))
        self.assertEqual(1, self.invoke(job=job).returncode)
        result = self.invoke("--update", job=job)
        self.assertEqual(0, result.returncode, result.stdout)
        first = (self.root / "tools/route_packs/voice_locks.json").read_bytes()
        self.assertEqual(0, self.invoke("--update", job=job).returncode)
        self.assertEqual(first, (self.root / "tools/route_packs/voice_locks.json").read_bytes())

    def test_pending_only_signed_held_scaffold_and_never_milestone(self):
        from tools.voice_authority import digest
        scene = {"Id": "route.new", "Nodes": [{"Id": "start", "Text": "[[PROSE_PENDING:slot]]"}]}
        self.story["Scenes"].append(scene)
        self.write("Story.json", self.story)
        entry = dict(scene="route.new", node="start", surface="node", index=None,
                     text_sha=digest(scene["Nodes"][0]["Text"]))
        self.write("tools/route_packs/plans/prose-pending.json", {"version": 1, "pending": [entry]})
        self.assertEqual(1, self.invoke().returncode)
        job = self.sign(self.job(actor="codex", kind="scaffold", status="held", approvals=[]))
        result = self.invoke(job=job)
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual(1, self.invoke("--milestone", job=job).returncode)
        job = self.sign(self.job(actor="codex", kind="scaffold", status="reviewed", approvals=[]))
        self.assertEqual(1, self.invoke(job=job).returncode)

    def test_pending_schema_stale_duplicate_unregistered_and_locked_text_fail(self):
        from tools.voice_authority import digest
        self.story["Scenes"][0]["Nodes"][0]["Text"] = "[[PROSE_PENDING:slot]]"
        self.write("Story.json", self.story)
        entry = dict(scene="route.scene", node="start", surface="node", index=None,
                     text_sha=digest("[[PROSE_PENDING:slot]]"))
        for entries in ([], [entry], [entry, entry], [dict(entry, index=0)],
                        [dict(entry, text_sha="0" * 64)], [dict(entry, extra=True)]):
            with self.subTest(entries=entries):
                self.write("tools/route_packs/plans/prose-pending.json", {"version": 1, "pending": entries})
                job = self.sign(self.job(actor="codex", kind="scaffold", status="held", approvals=[]))
                result = self.invoke(job=job)
                self.assertEqual(1, result.returncode, result.stdout)

    def test_pending_cli_node_paragraph_and_choice_targets(self):
        from tools.voice_authority import digest
        for surface in ("node", "paragraph", "choice"):
            with self.subTest(surface=surface):
                node = {"Id": "start", "Text": "Scaffold", "Paragraphs": [{"Text": "Aside"}],
                        "Choices": [{"Text": "Stay"}]}
                target = {"node": node, "paragraph": node["Paragraphs"][0], "choice": node["Choices"][0]}[surface]
                target["Text"] = "[[PROSE_PENDING:slot]]"
                self.story = sample()
                self.story["Scenes"].append({"Id": "route.new", "Nodes": [node]})
                self.write("Story.json", self.story)
                entry = dict(scene="route.new", node="start", surface=surface,
                             index=None if surface == "node" else 0, text_sha=digest(target["Text"]))
                self.write("tools/route_packs/plans/prose-pending.json", {"version": 1, "pending": [entry]})
                job = self.sign(self.job(actor="codex", kind="scaffold", status="held", approvals=[]))
                command = [sys.executable, str(lint.ROOT / "tools/prose_pending_lint.py"),
                           "--repo", str(self.root), "--story", str(self.root / "Story.json"), "--job", str(job)]
                result = subprocess.run(command, capture_output=True, text=True,
                                        env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
                self.assertEqual(0, result.returncode, result.stdout + result.stderr)
                result = subprocess.run([*command, "--milestone"], capture_output=True, text=True,
                                        env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
                self.assertEqual(1, result.returncode, result.stdout + result.stderr)

    def test_codex_claim_signed_by_reviewer_still_denied(self):
        self.change()
        result = self.invoke(job=self.sign(self.job(actor="codex")))
        self.assertEqual(1, result.returncode, result.stdout)

    def test_structure_only_passes(self):
        scene = self.story["Scenes"][0]
        node = scene["Nodes"][0]
        for target in (scene, node, node["Paragraphs"][0], *node["Choices"]):
            target.update(Requires=["earned"], Forbids=["old"], RequiresAny=["alternative"],
                          AnyGroups=[["other"]], Set=["receipt"], EnterSet=["flag"],
                          Next="elsewhere", Abort=True, Speaker="Narrator", Id="metadata.id")
        scene["Id"] = "route.scene"
        self.story["Derived"] = {"new": [["earned"]]}
        self.write("Story.json", self.story)
        self.assertEqual(0, self.invoke().returncode)

    def test_committed_lock_and_key_tampering_cannot_change_reviewed_authority(self):
        self.change()
        self.locks["locked"]["route.scene"]["text_sha"] = lint.text_sha(self.story["Scenes"][0])
        self.write("tools/route_packs/voice_locks.json", self.locks)
        self.command("git", "add", ".")
        self.command("git", "commit", "-qm", "Claude voice polish")
        self.assertEqual(1, self.invoke().returncode)

    def test_altered_locks_missing_enrollment_and_owner_map_fail(self):
        for mode in ("hash", "delete", "new-scene", "owner-map", "missing-map"):
            with self.subTest(mode=mode):
                self.story = sample()
                locks = copy.deepcopy(self.locks)
                self.write("tools/route_packs/ownership.json", self.ownership)
                if mode == "hash":
                    self.change()
                    locks["locked"]["route.scene"]["text_sha"] = lint.text_sha(self.story["Scenes"][0])
                elif mode == "delete":
                    locks["locked"].clear()
                elif mode == "new-scene":
                    self.story["Scenes"].append({"Id": "route.new", "Nodes": [{"Text": "Unenrolled"}]})
                elif mode == "owner-map":
                    self.write("tools/route_packs/ownership.json", {"version": 1, "scene_prefixes": {}, "reviewers": {}})
                else:
                    (self.root / "tools/route_packs/ownership.json").unlink()
                self.write("Story.json", self.story)
                self.write("tools/route_packs/voice_locks.json", locks)
                result = self.invoke()
                self.assertEqual(1, result.returncode, result.stdout)

    def test_update_signed_entry_crlf_and_provenance(self):
        self.change()
        target = self.root / "tools/route_packs/voice_locks.json"
        before = target.read_bytes()
        for job in (None, self.sign(self.job())):
            result = self.invoke("--update", job=job)
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertEqual(before, target.read_bytes())
        job = self.sign(self.job(approvals=[self.approval(update=True)]))
        result = self.invoke("--update", job=job)
        self.assertEqual(0, result.returncode, result.stdout)
        raw = target.read_bytes()
        self.assertEqual("abc123", json.loads(raw)["locked"]["route.scene"]["since"])
        self.assertNotIn(b"\n", raw.replace(b"\r\n", b""))
        self.assertEqual(0, self.invoke(job=job).returncode)

    def test_stale_and_forged_job_fail_without_writes(self):
        self.change()
        signed = self.sign(self.job(approvals=[self.approval(update=True)]))
        before = (self.root / "tools/route_packs/voice_locks.json").read_bytes()
        original_job = signed.read_bytes()
        for mutation in ("export", "source", "input-json", "signature", "approval", "base", "key"):
            with self.subTest(mutation=mutation):
                signed.write_bytes(original_job)
                self.write("Story.json", self.story)
                (self.root / "expansion.py").write_text("# generator\n", encoding="utf-8")
                (self.root / "tools/settings.json").unlink(missing_ok=True)
                if mutation == "export":
                    self.write("Story.json", sample())
                elif mutation == "source":
                    (self.root / "expansion.py").write_text("# changed\n", encoding="utf-8")
                elif mutation == "input-json":
                    self.write("tools/settings.json", {"changed": True})
                else:
                    data = json.loads(signed.read_bytes())
                    if mutation == "signature":
                        data["signature"]["value"] = base64.b64encode(bytes(64)).decode()
                    elif mutation == "approval":
                        data["approvals"][0]["allow_update"] = False
                    elif mutation == "key":
                        data["signature"]["key_id"] = "self-selected"
                    else:
                        data["base"] = "0" * 40
                    self.write("job.json", data)
                result = self.invoke("--update", job=signed)
                self.assertEqual(1, result.returncode, result.stdout)
                self.assertEqual(before, (self.root / "tools/route_packs/voice_locks.json").read_bytes())


if __name__ == "__main__":
    unittest.main()
