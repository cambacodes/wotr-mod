# Irabeth departure visit Rules handoff

Date: 2026-09-26.
Status: implementation frozen for independent review, not self-approved.
Owned production file: src/Story.cs.
Owned test file: tests/IrabethDepartureVisitTests.cs.
No Main, meeting helper, story module, Program, shared export, or installed asset was edited.

## Reproduction and scope

Before editing, an isolated project compiled the actual original Rules source.
A living departed Chapter 5 Trickster in Drezen with positive correspondence evidence remained unavailable in both Rules.Available and Rules.ContactAvailable because the relationship still contained irabeth_gone.
This reproduces the pure policy failure, not the full Unity delivery path.
Native actor observation, arrival, and meeting lifecycle belong to the separate Main and IrabethMeeting implementation.

Scene.AfterDeparture is a nullable string with exactly one accepted value, irabeth.
Validation restricts it to irabeth.return_request, irabeth.return_reply, and irabeth.return_first_words.
All three must belong to the existing Irabeth relationship and owner, use Chapter 5 only and exact Drezen area 2570015799edf594daf2f076f2f975d8, and require Trickster plus the existing departure flag.
Only relationship unavailability caused by irabeth_gone is bypassed.
Death, other path restrictions, scene prerequisites, native contact, closure, and refusal remain effective.
Unmarked ordinary scenes retain the original block.
No relationship is cloned to escape its unavailable state.

All three forbid closed, irabeth.closed, irabeth.return_meeting_declined, irabeth_dead, inhuman, swarm, and true_lich.
They cannot carry ForbidOverrides, recovery metadata, or extra actors.
For these scenes, ContactAvailable also rechecks every authored forbid and relationship closure, so refusal or closure during an open conversation does not leave its choices enabled.
Existing scenes keep the original ContactAvailable behavior.

The remote request and reply require irabeth.return_correspondence_available and cannot require a physical ContactUnit or answer-list attachment.
The reply also requires the completed request and irabeth.return_request_sent, forbids prior acceptance, and waits at least 48 hours.
The physical scene requires the completed reply, irabeth.return_meeting_accepted, and irabeth.return_meeting_arrived.
It requires the original actor 280d4712dceb37f4a88e98f1f4c6e64f and native answer list 871af36f2ab2b1f40b5de77976c54276.
It waits at least 12 hours after acceptance.

Rules.Available requires the specific sent or accepted timestamp for those two waits.
Missing, negative, and future timestamps do not satisfy them.
The timestamp difference uses a long subtraction to avoid overflow in that specific guard.
The existing general delay logic remains in place afterward, including any additional authored prerequisites.
ContactAvailable retains the existing policy of not reapplying delays while a dialogue is open.
The physical arrival flag must independently come from the meeting helper after its own acceptance delay.

The two new positive evidence flags are read-only derived observations.
Scene completion, choice writes, relationship-state aliases, and every supported native binding dictionary cannot manufacture them.
Choices in these three typed scenes may write only non-native flags within irabeth.return_.
This permits narrative case details and accepted or declined replies while forbidding native history writes, romance commitment, and changes to another woman's route.
The existing global validator still rejects a write to either derived proof even though it shares that prefix.

## Verification

Temporary project: C:/Users/Z/AppData/Local/Temp/irabeth-departure-rules-da9a78d7/Review.csproj.
It compiles actual src/Story.cs and tests/IrabethDepartureVisitTests.cs into isolated outputs.
Run with C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe run --project C:/Users/Z/AppData/Local/Temp/irabeth-departure-rules-da9a78d7/Review.csproj.

Final result: 181 focused assertions passed and the full isolated 588-scene candidate passed Rules.Validate.
The candidate was built from current expansion source with the author's three Irabeth return scenes appended locally.
This construction does not approve unrelated unreviewed prose that may also be present in the working tree.
No shared Story.json was generated.

The tests use the caller's actual three scenes, then isolate those scenes and their relationship for small mutation cases.
They cover JSON roundtrip, positive remote and physical eligibility, unmarked departure blocks, every missing required flag, death, both closure flags, refusal, incompatible paths, wrong chapter and area, exact waits, missing or invalid timestamps, no actor, wrong actor, correspondence substituted for arrival, and preservation of both Seelah and Arueshalae commitments.
Malformed metadata cases cover wrong owner or relationship, unknown future scenes, removed requirements and forbids, mixed recovery metadata, extra actors, overrides, missing or incorrect native entry, remote or physical confusion, shortened waits, history writes, and every supported alias route for forged evidence.

Root must register IrabethDepartureVisitTests.Run(story, check) in its test Program after adopting the three scenes.
No shared test registration was changed here.
Production callers must validate story metadata before calling Rules, as with the existing Recovery and AfterRecovery contracts.
The exception relies on that existing validation boundary rather than rebuilding the entire metadata validator on each availability call.

This result does not demonstrate a retained actor is alive, visible, movable, correctly owned by the meeting helper, or reachable through native dialogue.
Those are separate observation, meeting, and Unity integration requirements.
The Rules layer only consumes the positive observations and preserves the remaining policy checks.

## Frozen hashes

| File | SHA256 |
| --- | --- |
| src/Story.cs | F70AFD9652D2660E7F33AB9A451F501980958616C5351E9BEBEB3103220AC56C |
| tests/IrabethDepartureVisitTests.cs | 2073F16DF3078684FCE0B6141E38A2D0256BB2DA303F64FCED78F6BFD9DA97D2 |
| Isolated candidate.json | 1F6854ED6C61F6F538C9C415A47AFED151660E03E112BA5842E890A24E5081A3 |
