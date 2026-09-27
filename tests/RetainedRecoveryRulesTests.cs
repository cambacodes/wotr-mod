using System;
using System.Collections.Generic;
using System.Text.Json;
using Tirabade;

internal static class RetainedRecoveryRulesTests
{
    internal static void Run(Action<bool, string> check)
    {
        const string unit = "ca2d58c5c65723945857e04fb85d30ce";
        const string capital = "2570015799edf594daf2f076f2f975d8";
        var restore = new Choice { Revive = "konomi", Set = new[] { "konomi.retained_return_confirmed" } };
        Scene Page(string id) => new Scene {
            Id = id, Relationship = "konomi", Owner = "Memory", Remote = true,
            MinChapter = 3, MaxChapter = 5, Chapters = new[] { 3, 5 }, Areas = new[] { capital },
            Nodes = new List<Node> { new Node { Id = "start", Text = "A retained return witness.", Choices = new List<Choice> { new Choice() } } }
        };
        var attempt = Page("konomi.recovery_fixture");
        attempt.Recovery = "konomi";
        attempt.Requires = new[] { "trickster", "konomi.retained_dead" };
        attempt.Nodes[0].Choices[0] = restore;
        var after = Page("konomi.after_fixture");
        after.AfterRecovery = "konomi";
        after.ContactUnit = unit;
        after.Requires = new[] { "konomi.retained_return_confirmed", "konomi.return_contact_available" };
        var ordinary = Page("konomi.ordinary_fixture");
        var story = new Story { Scenes = new List<Scene> { attempt, after, ordinary } };
        story.Relationships["konomi"] = new Relationship {
            Title = "Konomi", StartedFlag = "konomi.started", ClosedFlag = "konomi.closed", CommittedFlag = "konomi.committed",
            UnavailableFlags = new[] { "konomi.retained_dead", "inhuman" }
        };
        story.Revivals["konomi"] = new Revival { Relationship = "konomi", Unit = unit, DeathFlag = "konomi.retained_dead" };
        Rules.Validate(story);
        var state = new Snapshot { Chapter = 3, Hour = 100, Area = capital };
        state.Flags.UnionWith(new[] { "trickster", "konomi.retained_dead", "revive.konomi.available", "konomi.closed" });
        check(Rules.Available(story, attempt, state), "Romantic refusal must not prohibit a valid restoration choice.");
        check(!Rules.Available(story, ordinary, state), "Recovery bypass reopened a closed ordinary relationship.");
        foreach (var required in new[] { "trickster", "konomi.retained_dead", "revive.konomi.available" })
        {
            state.Flags.Remove(required);
            check(!Rules.Available(story, attempt, state), "Recovery ignored required evidence: " + required);
            check(!Rules.ContactAvailable(story, attempt, state), "In-progress recovery ignored lost evidence: " + required);
            state.Flags.Add(required);
        }
        state.Flags.Add("inhuman");
        check(!Rules.Available(story, attempt, state), "Death exception suppressed an unrelated native restriction.");
        state.Flags.Remove("inhuman");
        state.Flags.Remove("konomi.retained_dead");
        state.Flags.Remove("revive.konomi.available");
        state.Flags.Remove("trickster");
        state.Flags.UnionWith(new[] { "konomi.retained_return_confirmed", "konomi.return_contact_available" });
        state.AvailableContacts.Add(unit);
        check(Rules.Available(story, after, state), "Verified aftercare requires neither renewed mythic casting nor reopened romance.");
        check(state.Has("konomi.closed") && !Rules.Available(story, ordinary, state), "Aftercare erased prior refusal.");
        state.Flags.Remove("konomi.return_contact_available");
        check(!Rules.Available(story, after, state) && !Rules.ContactAvailable(story, after, state), "Saved return flag substituted for current original-actor evidence.");
        state.Flags.Add("konomi.return_contact_available");
        state.AvailableContacts.Clear();
        check(!Rules.Available(story, after, state) && !Rules.ContactAvailable(story, after, state), "Hidden recovered actor gained a physical conversation.");
        state.AvailableContacts.Add(unit);
        state.Area = "elsewhere";
        check(!Rules.Available(story, after, state), "Retained source meeting escaped its area restriction.");

        var letter = Page("konomi.return_letter_fixture");
        letter.AfterRecovery = "konomi";
        letter.Requires = new[] { "konomi.retained_return_confirmed", "konomi.return_correspondence_available" };
        story.Scenes.Add(letter);
        Rules.Validate(story);
        state.Area = capital;
        state.AvailableContacts.Clear();
        state.Flags.Remove("konomi.return_contact_available");
        check(!Rules.Available(story, letter, state), "A saved return checkpoint manufactured current correspondence.");
        state.Flags.Add("konomi.return_correspondence_available");
        check(Rules.Available(story, letter, state) && Rules.ContactAvailable(story, letter, state),
            "Verified living hidden Konomi cannot answer a remote invitation after a prior refusal.");
        check(!Rules.Available(story, after, state) && !Rules.Available(story, ordinary, state),
            "Correspondence proof substituted for physical arrival or reopened ordinary romance.");
        state.Flags.Remove("konomi.return_correspondence_available");
        check(!Rules.ContactAvailable(story, letter, state), "A remote reply ignored lost current life/contact evidence.");
        state.Flags.Add("konomi.return_correspondence_available");
        state.Flags.Remove("konomi.retained_return_confirmed");
        check(!Rules.Available(story, letter, state), "Unconfirmed restoration admitted correspondence.");
        state.Flags.Add("konomi.retained_return_confirmed");
        state.Area = "elsewhere";
        check(!Rules.Available(story, letter, state), "Retained correspondence escaped its loaded source area.");

        void Reject(Action change, Action restoreValue, string description)
        {
            change();
            bool rejected = false;
            try { Rules.Validate(story); } catch (InvalidOperationException) { rejected = true; }
            finally { restoreValue(); }
            check(rejected, description);
        }
        Reject(() => restore.Set = new[] { "konomi.retained_return_confirmed", "konomi.committed" }, () => restore.Set = new[] { "konomi.retained_return_confirmed" },
            "Restoration was allowed to grant romance as an effect.");
        Reject(() => restore.Revive = null, () => restore.Revive = "konomi", "An ordinary choice fabricated confirmed return.");
        Reject(() => after.ContactUnit = null, () => after.ContactUnit = unit, "Aftercare bypass accepted an unverified speaker.");
        Reject(() => after.Requires = new[] { "konomi.retained_return_confirmed" }, () => after.Requires = new[] { "konomi.retained_return_confirmed", "konomi.return_contact_available" },
            "Aftercare bypass accepted only stale saved proof.");
        Reject(() => after.AfterRecovery = "unknown", () => after.AfterRecovery = "konomi", "Unknown recovery bypassed closure.");
        Reject(() => story.Revivals["konomi"].Unit = "280d4712dceb37f4a88e98f1f4c6e64f", () => story.Revivals["konomi"].Unit = unit,
            "Konomi service accepted a different actor binding.");
        Reject(() => attempt.Requires = new[] { "konomi.retained_dead" }, () => attempt.Requires = new[] { "trickster", "konomi.retained_dead" },
            "Retained restoration omitted current Trickster authorization.");
        Reject(() => after.Nodes[0].Choices[0].Set = new[] { "konomi.return_contact_available" }, () => after.Nodes[0].Choices[0].Set = Array.Empty<string>(),
            "Authored choice manufactured native contact evidence.");
        Reject(() => letter.Requires = new[] { "konomi.retained_return_confirmed" },
            () => letter.Requires = new[] { "konomi.retained_return_confirmed", "konomi.return_correspondence_available" },
            "Remote aftercare accepted stale proof without current correspondence evidence.");
        Reject(() => { letter.Remote = false; letter.Owner = "Konomi"; },
            () => { letter.Remote = true; letter.Owner = "Memory"; }, "A physical conversation used the remote correspondence exception.");
        Reject(() => letter.ContactUnit = unit, () => letter.ContactUnit = null,
            "Physical contact metadata accepted correspondence in place of arrival evidence.");
        foreach (string reserved in new[] { "konomi.retained_dead", "konomi.return_contact_available", "konomi.return_correspondence_available", "konomi.retained_return_confirmed" })
        {
            Reject(() => ordinary.Id = reserved, () => ordinary.Id = "konomi.ordinary_fixture", "Scene completion manufactured reserved evidence: " + reserved);
            Reject(() => story.Relationships["konomi"].StartedFlag = reserved, () => story.Relationships["konomi"].StartedFlag = "konomi.started",
                "Journal entry manufactured reserved evidence: " + reserved);
            Reject(() => story.CompletedQuests[reserved] = unit, () => story.CompletedQuests.Remove(reserved),
                "Quest history aliased reserved evidence: " + reserved);
            Reject(() => story.SeenCues[reserved] = new[] { unit }, () => story.SeenCues.Remove(reserved),
                "Dialogue history aliased reserved evidence: " + reserved);
        }
        Reject(() => attempt.Nodes[0].Choices.Add(new Choice { Revive = "konomi", Set = new[] { "konomi.retained_return_confirmed" } }),
            () => attempt.Nodes[0].Choices.RemoveAt(1), "Ambiguous identical saved request choices were accepted.");
        state.Area = capital;
        state.Flags.Add("konomi.retained_dead");
        check(!Rules.Available(story, letter, state) && !Rules.ContactAvailable(story, letter, state),
            "A later death failed to stop return correspondence.");
        check(!Rules.Available(story, ordinary, state) && !Rules.Available(story, after, state), "A later retained death was ignored after verified recovery.");
        check(!Rules.Available(story, attempt, state), "A later death without recovery eligibility reused an old request.");
        var options = new JsonSerializerOptions { IncludeFields = true };
        var restored = JsonSerializer.Deserialize<Story>(JsonSerializer.Serialize(story, options), options)!;
        Rules.Validate(restored);
        check(restored.Scenes[1].AfterRecovery == "konomi", "Aftercare scope was lost through JSON serialization.");
    }
}
