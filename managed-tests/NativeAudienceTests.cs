using System;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Tirabade;

internal static class NativeAudienceTests
{
    private const BindingFlags Members = BindingFlags.Static | BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;

    // Inspect Main.Build's registered graph. This does not execute Unity's dialog lifecycle.
    internal static void Run(Story story, Action<bool, string> check)
    {
        var scenes = story.Scenes.Where(scene => scene.NativeReturnCue != null).ToArray();
        if (scenes.Length == 0) return;
        var guidFor = typeof(Main).GetMethod("GuidFor", Members)!;
        BlueprintGuid Id(string key) => (BlueprintGuid)guidFor.Invoke(null, new object[] { key })!;
        SimpleBlueprint? Find(string key) => ResourcesLibrary.TryGetBlueprint(Id(key));
        int terminals = 0;

        foreach (var scene in scenes)
        {
            var native = ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(scene.NativeReturnCue!)) as BlueprintCue;
            check(native != null, "Native audience return does not resolve to a basic cue: " + scene.Id);
            var entry = Find("entry." + scene.Id) as BlueprintAnswer;
            check(entry != null, "Native audience entry is missing: " + scene.Id);
            check(entry!.OnSelect.Actions.Length == 0,
                "Inline audience entry must not queue a book or auto-write the relationship StartedFlag: " + scene.Id);
            check(entry.NextCue.Cues.Count == 1
                && ReferenceEquals(entry.NextCue.Cues[0].Get(), Find("cue." + scene.Id + "." + scene.Nodes[0].Id)),
                "Inline entry does not lead directly to Nodes[0]: " + scene.Id);
            check(entry.ShowConditions.Conditions.Length == 1
                && entry.ShowConditions.Conditions[0] is Main.RouteCondition visible
                && ReferenceEquals(visible.Scene, scene)
                && entry.SelectConditions.Conditions.Length == 1
                && entry.SelectConditions.Conditions[0] is Main.RouteCondition selectable
                && ReferenceEquals(selectable.Scene, scene),
                "Inline entry lost its display or selection availability guard: " + scene.Id);
            check(Find("dialog." + scene.Id) == null,
                "Inline scene unexpectedly registered a replacement book dialog: " + scene.Id);
            foreach (string target in Rules.EntryTargets(scene))
            {
                var list = ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(target)) as BlueprintAnswersList;
                check(list != null && list.Answers.Count(reference => ReferenceEquals(reference.Get(), entry)) == 1,
                    "Inline entry is absent or duplicated in its native answer list: " + scene.Id);
            }

