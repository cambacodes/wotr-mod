# Konomi ordinary physical contact handoff

Status: implementation submitted for independent review; shared integration remains with the parent.

## Scope and exact release

- `storylines/konomi_contact.py`: SHA256 `5BC57BDF458285E719AA04587845B0FEB8EFED5A62037403FB9A0CB9F2870AE0`.
- `tests/KonomiContactTests.cs`: SHA256 `F7BC6A2948965272A190EB1C490B2727EE1AD32BEB6BCEB8701F77220CA061E4`.

Call `konomi_contact.integrate(payload)` after all Konomi scene modules have been assembled.
Register `KonomiContactTests.Run(story, Check)` in the shared test runner after that overlay is present.
The overlay adds only `ContactUnit = ca2d58c5c65723945857e04fb85d30ce` to the following 22 exact scene IDs, each prefixed `konomi.`:

```text
margin reception letter evening disagreement leak reckoning
return power ordinary farewell parting hearing hearing_after
new_letter political_account a_useful_supper the_upper_passage
two_bad_prices the_trial_day a_name_beside_hers the_evening_she_kept
```

The existing guarded `konomi.a_turn_for_herself` is unchanged, yielding 23 physical scenes in the resulting fixture.
All 39 other Konomi scenes are explicitly excluded by the test inventory, including `another_evening`, whose positive presence requirement accompanies solitary invitation reading rather than a meeting.
The complete excluded ID list is in the focused tests and the independent native audit.
Private dismissed meetings, letters, Chapter 4 absence and epilogues retain their existing delivery contracts.

The overlay rejects a missing or duplicated target, another relationship/owner, remote or manual delivery, absent native presence prerequisite, changed area or answer list, unsupported chapter, or conflicting actor GUID.
It validates every target before changing any, so a late invalid target does not partially modify earlier scenes.
Repeated integration is idempotent.
No text, nodes, authored choices, IDs, native flags, timing, spawning or hiding behavior is changed.

## Evidence and behavior

Native evidence is independently recorded in `reference/canon-review/konomi-contact-independent-review.md` and `konomi-contact-records.json`.
The actual default-capital spawner references the Lady Konomi unit above and ordinary dialogue `a81655ed97277974e947c1aaf9e33525`.
The ordinary answer list is `0dc8b8604bb33c846a63f3eb62443674`, and the audited area is `2570015799edf594daf2f076f2f975d8`.
Native presence etude `b5f301fbc4c44535a6309d610d5bd28a` controls unhiding/translocation; its historical existence alone is insufficient to prove a currently usable actor.

The existing NativeContact observer supplies the live actor observation, while Rules checks the actor observation together with current office presence, area, chapter, native exclusions and other required state.
Consequently loss of the loaded actor or office presence blocks new entry and further authored selections.
The existing engine contact-lost exit permits leaving without recording a new choice or completing the scene.
Already recorded choices are retained, and restoring valid contact permits ordinary unfinished-scene access again.
Authored midscene closure flags and entry delays are deliberately not reapplied as continuation conditions.
This change inherits those engine behaviors; the new module does not implement a second observer or transaction mechanism.

## Verification performed

An isolated temporary project compiled the actual `src/Story.cs`, the normal test sources and the owned focused test.
Its candidate was built in memory from `expansion.make_expansion()` and the overlay, without overwriting shared development payloads or installed files.
`Rules.Validate` and **1,120 focused assertions passed**.
The temporary project is `C:/Users/Z/AppData/Local/Temp/konomi-contact-check-osbm995h/Check.csproj`.

The test temporarily removes contact metadata under `try/finally` to reproduce the old behavior on each actual scene: entry can succeed without an available actor, and continuation can remain available after office presence is lost.
Restored metadata rejects both conditions, accepts valid physical contact, and accepts contact again after temporary displacement ends.
Further cases cover actor disappearance, native exclusion and restoration, authored nonterminal effects, completed-scene non-replay, area/chapter changes, and continuation after a start delay would otherwise be reapplied.
All excluded scenes retain no ordinary contact requirement, and the solitary invitation remains readable without a loaded officer.
Tests confirm observation does not mutate flags or timing.

An independent Python payload comparison confirmed exactly the intended 22 ContactUnit additions and byte-equivalent values for all remaining structured content.
A second integration produced no further changes.
Eleven negative mutations covering missing, duplicate, remote, manual, relationship, owner, presence, area, answer list, chapter and conflicting contact were all rejected with the entire input unchanged.
These Python checks were temporary verification, not an additional installed tool or framework.

## Shared fixture integration notes

Existing positive ordinary-meeting fixtures need to describe an actually available Konomi actor.
Seed that actor only in the physical scenario under test; do not globally claim that every actor exists.
Relevant reviewed fixture sites include `KonomiTests` initial campaign/repair/Drezen states, `KonomiPoliticalTests` ordinary Chapter 5 state, `KonomiOrdinaryExpansionTests` ordinary and transformed contact states, and the ordinary branch of `Program.CheckKonomiHearing`.
`KonomiEarlyReciprocityTests` already seeds its physical actor.
The shared generic presence fixture has already received a conditional contact adjustment by the parent.
These shared files were not edited by this worker.

## Limits

The focused reproduction runs actual Rules with explicitly seeded observations; it does not exercise a Unity scene or claim that a seeded snapshot proves the observer itself.
Current-area storage, hidden/inactive views, duplicate actors, dead/unconscious/hostile actors, combat and stale loaded state remain the existing observer's responsibilities and separate managed/runtime verification concerns.
The observer authenticates a unique eligible blueprint match, not a particular saved spawner identity, and does not impose proximity.
Live Chapter 3/5 dialogue, queued opening, rank-up return, save/load, skill-check interruption and the visible leave-only state still require the corresponding engine/runtime checks.
This bounded metadata upgrade neither certifies private-route physical delivery nor full character writing, art, campaign completeness or universal Trickster access.
