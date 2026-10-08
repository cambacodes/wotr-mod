# H04 ownership review

Integration runs `python tools/voice_lock_lint.py --strict --integration --story <export>`
and `python tools/prose_pending_lint.py --integration --story <export>`.
An owned prose change requires an exact coordinator approval record.
`--update` applies approved hash updates and enrollments; `--milestone` forbids
all pending prose. Ownership failures return nonzero even without `--strict`.

The coordinator owns `refs/rrt/ownership-reviewed`, independently of a worker's
`HEAD`. The runner must prevent workers from moving this ref or fetching over
it during review. The lint reads the ref but never advances it. Branch names,
commit messages, author strings and `RRT_VOICE_OWNER` grant no authority.
This protects against accidental or agent-induced changes under one machine
owner/coordinator; it does not defend against a malicious root operator.

`ownership.json` contains `version: 1` and `scene_prefixes`, mapping each scene
prefix to its prose owner. Prefixes match exact IDs and dot-separated descendants.
The initial map preserves the existing 576 locks without claiming whole routes.
Policy changes require coordinator review and a ref advance. Every owned scene
requires a lock or registered integration/held scaffold prose. Existing locks
cannot be removed, and a held scaffold cannot overwrite locked prose.

Until the protected ref exists, the existing integration remote
`refs/remotes/origin/claude/trickster-expansion` can supply the legacy lock/policy
baseline. If the reviewed snapshot has no policy, its committed locks supply the
exact owner map. If it has no approval registry, only an empty local registry is
accepted. This bootstrap grants no prose-change authority: an actual approval
must be present at `refs/rrt/ownership-reviewed`. A clone with neither baseline
ref fails closed.

## Exact voice approval records

`voice-approvals.json` has this shape:

```json
{
  "version": 1,
  "approvals": [
    {
      "scene": "route.scene",
      "before_sha": "<64-hex predecessor projection hash, or null for enrollment>",
      "after_sha": "<64-hex candidate projection hash>",
      "owner": "claude",
      "source_branch": "claude/voice-branch",
      "source_commit": "<40-hex source commit>",
      "reason": "Coordinator accepted the owned voice rewrite"
    }
  ]
}
```

The registry must have exactly the same bytes as its file at the protected ref,
including JSON formatting and line endings. A locked-scene change is accepted
only when an entry matches its scene ID, reviewed predecessor hash and candidate
hash exactly. Hashes cover ordered node text, paragraph text and choice labels;
gameplay metadata remains outside the projection. Historical entries may remain
in the registry but cannot authorize a different delta. Duplicate deltas and
unowned entries fail. Source branch/commit and reason record review provenance;
they are not alternate ways to authorize prose.

An enrollment uses `before_sha: null`. `--update` writes its lock with `since`
set to `source_commit`. Existing `owner` and `since` values are preserved when
hashes change, as is the lock file's newline style. Unapproved changes fail
without writing locks. No signing key, key enrollment or per-change signature
is required.

## Coordinator procedure

1. Pin the reviewed lock inventory and owner map before launching workers.
   For the legacy bootstrap, retain all existing locks and the exact derived
   owner map; start `voice-approvals.json` with an empty approvals list. Review
   any new ownership prefixes separately before using them for enrollment.
2. Review the owner's candidate source and regenerate its export. Obtain a base
   export whose selected scene projections match the current reviewed locks.
   Prepare the selected exact deltas with the candidate's source provenance:

   ```bash
   python tools/voice_approve.py --base <base-export> --candidate <candidate-export> --prefixes <scene-prefix> <another-prefix> --source-branch <owner-branch> --source-commit <full-source-commit> --reason "<review reason>"
   ```

   The CLI writes `tools/route_packs/voice-approvals.json`, retaining reviewed
   history. It rejects a stale base, deleted scenes, unknown prefixes or unowned
   targets. It never moves the protected ref. Prepared records grant no authority
   until the coordinator commits and pins them.
3. Commit the approvals together with the reviewed policy and predecessor locks
   in a coordinator commit. Keep a matching reviewed `development/Story.json`
   available for pending-choice append comparisons. Advance the ref with
   compare-and-swap:

   ```bash
   git update-ref refs/rrt/ownership-reviewed <reviewed-commit> <previous-ref>
   ```

   Use the all-zero old ID for first creation. Hold the runner's coordinator
   lock, and stop/review again if the previous ref no longer matches. Distribute
   the reviewed pin and exact registry bytes to workers.
