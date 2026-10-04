using System;
using System.Linq;
using System.Text.Json;
using Tirabade;

internal static class NativeWorldReconciliationInventoryTests
{
    private sealed class Display { public bool Visible; public Display(bool visible) { Visible = visible; } }
    internal static void Run(Story shipped, Action<bool, string> check)
    {
        // Exercise the actual runtime visibility ownership through three area reloads and two save owners.
        var lease = new NativeVisibilityLease<Display>();
        var owner = new object(); lease.Reset(owner);
        for (int reload = 0; reload < 3; reload++)
        {
            var corpses = Enumerable.Range(0, 4).Select(_ => new Display(true)).ToArray();
            var unrelated = new Display(true);
            int writes = 0;
            void Write(Display display, bool value) { display.Visible = value; writes++; }
            foreach (var display in corpses) lease.Hide(display, d => d.Visible, Write);
            check(corpses.All(d => !d.Visible) && unrelated.Visible && writes == 4, "Burial hid unrelated objects or omitted a corpse.");
            foreach (var display in corpses) lease.Hide(display, d => d.Visible, Write);
            check(writes == 4, "Repeated tick changed visibility again.");
            lease.ReleaseExcept(corpses, Write, _ => check(false, "Visibility keep failed."));
            check(writes == 4, "Reload keep restored an earned display.");
            lease.ReleaseExcept(Array.Empty<Display>(), Write, _ => check(false, "Visibility release failed."));
            check(corpses.All(d => d.Visible) && unrelated.Visible, "Off-path/disabled release did not restore native visibility.");
        }
        var nativeHidden = new Display(false);
        lease.Hide(nativeHidden, d => d.Visible, (d, v) => d.Visible = v);
        lease.ReleaseExcept(Array.Empty<Display>(), (d, v) => d.Visible = v, _ => check(false, "Hidden release failed."));
        check(!nativeHidden.Visible, "Release unhid a natively hidden object.");
        var nativeWouldUnhide = new Display(false);
        nativeWouldUnhide.Visible = true; // The reviewed native unhide still executes before view suppression.
        lease.Hide(nativeWouldUnhide, d => d.Visible, (d, v) => d.Visible = v);
        lease.ReleaseExcept(Array.Empty<Display>(), (d, v) => d.Visible = v, _ => check(false, "Native unhide release failed."));
        check(nativeWouldUnhide.Visible, "Native unhide wrapper lost its original visibility when disabled.");
        var oldSave = new Display(true); lease.Hide(oldSave, d => d.Visible, (d, v) => d.Visible = v);
        lease.Reset(new object());
        lease.ReleaseExcept(Array.Empty<Display>(), (d, v) => d.Visible = v, _ => check(false, "Save release failed."));
        check(!oldSave.Visible, "Reload wrote visibility into another save's actor.");

        check(shipped.NativeWorldReconciliations.Count == 8, "E-Q7-32 mapped targets are incomplete.");
        foreach (var pair in shipped.NativeWorldReconciliations)
        {
            var spec = pair.Value;
            foreach (var group in spec.When)
            {
                var state = new Snapshot(); state.Flags.UnionWith(group);
                check(Rules.NativeWorldHolds(shipped, pair.Key, state), "Earned world reconciliation unavailable: " + pair.Key);
                foreach (var omitted in group)
                {
                    var missing = new Snapshot(); missing.Flags.UnionWith(group.Where(f => f != omitted));
                    check(!Rules.NativeWorldHolds(shipped, pair.Key, missing), "World outcome became free: " + omitted);
                }
                state.Flags.Add(Rules.DegradedPrefix + spec.Relationship);
                check(!Rules.NativeWorldHolds(shipped, pair.Key, state), "Degraded world edit changes canon.");
                if (Rules.ReviewedNativeWorldTargets[pair.Key].EndsWith(":JOURNAL", StringComparison.Ordinal))
                {
                    state.Flags.Remove(Rules.DegradedPrefix + spec.Relationship);
                    // Selection is independent of quest start, completion and objective state; progression remains native.
                    foreach (var questState in new[] { "", "seelah.q3_started", "seelah.souls_returned" })
                    {
                        if (questState.Length > 0) state.Flags.Add(questState);
                        check(Rules.NativeJournalText(shipped, pair.Key, false, state) == spec.Description,
                            "Paid journal description unavailable before/after quest start.");
                        check(Rules.NativeJournalText(shipped, pair.Key, true, state) == (spec.TitleKey.Length == 0 ? null : spec.Title),
                            "Paid journal title selection changed an unrelated title.");
                    }
                    var partial = new Snapshot(); partial.Flags.UnionWith(Rules.Q3RecoveryPartialRequirements);
                    check(Rules.NativeJournalText(shipped, pair.Key, false, partial) == null, "Partial rescue erased unrecovered souls from the journal.");
                }
            }
            foreach (var path in new[] { "angel", "aeon", "azata", "demon", "devil", "dragon", "legend", "lich", "swarm", "trickster.failed" })
            {
                var off = new Snapshot(); off.Flags.UnionWith(spec.When[0].Where(f => f != "trickster.now"));
                off.Flags.UnionWith(new[] { "trickster.ever", path });
                if (path is "dragon" or "legend" or "swarm" or "trickster.failed") off.Flags.Add("trickster");
                Rules.Complete(shipped, off);
                check(!Rules.NativeWorldHolds(shipped, pair.Key, off), "World reconciliation changes canon off Trickster: " + path);
            }
        }
        var options = new JsonSerializerOptions { IncludeFields = true };
        foreach (var target in shipped.NativeWorldReconciliations.Keys)
        {
            var copy = JsonSerializer.Deserialize<Story>(JsonSerializer.Serialize(shipped, options), options)!;
            copy.NativeWorldReconciliations[target].When = new[] { new[] { "trickster.ever" } };
            bool rejected = false;
            try { Rules.Validate(copy); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "World contract mutation passed offline/Main.Load validation: " + target);
            if (Rules.ReviewedNativeJournalKeys.ContainsKey(target))
            {
                copy.NativeWorldReconciliations[target].When = shipped.NativeWorldReconciliations[target].When;
                copy.NativeWorldReconciliations[target].DescriptionKey = "unreviewed";
                rejected = false;
                try { Rules.Validate(copy); } catch (InvalidOperationException) { rejected = true; }
                check(rejected, "Journal localization drift passed Main.Load validation: " + target);
            }
        }
        Console.WriteLine("PASS: E-Q7-32 all eight serialized targets, paid/partial/unearned/off-path states and negative contracts.");
    }
}
