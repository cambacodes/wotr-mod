using System;
using System.IO;
using HarmonyLib;
using Kingmaker.Blueprints.JsonSystem;
using UnityEngine;
using UnityModManagerNet;

namespace RRT.TestHarness
{
    public static class Entry
    {
        public const string Id = "RRTTestHarness";
        public const string RrtId = "RanRomanceTirabade";
        internal static UnityModManager.ModEntry Mod = null!;
        internal static volatile bool CacheInitSeen;

        public static bool Load(UnityModManager.ModEntry mod)
        {
            Mod = mod;
            string? planPath;
            bool fromModFolder;
            try { planPath = HarnessPlan.FindActivation(mod.Path, Environment.GetEnvironmentVariable, out fromModFolder); }
            catch (Exception ex) { mod.Logger.LogException(ex); return true; }
            if (planPath == null)
            {
                mod.Logger.Log("Inactive: no " + HarnessPlan.FileName + " in the mod folder and no " + HarnessPlan.EnvVar + " variable.");
                return true;
            }

            var report = new HarnessReport { PlanPath = planPath.Length == 0 ? "(env default)" : planPath };
            string reportPath = Path.Combine(mod.Path, HarnessPlan.ReportFileName);
            try
            {
                if (planPath.Length > 0)
                {
                    report.Plan = HarnessPlan.Parse(File.ReadAllText(planPath));
                    // Consume the plan so a forgotten install never hijacks a normal play session.
                    if (fromModFolder) File.Move(planPath, planPath + ".consumed-" + DateTime.Now.ToString("yyyyMMdd-HHmmss"));
                }
                if (!string.IsNullOrWhiteSpace(report.Plan.ReportPath)) reportPath = Path.GetFullPath(report.Plan.ReportPath);
                if (File.Exists(reportPath)) File.Delete(reportPath);
            }
            catch (Exception ex)
            {
                report.Status = "aborted";
                report.AbortReason = "Plan could not be read: " + ex.Message;
                report.ComputeSummary();
                try { report.Write(reportPath); } catch (Exception wex) { mod.Logger.LogException(wex); }
                mod.Logger.LogException(ex);
                return true;
            }

            // Minimised or unfocused windows must keep ticking.
            Application.runInBackground = true;
            var harmony = new Harmony(Id);
            LogCapture.Install(harmony, mod.Logger);
            try
            {
                var init = AccessTools.Method(typeof(BlueprintsCache), nameof(BlueprintsCache.Init));
                harmony.Patch(init, postfix: new HarmonyMethod(typeof(Entry), nameof(CachePostfix)) { priority = Priority.Last - 1, after = new[] { RrtId } });
            }
            catch (Exception ex) { mod.Logger.Log("BlueprintsCache.Init hook failed: " + ex.Message); }

            var host = new GameObject("RRT.TestHarness");
            UnityEngine.Object.DontDestroyOnLoad(host);
            var runner = host.AddComponent<HarnessRunner>();
            runner.Configure(report, reportPath, harmony);
            mod.Logger.Log("ACTIVE. Plan: " + report.PlanPath + "; report: " + reportPath);
            return true;
        }

        static void CachePostfix() => CacheInitSeen = true;
    }
}
