# Alternative prerequisite groups

The Konomi missed-contact candidate needs a truthful alternative to two native prerequisites without altering the historical dismissal route.
`Scene.RequiresAnyGroups` is an optional array of nonempty flag arrays.
Every group must contain at least one satisfied flag; the existing `Requires` conjunction and `RequiresAny` disjunction remain independent.
For example, `[[dismissed, earned], [office_done, earned]]` means `(dismissed AND office_done) OR earned`.
The parser rejects null groups, empty groups, blank flags and repeated flags within a group.

Both entry and physical or remote continuation check these groups.
Entry delays include recorded times for satisfied group alternatives, so a newly earned meeting cannot skip a waiting period by replacing an old required scene.
Timestamps for absent alternative flags do not affect that delay.
Continuation still does not reapply entry delays or authored closure.
The selected Konomi content counter and the existing generic condition scan now recognize groups.

The Konomi author independently read the shared implementation and focused tests against the proposed overlay and reported no mandatory defect in that bounded review.
The candidate story and native observer remain separate unfinished work; this engine change does not claim that Konomi's new acquisition is playable yet.

Verification completed with 79 focused truth-table, timing, invalid-input and serialization assertions.
The existing 527-scene expansion passed 24,107,282 Rules assertions and 64,462 managed construction assertions.
Source and managed builds completed with zero warnings or errors.
Managed construction still registered 18,853 blueprints and preserved fourteen native answer lists.
Story SHA256 remains `0CB9BDDB2BA353FED08E2C43A58A63BE798C0A73356D46367CFBC73BD1FE7387`.
Tested assembly SHA256 is `111CBAA0A189D30A0884CD22655977FF35A25601455D676CB0A00C3F29970820`.
These are headless checks, not Unity, native parent initialization, saved game or ToyBox execution.