4. Run the integration lints against the candidate export. Apply approved hashes
   with `python tools/voice_lock_lint.py --strict --integration --update --story <candidate-export>`.
   After successful integration, commit the accepted inventory/export and advance
   the protected ref with another compare-and-swap. This makes the new hashes the
   predecessors for subsequent reviews. Do not advance it to an unreviewed worker
   snapshot. The wrapper/coordinator owns commits; workers do not commit.

## Pending prose and held scaffolds

`plans/prose-pending.schema.json` describes `plans/prose-pending.json`. Entries
name `scene`, `node`, `surface` (`node`, `paragraph`, `choice`), `index` (null for
nodes, zero-based otherwise), and `text_sha` from `voice_authority.digest(text)`.
Integration placeholders use `[PROSE PENDING: <woman> - <want / act / cost>]`;
appended player labels use `[PROSE PENDING: choice - <intent>]`.
`[[PROSE_PENDING:<slot>]]` markers remain supported. Spelling variants and the
word placeholder are detected. Duplicate, missing, ambiguous, stale and
unregistered targets fail. Integration permits exact registered placeholders
without granting permission to change locked prose. Milestone always forbids
pending prose.

Worker scaffold gates omit `--integration` and require `--job <held-job.json>`.
A held job retains the version-1 identity fields `job_id`, `actor`, `kind`,
`status`, `branch`, `base`, `source_sha`, `story_sha`, `locks_sha`, `pending_sha`
and `approvals`. Use `kind: scaffold`, `status: held` and an empty approvals list.
Generate identity hashes with `tools.voice_authority.snapshot(repo, export)`.
The job must be at a repository path with identical bytes at the protected ref,
and still match candidate HEAD, branch, source, export, locks and pending registry.
Put it outside generator-input directories, for example at `held-job.json` in the
repository root, to avoid hashing the record into its own source identity.
Embedded job approvals do not replace the voice registry. FAST/FULL retain
`--voice-job`; `build-expansion.ps1` retains `-VoiceJob` and milestone policy.

`plans/claude-work-queue.json` lists work requests, not prose authority. It may
contain multiple requests for a scene. When Claude fills a target, remove its
exact pending-registry row and complete the corresponding queue request in the
same reviewed change. Stale targets fail.

## J05b: separate pending-choice append review

[The explicit J05b request](plans/j05b-append-approval-request.json) names the
permitted hosts and predecessor hashes. It is a request, not an approval record.
After the actual choices are appended and their exact labels registered, run:

```bash
python tools/prepare_voice_job.py --story <fresh-export> --output tools/route_packs/plans/j05b-append-approvals.json --source-branch <source-branch> --source-commit <full-source-commit> --reason "<review reason>"
```

The output uses the same `version`/`approvals` record form as voice approvals.
Commit that separate file and advance the protected ref by compare-and-swap,
then run:

```bash
python tools/voice_lock_lint.py --strict --integration --story <fresh-export> --append-approvals tools/route_packs/plans/j05b-append-approvals.json
python tools/prose_pending_lint.py --integration --story <fresh-export>
```

Append approval requires an exact before/after match and the reviewed export.
Existing node text, paragraph text, choice labels and node order must remain
unchanged; each new choice appends at the end and matches a registered pending
choice label. At least one actual append is required. New nodes in locked scenes
are outside this exception. Gameplay metadata remains subject to the normal
save-compatibility and progression checks.

Predecessor locks are retained; the lint reports approved appends and changed
scene hashes. `--update` and `--milestone` reject this exception. After Claude
fills the labels, use the ordinary voice registry, remove completed pending rows,
update locks and advance the reviewed ref. No release may contain pending labels.

Acceptance: `python -m unittest tests.test_voice_authority tests.test_voice_lock_lint tests.test_prose_integration -q`.
The probes use real Git refs and disposable repositories in system temp, covering
exact approvals, worker forgeries, hash mismatches, enrollment, selective updates,
pending targets, held jobs and append boundaries, with mutation witnesses.
