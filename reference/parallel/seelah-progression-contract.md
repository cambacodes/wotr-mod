# Seelah progression contract

This is a read-only implementation proposal based on the actual Seelah scene modules, the assembled readiness audit, `Rules.Available`, `Rules.Match`, and `Main.RecordProgress`.
Only this planning document was authored for the assignment.
It does not approve the assembled route, supply the missing early native-friend development, or replace independent review.

## Recommended minimum

Keep `seelah.road` discoverable at its existing `seelah.weight` threshold.
Before its strongest future promise, require the completed shared activity `seelah.late_race_kept`, address any abandoned copyist episode, and speak about the current native quest circumstances.
Offer an explicit shorter relationship outcome for someone who chooses not to complete that development.
Preserve existing commitments and completed scenes instead of rewriting old saves to resemble a new playthrough.

The recommended activity is the race outcome, not winning the race or choosing physical intimacy.
Its actual prerequisite chain already includes meaningful disagreement, quest reflection, and reciprocal courtship.
Requiring it promotes a substantial existing arc into the ordinary developed route without requiring all six late scenes.
The two later scenes, `late_afterglow` and `late_first_step`, remain optional opportunities with an explicit pre-farewell reminder.
The separate native-friend social decision requested by the audit is still missing; this contract does not claim the race substitutes for that work.

## Existing evidence and dependency chain

| Evidence | Actual meaning |
|---|---|
| `seelah.weight` | Original core discussion completed; currently sufficient to expose `road`. |
| `seelah.saw_arranged` | The borrowed-saw disagreement reached an arranged response. |
| `seelah.platform_kept` | Its later consequence and Seelah's gift/loan distinction were played. |
| `seelah.faith_spoken` | The faith conversation reached its end after an actual current quest branch. |
| `seelah.aftermath_ready` | The roof evening completed, after the preceding three aftermath scenes. |
| `seelah.late_course_planned` | The course and lesson arrangement were selected. |
| `seelah.late_lesson_kept` | The actual lesson was experienced. |
| `seelah.late_page_kept` | The booklet conversation and the Commander's preference were played. |
| `seelah.late_race_kept` | The race, losing/winning song, and shared afternoon completed. |
| `seelah.late_evening_kept` | Optional afterglow completed, including the quiet alternative. |
| `seelah.late_campaign_kept` | Optional first-step outing completed. |

The late helper requires `seelah.courting` and `seelah.aftermath_ready` for every late scene.
`late_race` additionally requires both `late_lesson_kept` and `late_page_kept`.
The latter requires the former, which follows the course.
Thus the proposed activity threshold entails four aftermath scenes and four late scenes, not merely a flag selected on the race invitation.
It leaves the two final late scenes, the old optional `aftercare`, and every alternative branch optional.
Do not add redundant requirements for each intermediate scene unless protecting a documented malformed-save case.
Existing legitimate earned terminal flags should retain their meaning after an update.

The authored timing remains significant.
These scenes use 24-hour waits, with 48 hours before the race.
The contract must explain that this is a developing relationship over several visits, rather than presenting all the content as a single conversation available immediately before Threshold.
Do not remove the timers or fabricate completion to accommodate a late start.

## Precise predicates

The following notation describes conditions, not newly implemented flags.

```text
activity_earned := Has("seelah.late_race_kept")

abyss_addressed := !Has("seelah.letter_unsettled")
               || Has("seelah.copyist_followed")
               || Has("seelah.letter_return_addressed")

quest_case := unfinished                  if !souls_returned
           := returned_bad                if souls_returned && ending_bad
           := returned_moderate           if souls_returned && !ending_bad && ending_moderate
           := returned_other              otherwise

living_contact := ordinary existing relationship, area, chapter,
                  native contact, death/departure and path restrictions

developed_offer := living_contact && activity_earned && abyss_addressed
```

`quest_case` uses the existing native-backed flags `seelah.souls_returned`, `seelah.ending_bad`, and `seelah.ending_moderate`.
Within returned cases, use the existing `seelah.elan_dead` alias for any statement about Elan.
Bad takes precedence over moderate, as in the existing source.
Unfinished work is a valid case, not a requirement to finish Seelah's native quest or manufacture its good ending.

The native case must be discussed at the actual future conversation before the developed choice.
`faith_spoken` and its earlier outcome flag prove an earlier conversation, not that the current quest state is unchanged.
A player can complete the rescue between the faith scene and `road`.
Avoid a permanent generic `quest_ready` flag that becomes stale after that transition.
Read the native case again for any ending and any later migration conversation.

