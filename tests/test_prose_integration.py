"""Integration policy and coordinator-ref lifecycle with real protected-ref CLI probes."""
import copy
import json
import subprocess
import sys
import unittest

from tests.test_voice_authority import AuthorityFixture, sample
from tools import prose_pending_lint as pending, voice_authority as authority
from tools import claude_work_queue_lint as queue, prepare_voice_job


class IntegrationTests(AuthorityFixture, unittest.TestCase):
    def invoke_pending(self, *args, script=None):
        return subprocess.run([sys.executable, str(script or pending.ROOT / "tools/prose_pending_lint.py"),
            "--repo", str(self.root), "--story", str(self.root / "Story.json"), *args],
            capture_output=True, text=True, encoding="utf-8", check=False)

    def register(self, sid="route.new", surface="node"):
        node = {"Id": "start", "Text": "Ordinary", "Paragraphs": [{"Text": "Aside"}],
                "Choices": [{"Text": "Stay"}]}
        target = {"node": node, "paragraph": node["Paragraphs"][0], "choice": node["Choices"][0]}[surface]
        target["Text"] = "[PROSE PENDING: choice - deliver the stock]" if surface == "choice" else "[PROSE PENDING: want / act / cost]"
        self.story["Scenes"].append({"Id": sid, "Nodes": [node]})
        self.write("Story.json", self.story)
        entry = dict(scene=sid, node="start", surface=surface, index=None if surface == "node" else 0,
                     text_sha=authority.digest(target["Text"]))
        self.write(authority.PENDING, dict(version=1, pending=[entry]))
        return entry

    def test_integration_registered_targets_all_surfaces_and_milestone(self):
        for surface in ("node", "paragraph", "choice"):
            with self.subTest(surface=surface):
                self.story = sample()
                self.register(surface=surface)
                self.assertEqual(1, self.invoke_pending().returncode)
                result = self.invoke_pending("--integration")
                self.assertEqual(0, result.returncode, result.stdout)
                result = self.invoke("--integration")
                self.assertEqual(0, result.returncode, result.stdout)
                self.assertEqual(1, self.invoke_pending("--integration", "--milestone").returncode)
                self.assertEqual(1, self.invoke("--integration", "--milestone").returncode)

    def test_integration_does_not_waive_target_faults_or_locked_prose(self):
        entry = self.register()
        for entries in ([], [dict(entry, text_sha="0" * 64)], [entry, entry],
                        [dict(entry, node="missing")], [dict(entry, extra=True)]):
            with self.subTest(entries=entries):
                self.write(authority.PENDING, dict(version=1, pending=entries))
                self.assertEqual(1, self.invoke_pending("--integration").returncode)
        self.write(authority.PENDING, dict(version=1, pending=[entry]))
        self.change()
        self.assertEqual(1, self.invoke("--integration").returncode)

    def test_main_reviewed_ref_policy_update_and_worker_commit_fail_closed(self):
        self.command("git", "checkout", "-qb", "claude/trickster-expansion")
        self.ownership["scene_prefixes"]["new.family"] = "claude"
        self.write(authority.OWNERSHIP, self.ownership)
        self.assertEqual(1, self.invoke().returncode)
        self.command("git", "add", authority.OWNERSHIP)
        self.command("git", "commit", "-qm", "Candidate ownership enrollment")
        self.assertEqual(1, self.invoke().returncode)
        # Only the coordinator's explicit pin accepts the reviewed policy.
        reviewed = self.command("git", "rev-parse", "HEAD").stdout.strip()
        self.command("git", "update-ref", "refs/rrt/ownership-reviewed", reviewed, self.base)
        result = self.invoke()
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual(self.ownership, authority.trusted(self.root)[1])
        self.ownership["scene_prefixes"]["forged"] = "claude"
        self.write(authority.OWNERSHIP, self.ownership)
        self.assertEqual(1, self.invoke().returncode)

    def append_fixture(self):
        self.write("development/Story.json", sample())
        self.command("git", "add", "development/Story.json")
        self.command("git", "commit", "-qm", "Coordinator reviewed source/export")
        self.base = self.command("git", "rev-parse", "HEAD").stdout.strip()
        self.command("git", "update-ref", "refs/rrt/ownership-reviewed", self.base)
        node = self.story["Scenes"][0]["Nodes"][0]
        node["Choices"].append({"Text": "[PROSE PENDING: choice - deliver the stock]", "Next": "end"})
        self.write("Story.json", self.story)
        self.write(authority.PENDING, dict(version=1, pending=[dict(scene="route.scene", node="start",
            surface="choice", index=1, text_sha=authority.digest(node["Choices"][1]["Text"]))]))
        request = dict(version=1, job_id="J05b-pending-choice-appends", actor="codex", kind="scaffold",
            status="awaiting-coordinator-approval", hosts=[dict(scene="route.scene",
            before=self.locks["locked"]["route.scene"]["text_sha"])])
        return self.write(prepare_voice_job.REQUEST, request)

    def test_exact_reviewed_append_separate_from_voice_approvals_and_no_lock_update(self):
        request = self.append_fixture()
        before = (self.root / authority.LOCKS).read_bytes()
        job = prepare_voice_job.prepare(self.root, self.root / "Story.json", request)
        records = self.review(job, "append-approvals.json")
        self.assertEqual(1, self.invoke("--integration").returncode)
        self.assertEqual(1, self.invoke("--integration", job=records).returncode)
        result = self.invoke("--integration", "--append-approvals", str(records))
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("1 approved pending-choice appends", result.stdout)
        for flags in (("--update",), ("--milestone",)):
            self.assertEqual(1, self.invoke("--integration", "--append-approvals", str(records), *flags).returncode)
        self.assertEqual(1, self.invoke("--append-approvals", str(records)).returncode)
        self.assertEqual(before, (self.root / authority.LOCKS).read_bytes())

    def test_reviewed_append_rejects_old_text_change_nodes_and_unregistered_labels(self):
        self.append_fixture()
        valid = copy.deepcopy(self.story)
        for mode in ("node", "paragraph", "old-choice", "new-node", "plain-label", "reorder", "delete-choice"):
            with self.subTest(mode=mode):
                self.story = copy.deepcopy(valid)
                node = self.story["Scenes"][0]["Nodes"][0]
                if mode == "node":
                    node["Text"] += " changed"
                elif mode == "paragraph":
                    node["Paragraphs"][0]["Text"] += " changed"
                elif mode == "old-choice":
                    node["Choices"][0]["Text"] += " changed"
                elif mode == "new-node":
                    self.story["Scenes"][0]["Nodes"].append(dict(Id="new", Text="New"))
                elif mode == "plain-label":
                    node["Choices"][1]["Text"] = "Plain new choice"
                elif mode == "reorder":
                    node["Choices"].reverse()
                else:
                    node["Choices"].pop(0)
                self.write("Story.json", self.story)
                job = self.review(dict(version=1, approvals=[self.approval()]), "append-approvals.json")
                self.assertEqual(1, self.invoke("--integration", "--append-approvals", str(job)).returncode)

    def test_request_is_not_authority_and_preparation_needs_actual_append(self):
        request = self.append_fixture()
        self.assertEqual(1, self.invoke("--integration", "--append-approvals", str(request)).returncode)
        self.story = sample()
        self.write("Story.json", self.story)
        self.write(authority.PENDING, dict(version=1, pending=[]))
        with self.assertRaisesRegex(ValueError, "no pending-choice append"):
            prepare_voice_job.prepare(self.root, self.root / "Story.json", request)

    def test_worker_append_records_not_at_ref_are_rejected(self):
        request = self.append_fixture()
        data = prepare_voice_job.prepare(self.root, self.root / "Story.json", request)
        path = self.write("append-approvals.json", data)
        result = self.invoke("--integration", "--append-approvals", str(path))
        self.assertEqual(1, result.returncode, result.stdout)
        self.pin(path)
        self.assertEqual(0, self.invoke("--integration", "--append-approvals", str(path)).returncode)

    def test_held_scaffold_requires_reviewed_record_and_milestone_still_forbids_it(self):
        self.register()
        path = self.write("held-job.json", self.job())
        self.assertEqual(1, self.invoke(job=path).returncode)
        self.pin(path)
        result = self.invoke(job=path)
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual(0, self.invoke_pending("--job", str(path)).returncode)
        self.assertEqual(1, self.invoke("--milestone", job=path).returncode)
        self.assertEqual(1, self.invoke_pending("--milestone", "--job", str(path)).returncode)
        self.review(self.job(status="reviewed"), "held-job.json")
        self.assertEqual(1, self.invoke(job=path).returncode)

    def test_held_job_stale_identity_and_locked_placeholder_fail_without_writes(self):
        self.register()
        job = self.job()
        path = self.review(job, "held-job.json")
        self.assertEqual(0, self.invoke(job=path).returncode)
        before = (self.root / authority.LOCKS).read_bytes()
        for mode in ("export", "source", "input-json", "pending", "branch", "locked", "base"):
            with self.subTest(mode=mode):
                self.story = sample()
                self.register()
                (self.root / "expansion.py").write_text("# generator\n", encoding="utf-8")
                (self.root / "tools/settings.json").unlink(missing_ok=True)
                self.command("git", "checkout", "claude/pol-forged")
                self.assertEqual(0, self.invoke(job=path).returncode)
                if mode == "export":
                    self.story["Scenes"][1]["Nodes"][0]["Text"] += " changed"
                    self.write("Story.json", self.story)
                elif mode == "source":
                    (self.root / "expansion.py").write_text("# changed\n", encoding="utf-8")
                elif mode == "input-json":
                    self.write("tools/settings.json", {"changed": True})
                elif mode == "pending":
                    self.write(authority.PENDING, dict(version=1, pending=[]))
                elif mode == "branch":
                    self.command("git", "checkout", "-qb", "codex/other")
                elif mode == "base":
                    self.command("git", "commit", "--allow-empty", "-qm", "Worker advanced HEAD")
                else:
                    self.story["Scenes"][0]["Nodes"][0]["Text"] = "[PROSE PENDING: locked]"
                    self.write("Story.json", self.story)
                self.assertEqual(1, self.invoke(job=path).returncode)
                self.assertEqual(before, (self.root / authority.LOCKS).read_bytes())

    def test_held_scaffold_cannot_authorize_registered_locked_placeholder(self):
        node = self.story["Scenes"][0]["Nodes"][0]
        node["Text"] = "[PROSE PENDING: locked]"
        self.write("Story.json", self.story)
        self.write(authority.PENDING, dict(version=1, pending=[dict(scene="route.scene", node="start",
            surface="node", index=None, text_sha=authority.digest(node["Text"]))]))
        path = self.review(self.job(), "held-job.json")
        self.assertEqual(0, self.invoke_pending("--job", str(path)).returncode)
        result = self.invoke(job=path)
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("changed prose requires reviewed Claude approval", result.stdout)

    def test_integration_never_waives_locked_placeholder_or_enrolls_pending_scene(self):
        self.register(sid="route.scene")
        self.story["Scenes"] = self.story["Scenes"][1:]
        self.write("Story.json", self.story)
        self.assertEqual(1, self.invoke("--integration").returncode)
        self.story = sample()
        self.register()
        before = (self.root / authority.LOCKS).read_bytes()
        self.assertEqual(0, self.invoke("--integration").returncode)
        self.assertEqual(before, (self.root / authority.LOCKS).read_bytes())

    def test_mutations_prove_integration_target_and_milestone_policy(self):
        entry = self.register()
        folder = self.mutant("pending-target", "prose_pending_lint.py", '    targets = {}',
                             '    if integration:\n        return []\n    targets = {}')
        self.write(authority.PENDING, dict(version=1, pending=[dict(entry, text_sha="0" * 64)]))
        self.assertEqual(1, self.invoke_pending("--integration").returncode)
        result = self.invoke_pending("--integration", script=folder / "prose_pending_lint.py")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.write(authority.PENDING, dict(version=1, pending=[entry]))
        folder = self.mutant("pending-milestone", "prose_pending_lint.py", '        if milestone:',
                             '        if milestone and not integration:')
        self.assertEqual(1, self.invoke_pending("--integration", "--milestone").returncode)
        result = self.invoke_pending("--integration", "--milestone", script=folder / "prose_pending_lint.py")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)


class QueueTests(unittest.TestCase):
    def test_queue_requests_allow_multiple_beats_per_scene(self):
        request = dict(scene="route.scene", woman="woman", beat="want / act / cost", ruling=3)
        self.assertEqual([], queue.check([request, dict(request, node="start", choice=1), request]))
        for value in ({"version": 1, "pending": []}, [dict(request, choice=1)],
                      [dict(request, node="start", choice=True)], [dict(request, ruling=False)],
                      [dict(request, beat="")], [dict(request, extra=True)]):
            self.assertTrue(queue.check(value))


if __name__ == "__main__":
    unittest.main()
