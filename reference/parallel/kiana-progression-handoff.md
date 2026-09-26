# Kiana progression repair handoff

This change repairs delivery and ending progression identified in the assembled audit.
It does not complete Kiana's full route, native contact, mythic access, artwork or game verification.
I own the three existing Kiana modules, new kiana_progression.py, KianaProgressionTests.cs and this handoff for this assignment only.
The parent owns shared engine/schema, Program registration, export and promotion.
Independent review is required before main-export promotion.

## Reproduced problems and changes

The parent reproduced the automatic-rest defect using the initial KianaProgressionTests against the existing main export.
The failure was `Ordinary rest closes or interrupts Kiana before her developed continuation.`
The snapshot follows the old morning milestone, with earlier base scenes completed and the proper 48-hour wait satisfied.
The original first-available selection found farewell before guest_table.
Completing farewell then forbade all ten continuation scenes.

Simply moving farewell later in the export would still permit it to run while a continuation delay was pending.
Farewell now requires either `kiana.future_settled` or the existing `inhuman` fallback, in addition to its original morning prerequisite.
For supported ordinary bodies, future_settled is written only when the new post-followthrough decision is completed.
The existing transformed route remains able to reach its old farewell without entering physical scenes it cannot play.
That abbreviated transformed path is still unfinished route work, not full-depth approval.

Gating farewell exposed a second queue obstruction: the old parting scene could repeat its aborting stay answer before the continuation.
The parent added ManualOnly metadata and centralized automatic selection in Rules.NextRemote.
Kiana's existing parting scene is ManualOnly, preserving its anytime manual Read entry and original answers while removing forced breakup prompts from rests.
Optional retains its previous meaning.

The previously fixed invitation deferral prerequisite remains `kiana.invitation`, not the journal-started flag.
No change here reintroduces that bug.

## Old-save catch-up

New `kiana.another_page` is a manual-only letter available in chapter 5 Drezen after an old completed farewell and morning, with the relationship still open and a supported body.
Its deferral aborts without writing flags, so the player can return later.
Accepting and completing the reply sets `kiana.catchup_requested`.
The old farewell and farewell_kept flags and their timestamps remain untouched.
Commitment, marital history, native quest state and other romances remain untouched.

The parent implemented ForbidOverrides as a narrow exception to an authored scene Forbid.
All ten consequences/follow-through scenes, and the new later-decision scene, declare `{"kiana.farewell": "kiana.catchup_requested"}`.
No other forbidden condition is overridden.
The native completed quest, genuine prior scene milestones, delays, chapter/area, closed relationship and inhuman exclusions remain in force.
Completed scenes remain completed; catch-up resumes remaining eligible work rather than clearing history to replay it.
The catch-up letter is not automatically queued and does not reinterpret every old save as consent to resume.

The letter originally referred to a last line on the farewell page.
Independent review correctly noted that the old farewell gives a clean page.
The corrected opening now offers room for a new invitation without inventing existing writing.

## Later decision and endings

New `kiana.a_place_afterward` requires followthrough_kept, morning, lovers and the completed native soul quest, with 48 hours after the latest required authored milestone.
It has separate separated and bereaved history pages.
It does not invent Elan's approval, death, resurrection, a changed marriage outcome or an earlier promise by an uncommitted Commander.

An already committed Commander can reaffirm or part, preserving the old committed flag in either case.
An uncommitted Commander can now commit, choose to continue without promising a lifetime, or part.
The continuing uncommitted choice sets future_open; the committed choice sets committed.
All completed decisions set future_settled, with closure additionally setting closed.
The initial deferral records no decision or commitment.
Quiet earlier paths and other relationships are neither tested for exclusivity nor cleared.

The old together, bereaved and ascended endings now require future_settled.
Their existing scene IDs, page IDs, prose and answer indices are preserved.
The old unfinished ending excludes future_settled, so it no longer overwrites an explicitly continuing uncommitted relationship.
The existing apart and committed Aeon endings retain their previous history applicability.
The committed Aeon text describes the loss of a possible history, not a claim that the extended campaign was fully played.

New open and open_ascended endings cover the fully developed continuing uncommitted relationship.
New open_aeon covers that history when the timeline is replaced.
New promised is a deliberately provisional outcome for an existing commitment without the new resolution milestone.
It preserves the promise without claiming that the couple already played a complete developed life.
Thus older committed saves are not stripped of their commitment or given an uncommitted breakup ending merely because they lack new content.

Independent review found an early open_ascended sentence claiming Kiana had never asked for a shared lifetime.
The capstone does ask, and accepts the smaller answer.
The corrected ending states that they chose to continue without making that promise.

