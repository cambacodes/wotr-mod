using System;
using System.Collections.Generic;
using Tirabade;

internal static class ReachabilityCacheTests
{
    internal static void Run(Action<bool, string> check)
    {
        using var cache = new ReachabilityCache();
        var initial = new Snapshot { Chapter = 3, Hour = 100 };
        int traversed = 0;
        IEnumerable<Snapshot> History()
        {
            traversed++;
            var middle = Program.Copy(initial); middle.Flags.Add("refused"); yield return middle;
            var end = Program.Copy(initial); end.Flags.Add("committed"); yield return end;
        }
        check(cache.Reaches(initial, "committed", 3, History), "Shared walk lost the late target");
        check(cache.Reaches(initial, "refused", 3, History), "Shared walk lost an earlier aborted outcome");
        check(!cache.Reaches(initial, "unearned", 3, History), "Shared walk manufactured an outcome");
        check(traversed == 1, "Same world was traversed again");
        var poor = Program.Copy(initial);
        poor.CrusadeResources = new Dictionary<string, int> { ["Finances"] = 0 };
        check(!cache.Reaches(poor, "committed", 3, () => new[] { poor }), "Paid history leaked into an insolvent world");
        var stale = Program.Copy(initial); stale.Times["invitation"] = 99;
        check(!cache.Reaches(stale, "committed", 3, () => new[] { stale }), "Timestamp history was merged");
        var absent = Program.Copy(initial); absent.AvailableContacts.Add("absent-fixture");
        check(!cache.Reaches(absent, "committed", 3, () => new[] { absent }), "Actor observations were merged");
        check(!cache.Reaches(initial, "committed", 3, () => new[] { initial }, "other-area"), "Area histories were merged");
        check(!cache.Reaches(initial, "committed", 5, () => new[] { initial }), "Chapter histories were merged");
    }
}
