using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using HarmonyLib;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Root.Strings;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.Localization;
using Kingmaker.UI.Common;
using Tirabade;

// E15, the RRT book, as the real Build constructs it: mailbag v2 (one portrait page per letter, the paged satchel list,
// the archive link), the read-only archive (no condition, action or effect anywhere in a replay), data books (contents,
// entry pages, tooltip links), live "N of M" titles, portrait keys with the native fallback, and glossary tooltips
// resolving through the native GlossaryHolder.
internal static class BookManagedTests
{
    public static void Run(Story story, Func<string, BlueprintGuid> id, string artFolder, Action<bool, string> check)
    {
        var main = typeof(Main);
        var views = (System.Collections.IDictionary)main.GetField("views", BindingFlags.NonPublic | BindingFlags.Static)!.GetValue(null);
        var pages = (Dictionary<string, Tirabade.Node>)main.GetField("pages", BindingFlags.NonPublic | BindingFlags.Static)!.GetValue(null);
        var letters = story.Scenes.Where(Rules.IsMailbagLetter).ToArray();
        check(views.Contains("mailbag") && views.Contains("archive") && story.Books.Keys.All(k => views.Contains("book." + k)),
            "Book views were not built (mailbag, archive, every data book).");
        object View(string key) => views[key]!;
        List<BlueprintCueBase> Items(string key) => (List<BlueprintCueBase>)View(key).GetType().GetField("ItemPages")!.GetValue(View(key));
        List<BlueprintCueBase> Lists(string key) => (List<BlueprintCueBase>)View(key).GetType().GetField("ListPages")!.GetValue(View(key));
        BlueprintDialog Dialog(string key) => (BlueprintDialog)View(key).GetType().GetField("Dialog")!.GetValue(View(key))!;
        BlueprintAnswer A(BlueprintAnswerBaseReference r) => (BlueprintAnswer)r.Get();

        // Mailbag v2: one page per letter, each gated on the cursor being on it, first answer breaks the seal (starts the
        // letter, brings the satchel back), then next / previous / the whole satchel / letters already read / later.
        var mail = Items("mailbag").Cast<BlueprintBookPage>().ToList();
        check(mail.Count == letters.Length && Dialog("mailbag").Type.ToString() == "Book"
            && Dialog("mailbag").FirstCue.Cues.Select(c => c.Guid).SequenceEqual(mail.Select(p => p.AssetGuid)), "Mailbag v2 pages or dialog are wrong.");
        for (int i = 0; i < letters.Length; i++)
        {
            var page = mail[i];
            check(page.Conditions.Conditions.Single() is Main.ViewCondition vc && vc.View == "mailbag" && vc.Mode == "item" && vc.Item == letters[i].Id,
                "A mailbag page is not gated on the cursor: " + letters[i].Id);
            var read = A(page.Answers[0]);
            check(read.ShowConditions.Conditions.Single() is Main.MailbagCondition mc && mc.Scene == letters[i]
                && read.OnSelect.Actions[0] is Main.RouteAction start && start.Start == letters[i]
                && read.OnSelect.Actions[1] is Main.MailbagAction back && back.Reopen, "Break the seal does not read its own letter: " + letters[i].Id);
            check(page.Answers.Count == 6, "A mailbag page does not offer read, next, previous, the satchel, letters read and later: " + letters[i].Id);
            var node = pages[page.AssetGuid.ToString()];
            string expected = !string.IsNullOrEmpty(letters[i].Nodes[0].Portrait) ? letters[i].Nodes[0].Portrait : letters[i].Owner;
            check(node.Portrait == expected, "A mailbag page does not show its sender's portrait key: " + letters[i].Id);
        }
        var lists = Lists("mailbag").Cast<BlueprintBookPage>().ToList();
        check(lists.Count == 2 && lists.All(p => p.Answers.Take(8).Select(A).All(a => a.OnSelect.Actions.Single() is Main.ViewAction va && va.Op == "slot")),
            "The satchel list is not two alternating pages of eight slots.");

        // Archive: one kept-letter page per letter; every replay page and replay answer is inert.
        var kept = Items("archive").Cast<BlueprintBookPage>().ToList();
        check(kept.Count == letters.Length, "The archive does not have one page per letter.");
        int replayPages = 0, replayAnswers = 0;
        foreach (var cover in kept)
        {
            var again = A(cover.Answers[0]);
            check(again.OnSelect.Actions.Length == 0 && again.NextCue.Cues.Count == 1, "Read it again is not an inert page turn: " + cover.name);
        }
        // Every node of every letter has a replay page (by its save name), and every replay page and answer is inert.
        foreach (var scene in letters)
            foreach (var node in scene.Nodes)
            {
                var page = ResourcesLibrary.TryGetBlueprint(id("page.replay." + scene.Id + "." + node.Id)) as BlueprintBookPage;
                check(page != null, "A letter node has no replay page: " + scene.Id + "/" + node.Id);
                replayPages++;
                check(page!.Conditions.Conditions.Length == 0 && page.OnShow.Actions.Length == 0
                    && page.Cues.Select(c => (BlueprintCue)c.Get()).All(c => c.OnShow.Actions.Length == 0 && c.OnStop.Actions.Length == 0 && c.Conditions.Conditions.Length == 0),
                    "A replay page has a condition or an action: " + page.name);
                check(page.Answers.Count >= 1, "A replay page cannot be left: " + page.name);
                foreach (var answer in page.Answers.Select(A))
                {
                    replayAnswers++;
                    check(answer.OnSelect.Actions.Length == 0 && answer.ShowConditions.Conditions.Length == 0 && answer.SelectConditions.Conditions.Length == 0
                        && answer.NextCue.Cues.Count == 1, "A replay answer has an effect or a condition: " + answer.name);
                }
            }

        // Data books: a contents page, one page per entry (portrait speaker "Book"), a closing tooltip link where declared.
        foreach (var pair in story.Books)
        {
            var bookPages = Items("book." + pair.Key).Cast<BlueprintBookPage>().ToList();
            var cover = (BlueprintBookPage)Dialog("book." + pair.Key).FirstCue.Cues.Single().Get();
            check(bookPages.Count == pair.Value.Entries.Count && cover.Answers.Count == pair.Value.Sections.Length + 1,
                "A data book does not have a contents page and one page per entry: " + pair.Key);
            for (int i = 0; i < bookPages.Count; i++)
            {
                var entry = pair.Value.Entries[i];
                var cues = bookPages[i].Cues.Select(c => (BlueprintCue)c.Get()).ToList();
                check(cues.Count == 1 + entry.Lines.Count + (entry.Tooltip.Length > 0 ? 1 : 0)
                    && cues.Skip(1).Take(entry.Lines.Count).All(c => c.Conditions.Conditions.Single() is Main.ParagraphCondition),
                    "A book entry's text, conditional lines or tooltip are missing: " + entry.Id);
                if (entry.Tooltip.Length > 0)
                    check(LocalizationManager.CurrentPack.GetText(Key(cues.Last().Text), false).Contains("{g|" + entry.Tooltip + "}"),
                        "A book entry's tooltip line does not link its glossary key: " + entry.Id);
                check(pages[bookPages[i].AssetGuid.ToString()].Speaker == "Book", "A book page would show the narrator's default picture: " + entry.Id);
            }
        }

        // Live titles: an updater writes "N of M" before the page binds (no game here, so empty lists).
        main.GetMethod("UpdatePage", BindingFlags.NonPublic | BindingFlags.Static)!.Invoke(null, new object[] { lists[0].AssetGuid.ToString() });
        check(LocalizationManager.CurrentPack.GetText(Key(lists[0].Title), false) == "The satchel (1 of 1)", "The satchel list title is not live.");

        // Portraits: keys with art resolve to a file; keys without art resolve to nothing, and the page keeps the native picture.
        var withArt = letters.Select(l => pages[mail[Array.IndexOf(letters, l)].AssetGuid.ToString()].Portrait).Distinct().ToList();
        // A key is covered by its own file, a native portrait fallback (resolved in game), or an alias to a shipped file.
        bool Covered(string key) => File.Exists(Path.Combine(artFolder, key + ".png"))
            || story.PortraitFallbacks.TryGetValue(key, out var target)
               && (target.Length == 32 || File.Exists(Path.Combine(artFolder, target + ".png")));
        int resolved = withArt.Count(Covered);
        check(resolved > 0, "No letter sender resolves to portrait art.");
        Console.WriteLine("Book portraits: " + resolved + " of " + withArt.Count + " letter senders have art (own file, native portrait or alias); the rest keep the native book picture ("
            + string.Join(", ", withArt.Where(key => !Covered(key)).Take(12)) + (withArt.Count - resolved > 12 ? ", ..." : "") + ").");

        // Glossary: every RRT entry joins the native glossary and resolves through GlossaryHolder.GetEntry.
        var entries = (IReadOnlyList<GlossaryEntry>)main.GetProperty("GlossaryEntries", BindingFlags.NonPublic | BindingFlags.Static)!.GetValue(null);
        check(entries.Count == story.Glossary.Count, "Not every glossary entry was built.");
        AccessTools.Field(typeof(GlossaryHolder), "s_EntriesbyKey").SetValue(null, new Dictionary<string, GlossaryEntry>());
        AccessTools.Field(typeof(GlossaryHolder), "s_Initialized").SetValue(null, true);
        int injected = (int)main.GetMethod("InjectGlossary", BindingFlags.NonPublic | BindingFlags.Static)!.Invoke(null, null);
        check(injected == story.Glossary.Count && story.Glossary.All(p => GlossaryHolder.GetEntry(p.Key) is GlossaryEntry g
            && LocalizationManager.CurrentPack.GetText(Key(g.Name), false) == p.Value.Name
            && LocalizationManager.CurrentPack.GetText(Key(g.Description), false) == p.Value.Description),
            "A glossary entry does not resolve through the native glossary.");
        Console.WriteLine("PASS: E15 book (" + mail.Count + " mailbag pages, " + kept.Count + " kept letters, " + replayPages + " inert replay pages, "
            + story.Books.Count + " data book(s), " + entries.Count + " glossary tooltips, live titles).");
    }

    private static string Key(LocalizedString text) => (string)AccessTools.Field(typeof(LocalizedString), "m_Key").GetValue(text);
}
