using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Tirabade;

internal static class NurahHubTests
{
    private const string NurahUnit = "f999fc37ddb225640b7f98c0a05d6948";

    private static string? VisitRequest(Func<string, int> read, int hour) => (string?)typeof(Main)
        .GetMethod("NurahVisitRequest", BindingFlags.NonPublic | BindingFlags.Static)!
        .Invoke(null, new object[] { read, hour });

    private static string RetryKey => (string)typeof(Main)
        .GetField("NurahMeetingRetry", BindingFlags.NonPublic | BindingFlags.Static)!.GetRawConstantValue()!;

    private static void Reject(Scene scene, Action<bool, string> check, string label)
    {
        try { Rules.EntryTargets(scene); }
        catch (InvalidOperationException) { check(true, label); return; }
        check(false, label);
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        var scenes = story.Scenes.Where(scene => scene.Relationship == "nurah").ToArray();
        var physical = scenes.Where(scene => !Rules.IsRemote(scene)).ToArray();
        var remote = scenes.Where(Rules.IsRemote).ToArray();
        check(scenes.Length == 13 && physical.Length == 11 && remote.Length == 2,
            "Nurah route no longer has the reviewed remote introduction and physical continuation split");
        check(physical.All(scene => Rules.IsNurahHubScene(scene) && Rules.EntryTargets(scene).Length == 0),
            "Physical Nurah scenes do not use the reviewed authored hub contract");
        check(physical.All(scene => scene.Requires.Contains("nurah.meeting_accepted")
            && scene.Requires.Contains("nurah.meeting_arrived") && scene.ContactUnit == NurahUnit),
            "Physical Nurah scene escaped accepted-arrival and retained-contact gates");
        check(remote.All(scene => scene.InteractionHub == null && scene.ContactUnit == null
            && Rules.EntryTargets(scene).Length == 0), "Nurah correspondence acquired a physical interaction hub");

        var source = physical[0];
        Scene Copy() => new Scene { Id = source.Id, Owner = source.Owner, Relationship = source.Relationship,
            InteractionHub = source.InteractionHub, ContactUnit = source.ContactUnit, Areas = source.Areas,
            Chapters = source.Chapters, Requires = source.Requires, AnswerLists = source.AnswerLists };
        var wrongUnit = Copy(); wrongUnit.ContactUnit = "00000000000000000000000000000001";
        check(!Rules.IsNurahHubScene(wrongUnit), "Wrong unit was accepted as Nurah's authored hub target");
        var wrongChapter = Copy(); wrongChapter.Chapters = new[] { 4 };
        check(!Rules.IsNurahHubScene(wrongChapter), "Wrong chapter was accepted as Nurah's authored hub target");
        var missingArrival = Copy(); missingArrival.Requires = missingArrival.Requires.Where(flag => flag != "nurah.meeting_arrived").ToArray();
        check(!Rules.IsNurahHubScene(missingArrival), "Unarrived Nurah scene was accepted by authored hub contract");
        var mixed = Copy(); mixed.AnswerLists = new[] { "00000000000000000000000000000002" };
        Reject(mixed, check, "Physical Nurah scene silently accepted an unrelated native answer list");
        var unregistered = Copy(); unregistered.InteractionHub = "other.hub";
        Reject(unregistered, check, "Unrecognized interaction hub was accepted");

        var values = new Dictionary<string, int>();
        int Read(string key) => values.TryGetValue(key, out var value) ? value : 0;
        values["nurah.meeting_accepted"] = 1;
        values["hour.nurah.meeting_accepted"] = 100;
        check(VisitRequest(Read, 110) == null, "Nurah appointment opened before the twelve-hour delay");
        check(VisitRequest(Read, 111) == "nurah.private/0", "Accepted Nurah appointment did not produce the stable first request");
        values[RetryKey] = 3;
        check(VisitRequest(Read, 111) == "nurah.private/3", "Nurah retry did not receive a distinct request identity");
        foreach (var blocker in new[] { "nurah.meeting_declined", "nurah.meeting_withdrawn", "nurah.closed",
            "nurah.complete", "closed", "inhuman" })
        {
            values[blocker] = 1;
            check(VisitRequest(Read, 111) == null, "Nurah appointment ignored blocker " + blocker);
            values[blocker] = 0;
        }
    }
}
