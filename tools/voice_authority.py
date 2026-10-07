"""Reviewed job authority, anchored in the coordinator's reviewed Git ref.

Call snapshot to prepare review inputs, then verify_job to authenticate them.
Private signing keys belong to the coordinator, outside the candidate tree.
"""
import base64
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile

OWNERSHIP = "tools/route_packs/ownership.json"
LOCKS = "tools/route_packs/voice_locks.json"
PENDING = "tools/route_packs/plans/prose-pending.json"


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding="utf-8-sig"), object_pairs_hook=unique)


def git(root, *args):
    try:
        return subprocess.run(["git", "-C", str(root), *args], check=True,
                              capture_output=True, timeout=15).stdout
    except (OSError, subprocess.SubprocessError) as error:
        raise ValueError("cannot read trusted Git baseline") from error


def baseline(root):
    # A caller cannot choose an older ref to bypass newer enrollment/policy.
    return git(root, "rev-parse", "HEAD").decode().strip()


def trusted(root):
    base = baseline(root)
    review = reviewed_revision(root)
    locks = json.loads(git(root, "show", f"{review}:{LOCKS}"))
    paths = git(root, "ls-tree", "-r", "--name-only", review).decode().splitlines()
    if OWNERSHIP in paths:
        policy = json.loads(git(root, "show", f"{review}:{OWNERSHIP}"))
        if not (root / OWNERSHIP).is_file():
            raise ValueError("missing reviewed ownership policy")
    else:
        # One-time migration: existing committed locks remain authoritative.
        # No reviewer key is invented, so voice approvals remain default-deny.
        policy = {"version": 1, "scene_prefixes": {sid: lock["owner"]
                  for sid, lock in locks["locked"].items()}, "reviewers": {}}
    validate_policy(policy)
    if (root / OWNERSHIP).exists() and read_json(root / OWNERSHIP) != policy:
        raise ValueError("ownership policy differs from reviewed Git baseline")
    return base, policy, locks


def reviewed_revision(root):
    # This coordinator-managed ref is distinct from the job's mutable HEAD.
    # The existing integration remote is the backward-compatible bootstrap.
    refs = git(root, "for-each-ref", "--format=%(refname)").decode().splitlines()
    for ref in ("refs/rrt/ownership-reviewed", "refs/remotes/origin/claude/trickster-expansion"):
        if ref in refs:
            return git(root, "rev-parse", ref).decode().strip()
    raise ValueError("missing coordinator-reviewed ownership ref")


def validate_policy(policy):
    if (not isinstance(policy, dict) or set(policy) != {"version", "scene_prefixes", "reviewers"}
            or type(policy["version"]) is not int or policy["version"] != 1
            or not isinstance(policy["scene_prefixes"], dict)
            or not isinstance(policy["reviewers"], dict)):
        raise ValueError("invalid ownership policy")
    for prefix, owner in policy["scene_prefixes"].items():
        if not prefix.strip() or prefix.endswith(".") or owner != "claude":
            raise ValueError("invalid scene prefix/owner")
    for key, reviewer in policy["reviewers"].items():
        if (not key.strip() or not isinstance(reviewer, dict) or set(reviewer) != {"public_key"}
                or not isinstance(reviewer["public_key"], str)
                or "BEGIN PUBLIC KEY" not in reviewer["public_key"]):
            raise ValueError("invalid reviewer public key")


def owner_for(policy, sid):
    matches = [prefix for prefix in policy["scene_prefixes"]
               if sid == prefix or sid.startswith(prefix + ".")]
    return policy["scene_prefixes"][max(matches, key=len)] if matches else None


def source_sha(root):
    # Include new/deleted/untracked generator inputs, not generated exports,
    # reports, caches or test/build scratch. Tools may be generator imports.
    files = set(root.glob("*.py"))
    for folder, pattern in (("storylines", "*.py"), ("tools", "*.py"),
                            ("tools", "*.json"),
                            ("reference", "*.json")):
        files.update((root / folder).rglob(pattern))
    separately_bound = {root / path for path in (OWNERSHIP, LOCKS, PENDING)}
    files = sorted(path for path in files if path.is_file() and path not in separately_bound)
    return digest([[path.relative_to(root).as_posix(), hashlib.sha256(path.read_bytes()).hexdigest()]
                   for path in files])