            foreach (var node in scene.Nodes)
            {
                string key = scene.Id + "." + node.Id;
                var cue = Find("cue." + key) as BlueprintCue;
                check(cue != null, "Inline node is not a registered concrete BlueprintCue: " + key);
                check(Find("page." + key) == null, "Inline node also registered a book page: " + key);
                check(!cue!.ShowOnce && cue.Conditions.Conditions.Length == 0,
                    "Inline cue could disappear on return or after a terminal flag write: " + key);
                check(cue.Continue.Cues.Count == 0,
                    "Inline cue Continue would override its authored answers: " + key);
                check(cue.OnShow.Actions.Length == 0 && cue.OnStop.Actions.Length == 0,
                    "Inline node writes progress or starts another dialog outside a selected choice: " + key);
                check(cue.Answers.Count == node.Choices.Count,
                    "Inline cue changed the authored choice count: " + key);
                if (node.Speaker == scene.Owner)
                    check(ReferenceEquals(cue.Speaker, native!.Speaker), "Owner cue lost the native audience speaker: " + key);
                else
                    check(cue.Speaker.NoSpeaker && !cue.Speaker.MoveCamera,
                        "Non-owner prose is incorrectly voiced by the native NPC: " + key);

                for (int i = 0; i < node.Choices.Count; i++)
                {
                    var choice = node.Choices[i];
                    string answerKey = "answer." + key + "." + i;
                    var answer = Find(answerKey) as BlueprintAnswer;
                    check(answer != null && ReferenceEquals(cue.Answers[i].Get(), answer),
                        "Inline choice ID or ordering changed: " + answerKey);
                    // E5/E11: the only actions after the RouteAction are the choice's own native effects (the mythic-choice
                    // counter, a crusade resource change, an item removal), each present only when authored.
                    var effects = answer!.OnSelect.Actions.Skip(1).ToArray();
                    check(answer.OnSelect.Actions.Length >= 1 && answer.OnSelect.Actions[0] is Main.RouteAction
                        && effects.Count(a => a is Kingmaker.Kingdom.Blueprints.AddCrusadeResources || a is Kingmaker.Kingdom.Blueprints.RemoveCrusadeResources) == (choice.Crusade != null ? 1 : 0)
                        && effects.All(a => a is Kingmaker.Kingdom.Blueprints.AddCrusadeResources || a is Kingmaker.Kingdom.Blueprints.RemoveCrusadeResources
                            || a is Kingmaker.Designers.EventConditionActionSystem.Actions.RemoveItemFromPlayer && choice.RemoveItem != null
                            || a is Kingmaker.Designers.EventConditionActionSystem.Actions.IncrementFlagValue && choice.Mythic != null),
                        "Inline choice lost its sole authored RouteAction: " + answerKey);
                    var action = (Main.RouteAction)answer.OnSelect.Actions[0];
                    bool terminal = choice.Next == null && choice.Check == null;
                    check(action.Start == null && ReferenceEquals(action.Choice, choice)
                        && ReferenceEquals(action.Owner, answer),
                        "Inline choice queues a dialog or substitutes authored flag writes: " + answerKey);
                    check(ReferenceEquals(action.Complete, terminal && !choice.Abort ? scene : null),
                        "Inline choice records completion on an internal or aborted transition: " + answerKey);
                    check(answer.ShowConditions.Conditions.Length == 1
                        && answer.ShowConditions.Conditions[0] is Main.RouteCondition shown
                        && ReferenceEquals(shown.Choice, choice)
                        && answer.SelectConditions.Conditions.Length == 1
                        && answer.SelectConditions.Conditions[0] is Main.RouteCondition selected
                        && ReferenceEquals(selected.Choice, choice),
                        "Inline choice lost authored availability guards: " + answerKey);
                    check(answer.NextCue.Cues.Count == 1, "Inline choice can stop the native audience: " + answerKey);
                    var destination = answer.NextCue.Cues[0].Get();
                    if (terminal)
                    {
                        terminals++;
                        // E5: a terminal native_next continues into that native cue of the same dialog instead.
                        var expected = choice.NativeNext != null && choice.Check == null
                            ? ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(choice.NativeNext)) : native;
                        check(expected != null && ReferenceEquals(destination, expected),
                            "Terminal, refusal or abort does not return to the original native cue: " + answerKey);
                    }
                    else if (choice.Next != null)
                        check(ReferenceEquals(destination, Find("cue." + scene.Id + "." + choice.Next)),
                            "Inline choice points outside its authored local cue graph: " + answerKey);
                    else
                    {
                        var roll = destination as BlueprintCheck;
                        check(roll != null && roll.DC == choice.Check!.DC,
                            "Inline skill check is missing or has the wrong difficulty: " + answerKey);
                        foreach (var branch in new[] { ("m_Success", choice.Check!.Success), ("m_Fail", choice.Check.Failure) })
                        {
                            var reference = (BlueprintCueBaseReference)typeof(BlueprintCheck).GetField(branch.Item1, Members)!.GetValue(roll)!;
                            check(ReferenceEquals(reference.Get(), Find("cue." + scene.Id + "." + branch.Item2)),
                                "Inline skill-check outcome does not lead to its authored cue: " + answerKey);
                        }
                    }
                }
            }

            // These exact invariants come from the native archive, not a generic rule for return cues.
            if (scene.NativeReturnCue == "20451daada07f744b9d7f3e14a37a864")
            {
                check(!native!.ShowOnce && native.Conditions.Conditions.Length == 0
                    && native.OnShow.Actions.Length == 0 && native.OnStop.Actions.Length == 0
                    && native.Continue.Cues.Count == 0,
                    "Nocticula's native return cue gained side effects or lost repeatability");
                check(native.Answers.Count == 1
                    && native.Answers[0].Get().AssetGuid == BlueprintGuid.Parse("2729c49e2bf20c64caa4f54b352e03f6"),
                    "Nocticula return no longer exposes the original native audience answers");
            }
        }
        check(terminals > 0, "Native audience test fixture exercised no terminal return edges");
        Console.WriteLine("Native audience compiled graph: " + scenes.Length + " scenes, " + terminals + " terminal return edges checked; Unity lifecycle not executed.");
    }
}
