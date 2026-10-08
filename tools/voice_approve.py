#!/usr/bin/env python3
"""Prepare exact prose approvals for the coordinator to commit and pin."""
import argparse
import json
from pathlib import Path

try:
    from . import voice_authority as authority, voice_lock_lint as locks
except ImportError:
    import voice_authority as authority
    import voice_lock_lint as locks

ROOT = Path(__file__).resolve().parents[1]


def scene_map(story):
    scenes = {}
    for scene in story.get("Scenes", []):
        if scene["Id"] in scenes:
            raise ValueError(f"{scene['Id']}: ambiguous scene ID")
        scenes[scene["Id"]] = scene
    return scenes


def prepare(root, base_path, candidate_path, prefixes, source_branch, source_commit, reason):
    """Approve selected deltas only when the base export matches current locks."""
    _, policy, predecessor = authority.trusted(root)
    current = locks.validate_locks(predecessor)
    before = scene_map(authority.read_json(base_path))
    after = scene_map(authority.read_json(candidate_path))
    entries = []
    for prefix in prefixes:
        if not isinstance(prefix, str) or not prefix.strip() or prefix.endswith("."):
            raise ValueError("invalid scene prefix")
        if not any(sid == prefix or sid.startswith(prefix + ".") for sid in before.keys() | after.keys()):
            raise ValueError(f"{prefix}: scene prefix matches no scenes")
    selected = sorted(sid for sid in before.keys() | after.keys()
                      if any(sid == prefix or sid.startswith(prefix + ".") for prefix in prefixes))
    for sid in selected:
        if sid not in after:
            raise ValueError(f"{sid}: cannot approve a deleted scene")
        before_sha = locks.text_sha(before[sid]) if sid in before else None
        after_sha = locks.text_sha(after[sid])
        if sid in current:
            if before_sha != current[sid]["text_sha"]:
                raise ValueError(f"{sid}: base export differs from current lock")
            if before_sha == after_sha:
                continue
        else:
            # Enrollment has no predecessor lock, even for existing scaffolds.
            before_sha = None
        entries.append(dict(scene=sid, before_sha=before_sha, after_sha=after_sha,
                            owner=authority.owner_for(policy, sid), source_branch=source_branch,
                            source_commit=source_commit, reason=reason))
    result = dict(version=1, approvals=entries)
    authority.validate_approvals(result, policy)
    return result


def write_records(path, data):
    """Preserve newline style when the coordinator extends a record file."""
    newline = "\r\n" if path.exists() and b"\r\n" in path.read_bytes() else "\n"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8", newline=newline)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=ROOT)
    parser.add_argument("--base", type=Path, required=True, help="base export matching current locks")
    parser.add_argument("--candidate", type=Path, required=True, help="fresh candidate export")
    parser.add_argument("--prefixes", nargs="+", required=True)
    parser.add_argument("--source-branch", required=True)
    parser.add_argument("--source-commit", required=True, help="full source commit ID")
    parser.add_argument("--reason", required=True)
    args = parser.parse_args(argv)
    root = args.repo.resolve()
    try:
        _, policy, _ = authority.trusted(root)
        records = authority.approvals(root, policy)
        additions = prepare(root, args.base, args.candidate, args.prefixes,
                            args.source_branch, args.source_commit, args.reason)
        for entry in additions["approvals"]:
            existing = authority.approved(records, entry["scene"], entry["before_sha"], entry["after_sha"])
            if existing is not None and existing != entry:
                raise ValueError(f"{entry['scene']}: conflicting approval provenance")
            if existing is None:
                records["approvals"].append(entry)
        authority.validate_approvals(records, policy)
        write_records(root / authority.APPROVALS, records)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("HARD Voice approval:", error)
        return 1
    print(f"Voice approvals: {len(additions['approvals'])} exact deltas prepared; coordinator must commit and advance the ref")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
