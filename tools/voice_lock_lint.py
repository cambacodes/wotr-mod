#!/usr/bin/env python3
"""Protect Claude-owned scene prose in the generated Story.json.

Hashes cover ordered node Text, Paragraphs[].Text and Choices[].Text only,
using compact UTF-8 JSON; IDs and gameplay metadata are excluded. A Claude
voice delta requires a signed reviewed job and explicit per-scene approval.
Branch names, commit messages and environment variables grant no authority.
--update requires explicit signed update/enrollment approval and preserves
existing owner/since. Policy and predecessor locks come from the reviewed ref.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
try:
    from . import voice_authority as authority, prose_pending_lint as pending_lint
except ImportError:
    import voice_authority as authority
    import prose_pending_lint as pending_lint

ROOT = Path(__file__).resolve().parents[1]
LOCKS = ROOT / "tools/route_packs/voice_locks.json"


def text_sha(scene):
    """Keep text boundaries/order without including gates, links or flags."""
    text = [
        [node.get("Text", ""),
         [paragraph.get("Text", "") for paragraph in node.get("Paragraphs", [])],
         [choice.get("Text", "") for choice in node.get("Choices", [])]]
        for node in scene.get("Nodes", [])
    ]
    payload = json.dumps(text, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def validate_locks(data):
    if not isinstance(data, dict) or not isinstance(data.get("locked"), dict):
        raise ValueError("lock file must contain a 'locked' object")
    for sid, lock in data["locked"].items():
        if (not sid or not isinstance(lock, dict) or lock.get("owner") != "claude"
                or not isinstance(lock.get("since"), str) or not lock["since"].strip()
                or not isinstance(lock.get("text_sha"), str)
                or not re.fullmatch(r"[0-9a-f]{64}", lock["text_sha"])):
            raise ValueError(f"{sid}: invalid Claude voice lock (owner/since/text_sha)")
    return data["locked"]


def check(story, locks):
    """Return changed scenes separately from missing/ambiguous lock targets."""
    scenes = {}
    for scene in story.get("Scenes", []):
        scenes.setdefault(scene["Id"], []).append(scene)
    changed, errors = {}, []
    for sid, lock in locks.items():
        matches = scenes.get(sid, [])
        if len(matches) != 1:
            errors.append(f"{sid}: expected one locked scene, found {len(matches)}")
            continue
        digest = text_sha(matches[0])
        if digest != lock["text_sha"]:
            changed[sid] = digest
    return changed, errors


def pending_choice_append(before, after, pending):
    """Only appended registered choice labels may differ from locked prose."""
    old_nodes, new_nodes = before.get("Nodes", []), after.get("Nodes", [])
    if len(old_nodes) != len(new_nodes):
        return False
    targets = {(e["scene"], e["node"], e["surface"], e["index"]): e["text_sha"]
               for e in pending["pending"]}
    appended = False
    for old, new in zip(old_nodes, new_nodes):
        if (old.get("Id") != new.get("Id") or old.get("Text", "") != new.get("Text", "")
                or [p.get("Text", "") for p in old.get("Paragraphs", [])] !=
                   [p.get("Text", "") for p in new.get("Paragraphs", [])]):
            return False
        old_choices, new_choices = old.get("Choices", []), new.get("Choices", [])
        if (len(new_choices) < len(old_choices)
                or [c.get("Text", "") for c in old_choices] !=
                   [c.get("Text", "") for c in new_choices[:len(old_choices)]]):
            return False
        for index in range(len(old_choices), len(new_choices)):
            text = new_choices[index].get("Text", "")
            key = (after["Id"], new["Id"], "choice", index)
            if (not re.fullmatch(r"\[PROSE PENDING: choice - [^\]\r\n]+\]", text)
                    or targets.get(key) != authority.digest(text)):
                return False
            appended = True
    return appended


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=ROOT)
    parser.add_argument("--story", type=Path)
    parser.add_argument("--locks", type=Path)
    parser.add_argument("--job", type=Path, help="signed reviewed job record")
    parser.add_argument("--integration", action="store_true", help="allow registered integration placeholders")
    parser.add_argument("--append-approvals", type=Path, help="separate signed pending-choice append record")
    parser.add_argument("--milestone", action="store_true", help="forbid all pending prose")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--update", action="store_true")
    args = parser.parse_args(argv)
    root = args.repo.resolve()
    args.story = args.story or root / "development/Story.json"
    args.locks = args.locks or root / authority.LOCKS
    try:
        base, policy, predecessor = authority.trusted(root)
        old = validate_locks(predecessor)
        data = authority.read_json(args.locks)
        locks = validate_locks(data)
        story = authority.read_json(args.story)
        job = authority.verify_job(root, args.story, args.job, policy, base) if args.job else None
        if args.update and (not job or (job["actor"], job["kind"], job["status"]) !=
                            ("claude", "voice", "reviewed") or not job["approvals"]
                            or not any(entry["allow_update"] for entry in job["approvals"])):
            raise ValueError("--update requires signed approval entries")
        pending_path = root / authority.PENDING
        pending = authority.read_json(pending_path) if pending_path.exists() else {"version": 1, "pending": []}
        errors = pending_lint.check(story, pending, job, args.milestone, args.integration)
        append_job = authority.verify_job(root, args.story, args.append_approvals, policy, base) if args.append_approvals else None
        if append_job and (not args.integration or args.milestone or args.update
                or append_job["job_id"] != "J05b-pending-choice-appends" or not append_job["approvals"]
                or (append_job["actor"], append_job["kind"], append_job["status"]) != ("codex", "scaffold", "reviewed")
                or any(entry["allow_update"] for entry in append_job["approvals"])):
            raise ValueError("pending append approvals require integration, Codex reviewed scaffold, and no lock updates")
        changed, target_errors = check(story, old)
        errors.extend(target_errors)
        scenes = {}
        for scene in story.get("Scenes", []):
            if scene["Id"] in scenes:
                errors.append(f"{scene['Id']}: ambiguous scene ID")
            scenes[scene["Id"]] = scene
        for entry in job["approvals"] if job else []:
            sid = entry["scene"]
            before = old[sid]["text_sha"] if sid in old else None
            if (sid not in scenes or entry["before"] != before
                    or entry["after"] != text_sha(scenes[sid])):
                errors.append(f"{sid}: approval does not match the exact voice delta")
        approved_appends = set()
        if append_job:
            baseline_story = json.loads(authority.git(root, "show",
                f"{authority.reviewed_revision(root)}:development/Story.json"))
            baseline_scenes = {}
            for scene in baseline_story.get("Scenes", []):
                baseline_scenes.setdefault(scene["Id"], []).append(scene)
            for entry in append_job["approvals"]:
                sid = entry["scene"]
                matches = baseline_scenes.get(sid, [])
                if (sid not in old or len(matches) != 1 or sid not in scenes
                        or entry["before"] != old[sid]["text_sha"]
                        or entry["before"] != text_sha(matches[0])
                        or entry["after"] != text_sha(scenes[sid])
                        or not pending_choice_append(matches[0], scenes[sid], pending)):
                    errors.append(f"{sid}: approval is not an exact registered pending-choice append")
                else:
                    approved_appends.add(sid)
        expected = json.loads(json.dumps(predecessor))
        for sid, lock in old.items():
            if authority.owner_for(policy, sid) != lock["owner"]:
                errors.append(f"{sid}: lock lacks ownership enrollment")
            if sid in changed:
                digest = changed[sid]
                if sid not in approved_appends and not authority.approved(job, sid, lock["text_sha"], digest):
                    errors.append(f"{sid}: changed prose requires reviewed Claude approval")
                if authority.approved(job, sid, lock["text_sha"], digest, update=True):
                    expected["locked"][sid]["text_sha"] = digest
                elif args.update:
                    errors.append(f"{sid}: --update lacks signed update approval")
        pending_scenes = {entry["scene"] for entry in pending["pending"]}
        for sid, scene in scenes.items():
            if authority.owner_for(policy, sid) and sid not in old:
                digest = text_sha(scene)
                if authority.approved(job, sid, None, digest, update=True):
                    expected["locked"][sid] = dict(owner="claude", since=base, text_sha=digest)
                    if not args.update and sid not in locks:
                        errors.append(f"{sid}: approved enrollment requires --update")
                elif sid not in pending_scenes or errors:
                    errors.append(f"{sid}: missing ownership enrollment/approval")
        # The only acceptable lock edits are the exact approved hash updates.
        # Before an update the complete predecessor remains valid as input.
        if data != predecessor and data != expected:
            errors.append("altered lock file: differs from reviewed/approved inventory")
        if args.update and not errors:
            newline = "\r\n" if b"\r\n" in args.locks.read_bytes() else "\n"
            args.locks.write_text(json.dumps(expected, ensure_ascii=False, indent=2) + "\n",
                                  encoding="utf-8", newline=newline)
            print("Voice locks: signed updates applied; owner/since preserved")
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"HARD Voice locks: {error}")
        return 1
    for error in errors:
        print("HARD", error)
    if approved_appends:
        print(f"Voice locks: {len(approved_appends)} signed pending-choice appends; predecessor hashes retained")
    for sid in changed:
        print("CHANGED", f"{sid}: locked player text differs")
    print(f"Voice locks: {len(locks)} locked scenes; {len(changed)} changed; {len(errors)} hard failures")
    # Ownership failures are hard in every mode; --strict stays CLI-compatible.
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