def snapshot(root, story_path, base=None):
    root = Path(root).resolve()
    old_locks = json.loads(git(root, "show", f"{reviewed_revision(root)}:{LOCKS}"))
    pending = read_json(root / PENDING) if (root / PENDING).exists() else {"version": 1, "pending": []}
    return dict(source_sha=source_sha(root), story_sha=digest(read_json(story_path)),
                locks_sha=digest(old_locks), pending_sha=digest(pending))


def verify_job(root, story_path, job_path, policy, base):
    job = read_json(job_path)
    fields = {"version", "job_id", "actor", "kind", "status", "branch", "base", "approvals",
              "source_sha", "story_sha", "locks_sha", "pending_sha", "signature"}
    if (not isinstance(job, dict) or set(job) != fields or type(job["version"]) is not int
            or job["version"] != 1):
        raise ValueError("invalid reviewed job schema")
    if (job["base"] != base or not isinstance(job["job_id"], str) or not job["job_id"].strip()
            or job["actor"] not in ("claude", "codex", "gemory")
            or job["kind"] not in ("voice", "scaffold")
            or job["status"] not in ("reviewed", "held")
            or job["branch"] != git(root, "branch", "--show-current").decode().strip()):
        raise ValueError("job is not bound to this reviewed base/branch")
    sig = job["signature"]
    if not isinstance(sig, dict) or set(sig) != {"key_id", "value"} or sig["key_id"] not in policy["reviewers"]:
        raise ValueError("approval requires a trusted reviewer signature")
    unsigned = {key: value for key, value in job.items() if key != "signature"}
    try:
        signature = base64.b64decode(sig["value"], validate=True)
    except (ValueError, TypeError) as error:
        raise ValueError("invalid approval signature encoding") from error
    with tempfile.TemporaryDirectory(prefix="rrt-voice-signature-") as directory:
        directory = Path(directory)
        (directory / "key").write_text(policy["reviewers"][sig["key_id"]]["public_key"], encoding="utf-8")
        (directory / "payload").write_bytes(canonical(unsigned))
        (directory / "signature").write_bytes(signature)
        try:
            subprocess.run(["openssl", "pkeyutl", "-verify", "-pubin", "-rawin", "-inkey",
                            str(directory / "key"), "-in", str(directory / "payload"),
                            "-sigfile", str(directory / "signature")], check=True,
                           capture_output=True, timeout=15)
        except (OSError, subprocess.SubprocessError) as error:
            raise ValueError("approval signature verification failed (requires OpenSSL)") from error
    expected = snapshot(root, story_path, base)
    if any(job[key] != value for key, value in expected.items()):
        raise ValueError("stale approval: source/export/locks/pending identity differs")
    if not isinstance(job["approvals"], list):
        raise ValueError("invalid per-change approvals")
    seen = set()
    for entry in job["approvals"]:
        if (not isinstance(entry, dict) or set(entry) != {"scene", "before", "after", "allow_update"}
                or not isinstance(entry["scene"], str) or entry["scene"] in seen
                or owner_for(policy, entry["scene"]) != "claude"
                or type(entry["allow_update"]) is not bool
                or entry["before"] is not None and not valid_sha(entry["before"])
                or not valid_sha(entry["after"])):
            raise ValueError("invalid/duplicate/unowned per-change approval")
        seen.add(entry["scene"])
    return job


def valid_sha(value):
    return isinstance(value, str) and bool(re.fullmatch(r"[0-9a-f]{64}", value))


def approved(job, sid, before, after, update=False):
    if not job or (job["actor"], job["kind"], job["status"]) != ("claude", "voice", "reviewed"):
        return False
    return any(entry["scene"] == sid and entry["before"] == before and entry["after"] == after
               and (not update or entry["allow_update"]) for entry in job["approvals"])
