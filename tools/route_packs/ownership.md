# H04 ownership review

Integration: run `python tools/voice_lock_lint.py --strict --integration --story <export>`
and `python tools/prose_pending_lint.py --integration --story <export>`. For an approved
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
scene requires a lock or registered integration/held scaffold prose. Existing locks cannot
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
`voice_authority.digest(text)`. Integration jobs use `[PROSE PENDING: <woman> - <want / act / cost>]`;
appended player labels use `[PROSE PENDING: choice - <intent>]`. Existing
`[[PROSE_PENDING:<slot>]]` scaffold markers remain supported.
The lint also detects prose-pending spelling variants and the word placeholder.
Duplicate, missing, ambiguous, stale and unregistered targets fail. Nonempty
pending registries pass with explicit `--integration` at the coordinator's main
integration gate. This mode grants no permission to change locked text. Worker
scaffold gates omit `--integration` and require a signed `scaffold`/`held` job
bound to their branch and export. `--milestone` always wins over integration
and signed scaffold jobs: every placeholder is forbidden. FAST uses integration;
FULL supplies milestone. A held worker job uses `--voice-job` at FAST only when
its runner deliberately selects that integration gate; run the direct lints
without `--integration` to enforce the held-scaffold policy.

`plans/claude-work-queue.json` is the separate list of Claude work requests,
including canon renames, verifier findings and placeholder beat briefs. The
migration preserves every request, including multiple requests for one scene.
Its companion schema and `python tools/claude_work_queue_lint.py` validate the
request shape. Queue entries grant no placeholder or voice authority; only the
exact `plans/prose-pending.json` text targets can register placeholders. When
Claude fills a target, remove that exact registry row and complete its queue
request as part of the same reviewed change. A stale registry never passes.

Acceptance: `python -m unittest tests.test_voice_authority
tests.test_voice_lock_lint -q` uses disposable repositories and real signatures.
Keys, exports and all fixture output are deleted from system temp on completion.

## Coordinator procedure: reviewed ownership ref

The coordinator performs these steps; worker branches do not move the ref,
enroll reviewer keys, sign approval records or substitute their own HEAD.
No production private key or signature is included in this implementation.

1. Review the merged inventory against the fresh export. Initially the trusted
   integration remote has no `ownership.json`; `trusted()` derives the exact
   scene-owner map from its committed locks with no reviewer keys. The candidate
   ownership map must equal that map until an explicit review accepts a policy
   update. Every old locked scene remains enrolled. Add only the approved new
   prefixes and the actual coordinator reviewer public key to `ownership.json`.
2. Record the approved policy and unchanged predecessor locks in a reviewed
   coordinator commit, together with its generated `development/Story.json`.
   The reviewed export is needed to prove that J05b retains all original text.
   Sign the policy-bearing Git commit with the coordinator's established Git
   signing identity (`git commit -S`); verify that signature/identity under the
   coordinator's existing key trust before pinning. This administrative review
   is separate from an Ed25519 per-change approval. The lint itself trusts the
   protected ref; it does not authenticate Git commit author strings or move it.
3. Pin the full reviewed commit ID with a compare-and-swap, for example
   `git update-ref refs/rrt/ownership-reviewed <reviewed-commit> <previous-ref>`
   (use the all-zero old ID for first creation). Protect this ref under the
   runner's H4-P4b lock and distribute its pin to workers. Do not point it to
   an unreviewed candidate or use a worker fetch to advance it. On main, the
   policy file must match the policy at this ref byte-independently as JSON;
   `tools.voice_authority.trusted(repo)` now accepts that reviewed policy.
4. For each actual prose delta, regenerate from the candidate source and build
   a version-1 unsigned job using `snapshot(repo, export)`. Include the exact
   candidate HEAD, branch, per-scene predecessor/current text hashes and explicit
   `allow_update`. Attest `claude`/`voice`/`reviewed` only for Claude-reviewed
   prose. Enrollments use `before: null`; updates preserve existing owner/since.
   Put the payload, signature and signed job outside the candidate tree so that
   the source hash does not include the job itself.
5. Sign the canonical unsigned job with the private key matching the enrolled
   public key. Attach `signature: {key_id, value}` with base64 signature bytes.
   Run the exact lints with `--job <external-signed-job>`. Apply `--update` only
   for signed voice updates/enrollments. After successful review, the coordinator
   may advance the reviewed ref to the accepted inventory/export. Reissue job
   records after a changed HEAD, branch, source, export, registry or predecessor
   inventory; old records are invalidated automatically.

Tests simulate both the initial pin and subsequent policy enrollment on a main
branch. A candidate policy edit or worker commit remains rejected until the
coordinator advances the protected ref; later forged key enrollment still fails.
Fixture signatures use disposable Ed25519 keys outside the fixture checkout.

## J05b: separate pending-choice append review

[The explicit J05b request](plans/j05b-append-approval-request.json) names the
locked Hepzamirah instructions host (05) and Areelu wager/lens hosts (10–15),
their predecessor hashes, permitted pending choice surface and authored intent.
Ruling 16 is a packet-reader dependency, never blanket prose approval. This
request is unsigned and deliberately fails as `--append-approvals`; it cannot
approve prospective text whose exact hash has not yet been reviewed.

After J05b implements the actual appended choices and registers their exact
labels, the coordinator runs:

```bash
python tools/prepare_voice_job.py --story <fresh-export> --output <external-payload>
openssl pkeyutl -sign -rawin -inkey <external-key> -in <external-payload> -out <external-signature>
```

Attach the base64 signature and enrolled `key_id` to the payload JSON as above,
writing `<external-signed-append-job>`. Pass it separately from a Claude voice job:

```bash
python tools/voice_lock_lint.py --strict --integration --story <fresh-export> --append-approvals <external-signed-append-job>
python tools/prose_pending_lint.py --integration --story <fresh-export>
```

The record is `codex`/`scaffold`/`reviewed`, has exact `before`/`after` per-scene
hashes and `allow_update: false`. The lint also compares with the export at the
reviewed ref: no existing node text, paragraph text, choice label or node order
may change; each added choice must append at the end and match a registered
`[PROSE PENDING: choice - ...]` label. It requires at least one actual append.
New nodes in locked scenes are outside this exception. Appended choices may
point to retained/new external targets as allowed by the task; ordinary
save-compatibility and progression checks still apply to all gameplay metadata.

Predecessor locks are retained. The lint reports the signed append count and
also reports actual changed scene hashes, so this exception never disguises a
pending append as finished Claude prose. `--update` and `--milestone` reject
append approvals; signing a generic Codex voice job still cannot authorize any
owned prose change. After Claude fills the labels, use the usual exact signed
Claude voice update, remove the completed registry targets, re-lock and have the
coordinator advance the reviewed ref. No release can contain pending labels.

Acceptance: `python -m unittest tests.test_voice_authority
tests.test_voice_lock_lint tests.test_prose_integration tests.test_test_gate -q`.
The probes cover registered/unregistered integration targets on all surfaces,
stale/duplicate/schema faults, milestone rejection, policy updates at a reviewed
main ref, signature enforcement and locked-text/append boundaries.
