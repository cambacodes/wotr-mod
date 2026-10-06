using System;
using System.Linq;
using System.Reflection;
using HarmonyLib;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.Localization;
using Tirabade;

// E15b, book-page polish for RRT pages only: the patch targets exist on the real BookEvent view, the decisions (overlay
// alpha, short page, speaker caption, letter header) are the specified ones, a native page is never treated as ours, and a
// remote scene's page is headed and flagged as correspondence while an in-person page keeps its own title.
internal static class BookPolishManagedTests
{
    public static void Run(Story story, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        var polish = typeof(Main).GetNestedType("BookPolish", BindingFlags.NonPublic)!;
        check(polish != null, "E15b BookPolish is missing.");
        var viewType = (Type)polish!.GetField("ViewType", BindingFlags.NonPublic | BindingFlags.Static)!.GetValue(null)!;
        check(AccessTools.Method(viewType, "SetPicture") != null && AccessTools.Method(viewType, "OnContentChanged") != null,
            "E15b patch targets (BookEventView.SetPicture / OnContentChanged) do not resolve.");
        foreach (var field in new[] { "PictureField", "CuesLayoutField", "CueViewField" })
            check(polish.GetField(field, BindingFlags.NonPublic | BindingFlags.Static)!.GetValue(null) != null, "E15b view field not found: " + field);

        T Call<T>(string name, params object?[] args) => (T)polish.GetMethod(name, BindingFlags.NonPublic | BindingFlags.Static)!.Invoke(null, args)!;
        check(Math.Abs(Call<float>("OverlayAlpha", 0.45f) - 0.15f) < 1e-6 && Math.Abs(Call<float>("OverlayAlpha", 0.1f) - 0.1f) < 1e-6,
            "E15b overlay alpha is not min(native, 0.15).");
        check(Call<bool>("IsShortPage", new object?[] { new[] { new string('x', 480) } })
            && !Call<bool>("IsShortPage", new object?[] { new[] { new string('x', 500), new string('x', 400) } }), "E15b short-page threshold is wrong.");
        check(Call<string?>("CaptionFor", "Ember", "Chadali") == "Ember" && Call<string?>("CaptionFor", "Chadali", "Chadali") == null
            && Call<string?>("CaptionFor", "Narrator", "Chadali") == null && Call<string?>("CaptionFor", "Together", "Anevia") == null
            && Call<string?>("CaptionFor", "Ember", null) == null, "E15b speaker caption rule is wrong.");

        // A native page (not built by RRT) is never polished.
        var native = new BlueprintBookPage { AssetGuid = BlueprintGuid.Parse("00000000000000000000000000000abc") };
        var isRrt = polish.GetMethod("IsRrtPage", BindingFlags.NonPublic | BindingFlags.Static)!;
        var args = new object?[] { native, null, null };
        check(!(bool)isRrt.Invoke(null, args)!, "E15b treats a native book page as an RRT page.");

        // E15c: letters vs visits vs sendings vs events, as built.
        var letter = story.Scenes.FirstOrDefault(s => Rules.KindOf(s) == "letter" && s.NativeReturnCue == null && s.Nodes.Count > 0);
        var visit = story.Scenes.FirstOrDefault(s => Rules.IsRemote(s) && Rules.KindOf(s) == "visit" && s.NativeReturnCue == null && s.Nodes.Count > 0
            && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal));
        var sending = story.Scenes.FirstOrDefault(s => Rules.KindOf(s) == "sending" && s.NativeReturnCue == null && s.Nodes.Count > 0);
        var person = story.Scenes.FirstOrDefault(s => !Rules.IsRemote(s) && s.NativeReturnCue == null
            && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal) && s.Nodes.Count > 0 && s.Title.Length > 0);
        check(letter != null && visit != null && sending != null && person != null, "E15c test fixture: a letter, a remote visit, a sending or an in-person scene is missing.");
        BlueprintBookPage Page(Scene s) => (BlueprintBookPage)ResourcesLibrary.TryGetBlueprint(id("page." + s.Id + "." + s.Nodes[0].Id))!;
        string Key(LocalizedString text) => (string)AccessTools.Field(typeof(LocalizedString), "m_Key").GetValue(text);
        string Title(BlueprintBookPage p) => LocalizationManager.CurrentPack.GetText(Key(p.Title), false);
        var isLetter = polish.GetMethod("IsLetterPage", BindingFlags.NonPublic | BindingFlags.Static)!;
        bool IsLetter(BlueprintBookPage p) => (bool)isLetter.Invoke(null, new object[] { p.AssetGuid.ToString() })!;
        var lp = Page(letter!); var vp = Page(visit!); var sp = Page(sending!); var pp = Page(person!);
        var kindOf = polish.GetMethod("PageKind", BindingFlags.NonPublic | BindingFlags.Static)!;
        string Kind(BlueprintBookPage p) => (string)kindOf.Invoke(null, new object[] { p.AssetGuid.ToString() })!;
        bool FirstCueIs(BlueprintBookPage p, Scene scene, bool header) => p.Cues[0].Get().AssetGuid
            == id("cue." + scene.Id + "." + scene.Nodes[0].Id + (header ? ".kind" : ""));
        foreach (var scene in new[] { letter!, visit!, sending!, person! })
        {
            var page = Page(scene);
            check(Key(page.Title) == "RRT.title." + scene.Id + "." + scene.Nodes[0].Id
                && !string.IsNullOrWhiteSpace(Title(page)), "E15c missing page title localization: " + scene.Id);
        }
        check(IsLetter(lp) && Kind(lp) == "letter" && FirstCueIs(lp, letter!, true),
            "E15c letter metadata/header cue missing: " + letter!.Id);
        check(!IsLetter(vp) && Kind(vp) == "visit" && FirstCueIs(vp, visit!, false),
            "E15c remote visit metadata/header cue wrong: " + visit!.Id);
        check(!IsLetter(sp) && Kind(sp) == "sending" && FirstCueIs(sp, sending!, true),
            "E15c sending metadata/header cue missing: " + sending!.Id);
        check(!IsLetter(pp) && FirstCueIs(pp, person!, false), "E15b in-person page gained a correspondence header: " + person!.Id);
        var vigil = story.Scenes.FirstOrDefault(s => s.Id == "trickster.lastcall.bottle.alone");
        if (vigil != null)
            check((string)kindOf.Invoke(null, new object[] { Page(vigil).AssetGuid.ToString() })! == "event" && !IsLetter(Page(vigil)),
                "E15c the Commander's Last Call vigil is not an event page (it must show no partner portrait).");
        check(Math.Abs(Call<float>("ShortViewportHeight", 100f, 30f) - 150f) < 1e-3, "E15c short viewport height is not whole lines plus one.");
        var prefix = typeof(Main).GetMethod("MailbagPrefix", BindingFlags.NonPublic | BindingFlags.Static)!;
        string Prefix(Scene s) => (string)prefix.Invoke(null, new object[] { s })!;
        var visitLabel = new Scene { Owner = "owner.fixture", Remote = true, Kind = "visit" };
        var sendingLabel = new Scene { Owner = "owner.fixture", Remote = true, Kind = "sending", Sender = "sender.fixture" };
        var letterLabel = new Scene { Owner = "owner.fixture", Remote = true, Kind = "letter" };
        check(Prefix(visitLabel).Contains(visitLabel.Owner)
            && Prefix(sendingLabel).Contains(sendingLabel.Sender!) && !Prefix(sendingLabel).Contains(sendingLabel.Owner)
            && Prefix(letterLabel).Contains(letterLabel.Owner)
            && Prefix(new Scene { Owner = "owner.fixture", Remote = true, Kind = "event" }).Length == 0,
            "E15c correspondence sender identity/prefix presence by kind is wrong.");
        foreach (string kind in new[] { "visit", "event" })
            check(Call<string>("PageTitle", new Scene { Owner = "owner.fixture", Title = "title.fixture", Kind = kind }) == "title.fixture",
                "E15b ordinary page lost its supplied title identity: " + kind);
        var counts = story.Scenes.Where(s => Rules.IsRemote(s) && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal))
            .GroupBy(Rules.KindOf).OrderBy(g => g.Key).Select(g => g.Key + " " + g.Count());
        Console.WriteLine("PASS: E15b/c book polish (overlay <= 15%, short-page viewport, speaker captions, remote scenes by kind: "
            + string.Join(", ", counts) + "; event pages portrait-free; native pages untouched).");
    }
}
