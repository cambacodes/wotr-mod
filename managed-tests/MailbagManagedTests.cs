using System;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Xml.Serialization;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Tirabade;

// E8b: the mailbag dialog built by the real Build (one Book page: an entry per rest letter, gated on that letter being in the bag
// and available, starting it and bringing the list back; "Read the rest later" last), and old settings files default to it.
internal static class MailbagManagedTests
{
    public static void Run(Story story, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        var main = typeof(Main);
        var dialog = (BlueprintDialog?)main.GetField("mailbagDialog", BindingFlags.NonPublic | BindingFlags.Static)!.GetValue(null);
        var letters = story.Scenes.Where(Rules.IsMailbagLetter).ToArray();
        check(letters.Length > 0 && dialog != null, "Mailbag dialog was not built although the story has rest letters.");
        var page = (BlueprintBookPage)dialog!.FirstCue.Cues.Single().Get();
        check(dialog.Type.ToString() == "Book" && page.AssetGuid == id("page.mailbag") && dialog.AssetGuid == id("dialog.mailbag"),
            "Mailbag dialog/page identity wrong.");
        check(page.Answers.Select(a => a.Guid).SequenceEqual(letters.Select(s => id("answer.mailbag." + s.Id)).Concat(new[] { id("answer.mailbag.later") })),
            "Mailbag answers: one per rest letter in story order, then 'later'.");
        for (int i = 0; i < letters.Length; i++)
        {
            var answer = (BlueprintAnswer)page.Answers[i].Get();
            var scene = letters[i];
            check(answer.ShowConditions.Conditions.Single() is Main.MailbagCondition shown && shown.Scene == scene
                && answer.SelectConditions.Conditions.Single() is Main.MailbagCondition selected && selected.Scene == scene,
                "Mailbag entry is not gated on its own letter: " + scene.Id);
            check(answer.OnSelect.Actions.Length == 2 && answer.OnSelect.Actions[0] is Main.RouteAction start && start.Start == scene
                && answer.OnSelect.Actions[1] is Main.MailbagAction back && back.Reopen, "Mailbag entry does not start its letter and return: " + scene.Id);
        }
        var later = (BlueprintAnswer)page.Answers.Last().Get();
        check(later.OnSelect.Actions.Single() is Main.MailbagAction close && !close.Reopen, "'Read the rest later' does not close the mailbag.");
        check(!letters.Any(s => s.ManualOnly || s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)), "Manual reads or epilogue pages listed in the mailbag.");
        var label = (string)main.GetMethod("MailbagLabel", BindingFlags.NonPublic | BindingFlags.Static)!.Invoke(null, new object[] { letters[0] })!;
        check(label.StartsWith(letters[0].Owner == "Memory" ? "[A memory] " : "[Letter from " + letters[0].Owner + "] ", StringComparison.Ordinal),
            "Mailbag label format changed.");

        // Settings written before E8b have no Mailbag element; they load with the mailbag on and the old bag size kept.
        var old = "<?xml version=\"1.0\"?><Settings xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">"
            + "<Narration>false</Narration><PostBagSize>2</PostBagSize></Settings>";
        var loaded = (Settings)new XmlSerializer(typeof(Settings)).Deserialize(new StringReader(old))!;
        check(loaded.Mailbag && loaded.PostBagSize == 2 && !loaded.Narration, "An old settings file does not load with the mailbag on.");
        check(new Settings().Mailbag, "The mailbag is not the default delivery.");
        // Nothing the mailbag holds is saved: its state is a plain runtime list.
        check(typeof(Mailbag).GetFields().All(f => !f.GetCustomAttributes(true).Any(a => a.GetType().Name == "JsonPropertyAttribute")),
            "Mailbag state became serialized.");
        Console.WriteLine("PASS: E8b mailbag dialog built (" + letters.Length + " letter entries gated per letter, 'later' last); old settings default to the mailbag.");
    }
}
