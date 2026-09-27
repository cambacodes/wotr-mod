# Optional parent ending attachment

The previous goal turn fixed native ending replay in commit `e253884`, so it counts as progress.
This continuation adopts the independently reviewed Nurah observer in `41c2d06` and addresses the separate missing optional ending attachment.

## Source contract and reproduction

Installed RanRomance 0.1.11 creates `RanRomInt`, GUID `2b9424b1b93e4d0896b0958db79d2339`, when it detects the RanEpilogue Harmony owner.
The independently reviewed `EpSetup.Configure` source uses the same parent page assets in its default and conditional sequences.
The addon initializes after RanRomance's blueprint-cache postfix, so it can inspect whether this conditional sequence exists.
The actual optional plugin, version and complete caller graph are absent from this installation.

The managed fixture creates an optional sequence from existing parent fixture references, then invokes actual `Main.Build`.
Before the fix it failed with `Optional epilogue omits or reorders addon endings`.
The reproduction log is `C:/Users/Z/AppData/Local/Temp/optional-ending-repro.err`.
This reproduces missing attachment; it does not reproduce a complete playthrough with the external plugin.

## Implementation and checks

Main preflights the optional blueprint before creating addon objects.
Absence leaves default behavior intact.
A present object with the wrong type rejects initialization before addon registration or dialogue mutation.
When the optional sequence exists, ordinary ending pages are appended to both existing sequences using the same generated page references.
Aeon pages remain attached only to the Aeon sequence.
The reviewed global ShowOnce policy prevents the same page from displaying twice against the same player history.
Existing sequence contents, exits and conditions are preserved.

| Shared managed fixture | Result |
| --- | --- |
| Optional sequence absent | 79,952 assertions passed |
| Optional sequence present | 79,955 assertions passed |
| Optional GUID with wrong blueprint type | 774 assertions passed; rejected before mutation |

Both builds passed with zero warnings and errors.
All runs use story `A23F0AE6ABE6FAB6F0C275FBF8E1E8044EBEEA1FD040C12D61C4BD0F7D5829CC` and DLL `329E1A49C3AD47114DC46DDFDFF58C2CA46EE86D9EEE0030BBC9BEE649CAF162`.
Logs are `C:/Users/Z/AppData/Local/Temp/optional-ending-0-fixed.out`, `optional-ending-1-fixed.out`, and `optional-ending-wrong-type-fixed.out`, with adjacent error streams.
The packaging script now invokes all three fixture modes and restores the caller's environment value afterward.
That packaging script change has not yet been exercised as a complete packaging command at this checkpoint.

## Review and remaining verification

The independent report `reference/parallel/optional-ending-attachment-independent-review.md` grants a scoped pass to the attachment and tests.
Its isolated actual-Main probes pass with absent, present and wrong-type optional objects, including a deliberately different optional prefix, exact reference preservation and repeated-Build idempotence.
It also statically reviewed the packaging script's three-mode loop and environment restoration.
The fixture deliberately excludes the absent plugin's external caller graph and final parent initialization.
It cannot establish correct ending timing for an uninstalled plugin version or a real game save round trip.
These remain explicit compatibility checks, not reasons to claim the attachment alone completes the expansion.
No installed files changed and no fresh package has been produced from this candidate.
