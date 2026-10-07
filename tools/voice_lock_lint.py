#!/usr/bin/env python3
"""Protect Claude-owned scene prose in the generated Story.json.

Hashes cover ordered node Text, Paragraphs[].Text and Choices[].Text only,
using compact UTF-8 JSON; IDs and gameplay metadata are excluded. A Claude
voice job is a claude/voice-* or claude/pol[-ish]-* branch, or a commit message
containing both Claude and a standalone voice, polish or pol token. Voice
lock/lint/tool jobs are excluded. Merely having a Claude co-author or branch
prefix is insufficient.

--update refreshes existing locks only, requires RRT_VOICE_OWNER=claude, and
preserves owner/since (the original locking commit). It never enrolls scenes.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
LOCKS = ROOT / "tools/route_packs/voice_locks.json"
VOICE_JOB = re.compile(
    r"(?<![a-z0-9])(?:voice(?![-_\s]+(?:lock|lint|tool))|polish|pol)(?![a-z0-9])", re.I)
CLAUDE = re.compile(r"(?<![a-z0-9])claude(?![a-z0-9])", re.I)


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


def git_context():
    def read(*args):
        try:
            return subprocess.run(
                ["git", "-C", str(ROOT), *args], check=True, capture_output=True,
                text=True, encoding="utf-8").stdout.strip()
        except (OSError, subprocess.CalledProcessError):
            return ""
    return read("branch", "--show-current"), read("log", "-1", "--format=%B")


def claude_voice_job(branch, message):
    branch_job = branch.lower().startswith("claude/") and bool(VOICE_JOB.match(branch[7:]))
    message_job = bool(CLAUDE.search(message) and VOICE_JOB.search(message))
    return branch_job or message_job


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path, default=ROOT / "development/Story.json")
    parser.add_argument("--locks", type=Path, default=LOCKS)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--update", action="store_true")
    args = parser.parse_args(argv)
    if args.update and os.environ.get("RRT_VOICE_OWNER") != "claude":
        print("HARD --update requires RRT_VOICE_OWNER=claude")
        return 1
    try:
        data = json.loads(args.locks.read_text(encoding="utf-8-sig"))
        locks = validate_locks(data)
        story = json.loads(args.story.read_text(encoding="utf-8-sig"))
        changed, errors = check(story, locks)
        if args.update and not errors and changed:
            for sid, digest in changed.items():
                locks[sid]["text_sha"] = digest
            newline = "\r\n" if b"\r\n" in args.locks.read_bytes() else "\n"
            args.locks.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                                  encoding="utf-8", newline=newline)
            print(f"Voice locks: updated {len(changed)} hashes; owner/since preserved")
            changed = {}
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"HARD Voice locks: {error}")
        return 1
    allowed = bool(changed) and claude_voice_job(*git_context())
    for error in errors:
        print("HARD", error)
    for sid in changed:
        print("CLAUDE VOICE JOB" if allowed else "CHANGED", f"{sid}: locked player text differs")
    print(f"Voice locks: {len(locks)} locked scenes; {len(changed)} changed; {len(errors)} missing/ambiguous")
    return int(bool(errors) or (args.strict and bool(changed) and not allowed))


if __name__ == "__main__":
    raise SystemExit(main())
