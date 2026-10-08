using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using HarmonyLib;
using Owlcat.Runtime.Core.Logging;
using UnityEngine;

namespace RRT.TestHarness
{
    /// <summary>
    /// Collects errors and exceptions from every channel the game and mods write to:
    ///  - Application.logMessageReceivedThreaded (Unity Debug.Log*, uncaught exceptions);
    ///  - Owlcat.Runtime.Core.Logging.Logger sinks (PFLog / LogChannel, i.e. GameLogFull.txt);
    ///  - UnityModManager.Logger.Log(string,string) / LogException(string,Exception,string) (mod loggers);
    ///  - Harmony finalizers on the dialog controller and RRT route condition/action (exceptions with stacks).
    /// </summary>
    internal sealed class LogCapture : ILogSink
    {
        internal static LogCapture? Instance;
        readonly object gate = new object();
        readonly List<CapturedLog> entries = new List<CapturedLog>();
        readonly Queue<string> recent = new Queue<string>();
        readonly System.Diagnostics.Stopwatch clock = System.Diagnostics.Stopwatch.StartNew();
        internal volatile string? Context;
        internal const int Cap = 5000;

        internal static LogCapture Install(Harmony harmony, UnityModManagerNet.UnityModManager.ModEntry.ModLogger log)
        {
            var c = Instance = new LogCapture();
            Application.logMessageReceivedThreaded += c.OnUnity;
            try { Owlcat.Runtime.Core.Logging.Logger.Instance.AddLogger(c, false); }
            catch (Exception ex) { log.Log("Owlcat log sink unavailable: " + ex.Message); }
            try
            {
                var ummLogger = typeof(UnityModManagerNet.UnityModManager.Logger);
                harmony.Patch(AccessTools.Method(ummLogger, "Log", new[] { typeof(string), typeof(string) }),
                    prefix: new HarmonyMethod(typeof(LogCapture), nameof(UmmLogPrefix)));
                harmony.Patch(AccessTools.Method(ummLogger, "LogException", new[] { typeof(string), typeof(Exception), typeof(string) }),
                    prefix: new HarmonyMethod(typeof(LogCapture), nameof(UmmExceptionPrefix)));
            }
            catch (Exception ex) { log.Log("UMM logger hook unavailable: " + ex.Message); }
            return c;
        }

        internal static void PatchFinalizer(Harmony harmony, MethodBase? target, List<string> problems, string label)
        {
            if (target == null) { problems.Add("finalizer target missing: " + label); return; }
            try { harmony.Patch(target, finalizer: new HarmonyMethod(typeof(LogCapture), nameof(Finalizer))); }
            catch (Exception ex) { problems.Add("finalizer on " + label + " failed: " + ex.Message); }
        }

        // Harmony finalizer: records, then returns the exception unchanged so game behaviour is identical.
        static Exception? Finalizer(Exception? __exception, MethodBase __originalMethod)
        {
            if (__exception != null)
                Instance?.Add("finalizer", "Exception", __originalMethod.DeclaringType?.FullName + "." + __originalMethod.Name + ": "
                    + __exception.GetType().FullName + ": " + __exception.Message, __exception.ToString());
            return __exception;
        }

        static void UmmLogPrefix(string str, string prefix)
        {
            if (prefix == null || prefix.StartsWith("[" + Entry.Id + "]", StringComparison.Ordinal)) return;
            if (prefix.Contains("[Error]") || prefix.Contains("[Critical]") || prefix.Contains("[Exception]"))
                Instance?.Add("umm", prefix.Contains("[Critical]") ? "Critical" : "Error", prefix + str, null);
        }

        static void UmmExceptionPrefix(string key, Exception e, string prefix)
        {
            if (prefix != null && prefix.StartsWith("[" + Entry.Id + "]", StringComparison.Ordinal)) return;
            Instance?.Add("umm", "Exception", prefix + (key != null ? key + ": " : "") + e?.GetType().FullName + ": " + e?.Message, e?.ToString());
        }

        void OnUnity(string condition, string stackTrace, LogType type)
        {
            if (type == LogType.Error || type == LogType.Exception || type == LogType.Assert)
                Add("unity", type.ToString(), condition, stackTrace);
        }

