"""Coordinator approval authority anchored in the protected reviewed Git ref."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

OWNERSHIP = "tools/route_packs/ownership.json"
LOCKS = "tools/route_packs/voice_locks.json"
APPROVALS = "tools/route_packs/voice-approvals.json"
REVIEWED_REF = "refs/rrt/ownership-reviewed"
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
        # Missing approval records grant no prose authority.
        policy = {"version": 1, "scene_prefixes": {sid: lock["owner"]
                  for sid, lock in locks["locked"].items()}}
    validate_policy(policy)
    if (root / OWNERSHIP).exists() and read_json(root / OWNERSHIP) != policy:
        raise ValueError("ownership policy differs from reviewed Git baseline")
    return base, policy, locks


def reviewed_revision(root):
    # This coordinator-managed ref is distinct from the job's mutable HEAD.
    # The existing integration remote is the backward-compatible bootstrap.
    refs = git(root, "for-each-ref", "--format=%(refname)").decode().splitlines()
    for ref in (REVIEWED_REF, "refs/remotes/origin/claude/trickster-expansion"):
        if ref in refs:
            return git(root, "rev-parse", ref).decode().strip()
    raise ValueError("missing coordinator-reviewed ownership ref")


def validate_policy(policy):
    if (not isinstance(policy, dict) or set(policy) != {"version", "scene_prefixes"}
            or type(policy["version"]) is not int or policy["version"] != 1
            or not isinstance(policy["scene_prefixes"], dict)):
        raise ValueError("invalid ownership policy")
    for prefix, owner in policy["scene_prefixes"].items():
        if not isinstance(prefix, str) or not prefix.strip() or prefix.endswith(".") or owner != "claude":
            raise ValueError("invalid scene prefix/owner")


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
    separately_bound = {root / path for path in (OWNERSHIP, LOCKS, PENDING, APPROVALS)}
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
              "source_sha", "story_sha", "locks_sha", "pending_sha"}
    if (not isinstance(job, dict) or set(job) != fields or type(job["version"]) is not int
            or job["version"] != 1):
        raise ValueError("invalid reviewed job schema")
    if (job["base"] != base or not isinstance(job["job_id"], str) or not job["job_id"].strip()
            or job["actor"] not in ("claude", "codex", "gemory")
            or job["kind"] not in ("voice", "scaffold")
            or job["status"] not in ("reviewed", "held")
            or job["branch"] != git(root, "branch", "--show-current").decode().strip()):
        raise ValueError("job is not bound to this reviewed base/branch")
    # Held scaffold jobs retain their exact source/export binding, but their
    # authorization comes from the coordinator ref rather than a signing key.
    reviewed_file(root, job_path)
    expected = snapshot(root, story_path, base)
    if any(job[key] != value for key, value in expected.items()):
        raise ValueError("stale approval: source/export/locks/pending identity differs")
    validate_approvals({"version": 1, "approvals": job["approvals"]}, policy)

    return job


def valid_sha(value):
    return isinstance(value, str) and bool(re.fullmatch(r"[0-9a-f]{64}", value))


def reviewed_file(root, path):
    """Require the exact candidate bytes at the coordinator-controlled ref."""
    root, path = Path(root).resolve(), Path(path).resolve()
    try:
        relative = path.relative_to(root).as_posix()
    except ValueError as error:
        raise ValueError("approval record must have a reviewed repository path") from error
    review = git(root, "rev-parse", "--verify", REVIEWED_REF).decode().strip()
    expected = git(root, "show", f"{review}:{relative}")
    if path.read_bytes() != expected:
        raise ValueError("approval record differs from coordinator-reviewed ref")
    return read_json(path)


def validate_approvals(data, policy):
    if (not isinstance(data, dict) or set(data) != {"version", "approvals"}
            or type(data["version"]) is not int or data["version"] != 1
            or not isinstance(data["approvals"], list)):
        raise ValueError("invalid voice approval schema")
    seen = set()
    for entry in data["approvals"]:
        fields = {"scene", "before_sha", "after_sha", "owner", "source_branch", "source_commit", "reason"}
        if (not isinstance(entry, dict) or set(entry) != fields
                or not isinstance(entry["scene"], str) or not entry["scene"].strip()
                or entry["owner"] != owner_for(policy, entry["scene"]) or entry["owner"] != "claude"
                or entry["before_sha"] is not None and not valid_sha(entry["before_sha"])
                or not valid_sha(entry["after_sha"])
                or not isinstance(entry["source_commit"], str)
                or not re.fullmatch(r"[0-9a-f]{40}", entry["source_commit"])
                or any(not isinstance(entry[key], str) or not entry[key].strip()
                       for key in ("source_branch", "reason"))):
            raise ValueError("invalid/unowned voice approval entry")
        key = (entry["scene"], entry["before_sha"], entry["after_sha"])
        if key in seen:
            raise ValueError("duplicate voice approval delta")
        seen.add(key)
    return data


def approvals(root, policy, path=None):
    path = Path(path) if path is not None else Path(root) / APPROVALS
    data = read_json(path)
    validate_approvals(data, policy)
    # One-time bootstrap from the legacy reviewed inventory. An absent file
    # can only stand for the empty registry, never an approval of any change.
    paths = git(root, "ls-tree", "-r", "--name-only", reviewed_revision(root)).decode().splitlines()
    if path.resolve() == (Path(root) / APPROVALS).resolve() and APPROVALS not in paths:
        if data["approvals"]:
            raise ValueError("voice approvals are absent from coordinator-reviewed ref")
    else:
        reviewed_file(root, path)
    return data


def approved(records, sid, before, after):
    """Return the coordinator record matching this exact prose projection."""
    return next((entry for entry in records["approvals"]
                 if entry["scene"] == sid and entry["before_sha"] == before
                 and entry["after_sha"] == after), None)
