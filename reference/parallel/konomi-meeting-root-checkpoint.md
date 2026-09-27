# Konomi meeting integration checkpoint

The root integrated the native placement fixture and both Konomi meeting suites into managed-tests/Program.cs.
The production assembly and managed runner compiled without warnings or errors.
The actual shared runner passed 67,302 assertions across 538 scenes and 19,445 generated blueprints.
The story export was unchanged.

Story SHA256: `8DCEB83D44925E5C07C7407D1FCEABE9381CE147D9A862B22E4E88420583C300`.
DLL SHA256: `02318EFC56169F22B66B342F19FB6B2E52CB92AEE981845DD03635EF5A562C38`.

Independent review of production wiring remains a separate gate in reference/parallel/konomi-meeting-integration-independent-review.md.
The built assembly also contains the new typed parent ending policy, whose metadata is not yet exported or wired into native endings.
A successful 538-scene construction run does not validate that unintegrated ending behavior.

The runner uses native blueprint fixtures and preservation sentinels for the parent sequence.
It does not initialize RanRomance or execute ToyBox.
Native resurrection and meeting tick scheduling reach Unity-only ECall boundaries in this standalone process.
Actual unhide, movement, arrival, withdrawal, retry UI and game save/load remain unverified.
No installed game files were changed.