The new Act 5 bridge deliberately keeps `letter_unsettled` as historical evidence.
Never block solely on that flag without checking the two valid later completions.
`letter_discussed` alone does not satisfy the recommended strongest promise when the practical aftermath was abandoned.
That history receives the bridge's remembered-agreement version.
No original letter incident means no invented obligation to play the Abyss scenes or the return bridge.

## Implementation at the actual scenes

### 1. Give `road` a visible decision before its existing start

Insert a new entry page before the original `road/start`, retaining every existing node ID and choice index.
Do not hide the entire future conversation behind the race requirement: the player needs to learn why it is early and what Seelah wants next.
Use existing Requires/Forbids branches and a few gate pages rather than introducing a general expression language.
The current choice schema has conjunctive Requires/Forbids; scene RequiresAny alone cannot express all the groups above.

When the Abyss is unresolved, prioritize the concrete line: "We still owe each other that conversation about the copyist. I want to finish it before we make another promise."
Provide an initial deferral that names the existing `letter_return` opportunity.
When the activity is missing, use an invitation tied to the next uncompleted scene rather than a list of flags.
Examples are the washing-yard invitation before `saw_arranged`, her promised roof evening before `aftermath_ready`, and her course/race invitation afterward.
The journal guidance can name the current next visit and its required wait.

Do not have a readiness page award the missing activity, copyist resolution, or quest result.
Do not make a neutral terminal choice such as "Another time" complete `seelah.road`.
`Main.RecordProgress` automatically records the scene ID on non-aborted completion, and `Rules.Available` excludes that scene thereafter.
The early readiness deferral must Abort before any new progress write.

### 2. Refresh the quest context, then retain the original personal choice

After the readiness gates, add a concise current-state passage selected by `quest_case` and actual Elan state where relevant.
For unfinished work, Seelah should name that her responsibilities remain open rather than postponing the relationship until an automatic rescue.
For returned bad/moderate outcomes, preserve her possible independent travel and unresolved grief/questions.
For other returned outcomes, avoid declaring every friendship repaired merely because the rescue succeeded.
These passages are a focused current reckoning, not a replay of the whole faith scene.
They require new authored prose and independent review.

Then enter the existing `road/start`, home/travel/Trickster choice, and commitment decision.
The Trickster line remains a promise to investigate a price, not implemented universal fate access.
Retain the existing refusal to continue the relationship.
Append any new answers rather than shifting old choice indices, since those indices contribute to generated blueprint identity.

Record a new `seelah.developed_commitment` marker only when the developed path actually finishes after the contextual passage and accepted commitment.
Keep the existing `seelah.committed` and `seelah.chosen_future` flags for compatibility.
Do not redefine every old committed save as developed merely because that older flag exists.
Do not award the new marker on entry, on a readiness explanation, or on an interrupted acceptance page.
The final acceptance guard must still reject lost contact and an unresolved episode, including save/resume or external state changes between pages.
Root should use the existing live choice/contact guards and add a focused final guard if their present contract cannot express that check.

### 3. Preserve an explicit shorter outcome

The initial page may offer: "We have not had those evenings. I still want to see what we can make of this, without pretending we have."
That answer needs a brief authored response and a separate terminal marker such as `seelah.short_future_chosen`.
It must describe a modest ongoing relationship rather than feed the existing strongest shared-life promise unchanged.
If it retains `seelah.committed` for compatibility, endings must prefer the short-history branch unless a later developed conversation is actually completed.
It must never set `developed_commitment`, the race flags, or native rescue flags.
This shorter path is an informed option, not the unmarked default that currently skips the expansion.

## Farewell and remaining content

Keep the existing `ordinary` scene available to compatible committed histories.
Before `farewell/start`, offer a real choice to spend more time together when an authored arc remains incomplete.
The choice should name the remaining invitation rather than merely say "Are you sure?"
An example after the race is: "You asked me for an evening afterward. I would like to keep that before we leave."
The current `late_afterglow` requires `late_race_kept`; its quiet choice must remain enough to continue to `late_first_step`.

Use clear player-facing text when the player deliberately proceeds: "[Keep this farewell and leave the remaining Drezen meetings unfinished.]"
That is a consequential story choice, not an approval prompt.
An initial defer must not record `seelah.farewell`, because the current expansion helpers forbid that completed scene ID.
Do not put the only warning at the final answer after progress has already committed the player to the farewell.