Farewell retains its original 48-hour delay based on morning.
RequiresAny future_settled is an eligibility gate, not a new delay timestamp source in the current engine.
After completing the decision, a subsequent ordinary rest may therefore deliver farewell immediately.
This change does not claim a new native final-departure trigger.
An old completed farewell cannot replay after catch-up because normal completed-scene exclusion still applies.

## Test coverage and staging

KianaProgressionTests uses the production Rules.NextRemote against the actual ordered Kiana scene subset and shared relationship definitions.
Other characters can delay its global scheduling, but cannot change the relative Kiana ordering checked here.
The test plays actual invitation, rehearsal, stagecraft, married/widow branch, answer when applicable, date, morning and Seelah conversation.
It covers waited, affair and widow histories, both commitment states and both new/old-farewell saves.

For those 12 cases it checks the manual catch-up/deferral behavior, the actual ten-scene automatic queue, no farewell after arbitrarily long waits while required later work is missing, and the later decision after the final chain timestamp.
It walks every later-decision branch, checking protected native/prior flags, preserved commitment, unique normal and ascended endings, and a unique Aeon ending for continuing relationships.
It checks the catch-up exception cannot bypass closure, inhuman or the completed native quest requirement.
It checks the existing transformed farewell fallback remains reachable while physical catch-up remains unavailable.
Existing consequence and follow-through suites continue to cover the full literary branch combinations; this test does not multiply those combinations unnecessarily just to test queue delivery.

The parent stages `development/kiana-progression-review.json` by replacing the existing Kiana objects in the frozen main export and appending the new module scenes.
The parent added an isolated `--kiana-progression` suite switch while main integration is pending.
No shared source, Program, exporter or installed files were edited by this author.
All four modules imported successfully with Python `-B` after the corrected choice literal.
Final suite results and independent review status are recorded below when available.

The final 204-scene staged payload SHA256 is `17170B8915EFB569280EB76F7D50BD4656CBE46EE44BBBFE437E82975486DA17`.
The parent reports 8,140,239 passing rules assertions, including KianaProgressionTests and the updated older campaign test that now plays the ten continuations and capstone before farewell.
The older transformed case now expects the honest provisional promised ending.
These are parent-executed results, not a claim that this author independently ran the C# suite.
Independent review in `reference/story-review/kiana-progression-review.md` accepted the corrected final source with bounded writing 91 and canon 92, with no remaining contribution-level blocker.
Those are the independent reviewer's assessments, not author-awarded scores or full-character approval.
Managed construction and native-binding verification were still being prepared at ownership release.

## Amount and remaining limits

The new module contains two played scenes and four ending variants, 16 nodes, 1,582 raw words and 1,579 distinct-segment words.
Combined Kiana content is now 33 scene definitions, 20,252 raw words and 20,166 distinct-segment words.
This remains at least 834 words below the current floor before semantic meaningful-content review.
The additional text resolves specific choices and history outcomes; no word count is a full-route quality score.

The assembled audit's needs for played marital transition, later discovery wishes, actual exploration/check gameplay, native contact/interruption coverage and attainable Trickster recovery remain open.
This module supplies no skill roll, spawned location, native contact or physical restoration.
Conflicting Elan death/restoration histories still need explicit reconciliation rather than manufacturing one of the two ordinary marital branches.
The existing physical scene exclusions for transformed Commanders are retained.
Full route depth for those paths remains absent.

The shared journal currently completes its objective only for ClosedFlag or CommittedFlag.
A resolved continuing uncommitted relationship therefore remains Started in that objective.
The author has reported this limitation rather than falsely setting committed to satisfy journal display.
A generic objective progression improvement belongs to the parent, not these authored flags.
Real save indices, mid-book interruptions, Unity playback, ToyBox and final art remain unverified by this author.

## Source hashes

| File | SHA256 |
| --- | --- |
| `storylines/kiana.py` | `095CC97EB49E55E0E9DC73E2F59C5020C424360533D5A77BF83D4728078C2EF7` |
| `storylines/kiana_consequences.py` | `445023B128A4DD6B19C9F3F193E7EFCD8FFD6278AF00979257F43C1B79ACB3FE` |
| `storylines/kiana_followthrough.py` | `BDBEF6ABD0B3097DC480B11A05921BAD57E833877E15F54FBE560B647C31BACD` |
| `storylines/kiana_progression.py` | `9DA195E83020C5C3D09E86C654EA0BCD076939F7A339033AC92DEE7B356279A5` |
| `tests/KianaProgressionTests.cs` | `257C3716EE8EB0264936F8092D92DBBF42901009C1564E12633B344369ADD504` |
