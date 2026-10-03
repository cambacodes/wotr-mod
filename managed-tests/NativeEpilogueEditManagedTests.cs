using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.Localization;
using Kingmaker.ResourceLinks;
using Newtonsoft.Json.Linq;
using Tirabade;

// E14d: the reviewed native cues match their evidence in blueprints.zip, and the edit selects exactly one of
// replacement/original, keeping the native checker and falling back to the native text.
internal static class NativeEpilogueEditManagedTests
{
    // E14d extension: the Tirabade page BookPage_0307 and its four native cues (Cue_0308, Cue_0566, Cue_0310, Cue_0311).
    private const string Cue0311 = "3a3e561c6b05a284d93eb3bff7b712a6";
    private static readonly string[] TirabadePageCues = { "cba964e33d0a0704d847629be452b359", "2d6b09c6508010e49b882741add89dcf",
        "ccd140dbf2603734aa323261c2445bec", Cue0311 };

    public static IEnumerable<string> NativeIds => NativeEpilogueEdit.Reviewed.Keys
        .Concat(NativeEpilogueEdit.Reviewed.Values.Select(e => e.Page)).Concat(NativeEpilogueEdit.Reviewed.Values.Select(e => e.Sequence))
        .Concat(TirabadePageCues).Append(NativeEpilogueEdit.Companions).Distinct();

    private static T Seed<T>(string guid) where T : SimpleBlueprint, new()
    {
        var id = BlueprintGuid.Parse(guid);
        if (ResourcesLibrary.TryGetBlueprint(id) is T prior) return prior;
        var blueprint = new T { AssetGuid = id, name = "NativeFixture_" + guid };
        ResourcesLibrary.BlueprintsCache.AddCachedBlueprint(id, blueprint);
        return blueprint;
    }

