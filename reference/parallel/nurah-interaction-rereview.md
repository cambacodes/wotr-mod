# Nurah click interaction rereview

Date: 2026-09-27.

Reviewed `src/NurahInteraction.cs`, SHA256 `2112CD8FA72C90940B04764AD0C747F4C520EB1BE2647C352C1BC471AC23722F`.

Reviewed `managed-tests/NurahInteractionTests.cs`, SHA256 `6043048E74D7FC034789D818845A25BA87DB460317CB3D6DF39B965231CAADE8`.

Verdict: **pass for the bounded click-interaction helper and its focused suite**.

The prior development-mode null-selector finding is resolved in this revision, and the regression is exercised directly.

## Arbitration and ownership

`HasOtherInteraction` first uses the native `SelectClickInteraction` selector.

When that selector returns `null`, the helper snapshots the private native interaction list with `ToArray()` and checks each non-approach interaction's current availability.

This distinguishes an empty/unavailable set from a development-mode equal-priority tie, which the native selector logs and rejects with `null`.

The helper never rewrites the native list while checking candidates.

It removes only its exact `Click` reference through native `RemoveInteraction` and leaves other interaction objects in their original order.

If the private list field cannot be found or read, the helper throws into its fail-closed path; `Tick` withdraws the addon interaction, and click-time `Available` returns false.

The actor, Commander, and part are compared by reference at each ownership transition and again during click selection and execution.

Lost arrival, changed route availability, a replaced part, a different Commander, disabled native interactions, or a callback exception cannot authorize a click.

The addon click remains `EtudeBracket` priority 200.

An available native `Spawner` interaction at priority 100 is preserved and causes the addon interaction to withdraw, so the addon does not use its nominally higher priority to hide native content.

That policy can defer Nurah's interaction while a native click remains available, but it avoids changing native interaction selection.

## Frozen suite and mutant checks

The production project built with zero warnings and zero errors.

The exact frozen interaction suite was compiled in an isolated `net48` harness and passed 38 assertions against production DLL SHA256 `1D0FA735B77C11C4261512A232216D89C9AD1975B91B4EEC4EDEBC077A1CFB10`.

The suite forces `BuildModeUtility.IsDevelopment` true inside the real `UnitPartInteractions.SelectClickInteraction` method and removes only the Unity-backed error-log call, preserving the native tie arbitration.

With two available native `EtudeBracket` interactions, it confirms that the native selector returns `null`, the helper adds no third interaction, and the original references and order remain unchanged.

The test then disables both native candidates, confirms the addon can attach, re-enables them, and verifies selection/click-time rejection and withdrawal without deleting either native reference.

A temporary mutant that replaced the null-selector candidate scan with the previous `return false` behavior built successfully but failed the suite at `Ambiguous native selection attached a third interaction or changed original entries`.

The mutant source SHA256 was `72433A267B0D347E44B8BAA3E6902C7B0F191D6BAC0D49E9B650ABC7AABA32F8`, and its DLL SHA256 was `49F72C8B07B60C6C13E2238EACAF3782615F44E600C12F29D36C6A6B5E2171C1`.

This demonstrates that the new test detects the regression from the prior review.

`managed-tests/Program.cs`, SHA256 `41026F77D17256354861ABD5810354E371F2F5347D48D15D05CD3478BD6FA193`, now invokes `NurahInteractionTests.Run(Check)`.

The canonical managed-test project could not be built in the current shared worktree because the separate in-progress `managed-tests/NurahHubTests.cs` does not match the available production API: it references inaccessible `NurahMeeting` and absent `Main.NurahVisitRequest`/`Main.NurahMeetingRetry` members.

I therefore ran the exact frozen suite in isolation rather than treating that unrelated compile failure as a pass.

## Scope boundary

This pass covers the helper's actor/Commander checks, click arbitration, exact-reference attachment/removal, null-selector fallback, and failure behavior under the supplied callback seam.

It does not approve Main or authored-hub assembly, lifecycle scheduling, a live `NurahMeeting` arrival, save/load, actual `StartDialogWithUnit` rendering, Unity presentation, or ToyBox behavior.

The injected start callback records its arguments in headless verification; it does not show a dialogue in game.
