using System;
using System.Text.Json;
using Tirabade;

internal static class RecoveryTests
{
    public static void Run(Action<bool, string> check)
    {
        // Runs the production coordinator with a faulting native-call substitute.
        // It does not create Unity entities or execute the game's resurrection method.
        var attempt = new RecoveryAttempt { UnitId = "original-seelah", Roster = 2,
            SceneId = "seelah.fate_life", ChoiceJson = "recorded-choice" };
        var state = new RecoveryStatus { UnitId = attempt.UnitId, Roster = attempt.Roster, Eligible = true, Dead = true };
        int calls = 0;
        bool success = attempt.TryApply(() => state, () =>
        {
            calls++;
            state.Dead = false;
            state.Conscious = true;
            throw new InvalidOperationException("Native event failed after restoring life");
        }, out _);
        check(!success && calls == 1, "Faulting resurrection credited progress or was not attempted.");
        check(!state.Dead, "Partial-state reproduction did not change the dead-only readiness predicate.");
        var json = JsonSerializer.Serialize(attempt, new JsonSerializerOptions { IncludeFields = true });
        var resumed = JsonSerializer.Deserialize<RecoveryAttempt>(json, new JsonSerializerOptions { IncludeFields = true })!;
        check(resumed.SceneId == attempt.SceneId && resumed.ChoiceJson == attempt.ChoiceJson, "Checkpoint lost its authorized action.");
        check(resumed.TryApply(() => state, () => calls++, out _) && calls == 1,
            "Living partial recovery cannot finish without repeating native resurrection.");
        state.Conscious = false;
        check(!resumed.TryApply(() => state, () => calls++, out _) && calls == 1,
            "Unconscious partial recovery was credited or resurrected again.");
        state.Conscious = true;
        state.UnitId = "replacement-seelah";
        check(!resumed.TryApply(() => state, () => calls++, out _) && calls == 1, "Replacement entity received saved recovery credit.");
        state.UnitId = attempt.UnitId;
        state.Roster++;
        check(!resumed.IsRestored(state), "Changed party status received recovery credit.");
        state.Roster = attempt.Roster;
        state.Eligible = false;
        check(!resumed.TryApply(() => state, () => calls++, out _) && calls == 1, "Ineligible companion received recovery credit.");
        state.Eligible = true;
        state.Dead = true;
        check(!resumed.TryApply(() => state, () => { calls++; throw new Exception("Before mutation"); }, out _),
            "Failed native call on dead companion received recovery credit.");
        check(resumed.TryApply(() => state, () => { calls++; state.Dead = false; }, out _) && calls == 3,
            "Still-dead companion cannot retry the original recovery.");
        resumed.Version++;
        check(!resumed.IsRestored(state), "Unknown checkpoint schema received recovery credit.");
    }
}
