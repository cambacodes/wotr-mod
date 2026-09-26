# Konomi political context handoff

This bounded contribution addresses the assembled audit's missing retained-office Chapter 5 political reactions.
It does not replace the separate work on courtship length, ordinary culmination, unresolved patronage, ending readiness, artwork or runtime contact.
Ownership is limited to `storylines/konomi_political.py`, `tests/KonomiPoliticalTests.cs` and this handoff.
The parent owns the new `StartedDialogs` adapter, engine validation, typed binding verifier, managed tests, assembly and export.
No child agents, installed changes or production export writes were made by this author.

## Evidence and semantics

The selection follows `reference/canon-review/konomi-assembled-readiness-20260925.md` and the ordinary-route priority in `reference/story-review/konomi-assembled-readiness-20260925.md`.
The existing post-dismissal commercial work cannot establish native political coverage for a retained officer.
The immediate gap is what Konomi says about Mendev's current condition and what that means for the work she still wants.

`reference/canon-review/konomi-dialog-history-semantics.md` establishes that native `DialogSeen` reads serialized `Player.Dialog.ShownDialogs`, which records a dialogue start before finish actions.
It is not a completion predicate.
The existing shown-cue adapter alone could support remembered speeches but could not faithfully reproduce the native report's start-history predicates.
The parent agreed to implement the narrowly named `StartedDialogs` adapter rather than invent a completed-dialogue flag.

The inspected primary record SHA256 is `980835CF14D0B3007E7A77A12ECC6B0455110B659F20BB3B6A0BF04A249D30E5` for `reference/canon-review/konomi-political-native-records.json`.
The localized consumer-record SHA256 is `9D1F7678B43A64F49A2B3A33E0AE2CF7B69FB72C57F7DDA97A591A2CD032DBAF` for `reference/canon-review/konomi-political-consumers.json`.
The installed-assembly decompilation and its SHA are documented in the semantics report.

| Flag | Adapter | Exact native target |
| --- | --- | --- |
| `konomi.rank_six_started` | `StartedDialogs` | `30333438aac8d3647bef882fa87e978e` |
| `konomi.rank_eight_started` | `StartedDialogs` | `6178470b05c75484085753b821a6a614` |
| `konomi.foreign_help_playing` | Playing `Etudes` | `c6e9a69f602a48e18424f4b6d71062b4` |
| `konomi.council_conclusion_seen` | `SeenCues` | `7f64a30ceb4bfb046990bccbded7ac75` |
| `konomi.political_respect_seen` | `SeenCues` | `8311ef29223c4fe469c95cd8eb80e539` |

Native officer report order is foreign intervention, domestic recovery, ongoing crisis, then earlier fallback.
Foreign intervention requires rank-eight start history and the currently playing approved-help etude.
Domestic recovery requires rank-eight start history without the higher-priority foreign predicate.
Crisis requires rank-six start history without rank-eight start history.
The new choices express those mutually exclusive predicates explicitly rather than assuming the engine selects the first displayed answer.
Approved help by itself does not establish later occupation.
Rank-eight start by itself does not establish a remembered conclusion speech or completion of all finish actions.
The crisis passage describes the danger of famine, not an invented completed famine event.

The council-conclusion memory uses only its seen cue and does not dismiss Konomi or complete her officer etude.
The separate respect cue supports a remembered political acknowledgment without granting affection or requiring it for romance.
The existing selected dismissal answer `73c5728c4c6658344bedcc1b666e598c` and completed officer etude `b5f301fbc4c44535a6309d610d5bd28a` are preserved.

## Played behavior and integration

Append `konomi_political.SCENES`, then call `konomi_political.integrate(payload)`.
The module exposes `STARTED_DIALOGS`, `ETUDES` and `SEEN_CUES`; the integration function adds them with conflict checks.
It adds only `konomi.political_account` to the existing `konomi.power` prerequisites.
No original page, text, choice index, effect, or scene ID is changed.
Calling the overlay twice is idempotent.

