# Seelah progression implementation handoff

Status: source released for author-excluded literary and technical review, then staged integration.
This contribution changes `storylines/seelah_later.py` and adds `storylines/seelah_progression.py` plus `tests/SeelahProgressionTests.cs`.
No `expansion.py`, `Program.cs`, shared engine, generated export, installed content, or other author's source was edited by this author.
Root independently owns the new ForbidOverrides support and metadata on the affected expansion scenes.

| File | SHA256 |
|---|---|
| `storylines/seelah_later.py` | `AE09427F71D7866DA494A41D2E315DD3BEE3B3D7B4ABED95A9D0F41297E0B4C9` |
| `storylines/seelah_progression.py` | `BCA0727D632A636AC6BBC39E2E126B405B20A36A5EE5FE41AE50FF8A216B7EE8` |
| `tests/SeelahProgressionTests.cs` | `C88974604395067A0794EB70217359AD54C16B1DFA8BF72ABFED2705A6F3D76A` |

## Reproduction before editing

A read-only selected-choice walk started with `seelah.weight`, `seelah.courting`, and `seelah.lovers`.
It completed the original `road` through home/acceptance, then `ordinary`, then the boots branch of `farewell`.
The resulting state included `seelah.committed`, `chosen_future`, `home_plans`, `at_home`, both completed later scenes, and `farewell_kept`.
It contained none of `faith_spoken`, `aftermath_ready`, or `late_race_kept`.
This reproduced the actual authored bypass identified by the assembled audit before source changes began.
It was a story-graph reproduction, not a Unity execution claim.

## Implemented contract

`road` retains its existing scene ID, entry label, weight prerequisite, area/chapter restrictions, and delay.
New entry pages precede its original `start` node and make the requirements visible instead of hiding the conversation.
No original node IDs or choice indices were removed or reordered within their nodes.
The original `yes` node's existing index-zero answer now proceeds through a final classification page before completing the scene.
Its original `chosen_future` effect is retained.

The developed path requires `seelah.late_race_kept`.
That existing flag implies the played aftermath chain and course/lesson/page/race chain under their actual prerequisites.
Watching, winning, stumbling, and the non-roll wide route all qualify.
No physical intimacy, successful roll, specific lesson arrangement, or native good ending is required.
The two later activity scenes remain optional.

An existing copyist episode must have either `seelah.copyist_followed` or `seelah.letter_return_addressed`.
No originating `letter_unsettled` history means no artificial copyist requirement.
A discussed-only episode uses the return bridge before this stronger promise.
The original unresolved/history flags are never cleared.

The gate offers concrete next invitations when activity is missing: washing yard, repair consequence, faith conversation, roof evening, or the course/race sequence.
These pages defer without completing `road` or awarding missing content.
The actual entry remains available when the player returns.

Before the original future conversation, current native quest branches distinguish unfinished, returned bad, returned moderate, and other returned outcomes.
Bad takes precedence over moderate.
Returned branches further distinguish Elan's actual death alias without inventing a living appearance, agreement, or letter.
These branches read the existing current aliases when the player selects their answer.
They do not depend on an old stored `aftermath_ready` outcome and do not mutate any native quest.

The current-context passage records `seelah.future_reviewed` only on the developed road path when it reaches the original `start`.
This is evidence that the new road pages were played, not a generic reusable native-outcome cache.
Every normal new road entry traverses the current-context pages again before reaching that point.
The final classification also checks actual activity and copyist resolution before awarding `seelah.developed_commitment`.
Old saves resumed directly inside the original commitment nodes can finish their existing promise without receiving the new marker unless the required reviewed history exists.
Live native/contact changes during a resumed book still need engine-level verification; the source does not claim to freeze native quest state across arbitrary external edits.

## Explicit shorter relationship

When the activity is not completed, the player can explicitly say they cannot promise those days before the war ends.
This still passes through current quest context.
Seelah offers an ongoing relationship one evening at a time without declaring that they have already built a shared life.
Acceptance sets the compatible old `committed` and `chosen_future` flags plus `seelah.short_future_chosen`.
It does not grant activity, copyist resolution, `future_reviewed`, or `developed_commitment`.
Declining that smaller promise uses the existing honest parting node.

The shorter option does not bypass a live copyist conversation.
The player must first address an actual unsettled episode through the already authored bridge.
This keeps a necessary unresolved disagreement from being erased by choosing a shorter route.

## Existing promises and farewells

