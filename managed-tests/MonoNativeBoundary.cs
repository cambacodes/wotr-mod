using System;
using System.Collections.Generic;
using System.Reflection;
using HarmonyLib;

// Reproduce the Windows host's pre-mutation ECall rejection at a scoped managed boundary.
// Desktop Mono otherwise enters unavailable Unity code (or mutates incomplete fixture state).
internal sealed class MonoNativeBoundary : IDisposable
{
    internal static bool Enabled => Type.GetType("Mono.Runtime") != null;
    private static readonly Dictionary<MethodBase, MonoNativeBoundary> active = new Dictionary<MethodBase, MonoNativeBoundary>();
    private readonly Harmony harmony;
    private readonly MethodBase method;
    internal int Calls { get; private set; }

    internal MonoNativeBoundary(MethodBase method, string fixture)
    {
        this.method = method ?? throw new ArgumentNullException(nameof(method));
        harmony = new Harmony("RanRomance.Tirabade.MonoBoundary." + fixture);
        if (!Enabled) return;
        active.Add(method, this);
        try { harmony.Patch(method, prefix: new HarmonyMethod(typeof(MonoNativeBoundary), nameof(Reject))); }
        catch { Dispose(); throw; }
    }

    private static void Reject(MethodBase __originalMethod)
    {
        active[__originalMethod].Calls++;
        throw new System.Security.SecurityException("Headless Mono boundary: " + __originalMethod.DeclaringType!.FullName + "." + __originalMethod.Name);
    }

    public void Dispose()
    {
        if (!Enabled) return;
        try { harmony.UnpatchAll(harmony.Id); }
        finally { active.Remove(method); }
    }
}