The ordinary scene is a non-optional chapter-five conversation in Drezen after the actual `konomi.return` completion and a 24-hour delay.
It requires current officer presence and forbids selected dismissal or the existing farewell.
It uses the verified existing answer list `0dc8b8604bb33c846a63f3eb62443674`.
Completing it supplies an actual timestamp for the following power/future conversation's existing delay.
An already-played old `konomi.power` is not reset; legacy progress remains legacy progress rather than being credited with this new conversation.

The private counterpart is optional, remote and `ManualOnly`, available through the existing Read interface during the authored chapter-five return to Drezen.
It requires selected dismissal, completed officer state and `konomi.private_returned`, while forbidding ordinary presence, inhuman state, farewell and the completed private future.
It does not revive an officer, restore official access, or enter the automatic rest queue ahead of existing private events.
It is not required by the earlier chapter-three private career route.
Private contact remains dependent on the actual existing invitation/return progression.

The four report branches give Konomi different practical interests: limits on foreign administration, scrutiny of domestic recovery arrangements, the continuing crisis, or questions without an assumed later settlement.
Her council and respect memories then react to their own predicates independently.
The Commander can ask to see how she frames a future permitted inquiry or handles a difficult reply.
Those are authored invitations, not performed native policy changes or a claim that the promised follow-up has already been implemented.
The contact-specific opening and concluded-council response distinguish an active appointment from private correspondence after dismissal.
Neither political agreement nor native praise is used to buy commitment or physical intimacy.

All new choices have empty effect lists.
Only normal scene completion is recorded; all native history and other relationships are read-only.
Deferral records nothing.

## Verification checkpoint

A read-only assembly check applied the overlay twice and confirmed identical results.
It compared every old node and choice object with the original export and found them unchanged.
Only the existing power scene's prerequisite list changes among old scene objects.
The author graph walk covered all 30 new nodes across both contact modes and every combination of the five contextual predicates, reaching 128 completed selected paths.
Selected scene length is 651-757 words.
The two versions contain 2,921 raw words but only 1,643 exact-normalized distinct words because most contextual text is shared.
That shared text is not two separate route contributions and the sum does not establish campaign completeness.

`KonomiPoliticalTests.Run` checks the exact new native bindings and preserved dismissal bindings, all 64 contact/history combinations, unique report precedence, independent council/respect memories, current contact, chapter, area, delay, deferral, private queue exclusion and actual power unlock.
Every new page must be visited.
No result may add a flag other than its own scene completion or remove any prior flag.
The test deliberately covers rank-eight start without conclusion, old rank-six history alongside rank eight, help without rank eight, conclusion while still present, interrupted dismissal, missing private contact, and neutral missing history.
The parent owns execution and the new adapter's own type, serialization and native-state checks.
The parent reports that stage 227, SHA256 `B8E0788E85EB1A016C4455B1AA10465449D0FD4A5BB83AE3F618C6E9D5F71514`, passed 8,404,638 rules assertions including the registered `KonomiPoliticalTests` suite.
The parent implemented `StartedDialogs`, reports accepted source review of that adapter, and reports passing managed fixture checks using the actual native collections.
Managed construction of this full stage was still running at handoff freeze and is not claimed passed here.
These are parent-executed results rather than a duplicate run by this author.
Independent literary review of these new contextual pages is not presumed from the adapter review.

The code does not add `ContactUnit`, map NPCs, world interactions, native resource changes or a skill roll.
It inherits the existing retained-office attachment and authored private-book delivery limits.
The adapter and managed construction still require actual Unity/save verification before claiming live history persistence or native delivery.
Existing institutional wording in other scenes and the ordinary route's broader late-campaign depth still need their own review.
No full-route score or release approval is claimed.

## Current hashes

| File | SHA256 |
| --- | --- |
| `storylines/konomi_political.py` | `CA976117821628437F2FB2F74C8006D3000CBD3BD57B701D7438E7A7A899EF29` |
| `tests/KonomiPoliticalTests.cs` | `ED1A3FFD1B107774C2283E8CE25A4B540B7D7695EB042CE88186A91DE01721A8` |

Ownership of the module, test and handoff is released to the parent at these hashes.
No further author edits are planned unless a reviewer identifies a concrete correction.