New scene `seelah.future_followup` requires the old completed `road` and `committed` flags and excludes `developed_commitment`.
It preserves the earlier promise, explains missing invitations, and remains uncompleted when the player defers.
After the actual activity, resolved copyist history, and current native context, the player can reaffirm the existing commitment and earn the developed marker.
An old deliberately short history can also develop later; its original short marker remains historical, while ending selection gives the developed marker precedence.
No old scene flag is cleared to replay the original proposal.

`farewell` now begins with an explicit opportunity to review remaining invitations or proceed knowing that Drezen meetings will remain unfinished.
The review can point to the copyist, activity chain, after-race evening, or final activity outing.
All postponements happen without recording the farewell scene or changing history.
Original farewell nodes and choices remain intact after the new gate.

New scene `seelah.farewell_catchup` requires an existing completed farewell and commitment while in Chapter 5 Drezen.
It acknowledges the earlier goodbye and offers another invitation while they are still present.
Explicit acceptance sets `seelah.catchup_requested`; postponement does nothing.
The old farewell and commitment remain intact.

The migration scene itself forbids `seelah.farewell` unless `seelah.catchup_requested` supplies root's new override.
It includes `ForbidOverrides: {"seelah.farewell": "seelah.catchup_requested"}`.
The catch-up invitation itself does not need that override because it is the consent entry.

Root confirmed applying the same narrow metadata to these existing scenes:

- `seelah.borrowed_saw`
- `seelah.platform_finished`
- `seelah.inheritors_corner`
- `seelah.roof_evening`
- `seelah.late_course`
- `seelah.late_lesson`
- `seelah.late_page`
- `seelah.late_race`
- `seelah.late_afterglow`
- `seelah.late_first_step`
- `seelah.letter_return`

The override must waive only the matching authored farewell forbid.
It must never bypass closure, death, departure, inhuman restrictions, actual native availability, chapter, area, delay, or completed-scene exclusion.
No chapter transition, resurrection, or lost actor is manufactured by this catch-up.

## Ending behavior

The existing together, unsettled, grieving, unfinished-work, changed, and ascended ending IDs retain their original native/mythic availability requirements.
Their original `start` text remains available only through the new developed-history branch.
New short-history and earlier-promise pages distinguish a deliberate modest promise from an older commitment that has not played the new development.
Developed history wins when both developed and old short markers are present.
Each branch preserves the applicable native or mythic consequence without pretending that unplayed dates happened.
The apart, uncommitted, and Aeon endings are unchanged.
The older original ending still does not provide all desired home/travel/native-career callbacks; that larger ending-quality work remains open.

## Root integration hooks

Import and append `storylines.seelah_progression.SCENES` once in the expansion assembly.
`seelah_later.py` imports only its page factories and does not append the new module's standalone scenes itself.
Integrate the separately reviewed `seelah_return.SCENES` in the same staged story.
The new tests need the full core, Abyss, aftermath, late, return, and progression sources present.
Register `SeelahProgressionTests.Run(story, Check)` in `Program.cs` after checking that `seelah.future_followup` exists.
The project automatically includes the new test file through its existing C# project conventions.
Root must regenerate and verify the staged export, then run the rules suite before replacing the main artifact.

## Verification and review limits

Read-only Python imports verified unique node IDs and resolved edges across the modified later module and both new standalone progression scenes.
An actual fresh late-start core walk reached the explicit short promise without developed status.
The same core followed the real four aftermath and four late scenes, then reached developed acceptance.
Read-only graph walks also checked public/burned unresolved gates, the actual return bridge, migrated promises, current native outcome branches, and the three ending-history selections.
These checks passed before release.

`SeelahProgressionTests.cs` contains focused Rules-based tests for the reproduced bypass, untouched deferral state, the short route, farewell preservation, explicit catch-up and its non-overridable restrictions.
It walks actual fresh source chains for running and watching, including success, stumble, and wide-route results.
It walks the actual Abyss incident with and without discussion before leaving the act, then the bridge and developed road.
It verifies that full copyist follow-up excludes the return scene.
It changes current native quest aliases after the faith conversation and checks the selected new context pages, including Elan's death and bad-before-moderate precedence.
It covers already completed road migration and exclusive developed/short/legacy ending page selection.
Unrelated Konomi and Kiana commitment sentinels remain present in the tested paths.

The C# tests were authored but not run by this author against a staged export; root owns that export and registration.
No Unity execution, live save migration, native contact persistence, scene art, or installed UI has been claimed.
The new dialogue and changed ending presentation need independent literary/canon review, and the gates/migration/tests need independent technical review.
The new source is not a complete Seelah route approval or a substitute for the missing native-friend social development, attainable departure restoration, art, and game verification.
