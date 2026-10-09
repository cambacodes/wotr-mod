# struct2-02 structural evidence

Base: `78f9b714dd8b5ea35e58c0a37609d6a9defdbd36`.
All 20 assigned character source snapshots were read via their manifest
`bundle_path`; each matched the current source before edits. The bundle contains
no audit or plan input entries; the task's findings were checked against current
assembled behavior. No quality score is awarded by this implementation.

## Completed structural items

- **MEL-02 — fixed structurally, Claude prose pending.** The late cloud pass now
  invokes route-owned selection after prose transformations. Retained inaccurate
  owed paragraphs are retired with `Forbids: trickster.ever`; replacement
  placeholders keep the three independent voyage predicates. The sailor-debt
  commitment callback has the same retirement/replacement pair. No scene, node,
  answer ID, answer position or target changes. Regression exercises salt before
  first contact in all three meeting copies, the actual name/owed answer, and
  commitment. Replacement prose must avoid assuming a venue and premature return.
- **D1 — fixed.** Split the existing ending text at its paragraph boundary and
  retain the exact optional confession prose under `jerribeth.yard_confessed`.
  The breakup remains available for prisoner, check and pre-commission histories.
  Sibling farewell/start and room_measure/shelves callbacks retain their gates.
- **trickster_all_romance-cepilogue-p1-001 — already-fixed.** Current
  `dorgelinda_trickster.DERIVED_FORBIDS` excludes both quarrel_unmended and
  cold_unmended from harem.eligible. cold_unmended itself forbids quarrel_mended.
  Assembled regressions check current partner readers, preserved committed
  history and the mended control. Existing tests/test_dorgelinda_commitment.py
  also covers recomputing old saves and professional-progress/closure siblings.
- **CONVERT aranka.trickster.verse.her_letter — fixed structurally, Claude prose
  pending.** Original Chapter 3 and Chapter 5 IDs are physical presence-hub
  interactions, with no Kind. New yard variants use the established fallback
  actor. Original answers, ordering, flags, delays and voyage restrictions stay.
  Arrival readiness now includes the already-paid PRIMED history, eliminating
  the answered-before-presence cycle. Mutual completion forbids prevent replay
  between market and yard. All twelve changed node surfaces are registered.

## Escalated conversions

Owner: coordinator for venue/lifecycle decisions; engine owner for live bindings;
Claude for resulting staging prose. Existing remote copies stay playable until
an approved physical replacement can preserve their identity and consequences.
Changing only Remote or Kind would leave EntryTargets without an attachment.
Evidence: src/Story.cs EntryTargets (explicit AnswerLists or verified presence
hub), src/Story.cs Scene/Choice (no generic combat/travel authoring action),
storylines/melazmera_trickster.py SCENES/integrate, melazmera_hoard.py visit/letter,
jerribeth_trickster.py PRESENCES, and dorgelinda_ledger.py office/GATE.

| Item | Missing binding and recommendation |
| --- | --- |
| CONVERT melazmera.trickster.ch4.hunt | Colyphyr camp fire entry; bind rest-at-camp lifecycle and the cave-tour follow-up. |
| CONVERT melazmera.trickster.commit.stone | Physical lair entry plus flight, arrival and return; approve a playable travel contract before hosting the hoard decision. |
| CONVERT melazmera.trickster.beat.count | Drezen quarters/roof host; authorize a Melazmera presence and location-specific interaction. |
| CONVERT melazmera.trickster.beat.rain | Durable Drezen visit/return lifecycle and allowed physical venue; keep existing travel explanation until approved. |
| CONVERT melazmera.trickster.ch4.salt | Colyphyr lair interaction binding; retain the existing Thievery outcomes and seal removal while attaching to a verified local encounter. |
| CONVERT melazmera.trickster.visit.heap | Lair arrival/return contract; share the approved commit.stone travel binding. Preserve explicit-slot host IDs. |
| CONVERT melazmera.trickster.beat.dinner | Perimeter attack/reward lifecycle; bind actual encounter completion before presenting the heart. |
| CONVERT melazmera.trickster.stone.shield | Yard aftermath host; retain note and the existing disposal choices. |
| CONVERT melazmera.trickster.beat.joke | Drezen office presence; use the same approved physical actor lifecycle as count. |
| CONVERT melazmera.trickster.beat.putting_down | Quarters presence and optional well consequence; approve the latter's completion binding separately. |
| CONVERT melazmera.trickster.beat.seal | Window/quarters presence; keep letter setup separate from the physical exchange. |
| CONVERT jerribeth.farewell_review | Existing jerribeth.presence requires VISIT_DUE and forbids VISITED, so it cannot host general farewell histories. Approve a living/tenant-aware physical host without extending collection's promise. |
| CONVERT jerribeth.another_evening | Same host issue, plus current image/sending prose. Approve lifecycle and substantive continuation before replacing the remote copy. |
| CONVERT jerribeth.commission | Chapter 3 gate-yard/cell host; existing presence is Chapter 5 collection only. Approve native yard entry and prisoner lifecycle, preserving payments/checks. |
| CONVERT dorgelinda.ledger.the_west_gate | Office dialogue already narrates rescue, with a Mobility check, but has no real combat encounter/objective. Approve road area/enemy/rescue-completion bindings; the narrative wound flag is not damage. |

## Class sweep and limitations

Melazmera's three meeting copies, commitment count siblings (rent/harpoon/crevice),
shared hunt and heap were inspected; no replacement voice was written. The window
rent paragraph and commitment rent callback also assume an island venue: queue
Claude to provide venue-neutral wording (PROPOSE, outside the named owed fix).
Jerribeth's confession producer, prisoner alternative, successful-check terminals,
farewell and shelves consumers were checked after all transformations.
Aranka's late twin, market/yard fallback, closure and cross-venue completion were
checked in the assembled export. Dorgelinda's cooled, mended and committed readers
were checked through the real derivation model.

22 exact placeholder targets and matching Claude work requests were added, plus
one proposal for the sibling rent recollection.
Integration-placeholder lint passes; milestone quality remains pending on Claude.
No live placement/combat/travel or independent INT/HOW/COX >=91 acceptance exists.
Runner owns final source/export sealing, staging, commits and pushes.

## Own checks (not final runner receipts)

- `python expansion.py`, with RRT_STORY_OUTPUT in system temp: exit 0,
  4,083 assembled scenes; regeneration will be repeated for the final source.
- `python /work/Writer/tools/id_guard.py <system-temp-export-tree> --baseline
  <system-temp-base-export>`: exit 0; no lost IDs or shortened choice lists.
  Baseline bytes are from git show of the exact pinned base.
- `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io`, with
  RRT_TEST_STORY pointing to that export: exit 0, 23 tests. Earlier failures
  exposed the partial registry fixture and incomplete test history setup; both
  were corrected.
- `python tools/prose_pending_lint.py --story <system-temp-export> --integration`:
  exit 0, no hard failures. `python tools/claude_work_queue_lint.py`: exit 0.
- `git diff --check`: exit 0; changed existing files decode as UTF-8 and keep
  their original LF/CRLF style.
- Standalone unselected targeted unittest commands exited 137 and produced no
  test results. They are failed checks, not inherited passes or exemptions.

These observations do not replace the wrapper's final profile/environment/source
and export-bound receipts. Final report gates remain empty for the runner.
