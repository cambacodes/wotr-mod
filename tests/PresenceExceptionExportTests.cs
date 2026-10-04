using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

internal static class PresenceExceptionExportTests
{
    private static Story Clone(Story story) => JsonSerializer.Deserialize<Story>(JsonSerializer.Serialize(story,
        new JsonSerializerOptions { IncludeFields = true }), new JsonSerializerOptions { IncludeFields = true })!;

    internal static void Run(Story story, Action<bool, string> check)
    {
        if (!story.Derived.ContainsKey(Rules.TricksterNow)) return;
        // This instance was loaded from the same JSON that a fresh Python lint process reads.
        Rules.ValidatePresenceExceptionGuards(story);
        foreach (string name in new[] { "aranka.presence", "nenio.presence", "nenio.presence.arcade" })
            check(story.PresenceExceptions.ContainsKey(name), "Missing serialized bootstrap " + name);
        void Invalid(string label, Action<Story> mutation)
        {
            var bad = Clone(story); mutation(bad);
            bool rejected = false;
            try { Rules.ValidatePresenceExceptionGuards(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Managed reader accepts arbitrary bypass: " + label);
        }
        Invalid("undeclared Nenio", s => s.PresenceExceptions.Remove("nenio.presence"));
        Invalid("closure removed", s => s.DerivedForbids["nenio.presence.route_open"] = s.DerivedForbids["nenio.presence.route_open"].Where(f => f != "nenio.closed").ToArray());
        Invalid("arbitrary dissolution", s => s.PresenceExceptions["nenio.presence"].AbsentLosses["nenio.dissolved"] = "Invented bypass");
        Invalid("arbitrary dead lift", s => s.DerivedForbids["nenio.presence.route_open.blocked.nenio.dead"] = new[] { "nenio.trickster.primed_away" });
        Invalid("unearned declared flag", s => {
            s.PresenceExceptions["nenio.presence"].Overrides["nenio.sent_away"].Flag = "chapter_later";
            s.PresenceExceptions["nenio.presence.arcade"].Overrides["nenio.sent_away"].Flag = "chapter_later";
            s.DerivedForbids["nenio.presence.route_open.blocked.nenio.sent_away"] = new[] { "nenio.trickster.returned", "chapter_later" };
        });
        Invalid("path latch declared as payment", s => {
            s.PresenceExceptions["nenio.presence"].Overrides["nenio.sent_away"].Flag = "trickster.ever";
            s.PresenceExceptions["nenio.presence.arcade"].Overrides["nenio.sent_away"].Flag = "trickster.ever";
            s.DerivedForbids["nenio.presence.route_open.blocked.nenio.sent_away"] = new[] { "nenio.trickster.returned", "trickster.ever" };
        });
        foreach (string loss in new[] { "nenio.sent_away", "nenio.kicked_out" })
        {
            var initial = PresenceBootstrapInventoryTests.Fresh(story, 3, loss);
            check(!Rules.PresenceWanted(story.Presences["nenio.presence"], initial), "Declaration grants unpaid Nenio");
            var state = PresenceBootstrapInventoryTests.Play(story, "nenio.trickster.away.field_report", initial, "nenio.trickster.primed_away", check);
            state = PresenceBootstrapInventoryTests.Later(story, state);
            PresenceBootstrapInventoryTests.Contact(story, "nenio.presence", state, check);
            check(Rules.Available(story, story.Scenes.Single(s => s.Id == "nenio.trickster.away.correction_visitor"), state), "Nenio probation contact blocked");
            // Observe a failed primary anchor, then the arcade actor (not a fabricated source flag).
            var primary = story.Presences["nenio.presence"];
            var failed = new PresenceObservation { AreaLoaded = true, AnchorResolved = false };
            check(Rules.PresenceFailed(primary, Rules.PresenceWanted(primary, state), failed), "Nenio primary not failed");
            state.Flags.Add(Rules.PresenceFailedFlag("nenio.presence"));
            Rules.Complete(story, state); state.AvailableContacts.Clear();
            PresenceBootstrapInventoryTests.Contact(story, "nenio.presence.arcade", state, check);
            check(Rules.Available(story, story.Scenes.Single(s => s.Id == "nenio.trickster.away.correction_arcade"), state), "Nenio arcade probation blocked");
            foreach (string unrelated in new[] { "nenio.closed", "nenio.dead", "nenio.killed_by_commander", "nenio.dissolved" })
            {
                var bad = Program.Copy(state); bad.Flags.Add(unrelated); PresenceBootstrapInventoryTests.Recompute(story, bad);
                check(!Rules.PresenceWanted(story.Presences["nenio.presence.arcade"], bad), "Probation lifts unrelated loss " + unrelated);
            }
            var offPath = Program.Copy(state); offPath.Flags.Add("trickster.failed"); PresenceBootstrapInventoryTests.Recompute(story, offPath);
            check(!Rules.Available(story, story.Scenes.Single(s => s.Id == "nenio.trickster.away.correction_arcade"), offPath),
                "Probation return act fires off-Trickster");
        }
    }
}
