# H04 ownership review

Run `python tools/voice_lock_lint.py --strict --story <export>`. For an approved
voice delta, add `--job <signed-job.json>`. `--update` applies only explicitly
approved hash updates/enrollments. `--milestone` forbids all pending prose.
FAST/FULL accept `--voice-job`; `build-expansion.ps1` accepts `-VoiceJob` and
always enforces milestone prose policy. Existing entry points remain available.
Ownership failures return nonzero in every mode, including without `--strict`.

The coordinator owns `refs/rrt/ownership-reviewed`. It points to the reviewed
ownership policy and lock inventory, independently of a worker's `HEAD`.
Pin this ref to the reviewed launch snapshot before starting workers. Until
that ref exists, the existing integration remote
`refs/remotes/origin/claude/trickster-expansion` supplies the reviewed baseline.
A standalone clone with neither ref fails closed. Worker commits cannot replace
the reviewed inventory. Ref mutation/merge locking belongs to H4-P4b; the runner
must keep workers from moving the coordinator's ref or fetching over it during a
review. Candidate ownership policy edits fail until the coordinator reviews and
advances this authority. A ref name identifies a trust location; it never proves
an actor's identity.

`ownership.json` maps scene prefixes to their prose owner. A prefix matches its
exact ID and dot-separated descendants. The initial map preserves the existing
576 locked scenes, without claiming unenrolled scenes across whole routes.
Reviewed map extensions assign ownership to new scene families. Every owned
scene requires a lock or registered held scaffold prose. Existing locks cannot
be removed, and a held scaffold cannot overwrite locked prose.

The `reviewers` object maps key IDs to `{"public_key": "<PEM>"}`. It starts empty:
this package creates no production credentials and grants no approvals. The
coordinator must enroll a real reviewer's public key in the reviewed policy.
Keep its private key outside the candidate checkout and unavailable to workers.
Signature verification uses OpenSSL (`pkeyutl -verify -pubin -rawin`); a missing
executable or invalid signature fails closed. Fixtures use Ed25519 keys.

The reviewer produces a version-1 job record with these fields:

| Field | Reviewed value |
| --- | --- |
| `job_id` | Durable queue job identity; its spelling grants no authority |
| `actor` | `claude`, `codex`, or `gemory`, attested by the reviewer |
| `kind`, `status` | `voice`, `reviewed` for owned prose; `scaffold`, `held` for pending prose |
| `base`, `branch` | Exact candidate HEAD commit and current branch; both must still match |
| `source_sha` | Current generator input inventory hash |
| `story_sha` | Canonical JSON hash of the export reviewed with that source |
| `locks_sha` | Canonical JSON hash of the coordinator-reviewed predecessor inventory |
| `pending_sha` | Canonical JSON hash of the pending registry |
| `approvals` | Exact per-scene `scene`, `before`, `after`, `allow_update` entries |
| `signature` | `key_id` and base64 `value` of the reviewer's signature |

Generate the identity fields with
`tools.voice_authority.snapshot(repo, export_path)`. The reviewer must regenerate
the export from these inputs before signing; the lint verifies the approved
source/export pair rather than rerunning generation. Source identity includes
root Python files, storylines/tools Python files and tools/reference JSON files,
including added/deleted inputs. JSON formatting does not change export identity.
All approval entries must match the actual before/after prose projections.
An enrollment uses `before: null` and `allow_update: true`; `--update` writes its
lock with `since` set to the candidate base. Existing owner/since fields and the
lock file's newline style remain unchanged.

Sign `tools.voice_authority.canonical(unsigned_job)` (UTF-8 sorted compact JSON,
without `signature`) using the enrolled private key, for example:
`openssl pkeyutl -sign -rawin -inkey <external-key> -in <payload> -out <signature>`.
Attach the base64 signature as the final `signature` field. The signed actor and
per-change approvals certify ownership; branch/message strings and
`RRT_VOICE_OWNER` do not. Changing source, export, candidate base, predecessor
inventory, pending registry or approval fields invalidates the job.

`plans/prose-pending.schema.json` describes `plans/prose-pending.json`. Each entry
names `scene`, `node`, `surface` (`node`, `paragraph`, `choice`), `index` (null for
a node; zero-based for the other surfaces), and `text_sha` from
`voice_authority.digest(text)`. Use `[[PROSE_PENDING:<slot>]]` in that exact text.
The lint also detects prose-pending spelling variants and the word placeholder.
Duplicate, missing, ambiguous, stale and unregistered targets fail. Nonempty
pending registries pass only with a signed held scaffold job bound to this branch
and export. They fail every milestone, including a signed held scaffold job.

Acceptance: `python -m unittest tests.test_voice_authority
tests.test_voice_lock_lint -q` uses disposable repositories and real signatures.
Keys, exports and all fixture output are deleted from system temp on completion.
