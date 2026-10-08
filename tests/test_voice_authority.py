"""Protected-ref approvals exercised through real Git and CLI counterexamples."""
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tools import voice_authority as authority, voice_lock_lint as lint, voice_approve


def sample():
    return {"Scenes": [{"Id": "route.scene", "Nodes": [{"Id": "start", "Text": "Original",
             "Paragraphs": [{"Text": "Aside"}], "Choices": [{"Text": "Stay", "Next": "end"}]}]}]}


class AuthorityFixture:
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="rrt-voice-approvals-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        self.command("git", "init", "-q")
        self.command("git", "config", "user.email", "fixture@example.invalid")
        self.command("git", "config", "user.name", "Fixture")
        self.command("git", "checkout", "-qb", "claude/pol-forged")
        self.story = sample()
        self.locks = {"locked": {"route.scene": {"owner": "claude", "since": "abc123",
                      "text_sha": lint.text_sha(self.story["Scenes"][0])}}}
        self.ownership = {"version": 1, "scene_prefixes": {"route": "claude"}}
        self.write(authority.LOCKS, self.locks, crlf=True)
        self.write(authority.OWNERSHIP, self.ownership)
        self.write(authority.APPROVALS, dict(version=1, approvals=[]))
        self.write(authority.PENDING, dict(version=1, pending=[]))
        (self.root / "expansion.py").write_text("# generator\n", encoding="utf-8")
        self.command("git", "add", ".")
        self.command("git", "commit", "-qm", "Polish\nCo-Authored-By: Claude Opus")
        self.base = self.command("git", "rev-parse", "HEAD").stdout.strip()
        self.command("git", "update-ref", authority.REVIEWED_REF, self.base)
        self.write("Story.json", self.story)
        self.write("Base.json", sample())

    def command(self, *args):
        return subprocess.run(args, cwd=self.root, check=True, capture_output=True,
                              text=True, encoding="utf-8")

    def write(self, name, value, crlf=False):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8",
                        newline="\r\n" if crlf else "\n")
        return path

    def pin(self, path):
        """Simulate coordinator CAS without moving the worker's HEAD."""
        previous = self.command("git", "rev-parse", authority.REVIEWED_REF).stdout.strip()
        self.command("git", "add", str(path.relative_to(self.root)))
        tree = self.command("git", "write-tree").stdout.strip()
        commit = self.command("git", "commit-tree", tree, "-p", previous,
                              "-m", "Coordinator reviewed records").stdout.strip()
        self.command("git", "update-ref", authority.REVIEWED_REF, commit, previous)

    def review(self, data, name=authority.APPROVALS):
        path = self.write(name, data)
        self.pin(path)
        return path

    def approval(self, sid="route.scene", **overrides):
        scene = next(scene for scene in self.story["Scenes"] if scene["Id"] == sid)
        entry = dict(scene=sid, before_sha=self.locks["locked"].get(sid, {}).get("text_sha"),
                     after_sha=lint.text_sha(scene), owner="claude", source_branch="claude/voice",
                     source_commit=self.base, reason="Coordinator accepted the owned voice rewrite")
        entry.update(overrides)
        return entry

    def approve(self, *entries):
        return self.review(dict(version=1, approvals=list(entries or [self.approval()])))

    def job(self, **overrides):
        job = dict(version=1, job_id="held-scaffold", actor="codex", kind="scaffold", status="held",
                   branch=self.command("git", "branch", "--show-current").stdout.strip(),
                   base=self.command("git", "rev-parse", "HEAD").stdout.strip(), approvals=[],
                   **authority.snapshot(self.root, self.root / "Story.json"))
        job.update(overrides)
        return job

    def invoke(self, *args, job=None, script=None):
        command = [sys.executable, str(script or lint.ROOT / "tools/voice_lock_lint.py"),
                   "--repo", str(self.root), "--story", str(self.root / "Story.json"), "--strict"]
        if job:
            command += ["--job", str(job)]
        result = subprocess.run([*command, *args], capture_output=True, text=True, encoding="utf-8",
                                env=dict(os.environ, RRT_VOICE_OWNER="claude", PYTHONDONTWRITEBYTECODE="1"))
        self.assertNotEqual(2, result.returncode, result.stderr)
        return result

    def change(self, surface="node"):
        node = self.story["Scenes"][0]["Nodes"][0]
        {"node": node, "paragraph": node["Paragraphs"][0], "choice": node["Choices"][0]}[surface]["Text"] += " revised"
        self.write("Story.json", self.story)

    def mutant(self, label, filename, old, new):
        """Copy the CLI seam to system temp and disable one protection."""
        folder = Path(self.temp.name) / label
        folder.mkdir()
        for name in ("voice_authority.py", "voice_lock_lint.py", "prose_pending_lint.py"):
            source = (lint.ROOT / "tools" / name).read_text(encoding="utf-8")
            if name == filename:
                self.assertEqual(1, source.count(old), "mutation no longer targets one protection")
                source = source.replace(old, new)
            (folder / name).write_text(source, encoding="utf-8")
        return folder


