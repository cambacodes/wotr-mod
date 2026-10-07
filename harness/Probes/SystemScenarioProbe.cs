using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using HarmonyLib;

namespace RRT.TestHarness
{
    // A final-state fixture substitutes flags only. Chapter, area, contacts, purse and native actors stay real.
    // No condition checker is bypassed. State effects still execute on the disposable world.
    internal sealed class SystemScenarioProbe : IDisposable
    {
        const BindingFlags Static = BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;
        readonly Harmony patches = new Harmony("RRTTestHarness.SystemScenarios");
        readonly RrtBridge bridge;
        readonly int chapter;
        readonly HashSet<string>? flags;
        readonly Dictionary<string, int> times = new Dictionary<string, int>();
        readonly Dictionary<string, int> spent = new Dictionary<string, int>();
        static SystemScenarioProbe? active;

        internal SystemScenarioProbe(RrtBridge bridge, List<string>? fixtureFlags, int chapter)
        {
            this.bridge = bridge;
            this.chapter = chapter;
            var problems = RrtBridge.Validate(bridge.Assembly, RrtBridge.SystemScenarioExpectations);
            if (problems.Count > 0) throw new InvalidOperationException(string.Join("; ", problems));
            if (active != null) throw new InvalidOperationException("Another system scenario is active");
            flags = fixtureFlags == null ? null : new HashSet<string>(fixtureFlags, StringComparer.Ordinal);
            try
            {
                active = this;
                var main = bridge.Assembly.GetType("Tirabade.Main", true)!;
                patches.Patch(main.GetMethod("Update", Static)!, prefix: new HarmonyMethod(typeof(SystemScenarioProbe), nameof(OnlyQueuedUpdate)));
                if (flags != null)
                {
                    patches.Patch(main.GetMethod("State", Static)!, postfix: new HarmonyMethod(typeof(SystemScenarioProbe), nameof(State)));
                    patches.Patch(main.GetMethod("Set", Static)!, postfix: new HarmonyMethod(typeof(SystemScenarioProbe), nameof(Set)));
                    // RecordProgress reads the real unlockable values before writing effects. Keep those RRT values
                    // consistent with the fixture so a flag already held in the source save cannot mask a new write.
                    // The save guard is active; all changes are discarded by the mandatory source reload.
                    foreach (string key in bridge.Flags.Keys.Cast<string>())
                    {
                        if (key.StartsWith("rrt.degraded.", StringComparison.Ordinal)) continue;
                        bridge.Set(key, flags.Contains(key) ? 1 : 0);
                    }
                }
            }
            catch { Dispose(); throw; }
        }

        static bool OnlyQueuedUpdate() => active!.bridge.Assembly.GetType("Tirabade.Main", true)!
            .GetField("pending", Static)!.GetValue(null) != null;

        static void Set(string key, int value)
        {
            var p = active!;
            if (key.StartsWith("rrt.rest.spent.", StringComparison.Ordinal)) p.spent[key.Substring(15)] = value;
            else if (key.StartsWith("hour.", StringComparison.Ordinal)) p.times[key.Substring(5)] = value - 1;
            else if (value > 0) p.flags!.Add(key);
            else p.flags!.Remove(key);
        }

        static void State(ref object __result)
        {
            var p = active!;
            // Clone: never mutate Main.cachedState or its saved-history collections.
            var copy = Clone(__result);
            Put(copy, "Chapter", p.chapter);
            var flags = new HashSet<string>(p.flags!, StringComparer.Ordinal);
            flags.UnionWith(RrtBridge.FlagSet(__result).Where(key => key.StartsWith("rrt.degraded.", StringComparison.Ordinal)));
            Put(copy, "Flags", flags);
            Put(copy, "Times", new Dictionary<string, int>(p.times));
            Put(copy, "RestSpent", new Dictionary<string, int>(p.spent));
            Complete(p.bridge, copy);
            __result = copy;
        }

        internal static object Clone(object value) => Newtonsoft.Json.JsonConvert.DeserializeObject(
            Newtonsoft.Json.JsonConvert.SerializeObject(value), value.GetType())!;
        static void Put(object value, string field, object data) => value.GetType().GetField(field)!.SetValue(value, data);
        internal static void Complete(RrtBridge bridge, object state) => bridge.Assembly.GetType("Tirabade.Rules", true)!
            .GetMethod("Complete", Static)!.Invoke(null, new[] { bridge.Story!, state });

        internal static object Control(RrtBridge bridge, object state, SystemStep step)
        {
            var copy = Clone(state);
            var flags = (HashSet<string>)RrtBridge.Get(copy, "Flags")!;
            flags.ExceptWith(step.Remove); flags.UnionWith(step.Add);
            var spent = (Dictionary<string, int>)RrtBridge.Get(copy, "RestSpent")!;
            foreach (var pair in step.RestSpent) spent[pair.Key] = pair.Value;
            if (step.RestSucceeded.HasValue)
                bridge.Assembly.GetType("Tirabade.Rules", true)!.GetMethod("RestFinished", Static)!
                    .Invoke(null, new object[] { copy, step.RestSucceeded.Value });
            Complete(bridge, copy);
            return copy;
        }

        internal static List<string> TableEntries(RrtBridge bridge, object state) => ((IEnumerable)bridge.Assembly
            .GetType("Tirabade.Rules", true)!.GetMethod("TableEntries", Static)!.Invoke(null, new[] { bridge.Story!, state })!)
            .Cast<object>().Select(RrtBridge.SceneId).ToList();

        internal static List<string> LedgerEntries(RrtBridge bridge, object state)
        {
            var books = (IDictionary)RrtBridge.Get(bridge.Story!, "Books")!;
            return ((IEnumerable)bridge.Assembly.GetType("Tirabade.Rules", true)!.GetMethod("BookVisible", Static)!
                .Invoke(null, new[] { books["trickster.ledger"], state })!).Cast<object>()
                .Select(e => (string)RrtBridge.Get(e, "Id")!).ToList();
        }

        internal bool OpenTable() => (bool)bridge.Assembly.GetType("Tirabade.Main", true)!
            .GetMethod("OpenView", Static)!.Invoke(null, new object?[] { "table", null })!;

        public void Dispose()
        {
            patches.UnpatchAll(patches.Id);
            active = null;
        }
    }
}
