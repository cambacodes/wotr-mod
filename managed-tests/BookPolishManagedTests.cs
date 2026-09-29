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

        // Letters vs in-person pages, as built.
        var letter = story.Scenes.FirstOrDefault(s => Rules.IsRemote(s) && s.NativeReturnCue == null && s.Owner != "Memory"
            && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal) && s.Nodes.Count > 0);
        var person = story.Scenes.FirstOrDefault(s => !Rules.IsRemote(s) && s.NativeReturnCue == null
            && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal) && s.Nodes.Count > 0 && s.Title.Length > 0);
        check(letter != null && person != null, "E15b test fixture: no remote or in-person scene found.");
        BlueprintBookPage Page(Scene s) => (BlueprintBookPage)ResourcesLibrary.TryGetBlueprint(id("page." + s.Id + "." + s.Nodes[0].Id))!;
        string Title(BlueprintBookPage p) => LocalizationManager.CurrentPack.GetText((string)AccessTools.Field(typeof(LocalizedString), "m_Key").GetValue(p.Title), false);
        var isLetter = polish.GetMethod("IsLetterPage", BindingFlags.NonPublic | BindingFlags.Static)!;
        var lp = Page(letter!); var pp = Page(person!);
        string expected = (letter!.Parcel ? "A parcel from " : "Letter from ") + (letter.Owner == "Together" ? "Anevia and Irabeth" : letter.Owner);
        check(Title(lp).StartsWith(expected, StringComparison.Ordinal) && (bool)isLetter.Invoke(null, new object[] { lp.AssetGuid.ToString() })!,
            "E15b remote page is not headed and flagged as a letter: " + letter.Id + " title '" + Title(lp) + "'.");
        check(Title(pp) == person!.Title && !(bool)isLetter.Invoke(null, new object[] { pp.AssetGuid.ToString() })!,
            "E15b in-person page changed title or was styled as a letter: " + person.Id + ".");
        int letters = story.Scenes.Count(s => Rules.IsRemote(s) && s.NativeReturnCue == null && s.Owner != "Memory" && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal));
        Console.WriteLine("PASS: E15b book polish (overlay <= 15%, short-page answers, speaker captions, " + letters + " remote scenes styled as letters; native pages untouched).");
    }
}
