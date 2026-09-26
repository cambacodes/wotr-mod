using System;
using System.Text.Json;
using Tirabade;

internal static class TerendelevDeliveryTests
{
    internal static void Run(Action<bool, string> check)
    {
        var jsonOptions = new JsonSerializerOptions { IncludeFields = true };
        var attempt = new TerendelevDeliveryAttempt { UnitId = Guid.NewGuid().ToString(), Provenance = "trickster.remains.return" };
        int saves = 0, spawns = 0;
        string saved = "";
        Action persist = () => { saves++; saved = JsonSerializer.Serialize(attempt, jsonOptions); };
        check(!attempt.Submit(false, true, true, persist, () => spawns++), "Unauthorized return spawned.");
        check(!attempt.Submit(true, false, true, persist, () => spawns++), "Unloaded destination spawned.");
        check(!attempt.Submit(true, true, false, persist, () => spawns++), "Occupied identity spawned.");
        check(saves == 0 && spawns == 0, "Rejected request mutated checkpoint.");
        try
        {
            attempt.Submit(true, true, true, persist, () =>
            {
                check(saved.Contains(attempt.UnitId) && saves == 1, "Spawn preceded saved identity.");
                spawns++;
                throw new InvalidOperationException("Native creation threw after registering the actor.");
            });
        }
        catch (InvalidOperationException) { }
        var resumed = JsonSerializer.Deserialize<TerendelevDeliveryAttempt>(saved, jsonOptions)!;
        check(resumed.Valid && resumed.Submitted && resumed.Provenance == attempt.Provenance && resumed.UnitId == attempt.UnitId,
            "Reload lost identity, authorization provenance or submission state.");
        check(!resumed.Submit(true, true, true, persist, () => spawns++) && spawns == 1,
            "Ambiguous failed creation was retried and could duplicate the actor.");
        check(!resumed.TryConfirm(true, true, false, true), "Registry registration alone counted as durable insertion.");
        check(!resumed.TryConfirm(true, false, true, true), "A different entity received arrival credit.");
        check(!resumed.TryConfirm(true, true, true, false), "Dead, hostile or viewless entity received credit.");
        check(!resumed.TryConfirm(false, true, true, true), "Changed history received credit.");
        check(resumed.TryConfirm(true, true, true, true), "The exact committed usable actor was not adopted after reload.");
        saved = JsonSerializer.Serialize(resumed, jsonOptions);
        var confirmed = JsonSerializer.Deserialize<TerendelevDeliveryAttempt>(saved, jsonOptions)!;
        check(confirmed.Confirmed && !confirmed.CanSubmit(true, true, true), "Confirmed missing actor can be spawned again.");
        check(!confirmed.TryConfirm(true, true, true, false), "Historical confirmation bypasses current usability.");
        check(confirmed.TryConfirm(true, true, true, true), "Returning live actor cannot re-establish contact.");
        var pending = new TerendelevDeliveryAttempt { UnitId = Guid.NewGuid().ToString(), Provenance = "quest.return" };
        check(!pending.TryConfirm(true, true, true, true), "Unsubmitted identity received confirmation.");
        check(!pending.Submit(true, false, true, () => { }, () => spawns++), "Unavailable meeting place dispatched.");
        check(pending.Submit(true, true, true, () => { }, () => spawns++), "Pending unsubmitted arrival could not retry after destination became ready.");
        var failedSave = new TerendelevDeliveryAttempt { UnitId = Guid.NewGuid().ToString(), Provenance = "quest.return" };
        string priorPending = JsonSerializer.Serialize(failedSave, jsonOptions);
        int before = spawns;
        try { failedSave.Submit(true, true, true, () => throw new Exception("Save checkpoint failed"), () => spawns++); }
        catch (Exception) { }
        check(spawns == before, "Native creation ran after checkpoint write failure.");
        check(failedSave.Submitted, "Failed persistence did not retain its local submission state.");
        var reread = JsonSerializer.Deserialize<TerendelevDeliveryAttempt>(priorPending, jsonOptions)!;
        check(!reread.Submitted && reread.UnitId == failedSave.UnitId, "Reading the prior saved checkpoint cannot recover a failed write.");
        check(reread.Submit(true, true, true, () => { }, () => spawns++) && spawns == before + 1,
            "A known checkpoint-write failure prevented safe retry from the persisted unsubmitted state.");
        confirmed.Version++;
        check(!confirmed.Valid && !confirmed.TryConfirm(true, true, true, true), "Unknown checkpoint version was adopted.");
    }
}