    private static BlueprintCueBaseReference Ref(string guid)
    {
        var reference = new BlueprintCueBaseReference();
        typeof(BlueprintReferenceBase).GetField("deserializedGuid", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!
            .SetValue(reference, BlueprintGuid.Parse(guid));
        return reference;
    }

    public static void Run(Dictionary<string, JObject> native, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        string[] Refs(JObject data, string field) => ((JArray)data[field]!).Select(v => ((string)v!).Replace("!bp_", "")).ToArray();
        var sequence = Seed<BlueprintCueSequence>(NativeEpilogueEdit.Companions);
        if (sequence.Cues.Count == 0) sequence.Cues.AddRange(Refs(native[NativeEpilogueEdit.Companions], "Cues").Select(Ref));
        foreach (var pair in NativeEpilogueEdit.Reviewed)
        {
            var data = native[pair.Key];
            var onShow = (JArray)data["OnShow"]!["Actions"]!;
            bool onShowReviewed = pair.Value.Image == null ? onShow.Count == 0
                : onShow.Count == 1 && ((string)onShow[0]["$type"]!).EndsWith(", ChangeBookEventImage", StringComparison.Ordinal)
                    && (string)onShow[0]["m_Image"]!["AssetId"]! == pair.Value.Image;
            check((string)data["Text"]!["m_Key"]! == pair.Value.Key && !(bool)data["ShowOnce"]! && onShowReviewed
                && ((JArray)data["OnStop"]!["Actions"]!).Count == 0 && ((JArray)data["Components"]!).Count == 0
                && ((JArray)data["Answers"]!).Count == 0 && ((JArray)data["Continue"]!["Cues"]!).Count == 0,
                "Reviewed native cue evidence drifted: " + pair.Key);
            check(Refs(native[pair.Value.Page], "Cues").Count(c => c == pair.Key) == 1, "Reviewed cue is not exactly once on its page: " + pair.Key);
            check(Refs(native[pair.Value.Sequence], "Cues").Count(c => c == pair.Value.Page) == 1, "Reviewed page is not once in its sequence: " + pair.Key);
        }
        check(NativeEpilogueEdit.Reviewed.Where(pair => pair.Key != Cue0311).All(pair => pair.Value.DegradeOnRefusal)
              && !NativeEpilogueEdit.Reviewed[Cue0311].DegradeOnRefusal, "E14d refusal policy changed (only Cue_0311 is warning-only).");
        // Attach on the Wenduag cue with fixture objects shaped like the archive.
        const string cueId = "86bf0569a9029ae4b8c9d300a41e5739";
        var evidence = NativeEpilogueEdit.Reviewed[cueId];
        var page = Seed<BlueprintBookPage>(evidence.Page);
        if (page.Cues.Count == 0) page.Cues.AddRange(Refs(native[evidence.Page], "Cues").Select(Ref));
        var original = Seed<BlueprintCue>(cueId);
        // The host cannot run Owlcat's element reporting (Game.Instance needs Unity), so the native checker is the empty AND,
        // which is how these three cues' checkers evaluate once their own etude conditions hold.
        original.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = Array.Empty<Condition>() };
        original.OnShow = new ActionList { Actions = Array.Empty<GameAction>() };
        original.OnStop = new ActionList { Actions = Array.Empty<GameAction>() };
        original.Continue = new Kingmaker.DialogSystem.CueSelection { Cues = new List<BlueprintCueBaseReference>() };
        original.Text = new LocalizedString();
        typeof(LocalizedString).GetField("m_Key", BindingFlags.Instance | BindingFlags.NonPublic)!.SetValue(original.Text, evidence.Key);
        var spec = new NativeEpilogueEditSpec { Page = evidence.Page, Sequence = evidence.Sequence, Key = evidence.Key, Replacement = "wenduag.lastcall.cue0409",
            When = new[] { new[] { "wenduag.committed" } } };
        check(NativeEpilogueEdit.Check(cueId, spec, g => ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(g)), null) == null, "Reviewed evidence refused.");
        check(NativeEpilogueEdit.Check(cueId, new NativeEpilogueEditSpec { Page = evidence.Page, Sequence = evidence.Sequence, Key = "drifted", Replacement = spec.Replacement },
            g => ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(g)), null) != null, "Drifted text key accepted.");
        check(NativeEpilogueEdit.Check(cueId, new NativeEpilogueEditSpec { Page = evidence.Page, Sequence = evidence.Sequence, Key = evidence.Key,
            Replacement = spec.Replacement, When = spec.When, KeepNativeImage = true }, g => ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(g)), null) != null,
            "A kept native image was accepted on a cue without one.");
        var replacement = Seed<BlueprintCue>(id("native-edit." + cueId).ToString());
        bool applies = false;
        var plan = NativeEpilogueEdit.Prepare(cueId, spec, original, page, replacement, () => applies);
        var before = page.Cues.Select(c => c.Guid).ToArray();
        NativeEpilogueEdit.Attach(plan, Ref(replacement.AssetGuid.ToString()), () => applies);
        int at = Array.IndexOf(before, BlueprintGuid.Parse(cueId));
        check(page.Cues[at].Guid == replacement.AssetGuid && page.Cues.Where(c => c.Guid != replacement.AssetGuid).Select(c => c.Guid).SequenceEqual(before),
            "Replacement not inserted right before the native cue, or native members moved.");
        foreach (var condition in replacement.Conditions.Conditions) { condition.Owner = replacement; condition.name = "$Applies$fixture"; replacement.ElementsArray.Add(condition); }
        bool Shows(BlueprintCue cue) => cue.Conditions.Conditions.All(c => c.Check());
        check(Shows(original) && !Shows(replacement), "Without the earned condition the native cue must play alone.");
        applies = true;
        check(!Shows(original) && Shows(replacement), "With the earned condition the replacement must play alone.");
        check(replacement.Conditions.Conditions.Single() is NativeEpilogueEdit.Applies applied && ReferenceEquals(
            typeof(NativeEpilogueEdit.Applies).GetField("Original", BindingFlags.Instance | BindingFlags.NonPublic)!.GetValue(applied), plan.OriginalChecker),
            "The replacement does not carry the native cue's own checker.");
        Console.WriteLine("PASS: E14d reviewed native cues match blueprints.zip; replacement and original are mutually exclusive.");
    }

    private sealed class EtudeFixture : Condition
    {
        internal Func<bool> Holds = null!;
        protected override string GetConditionCaption() => "Native etude status (fixture)";
        protected override bool CheckCondition() => Holds();
    }

    // A native cue as the archive has it, unregistered, with the archive's ChangeBookEventImage. The host cannot run a
    // populated ConditionsChecker (its error reporting needs Game.Instance), so the cue's Owlcat checker is the empty AND and
    // the archive's EtudeStatus checker is returned beside it (Native), read against the fixture's Playing set. A cue plays
    // when both pass: exactly what Applies and ParentEndingGuard do with the native checker they wrap.
    private static BlueprintCue ArchiveCue(string guid, JObject data, Func<string, bool> playing, Action<bool, string> check, out Func<bool> nativeChecker)
    {
        var cue = new BlueprintCue { AssetGuid = BlueprintGuid.Parse(guid), name = "TirabadeFixture_" + guid };
        var conditions = new List<EtudeFixture>();
        check((string)data["Conditions"]!["Operation"]! == "And", "Tirabade native cue checker is not an AND: " + guid);
        foreach (JObject condition in (JArray)data["Conditions"]!["Conditions"]!)
        {
            check(((string)condition["$type"]!).EndsWith(", EtudeStatus", StringComparison.Ordinal) && (bool)condition["Playing"]!
                  && !(bool)condition["Started"]! && !(bool)condition["NotStarted"]! && !(bool)condition["Completed"]!
                  && !(bool)condition["CompletionInProgress"]!, "Tirabade native cue checker is not Playing-only EtudeStatus: " + guid);
            string etude = ((string)condition["m_Etude"]!).Replace("!bp_", "");
            bool not = (bool)condition["Not"]!;
            var fixture = new EtudeFixture { Holds = () => playing(etude) != not, Owner = cue, name = "$EtudeFixture$" + etude };
            conditions.Add(fixture);
        }
        nativeChecker = () => conditions.All(c => c.Holds());
        cue.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = Array.Empty<Condition>() };
        var actions = new List<GameAction>();
        foreach (JObject action in (JArray)data["OnShow"]!["Actions"]!)
        {
            check(((string)action["$type"]!).EndsWith(", ChangeBookEventImage", StringComparison.Ordinal), "Unexpected native OnShow action: " + guid);
            var change = new ChangeBookEventImage { Owner = cue, name = "$ChangeBookEventImage$fixture" };
            typeof(ChangeBookEventImage).GetField("m_Image", BindingFlags.Instance | BindingFlags.NonPublic)!
                .SetValue(change, new SpriteLink { AssetId = (string)action["m_Image"]!["AssetId"]! });
            cue.ElementsArray.Add(change);
            actions.Add(change);
        }
        cue.OnShow = new ActionList { Actions = actions.ToArray() };
        cue.OnStop = new ActionList { Actions = Array.Empty<GameAction>() };
        cue.Continue = new Kingmaker.DialogSystem.CueSelection { Cues = new List<BlueprintCueBaseReference>() };
        cue.ShowOnce = (bool)data["ShowOnce"]!;
        cue.Text = new LocalizedString();
        typeof(LocalizedString).GetField("m_Key", BindingFlags.Instance | BindingFlags.NonPublic)!.SetValue(cue.Text, (string)data["Text"]!["m_Key"]!);
        return cue;
    }

    // E14d extension: the native Tirabade page and the shipped Cue_0311 variants together, state by state. The page holds the
    // archive's four cues with their real etude checkers and image actions; the variants are prepared and attached as Main
    // does (Prepare, AttachGroup); a cue plays when its checker passes, as DialogController.PlayBookPage selects them.
    public static void RunTirabade(Story story, Dictionary<string, JObject> native, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        string[] Refs(JObject data, string field) => ((JArray)data[field]!).Select(v => ((string)v!).Replace("!bp_", "")).ToArray();
        if (!story.NativeEpilogueEdits.TryGetValue(Cue0311, out var spec)) { check(false, "Story does not replace the Tirabade Cue_0311."); return; }
        var evidence = NativeEpilogueEdit.Reviewed[Cue0311];
        check(Refs(native[evidence.Page], "Cues").SequenceEqual(TirabadePageCues), "BookPage_0307 cues drifted from Cue_0308, Cue_0566, Cue_0310, Cue_0311.");
        var playing = new HashSet<string>();
        Snapshot? current = null;
        var nativeCheckers = new Dictionary<string, Func<bool>>();
        var cues = TirabadePageCues.ToDictionary(g => g, g => { var cue = ArchiveCue(g, native[g], playing.Contains, check, out var checker); nativeCheckers[g] = checker; return cue; });
        var page = new BlueprintBookPage { AssetGuid = BlueprintGuid.Parse(evidence.Page), name = "TirabadeFixture_page" };
        page.Cues.AddRange(TirabadePageCues.Select(Ref));
        var sequence = new BlueprintCueSequence { AssetGuid = BlueprintGuid.Parse(evidence.Sequence), name = "TirabadeFixture_special" };
        sequence.Cues.AddRange(Refs(native[evidence.Sequence], "Cues").Select(Ref));
        var fixtures = new Dictionary<string, SimpleBlueprint> { [evidence.Page] = page, [evidence.Sequence] = sequence };
        foreach (var pair in cues) fixtures[pair.Key] = pair.Value;
        SimpleBlueprint? Resolve(string g) => fixtures.TryGetValue(g, out var bp) ? bp : null;
        check(NativeEpilogueEdit.Check(Cue0311, spec, Resolve, null) == null, "The archive-shaped Cue_0311 is refused by the E14d policy.");
        // A drifted image (another picture) is refused, and that refusal never degrades a relationship (warning only).
        var drifted = ArchiveCue(Cue0311, native[Cue0311], playing.Contains, check, out _);
        typeof(ChangeBookEventImage).GetField("m_Image", BindingFlags.Instance | BindingFlags.NonPublic)!
            .SetValue(drifted.OnShow.Actions[0], new SpriteLink { AssetId = "0123456789abcdef0123456789abcdef" });
        check(NativeEpilogueEdit.Check(Cue0311, spec, g => g == Cue0311 ? drifted : Resolve(g), null) != null
              && !NativeEpilogueEdit.DegradesOnRefusal(Cue0311), "A drifted Cue_0311 image is accepted, or its refusal degrades a relationship.");
        var original = cues[Cue0311];
        var variants = Rules.EditVariants(spec);
        var group = new NativeEpilogueEdit.Group(spec, () => current);
        var plans = new List<NativeEpilogueEdit.Plan>();
        var replacements = new Dictionary<NativeEpilogueEdit.Plan, BlueprintCue>();
        // Each page entry: its cue, its name, and the native checker its own conditions wrap (a variant wraps Cue_0311's).
        var byGuid = new Dictionary<BlueprintGuid, (BlueprintCue Cue, string Name, Func<bool> Native)>();
        foreach (var pair in cues) byGuid[pair.Value.AssetGuid] = (pair.Value, pair.Key, nativeCheckers[pair.Key]);
        for (int v = 0; v < variants.Length; v++)
        {
            int variant = v;
            var replacement = new BlueprintCue { AssetGuid = id(Rules.NativeEditCueName(Cue0311, spec, variant)), name = "TirabadeFixture_v" + variant };
            var plan = NativeEpilogueEdit.Prepare(Cue0311, spec, original, page, replacement, () => group.Selected() == variant, variant);
            foreach (var condition in replacement.Conditions.Conditions)
            { condition.Owner = replacement; condition.name = "$Applies$fixture" + variant; replacement.ElementsArray.Add(condition); }
            plans.Add(plan);
            replacements[plan] = replacement;
            byGuid[replacement.AssetGuid] = (replacement, variants[variant].Replacement, nativeCheckers[Cue0311]);
        }
        check(group.Selected() == -1, "A variant group selects before it is attached.");
        NativeEpilogueEdit.AttachGroup(group, plans, plan => Ref(replacements[plan].AssetGuid.ToString()));
        check(page.Cues.Select(r => byGuid[r.Guid].Name).SequenceEqual(TirabadePageCues.Take(3).Concat(variants.Select(v => v.Replacement)).Append(Cue0311)),
            "Cue_0311 variants are not inserted in order right before the native cue.");
        string[] Shown() => page.Cues.Select(reference => byGuid[reference.Guid])
            .Where(entry => entry.Native() && entry.Cue.Conditions.Conditions.All(c => c.Check())).Select(entry => entry.Name).ToArray();
        const string IrabethDead = "b14e13f9359585e498fcd81ab95d4d7e", AneviaGone = "09f46662bcd14a03a0874267e16d6e6f",
            IrabethGone = "395aad049186445f9f474d0a769ec8ff", Encouraged = "8b0924efc23df3540b4d8b5fbffd522f", Image = "f96ad5fa9c59d7549adff4c90f0703ab";
        const string Returned = "anevia.trickster.returned", IrabethReturned = "irabeth.trickster.returned", Committed = "anevia.committed";
        // (state, native etudes Playing, RRT flags or null for the mod disabled, the one cue that must play, its picture action)
        var rows = new (string What, string[] Etudes, string[]? Flags, string Plays, string? Picture)[]
        {
            ("widowed and gone, nothing returned", new[] { IrabethDead, AneviaGone }, new[] { "trickster.ever" }, Cue0311, Image),
            ("mod disabled after Anevia's return", new[] { IrabethDead, AneviaGone }, null, Cue0311, Image),
            ("Anevia returned, uncommitted", new[] { IrabethDead, AneviaGone }, new[] { "trickster.ever", Returned },
                "anevia.trickster.epilogue.native_tirabade_widow", Image),
            ("Anevia returned, committed", new[] { IrabethDead, AneviaGone }, new[] { "trickster.ever", Returned, Committed },
                "anevia.trickster.epilogue.native_tirabade_widow_committed", Image),
            ("both returned, uncommitted", new[] { IrabethDead, AneviaGone }, new[] { "trickster.ever", Returned, IrabethReturned },
                "anevia.trickster.epilogue.native_tirabade_back", null),
            ("both returned, Anevia committed", new[] { IrabethDead, AneviaGone }, new[] { "trickster.ever", Returned, IrabethReturned, Committed },
                "anevia.trickster.epilogue.native_tirabade_together", null),
            ("Irabeth returned, Anevia away", new[] { IrabethDead, AneviaGone }, new[] { "trickster.ever", IrabethReturned },
                "irabeth.trickster.epilogue.native_tirabade_south", Image),
            // Other native states keep their own cue: Cue_0311's checker fails there, so no variant can show.
            ("both stayed, Irabeth encouraged (return flags present)", new[] { Encouraged }, new[] { "trickster.ever", Returned, IrabethReturned, Committed },
                TirabadePageCues[0], null),
            ("both left at the Coronation", new[] { IrabethGone, AneviaGone }, new[] { "trickster.ever", Returned }, TirabadePageCues[2], Image),
        };
        foreach (var row in rows)
        {
            playing.Clear();
            playing.UnionWith(row.Etudes);
            if (row.Flags == null) current = null;
            else { current = new Snapshot { Chapter = 6 }; current.Flags.UnionWith(row.Flags); }
            var shown = Shown();
            check(shown.SequenceEqual(new[] { row.Plays }), "Tirabade slide, " + row.What + ": plays [" + string.Join(", ", shown) + "], expected " + row.Plays);
            var played = page.Cues.Select(r => byGuid[r.Guid]).Where(entry => entry.Name == row.Plays).Select(entry => entry.Cue).FirstOrDefault();
            var images = played?.OnShow?.Actions?.Select(NativeEpilogueEdit.ImageOf).ToArray() ?? Array.Empty<string?>();
            check(row.Picture == null ? images.Length == 0 : images.Length == 1 && images[0] == row.Picture,
                "Tirabade slide, " + row.What + ": wrong picture action [" + string.Join(", ", images) + "]");
        }
        check(original.Conditions.Conditions.Length == 1 && original.Conditions.Conditions[0].GetType().Name == "Guard",
            "Cue_0311 is not guarded exactly once.");
        Console.WriteLine("PASS: E14d Tirabade slide: native and RRT cues together, one per state, with the right picture.");
    }
}
