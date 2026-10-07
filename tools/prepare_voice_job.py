#!/usr/bin/env python3
"""Prepare exact unsigned J05b append approvals for coordinator signing."""
import argparse
import json
from pathlib import Path

try:
    from . import voice_authority as authority, voice_lock_lint as locks, prose_pending_lint as pending_lint
except ImportError:
    import voice_authority as authority
    import voice_lock_lint as locks
    import prose_pending_lint as pending_lint

ROOT = Path(__file__).resolve().parents[1]
REQUEST = "tools/route_packs/plans/j05b-append-approval-request.json"


def prepare(root, story_path, request_path):
    base, policy, predecessor = authority.trusted(root)
    request = authority.read_json(request_path)
    if (request.get("version") != 1 or request.get("job_id") != "J05b-pending-choice-appends"
            or request.get("status") != "awaiting-coordinator-signature"
            or (request.get("actor"), request.get("kind")) != ("codex", "scaffold")):
        raise ValueError("invalid J05b approval request")
    story = authority.read_json(story_path)
    pending = authority.read_json(root / authority.PENDING)
    errors = pending_lint.check(story, pending, integration=True)
    if errors:
        raise ValueError("; ".join(errors))
    old_story = json.loads(authority.git(root, "show",
        f"{authority.reviewed_revision(root)}:development/Story.json"))
    before, after = {}, {}
    for source, scenes in ((old_story, before), (story, after)):
        for scene in source.get("Scenes", []):
            if scene["Id"] in scenes:
                raise ValueError("ambiguous scene ID")
            scenes[scene["Id"]] = scene
    approvals = []
    changed, errors = locks.check(story, locks.validate_locks(predecessor))
    if errors:
        raise ValueError("; ".join(errors))
    hosts = {host["scene"]: host for host in request["hosts"]}
    for sid, digest in changed.items():
        old_hash = predecessor["locked"][sid]["text_sha"]
        if (sid not in hosts or authority.owner_for(policy, sid) != "claude"
                or hosts[sid]["before"] != old_hash or sid not in before
                or locks.text_sha(before[sid]) != old_hash
                or not locks.pending_choice_append(before[sid], after[sid], pending)):
            raise ValueError(f"{sid}: delta exceeds the explicit J05b append request")
        approvals.append(dict(scene=sid, before=old_hash, after=digest, allow_update=False))
    if not approvals:
        raise ValueError("no pending-choice append to approve; implement J05b before signing")
    return dict(version=1, job_id=request["job_id"], actor="codex", kind="scaffold", status="reviewed",
                branch=authority.git(root, "branch", "--show-current").decode().strip(), base=base,
                approvals=approvals, **authority.snapshot(root, story_path))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=ROOT)
    parser.add_argument("--story", type=Path)
    parser.add_argument("--request", type=Path)
    parser.add_argument("--output", type=Path, required=True, help="unsigned canonical payload outside the repo")
    args = parser.parse_args(argv)
    root = args.repo.resolve()
    if args.output.resolve().is_relative_to(root):
        parser.error("--output must be outside the repository")
    try:
        job = prepare(root, args.story or root / "development/Story.json", args.request or root / REQUEST)
        args.output.write_bytes(authority.canonical(job))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("HARD Approval preparation:", error)
        return 1
    print("Unsigned exact append review payload:", args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