class AuthorityTests(AuthorityFixture, unittest.TestCase):
    def test_branch_message_env_cannot_authorize(self):
        self.change()
        result = self.invoke()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("approval", result.stdout)
        self.command("git", "checkout", "-qb", "codex/structure")
        self.assertEqual(1, self.invoke().returncode)
        self.assertEqual(1, self.invoke("--update").returncode)

    def test_exact_reviewed_approval_all_surfaces(self):
        for surface in ("node", "paragraph", "choice"):
            with self.subTest(surface=surface):
                self.story = sample()
                self.change(surface)
                self.approve()
                result = self.invoke()
                self.assertEqual(0, result.returncode, result.stdout)

    def test_worker_written_and_committed_approval_is_not_authority(self):
        self.change()
        self.write(authority.APPROVALS, dict(version=1, approvals=[self.approval()]))
        self.assertEqual(1, self.invoke().returncode)
        self.command("git", "add", ".")
        self.command("git", "commit", "-qm", "Claude approved voice")
        self.assertEqual(1, self.invoke().returncode)

    def test_wrong_before_after_scene_and_owner_rejected_without_writes(self):
        self.change()
        before = (self.root / authority.LOCKS).read_bytes()
        for change in (dict(before_sha="0" * 64), dict(after_sha="0" * 64),
                       dict(scene="route.other"), dict(owner="codex"), dict(before_sha=None)):
            with self.subTest(change=change):
                self.approve(self.approval(**change))
                for flags in ((), ("--update",)):
                    self.assertEqual(1, self.invoke(*flags).returncode)
                    self.assertEqual(before, (self.root / authority.LOCKS).read_bytes())

    def test_missing_duplicate_and_unlocked_owned_scene_fail(self):
        for scenes in ([], sample()["Scenes"] * 2,
                       sample()["Scenes"] + [dict(Id="route.new", Nodes=[dict(Text="Unenrolled")])]):
            with self.subTest(count=len(scenes)):
                self.story["Scenes"] = scenes
                self.write("Story.json", self.story)
                self.assertEqual(1, self.invoke().returncode)
                self.assertEqual(1, self.invoke("--update").returncode)

    def test_enrollment_uses_source_commit_and_is_idempotent(self):
        self.story["Scenes"].append(dict(Id="route.new", Nodes=[dict(Id="start", Text="New")]))
        self.write("Story.json", self.story)
        entry = self.approval("route.new", source_commit="a" * 40)
        self.approve(entry)
        self.assertEqual(1, self.invoke().returncode)
        result = self.invoke("--update")
        self.assertEqual(0, result.returncode, result.stdout)
        target = self.root / authority.LOCKS
        first = target.read_bytes()
        self.assertEqual(dict(owner="claude", since="a" * 40, text_sha=entry["after_sha"]),
                         json.loads(first)["locked"]["route.new"])
        self.assertEqual(0, self.invoke("--update").returncode)
        self.assertEqual(first, target.read_bytes())

    def test_update_only_approved_scene_preserves_other_locks_and_crlf(self):
        second = dict(Id="route.other", Nodes=[dict(Id="start", Text="Keep")])
        self.story["Scenes"].append(second)
        self.locks["locked"]["route.other"] = dict(owner="claude", since="keep-since", text_sha=lint.text_sha(second))
        target = self.write(authority.LOCKS, self.locks, crlf=True)
        self.pin(target)
        self.change()
        before = target.read_bytes()
        self.assertEqual(1, self.invoke("--update").returncode)
        self.assertEqual(before, target.read_bytes())
        self.approve()
        result = self.invoke("--update")
        self.assertEqual(0, result.returncode, result.stdout)
        result_data = json.loads(target.read_bytes())["locked"]
        self.assertEqual(self.locks["locked"]["route.other"], result_data["route.other"])
        self.assertEqual("abc123", result_data["route.scene"]["since"])
        self.assertEqual("claude", result_data["route.scene"]["owner"])
        self.assertEqual(lint.text_sha(self.story["Scenes"][0]), result_data["route.scene"]["text_sha"])
        self.assertNotIn(b"\n", target.read_bytes().replace(b"\r\n", b""))
        self.assertEqual(0, self.invoke().returncode)
        second["Nodes"][0]["Text"] += " unauthorized"
        self.write("Story.json", self.story)
        after = target.read_bytes()
        self.assertEqual(1, self.invoke("--update").returncode)
        self.assertEqual(after, target.read_bytes())

    def test_historical_approval_does_not_authorize_later_delta(self):
        self.change()
        first = self.approval()
        self.approve(first)
        self.assertEqual(0, self.invoke("--update").returncode)
        self.pin(self.root / authority.LOCKS)
        self.change()
        self.assertEqual(1, self.invoke().returncode)
        current_before = first["after_sha"]
        self.approve(first, self.approval(before_sha=current_before))
        self.assertEqual(0, self.invoke("--update").returncode)

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

    def test_altered_locks_and_owner_map_fail(self):
        for mode in ("hash", "delete", "owner", "since", "owner-map", "missing-map"):
            with self.subTest(mode=mode):
                self.story = sample()
                locks = copy.deepcopy(self.locks)
                self.write(authority.OWNERSHIP, self.ownership)
                if mode == "hash":
                    self.change()
                    locks["locked"]["route.scene"]["text_sha"] = lint.text_sha(self.story["Scenes"][0])
                elif mode == "delete":
                    locks["locked"].clear()
                elif mode in ("owner", "since"):
                    locks["locked"]["route.scene"][mode] = "forged"
                elif mode == "owner-map":
                    self.write(authority.OWNERSHIP, dict(version=1, scene_prefixes={}))
                else:
                    (self.root / authority.OWNERSHIP).unlink()
                self.write("Story.json", self.story)
                self.write(authority.LOCKS, locks)
                self.assertEqual(1, self.invoke().returncode)

    def test_registry_schema_and_byte_identity(self):
        self.change()
        approved = dict(version=1, approvals=[self.approval()])
        path = self.review(approved)
        self.assertEqual(0, self.invoke().returncode)
        path.write_text(json.dumps(approved) + "\n", encoding="utf-8")
        self.assertEqual(1, self.invoke().returncode)
        for data in (dict(approved, version=True), dict(approved, extra=True),
                     dict(version=1, approvals=approved["approvals"] * 2),
                     dict(version=1, approvals=[self.approval(source_commit="short")]),
                     dict(version=1, approvals=[self.approval(reason="")])):
            with self.subTest(data=data):
                self.review(data)
                self.assertEqual(1, self.invoke().returncode)

    def test_symlink_cannot_substitute_another_reviewed_record_for_voice_registry(self):
        self.change()
        other = self.review(dict(version=1, approvals=[self.approval()]), "append-approvals.json")
        path = self.root / authority.APPROVALS
        path.unlink()
        path.symlink_to(other)
        result = self.invoke()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("approval record differs from coordinator-reviewed ref", result.stdout)
        folder = self.mutant("record-path", "voice_authority.py",
                             'root, path = Path(root).resolve(), Path(path).absolute()',
                             'root, path = Path(root).resolve(), Path(path).resolve()')
        result = self.invoke(script=folder / "voice_lock_lint.py")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_absent_legacy_registry_bootstrap_grants_no_approval(self):
        self.command("git", "rm", authority.APPROVALS)
        self.command("git", "commit", "-qm", "Legacy reviewed inventory")
        self.command("git", "update-ref", authority.REVIEWED_REF,
                     self.command("git", "rev-parse", "HEAD").stdout.strip())
        self.write(authority.APPROVALS, dict(version=1, approvals=[]))
        self.assertEqual(0, self.invoke().returncode)
        self.change()
        self.write(authority.APPROVALS, dict(version=1, approvals=[self.approval()]))
        self.assertEqual(1, self.invoke().returncode)

    def test_missing_reviewed_ref_cannot_approve_from_remote(self):
        self.change()
        self.approve()
        reviewed = self.command("git", "rev-parse", authority.REVIEWED_REF).stdout.strip()
        self.command("git", "update-ref", "refs/remotes/origin/claude/trickster-expansion", reviewed)
        self.command("git", "update-ref", "-d", authority.REVIEWED_REF)
        self.assertEqual(1, self.invoke().returncode)

    def test_coordinator_cli_prepares_selected_exact_deltas_and_keeps_history(self):
        self.change()
        other = dict(Id="route.other", Nodes=[dict(Id="start", Text="New scene")])
        self.story["Scenes"].append(other)
        self.write("Story.json", self.story)
        command = [sys.executable, str(lint.ROOT / "tools/voice_approve.py"), "--repo", str(self.root),
                   "--base", str(self.root / "Base.json"), "--candidate", str(self.root / "Story.json"),
                   "--prefixes", "route.scene", "--source-branch", "claude/voice", "--source-commit", self.base,
                   "--reason", "Coordinator accepted the owned voice rewrite"]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        data = authority.read_json(self.root / authority.APPROVALS)
        self.assertEqual([self.approval()], data["approvals"])
        self.assertEqual(1, self.invoke().returncode)  # Preparation never advances the ref.
        self.pin(self.root / authority.APPROVALS)
        command[command.index("route.scene")] = "route.other"
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual([self.approval(), self.approval("route.other")],
                         authority.read_json(self.root / authority.APPROVALS)["approvals"])
        self.pin(self.root / authority.APPROVALS)
        self.assertEqual(0, self.invoke("--update").returncode)

    def test_coordinator_rejects_stale_base_and_missing_or_unowned_targets(self):
        self.change()
        before = (self.root / authority.APPROVALS).read_bytes()
        self.write("Base.json", self.story)
        with self.assertRaisesRegex(ValueError, "base export differs from current lock"):
            voice_approve.prepare(self.root, self.root / "Base.json", self.root / "Story.json",
                                  ["route"], "claude/voice", self.base, "Reviewed")
        self.write("Base.json", sample())
        for mode in ("missing", "duplicate", "deleted", "unowned"):
            with self.subTest(mode=mode):
                story = sample()
                prefixes = ["route"]
                if mode == "missing":
                    prefixes = ["absent"]
                elif mode == "duplicate":
                    story["Scenes"] *= 2
                elif mode == "deleted":
                    story["Scenes"] = []
                else:
                    story["Scenes"].append(dict(Id="unowned.new", Nodes=[]))
                    prefixes = ["unowned"]
                self.write("Story.json", story)
                with self.assertRaises(ValueError):
                    voice_approve.prepare(self.root, self.root / "Base.json", self.root / "Story.json",
                                          prefixes, "claude/voice", self.base, "Reviewed")
                self.assertEqual(before, (self.root / authority.APPROVALS).read_bytes())

    def test_mutations_prove_ref_and_exact_hash_witnesses(self):
        self.change()
        # Each mutant is confined to system temp and exercised by the same CLI.
        for mutation in ("ref", "before", "after"):
            with self.subTest(mutation=mutation):
                folder = Path(self.temp.name) / mutation
                folder.mkdir()
                for name in ("voice_authority.py", "voice_lock_lint.py", "prose_pending_lint.py"):
                    source = (lint.ROOT / "tools" / name).read_text(encoding="utf-8")
                    if name == "voice_authority.py":
                        if mutation == "ref":
                            source = source.replace('        reviewed_file(root, path)', '        pass  # mutant skips protected ref')
                        else:
                            expression = (' and entry["before_sha"] == before' if mutation == "before"
                                          else 'and entry["after_sha"] == after')
                            source = source.replace(expression, '' if mutation == "before" else 'and True')
                    (folder / name).write_text(source, encoding="utf-8")
                entry = self.approval(**({mutation + "_sha": "0" * 64} if mutation != "ref" else {}))
                path = self.write(authority.APPROVALS, dict(version=1, approvals=[entry]))
                if mutation != "ref":
                    self.pin(path)
                self.assertEqual(1, self.invoke().returncode)
                result = self.invoke(script=folder / "voice_lock_lint.py")
                self.assertEqual(0, result.returncode, result.stdout + result.stderr)
                # Restore empty reviewed registry before the next witness.
                self.review(dict(version=1, approvals=[]))

    def test_mutation_proves_unlocked_owned_scene_needs_approval(self):
        self.story["Scenes"].append(dict(Id="route.new", Nodes=[dict(Id="start", Text="Unapproved")]))
        self.write("Story.json", self.story)
        folder = self.mutant("enrollment", "voice_lock_lint.py",
                             'errors.append(f"{sid}: missing ownership enrollment/approval")',
                             'pass  # mutant bypasses enrollment')
        self.assertEqual(1, self.invoke().returncode)
        result = self.invoke(script=folder / "voice_lock_lint.py")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_mutation_proves_update_preserves_unapproved_locks(self):
        other = dict(Id="route.other", Nodes=[dict(Id="start", Text="Keep")])
        self.story["Scenes"].append(other)
        self.locks["locked"]["route.other"] = dict(owner="claude", since="keep-since", text_sha=lint.text_sha(other))
        target = self.write(authority.LOCKS, self.locks, crlf=True)
        self.pin(target)
        self.change()
        self.approve()
        before = target.read_bytes()
        folder = self.mutant("update", "voice_lock_lint.py",
                             'expected["locked"][sid]["text_sha"] = digest',
                             'for record in expected["locked"].values():\n'
                             '                        record["text_sha"] = digest')

        def witness(script=None):
            target.write_bytes(before)
            result = self.invoke("--update", script=script)
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            updated = authority.read_json(target)["locked"]
            self.assertEqual(lint.text_sha(self.story["Scenes"][0]), updated["route.scene"]["text_sha"])
            self.assertEqual(self.locks["locked"]["route.other"], updated["route.other"])

        witness()
        with self.assertRaises(AssertionError):
            witness(folder / "voice_lock_lint.py")


if __name__ == "__main__":
    unittest.main()
