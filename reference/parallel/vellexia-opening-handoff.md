# Vellexia initial manor opening handoff

Released for independent review on 2026-09-26.
Only the four assigned source, focused-test, evidence and handoff files were changed.
No shared engine, exporter, main Story, installed mod or native file was edited.
No author quality score or full-route approval is claimed.

Source SHA256: `A48E7BC9EF3DA412D88EE2FCD6C1E408E8C7CC82E96DD340C8F38A91D3E62F2D`.
Focused-test SHA256: `AF3016B82044EAAB5F5F023B3AF5D6E0F81FF273BE049C91A440D7EC28669E74`.

## Integration

Import `storylines.vellexia_opening`.
Append `SCENES`, register `RELATIONSHIP` under `vellexia`, and merge `ETUDES`, `SEEN_CUES`, and `COMPLETED_QUESTS`.
Seen-cue values are arrays, as required by the existing schema.
Register `VellexiaOpeningTests.Run` when `vellexia.unfinished_likeness` is present.
The generic fabricated-prerequisite scene fixture may need to omit the later conditional-history scenes; the dedicated suite supplies their actual earned predecessors.
Do not seed all mutually exclusive flags to force those graphs through.

The six parts are unfinished_likeness, second_painter, price_of_novelty, two_observers, unadvertised_hour and a_question_kept.
Each requires the exact original manor actor, native witnessed greeting, Chapter 4 Upper City and its own prior earned milestone.
Every scene has zero delay so the user can play the extended interlude in one visit before the native Battlebliss invitation.
The guidance explicitly explains this timing.
Accepting the native invitation prevents later entry into this early interlude without clearing progress or marking the relationship closed.
A future continuation must handle those retained histories at real later contact.
This early window is not a substitute for the full path/recovery requirement.

## Played content

The opening concerns an enchanted portrait that suppresses surprises its artist expects Vellexia to dislike.
A real Commander-only Arcana DC28 check has success, failure and non-roll inquiry paths.
The artist's repair or demonstration leads to a choice of retaining the work at an honestly described price or sending it back.
The next encounter follows that disposition.
A reciprocal portrait exercise leads to a private conversation and voluntary courting, slow exploration or company.
The final chosen intimacy is graphic and explicit and records only authored opening history.
Jerribeth's existing advice is conditionally recalled without duplicating it or making her a broker of affection.
Vellexia retains her ancient, proud, dangerous and capricious characterization; this episode does not cure her boredom or free/erase her victims.

The standard inventory tokenizer measures 6,508 raw words and 6,508 distinct-segment words across six scenes and 50 pages.
An exhaustive successful-completion source walk found 384 paths across advice/no-advice and all choices/check outcomes, with 3,651 to 3,838 selected words including the chosen answers.
The two skill-check outcomes are never added together for one playthrough.
This is a substantial opening, still well below the 21,000-word full-route planning floor and not proof of RanRomance quality parity.

## Verification performed

Temporary isolated runner: `C:/Users/Z/AppData/Local/Temp/vellexia-opening-check-slxce2c6/Check.csproj`.
Temporary generated candidate: the adjacent `Story.json`.
Executed `dotnet run --project <temporary project> -c Release -- <temporary Story.json>` using the installed RanRomanceTools dotnet executable.
The runner invokes `Rules.Validate` and the focused suite against actual project sources, without editing shared registration or overwriting shared build outputs.
Result: 176,097 focused assertions passed.
The native blueprint GUID/type and transition details are in `reference/canon-review/vellexia-route-evidence.md`.

The source has terminal-only outcome effects, and every intermediate snapshot retains the entry flags/timestamps.
The suite tests all pages, known/unknown Jerribeth advice, ordinary/Trickster access, branch exclusivity, contact loss, native invitation/quest transition, chapter/area/prerequisite blockers, harmless deferral and native/other-romance preservation.
No new committed flag, native intimacy fact, gold movement, invented actor or resurrection is produced.

## Remaining work

Obtain independent writing, characterization and integration review of these exact hashes.
Run the combined schema/rules, typed native-binding and managed construction checks before promoting the source.
Verify actual loaded Default actor and injected initial conversation in a real save, including the native invitation transition.
Develop later real-contact continuation for players who accepted the native invitation, passed the third-date encounter, spared or lost Vellexia, or first approach her later.
The final native encounters teleport the ThirdDate actor away, so neither a historical greeting nor a completed quest proves that actor is present afterward.
Develop the promised Trickster recovery/access route with correct living identity and native consequences.
Complete full-route depth, later relationships, endings, art and ToyBox/runtime verification before calling her ready.

## Independent-review prop repair

The failure branch now first describes light spilling from beneath the face-down painting, then explicitly lifts the open frame upright before describing the painted surface.
The successful successor explicitly turns the closed frame before describing its new image.
Structural comparison against the prior candidate proved that only these two Text values changed.
IDs, choices, conditions and effects remain identical.
The isolated schema and focused suite were rerun on the revised candidate and passed 176,097 assertions again.
