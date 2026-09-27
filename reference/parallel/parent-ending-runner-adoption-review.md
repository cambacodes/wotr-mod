# Parent ending runner adoption review

Reviewed on 2026-09-26.
Verdict: pass for the small managed runner adoption diff.
I reviewed the new calls in `managed-tests/Program.cs`, their fixture lifecycle, and the existing preservation assertions.
I did not edit production code, fixtures or the runner.
The fixture implementation's earlier independent review remains separate evidence.

## Frozen inputs

| Input | SHA256 |
| --- | --- |
| `managed-tests/Program.cs` | 99C36EDAA6140FB28CB97751B3BF4413F335640AE81A988A6CA7A5903C484E23 |
| `managed-tests/ParentEndingIntegrationTests.cs` | FD7EA52F11EB4792D29A57E63CCA816555DC098E6DA1444587601DE64060486E |
| Managed test executable | 3F11F88A1158D0D968181EE621217D909B9A61189989DFA8AB9A9EA23057FBB6 |
| Production development DLL | AEB714C5AF2C88FD156588CC072DFE8A40C60AD2B75B4B43D8A5ACC4E7027176 |
| Current 585-scene export | 780BDC23146431CECD7F1ED9594B5F129C5E149DB535CC40F2BD128A2126647A |

## Conditional execution and ordering

The new block runs when either ordinary parent edits or loss rules are present.
Absent metadata retains the initialized empty collections in Story, and validation precedes this access.
Explicit null collections are rejected by validation.
Both fixture preparation and its post-build integration checks are skipped for the old no-metadata export.
I independently ran that actual 538-scene export through the current executable and production DLL: 67,302 assertions passed, with 19,445 generated blueprints.
Its hash was `8DCEB83D44925E5C07C7407D1FCEABE9381CE147D9A862B22E4E88420583C300`.

Fixture preparation follows native reference seeding and localization initialization, and precedes the real private `Main.Build` invocation.
Fixture Seed returns the existing cached sequence objects, so the runner's sequence dictionary still points to the objects populated by preparation.
The snapshot refresh occurs after preflight restores its deliberate mutations and before production construction.
The later assertions therefore require preservation of both sentinel references and the prepared parent pages, followed by precisely the authored addon pages.
They compare reference order and reference identity, not merely counts.
The integration checks separately preserve the original page cue references around private alternatives.
Their controlled observer, page action and game singleton mutations are restored in finally blocks.
The existing second Build invocation continues to check idempotence after the integration checks.

## Portable path and execution evidence

The contract path resolves from the executable directory to `managed-tests/fixtures/parent-ending-source/verified-contract.json` under the standard `bin/Release/net48` layout.
It does not depend on the process working directory or a machine-specific temporary extraction directory.
This matches Bootstrap's existing repository layout assumption and ReadNative's existing script path convention.
An arbitrarily relocated executable without that surrounding tree remains unsupported, as it already was before this change.

I independently invoked `managed-tests/bin/Release/net48/ManagedBuildTests.exe` with the installed game directory and `development/Story.json`, using the actual Python executable through RRT_PYTHON and the reviewed parent manifest through RRT_PARENT_BINDINGS.
The full 585-scene run exited zero with 71,672 assertions and 20,701 generated blueprints.
The executable reported the exact DLL and story hashes above.
This reproduces the root agent's full shared run rather than relying only on its report.
The root separately reported that the preceding shared build had zero warnings and errors; I reused that executable and did not overwrite shared build outputs.

## Limits

The adopted integration test is pinned to the currently reviewed parent contract and expects 17 variants.
It is not a general fixture generator for an arbitrary future ending contract.
The parent sequence still combines preservation sentinels with reconstructed reviewed parent pages, rather than running RanRomance initialization.
Actual managed construction and native method patch inspection do not establish an in-game epilogue, populated native condition results, ToyBox behavior or a save round trip.
Both runs explicitly reported the native resurrection and Unity LoadingProcess boundaries.
No live arrival or resurrection success is claimed.
