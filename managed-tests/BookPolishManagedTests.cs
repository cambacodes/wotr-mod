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
        string FirstCue(BlueprintBookPage p) => LocalizationManager.CurrentPack.GetText(Key(((BlueprintCue)p.Cues[0].Get()).Text), false);
        var isLetter = polish.GetMethod("IsLetterPage", BindingFlags.NonPublic | BindingFlags.Static)!;
        bool IsLetter(BlueprintBookPage p) => (bool)isLetter.Invoke(null, new object[] { p.AssetGuid.ToString() })!;
        var lp = Page(letter!); var vp = Page(visit!); var sp = Page(sending!); var pp = Page(person!);
        string expected = (letter!.Parcel ? "A parcel from " : "Letter from ") + Rules.SenderOf(letter);
        check(Title(lp).StartsWith(expected, StringComparison.Ordinal) && IsLetter(lp) && FirstCue(lp).Contains(expected),
            "E15c letter page is not headed, flagged and introduced as a letter: " + letter.Id + " first cue '" + FirstCue(lp) + "'.");
        check(!IsLetter(vp) && Title(vp) == visit!.Title && !FirstCue(vp).Contains("Letter from"),
            "E15c a remote visit is styled as a letter: " + visit!.Id + ".");
        check(!IsLetter(sp) && FirstCue(sp).Contains("A sending from " + Rules.SenderOf(sending!)),
            "E15c a sending is not introduced as one: " + sending!.Id + ".");
        check(Title(pp) == person!.Title && !IsLetter(pp), "E15b in-person page changed title or was styled as a letter: " + person.Id + ".");
        var kindOf = polish.GetMethod("PageKind", BindingFlags.NonPublic | BindingFlags.Static)!;
        var vigil = story.Scenes.FirstOrDefault(s => s.Id == "trickster.lastcall.bottle.alone");
        if (vigil != null)
            check((string)kindOf.Invoke(null, new object[] { Page(vigil).AssetGuid.ToString() })! == "event" && !IsLetter(Page(vigil)),
                "E15c the Commander's Last Call vigil is not an event page (it must show no partner portrait).");
        check(Math.Abs(Call<float>("ShortViewportHeight", 100f, 30f) - 150f) < 1e-3, "E15c short viewport height is not whole lines plus one.");
        var prefix = typeof(Main).GetMethod("MailbagPrefix", BindingFlags.NonPublic | BindingFlags.Static)!;
        string Prefix(Scene s) => (string)prefix.Invoke(null, new object[] { s })!;
        check(Prefix(new Scene { Owner = "Seelah", Remote = true, Kind = "visit" }) == "[Seelah asks to see you] "
            && Prefix(new Scene { Owner = "Memory", Remote = true, Kind = "sending", Sender = "Vellexia" }) == "[A sending from Vellexia] "
            && Prefix(new Scene { Owner = "Konomi", Remote = true, Kind = "letter" }) == "[Letter from Konomi] "
            && Prefix(new Scene { Owner = "Commander", Remote = true, Kind = "event" }) == "", "E15c mailbag labels by kind are wrong.");
        var counts = story.Scenes.Where(s => Rules.IsRemote(s) && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal))
            .GroupBy(Rules.KindOf).OrderBy(g => g.Key).Select(g => g.Key + " " + g.Count());
        Console.WriteLine("PASS: E15b/c book polish (overlay <= 15%, short-page viewport, speaker captions, remote scenes by kind: "
            + string.Join(", ", counts) + "; event pages portrait-free; native pages untouched).");
    }
}
