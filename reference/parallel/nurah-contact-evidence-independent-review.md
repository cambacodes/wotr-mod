# Nurah contact evidence independent review

Reviewed 2026-09-27.
Verdict: pass for the bounded schema and live-contact policy change.
No blocking finding in this scope.
This does not approve Nurah's movement, authored dialogue entry, manuscript, or Main integration.

## Reviewed inputs

| Input | SHA256 |
| --- | --- |
| `src/Story.cs` | `D1CBEEAEF3C79E58BE943ED8875434B5F7120FBB589A10CFE2F352B02714F843` |
| `tests/NurahContactEvidenceTests.cs` | `046633376BA07019AABE5C2A3F8F8B78602C6AE88F81BD1A0A276A8426BB0A2D` |
| `tests/Program.cs` | `FA72ABF25715A809F00455868A3087955814FBA28ED5FCBEA563E664F182F791` |

The production diff adds `nurah.correspondence_available` and `nurah.meeting_arrived` to the existing derived-flag registry, reserved contact-evidence registry, and live native-state predicate.
It does not produce either observation, mutate native state, or alter the existing contact algorithm.

## Source findings

The reservation checks cover scene IDs, all authored choice effects, all three relationship progress slots, and the six native-binding collections.
Native aliases cannot supply either reserved observation even when no authored write remains.
The derived registry permits legitimate reads without requiring an authored producer.
`IsNativeFlag` makes a forbidden Nurah observation participate in live `ContactAvailable` reevaluation.
Explicit required evidence is also reread from the current snapshot.

The actor contact guard remains separate.
Adding `nurah.meeting_arrived` to a snapshot does not satisfy a scene's `ContactUnit` requirement by itself.
This is an engine policy check, not proof that a runtime observer has supplied truthful arrival evidence.
The existing early return for scenes without physical contact requirements remains unchanged and is not broadened into a universal proof requirement by this patch.
Nurah's eventual physical scenes must declare their contact and arrival gates explicitly.

The runner registers the dedicated suite after validating its input story and before its mode branches.
The suite does not mutate that shared input story or print output, so the bindings mode retains its JSON output format.
Its cases use independent small fixtures rather than the unapproved manuscript.

## Independent verification

I compiled a frozen copy of Story.cs and the dedicated suite under `C:/Users/Z/AppData/Local/Temp/nurah-contact-evidence-independent/`.
The isolated runner passed 40 assertions: 30 submitted checks and 10 independent checks.
The additions cover the ClosedFlag and CommittedFlag forgery slots for both observations, plus grouped requirement absence, presence, and removal.

A temporary mutant removing only the two additions from `IsNativeFlag` failed with `Nurah observation is not checked as live state`.
This reproduces the missing live-forbid behavior through the public policy entry point.
The frozen source copy was restored afterward.
No shared source or build output was changed.

Root separately reports the complete Rules runner passing 27,527,097 assertions against the unchanged 612-scene export.
I did not repeat that full suite for this small change.
The focused independent execution and mutation establish the changed policy directly.

## Remaining scope

Main still needs a truthful read-only producer for both observations and the physical route needs reviewed entry wiring.
Native actor placement, click interaction, save/load, Unity visibility, and ToyBox behavior are separate checks.
Neither these schema fixtures nor their deliberately seeded snapshots count as native arrival or playable-route evidence.