        void ILogSink.Log(LogInfo info)
        {
            if (info == null || (info.Severity != LogSeverity.Error && !info.IsException)) return;
            string? stack = info.Callstack == null ? null
                : string.Join("\n", info.Callstack.Select(f => f.DeclaringType + "." + f.MethodName + (f.FileName != null ? " (" + f.FileName + ":" + f.LineNumber + ")" : "")));
            Add("owlcat", info.IsException ? "Exception" : "Error", (info.Channel != null ? "[" + info.Channel.Name + "] " : "") + info.Message, stack);
        }

        void ILogSink.Destroy() { }

        // Third-party behavior observed in live runs that is not an RRT defect. Kept in the report, tagged, never failing.
        private static readonly (string Pattern, string Reason)[] KnownBenign =
        {
            ("[Audio] Failed to play sound evt_RRT.", "WOTR_AIVO requests a voice clip for every cue; RRT cues are unvoiced (audio only, no effect on dialogue)"),
            ("[Audio] Failed to play sound ev_stop_aivo", "WOTR_AIVO stop event when an unvoiced RRT cue interrupts playback (audio only)"),
        };

        internal static string? BenignReason(string message) => BenignReason(message, null);

        // Any "[Audio] Failed to play sound" raised from the WOTR_AIVO voiceover shim (AiVoiceoverMod in the stack) is audio-only
        // noise, on RRT or native cues alike: the shim requests a clip for every cue it sees. Narrow on purpose: audio-shim
        // failures only, never other audio or dialog errors.
        internal static string? BenignReason(string message, string? stack)
        {
            var known = KnownBenign.Where(b => message.IndexOf(b.Pattern, StringComparison.Ordinal) >= 0).Select(b => b.Reason).FirstOrDefault();
            if (known != null) return known;
            if (message.IndexOf("[Audio] Failed to play sound", StringComparison.Ordinal) >= 0
                && stack != null && stack.IndexOf("AiVoiceoverMod", StringComparison.Ordinal) >= 0)
                return "WOTR_AIVO voiceover shim failed to play a clip (audio only, no effect on dialogue)";
            return null;
        }

        internal static bool IsRelevant(string message, string? stack)
        {
            if (BenignReason(message, stack) != null) return false;
            string text = message + "\n" + stack;
            return text.IndexOf("Tirabade", StringComparison.Ordinal) >= 0
                || text.IndexOf("RRT_", StringComparison.Ordinal) >= 0
                || text.IndexOf("RanRomance", StringComparison.Ordinal) >= 0
                || text.IndexOf("RRT.TestHarness", StringComparison.Ordinal) >= 0
                || text.IndexOf("DialogController", StringComparison.Ordinal) >= 0
                || text.IndexOf("BookEvent", StringComparison.Ordinal) >= 0
                || text.IndexOf("invalid dialog answer", StringComparison.OrdinalIgnoreCase) >= 0
                || text.IndexOf("Stack overflow while playing dialog cues", StringComparison.Ordinal) >= 0
                || text.IndexOf("Could not select any cue", StringComparison.Ordinal) >= 0;
        }

        internal void Add(string source, string severity, string message, string? stack)
        {
            lock (gate)
            {
                // The Owlcat logger mirrors Unity's log stream: drop exact repeats seen very recently.
                string key = message ?? "";
                if (recent.Contains(key)) return;
                recent.Enqueue(key);
                while (recent.Count > 64) recent.Dequeue();
                if (entries.Count >= Cap) return;
                entries.Add(new CapturedLog
                {
                    Source = source, Severity = severity,
                    Message = BenignReason(message ?? "", stack) is string reason ? "[known benign: " + reason + "] " + message : message ?? "", StackTrace = stack,
                    AtSeconds = Math.Round(clock.Elapsed.TotalSeconds, 3), Context = Context,
                    Relevant = source == "finalizer" || IsRelevant(message ?? "", stack),
                });
            }
        }

        internal int Mark() { lock (gate) return entries.Count; }

        internal List<CapturedLog> Since(int mark)
        {
            lock (gate) return entries.Skip(mark).ToList();
        }

        internal void ResetRecent() { lock (gate) recent.Clear(); }
    }
}