For an existing completed farewell while still in Chapter 5 Drezen, offer one new, explicitly authored catch-up entry.
It should acknowledge that they already said goodbye and still have time here; it must not replay the old first farewell as though it never happened.
On explicit selection, record a narrowly scoped `seelah.catchup_requested` marker and expose only otherwise-valid remaining Chapter 5 expansion scenes.
Root must replace the blanket farewell exclusion for those scenes with the explicit condition `!farewell || catchup_requested`.
Keep genuine chapter, area, death, departure, relationship closure and mythic restrictions in force.
Do not make that exception reopen past acts or the final campaign after transition.

If a generic local-contact guard is added to support this OR, share that predicate between initial availability and resumed-scene checks.
Do not sprinkle inconsistent farewell exceptions across each of the ten scenes.
A small Seelah-specific policy helper is preferable to an elaborate new condition DSL if the current authoring format cannot express the exception cleanly.

## Migration and late starts

| Save history | Required behavior |
|---|---|
| New early or late courtship, no commitment | Visible road readiness, valid unfinished native-quest branch, normal activity discovery and timers, explicit short option. |
| Existing `committed`, no farewell | Preserve the commitment and old `road` completion; offer a new follow-up scene to incorporate the earned activity and current quest circumstances. |
| Existing committed save with activity already earned | The follow-up acknowledges the existing promise and can award developed evidence after the fresh context and accepted continuation. |
| Existing committed save missing development | Offer catch-up or an explicitly limited legacy continuation; never invent prior meetings. |
| Existing farewell, still Chapter 5 Drezen | One voluntary catch-up entry, retaining farewell history and permitting only remaining valid content. |
| Past the last valid contact/area/chapter | Preserve history; no forced time travel, reset, or unreachable mandatory gate. |
| Completed `copyist_followed` | Exclude return bridge and treat the episode as addressed. |
| Discussed but did not follow the copyist | Return bridge remembers the actual agreement. |
| No Abyss incident, including late Act 5 start | No copyist requirement or fabricated recollection. |

Do not try to replay `road` by clearing its auto-recorded scene flag.
Use one new migration/follow-up scene for already completed road histories.
The follow-up must distinguish an existing commitment from a new offer and use its own stable completion ID.
Legacy classification should depend on actual historical flags and the played new conversation, not an assumption that absence of the new marker means the player knowingly chose a short route.

## Ending selection

Keep the native and mythic ending precedence, including death/departure, transformed outcomes, ascent, and Aeon history.
Within a compatible ongoing relationship, distinguish developed, deliberately short, and legacy-unclassified histories.
Only the developed ending should claim the more substantial shared life established by the new contract.
A legacy ending can honor the old promise without claiming that the race, roof evening, copyist follow-up, or particular native friendship happened.
Refresh native quest outcome at ending time rather than trusting the earlier conversation.
Use home/travel preferences and one or two genuinely played details; do not concatenate every flag into an epilogue.

## Focused verification

1. Reproduce the current short `weight -> road -> ordinary -> farewell` path and show that a new save can no longer receive developed status from it.
2. Walk the normal developed chain through the race, including running success, running failure, wide route, and watching; all four must satisfy the same activity predicate.
3. Cover no Abyss incident, public/burned unresolved, discussed-only person/signal, full copyist follow-up, and Act 5 return completion; only the actual two completions resolve an existing incident for the strongest promise.
4. Change native quest state between faith, road entry, and final acceptance; verify current context, bad-before-moderate precedence, Elan presence/death wording, and no native state mutation.
5. Defer each readiness and farewell entry and save/load; no scene completion, commitment, catch-up completion, or lost future opportunity may be recorded prematurely.
6. Load old committed and old farewell states with and without existing expansion progress; commitments and other romances must remain intact, and migration scenes must neither duplicate earlier meetings nor strand valid unfinished content.
7. Start in Act 5 with no Abyss flags and unfinished rescue; the route remains attainable through actual timers and valid contact, including the explicit shorter choice.
8. Verify death, departure, closure, inhuman and real chapter/area restrictions on ordinary, catch-up and resumed paths; a catch-up marker must not bypass any of them.
9. Check ending exclusivity for developed, deliberate-short and legacy histories under each native outcome, and retain authored decline/separation behavior.
10. Confirm stable original node/choice IDs, exact source/export equality, and genuine native entry/save behavior with ToyBox free love and no jealousy.

The graph tests establish the progression contract, not portrait presentation, native actor presence, actual skill UI, or full-route quality.
The remaining native-friend social development, supported Trickster departure restoration, art, and game-level verification still block complete approval.
