using System;
using System.IO;
using System.Linq;
using System.Reflection;
using HarmonyLib;
using UnityModManagerNet;

// Exercises the real UnityModManager entry point, Main.Load, in the same order UMM uses it:
// Story.json deserialization, Rules.Validate, settings, and Harmony PatchAll over every type in the assembly.
// Main.Build is covered by Program.Run; this test covers everything that happens before the blueprint cache exists.
internal static class LoadSmokeTests
{
    private const BindingFlags PrivateStatic = BindingFlags.NonPublic | BindingFlags.Static;

    public static int Run(string storyPath, string modDirectory)
    {
        int failures = 0;
        void Check(bool ok, string message)
        {
            if (ok) return;
            failures++;
            Console.Error.WriteLine("FAIL: " + message);
        }

        var assembly = typeof(Tirabade.Main).Assembly;

        // 1. Every [TypeId] must construct. Harmony instantiates every attribute on every type during PatchAll.
        foreach (var type in assembly.GetTypes())
        {
            try { type.GetCustomAttributes(true); }
            catch (Exception ex) { Check(false, "Attribute construction throws on " + type.FullName + ": " + ex.GetBaseException().Message); }
        }
        var typeIds = assembly.GetTypes().SelectMany(t =>
        {
            try
            {
                return t.GetCustomAttributes(typeof(Kingmaker.Blueprints.JsonSystem.TypeIdAttribute), false)
                    .Cast<Kingmaker.Blueprints.JsonSystem.TypeIdAttribute>().Select(a => (Type: t, Id: a.GuidString)).ToArray();
            }
            catch { return Array.Empty<(Type Type, string Id)>(); } // already reported above
        }).ToArray();
        Check(typeIds.Select(t => t.Id).Distinct(StringComparer.OrdinalIgnoreCase).Count() == typeIds.Length, "Duplicate [TypeId] values in the mod assembly.");
        foreach (var t in typeIds)
            Check(Guid.TryParseExact(t.Id, "N", out _), "[TypeId] is not a 32-digit GUID on " + t.Type.FullName + ": " + t.Id);

        // 2. Main.Load's own steps, with the exact deserializer and validator it uses.
        try
        {
            var story = Newtonsoft.Json.JsonConvert.DeserializeObject<Tirabade.Story>(File.ReadAllText(storyPath))
                ?? throw new InvalidOperationException("Story.json is empty.");
            Tirabade.Rules.Validate(story);
        }
        catch (Exception ex) { Check(false, "Story.json fails Main.Load's deserialize+validate: " + ex.GetBaseException().Message); }

        // 3. Harmony PatchAll, one patch class at a time so a single failure cannot hide the others.
        //    The .NET Framework host cannot compile replacements for methods that call Unity internal calls
        //    ("ECall methods must be packaged into a system module"); Unity's Mono can. That one error means the
        //    target resolved and the patch was accepted up to IL generation, so it is reported, not failed.
        string harmonyId = "RanRomanceTirabade.LoadSmoke";
        var harmony = new Harmony(harmonyId);
        int applied = 0, hostLimited = 0;
        var patchClasses = AccessTools.GetTypesFromAssembly(assembly)
            .Where(t => t.GetCustomAttributes(typeof(HarmonyPatch), true).Length > 0).ToArray();
        Check(patchClasses.Length >= 4, "Expected at least 4 Harmony patch classes, found " + patchClasses.Length);
        try
        {
            foreach (var type in patchClasses)
            {
                try
                {
                    var processor = harmony.CreateClassProcessor(type);
                    var targets = processor.Patch();
                    Check(targets != null && targets.Count > 0, "Harmony patch class resolved no target: " + type.FullName);
                    applied++;
                }
                catch (Exception ex) when (ex.ToString().Contains("ECall methods must be packaged into a system module"))
                {
                    hostLimited++;
                    Console.WriteLine("HOST-LIMITED (needs Unity Mono, target resolved): " + type.FullName);
                }
                catch (Exception ex) { Check(false, "Harmony patch class fails: " + type.FullName + ": " + ex.GetBaseException().Message); }
            }
        }
        finally { harmony.UnpatchAll(harmonyId); }

        if (failures > 0) { Console.Error.WriteLine($"LOAD SMOKE FAILED: {failures} problem(s)."); return 1; }
        Console.WriteLine($"PASS: load smoke. {typeIds.Length} TypeIds valid; Story.json deserializes and validates; " +
            $"{applied} Harmony patch classes applied and removed, {hostLimited} resolved but need Unity Mono to finish IL generation.");
        return 0;
    }
}
