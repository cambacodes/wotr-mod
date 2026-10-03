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
    private const string Cue0310 = "ccd140dbf2603734aa323261c2445bec";
    private static readonly string[] TirabadePageCues = { "cba964e33d0a0704d847629be452b359", "2d6b09c6508010e49b882741add89dcf",
        "ccd140dbf2603734aa323261c2445bec", Cue0311 };

    // E14i: the afterlogue's Cue_0001 continuation list (its seven account lines), read with their own checkers.
    private static readonly string[] AfterlogueLines = { "0fd42edf36604d5fa9563711dc124aca", "5afdbd2e61264e8fa227fd153bf21efb",
        "aa857d545e124ce9a5148221e07194b9", "2a4aab21bd184c91a39cdde39b3f3b88", "825786e8c5db4511ae30950bb286f0e9", "172325d4df134fdd98e831b93e6d857c",
        "1b53c189b767412f921b8294b980a51c" };

    public static IEnumerable<string> NativeIds => NativeEpilogueEdit.Reviewed.Keys
        .Concat(NativeEpilogueEdit.Reviewed.Values.Select(e => e.Page)).Concat(NativeEpilogueEdit.Reviewed.Values.Select(e => e.Sequence))
        .Concat(NativeEpilogueEdit.Reviewed.Values.Select(e => e.Parent ?? "")).Concat(NativeEpilogueEdit.Reviewed.Values.Select(e => e.Dialog ?? ""))
        .Concat(TirabadePageCues).Concat(AfterlogueLines).Append(NativeEpilogueEdit.Companions).Where(id => id.Length > 0).Distinct();

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
            var continued = Refs((JObject)data["Continue"]!, "Cues");
            bool continueReviewed = pair.Value.Continue == null ? continued.Length == 0
                : (string)data["Continue"]!["Strategy"]! == "First" && continued.SequenceEqual(pair.Value.Continue);
            check(ArchiveTextKey(data) == pair.Value.Key && !(bool)data["ShowOnce"]! && onShowReviewed
                && ((JArray)data["OnStop"]!["Actions"]!).Count == 0 && ((JArray)data["Components"]!).Count == 0
                && ((JArray)data["Answers"]!).Count == 0 && continueReviewed,
                "Reviewed native cue evidence drifted: " + pair.Key);
            if (pair.Value.Parent != null)   // E14i: listed once by its parent's Continue (First); the dialog opens on the parent
            {
                check(pair.Value.Page == "" && pair.Value.Sequence == "" && (string)native[pair.Value.Parent]["Continue"]!["Strategy"]! == "First"
                      && Refs((JObject)native[pair.Value.Parent]["Continue"]!, "Cues").Count(c => c == pair.Key) == 1
                      && Refs((JObject)native[pair.Value.Dialog!]["FirstCue"]!, "Cues").Count(c => c == pair.Value.Parent) == 1,
                    "Reviewed dialog cue is not once in its parent's Continue, or the dialog no longer opens on the parent: " + pair.Key);
                continue;
            }
            check(Refs(native[pair.Value.Page], "Cues").Count(c => c == pair.Key) == 1, "Reviewed cue is not exactly once on its page: " + pair.Key);
            check(Refs(native[pair.Value.Sequence], "Cues").Count(c => c == pair.Value.Page) == 1, "Reviewed page is not once in its sequence: " + pair.Key);
        }
        check(NativeEpilogueEdit.Reviewed.All(pair => pair.Value.DegradeOnRefusal == (pair.Key != Cue0311 && pair.Key != Cue0310
                && pair.Value.Page != NativeEpilogueEdit.CamelliaPage && pair.Value.Parent == null)),
            "E14d refusal policy changed (only the Tirabade Cue_0311 / Cue_0310, the Camellia BookPage_0347 slides and the E14i afterlogue "
            + "lines are warning-only).");
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
        // Each page entry: its cue, its name, and the native checker its own conditions wrap (a variant wraps its cue's).
        var byGuid = new Dictionary<BlueprintGuid, (BlueprintCue Cue, string Name, Func<bool> Native)>();
        foreach (var pair in cues) byGuid[pair.Value.AssetGuid] = (pair.Value, pair.Key, nativeCheckers[pair.Key]);
        var edited = story.NativeEpilogueEdits.Where(pair => pair.Value.Page == evidence.Page).OrderBy(pair => pair.Key, StringComparer.Ordinal).ToArray();
        check(edited.Select(pair => pair.Key).SequenceEqual(new[] { Cue0311, Cue0310 }.OrderBy(k => k, StringComparer.Ordinal)),
            "The Tirabade page edits are not exactly Cue_0310 and Cue_0311.");
        foreach (var edit in edited)
        {
            string cueId = edit.Key;
            var original = cues[cueId];
            var variants = Rules.EditVariants(edit.Value);
            check(NativeEpilogueEdit.Check(cueId, edit.Value, Resolve, null) == null, "The archive-shaped Tirabade cue is refused: " + cueId);
            var group = new NativeEpilogueEdit.Group(edit.Value, () => current);
            var plans = new List<NativeEpilogueEdit.Plan>();
            var replacements = new Dictionary<NativeEpilogueEdit.Plan, BlueprintCue>();
            for (int v = 0; v < variants.Length; v++)
            {
                int variant = v;
                var replacement = new BlueprintCue { AssetGuid = id(Rules.NativeEditCueName(cueId, edit.Value, variant)), name = "TirabadeFixture_" + cueId + "_v" + variant };
                var plan = NativeEpilogueEdit.Prepare(cueId, edit.Value, original, page, replacement, () => group.Selected() == variant, variant);
                foreach (var condition in replacement.Conditions.Conditions)
                { condition.Owner = replacement; condition.name = "$Applies$fixture" + variant; replacement.ElementsArray.Add(condition); }
                plans.Add(plan);
                replacements[plan] = replacement;
                byGuid[replacement.AssetGuid] = (replacement, variants[variant].Replacement, nativeCheckers[cueId]);
            }
            check(group.Selected() == -1, "A variant group selects before it is attached.");
            NativeEpilogueEdit.AttachGroup(group, plans, plan => Ref(replacements[plan].AssetGuid.ToString()));
            check(original.Conditions.Conditions.Length == 1 && original.Conditions.Conditions[0].GetType().Name == "Guard",
                "Tirabade cue is not guarded exactly once: " + cueId);
        }
        Func<string, string[]> variantsOf = cueId => Rules.EditVariants(story.NativeEpilogueEdits[cueId]).Select(v => v.Replacement).ToArray();
        check(page.Cues.Select(r => byGuid[r.Guid].Name).SequenceEqual(TirabadePageCues.Take(2).Concat(variantsOf(Cue0310)).Append(TirabadePageCues[2])
                .Concat(variantsOf(Cue0311)).Append(Cue0311)),
            "Tirabade variants are not inserted in order right before their native cues.");
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
            ("both left at the Coronation, nothing returned", new[] { IrabethGone, AneviaGone }, new[] { "trickster.ever" }, Cue0310, Image),
            ("both left, mod disabled after Anevia's return", new[] { IrabethGone, AneviaGone }, null, Cue0310, Image),
            ("both left, Anevia returned, uncommitted", new[] { IrabethGone, AneviaGone }, new[] { "trickster.ever", Returned },
                "anevia.trickster.epilogue.native_tirabade_left", Image),
            ("both left, Anevia returned, committed", new[] { IrabethGone, AneviaGone }, new[] { "trickster.ever", Returned, Committed },
                "anevia.trickster.epilogue.native_tirabade_left_committed", Image),
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
        Console.WriteLine("PASS: E14d Tirabade slides (Cue_0310, Cue_0311): native and RRT cues together, one per state, with the right picture.");
    }

    // The archive's text key: its own m_Key, or (a shared string, e.g. Camellia's Cue_0390) the shared asset's string key.
    private static string ArchiveTextKey(JObject data)
    {
        var text = (JObject)data["Text"]!;
        string own = (string?)text["m_Key"] ?? "";
        return own.Length > 0 ? own : (string?)text["Shared"]?["stringkey"] ?? "";
    }

    // NM1 / E14d extension: a seeded native cue gets the archive's reviewed OnShow image action, its continuation (Strategy First)
    // and its text key, own or shared (a SharedStringAsset is a ScriptableObject, so it is created uninitialized).
    public static void LoadArchiveShape(BlueprintCue cue, JObject data, Action<bool, string> check)
    {
        var actions = new List<GameAction>();
        foreach (JObject action in (JArray)data["OnShow"]!["Actions"]!)
        {
            check(((string)action["$type"]!).EndsWith(", ChangeBookEventImage", StringComparison.Ordinal), "Unexpected native OnShow action on an E14d cue: " + cue.AssetGuid);
            var change = new ChangeBookEventImage { Owner = cue, name = "$ChangeBookEventImage$archive" };
            typeof(ChangeBookEventImage).GetField("m_Image", BindingFlags.Instance | BindingFlags.NonPublic)!
                .SetValue(change, new SpriteLink { AssetId = (string)action["m_Image"]!["AssetId"]! });
            cue.ElementsArray.Add(change);
            actions.Add(change);
        }
        cue.OnShow = new ActionList { Actions = actions.ToArray() };
        cue.OnStop = new ActionList { Actions = Array.Empty<GameAction>() };
        var continued = (JObject)data["Continue"]!;
        cue.Continue = new Kingmaker.DialogSystem.CueSelection { Cues = ((JArray)continued["Cues"]!).Select(v => Ref(((string)v!).Replace("!bp_", ""))).ToList(),
            Strategy = (Kingmaker.DialogSystem.Strategy)Enum.Parse(typeof(Kingmaker.DialogSystem.Strategy), (string)continued["Strategy"]!) };
        cue.Text = new LocalizedString();
        var text = (JObject)data["Text"]!;
        typeof(LocalizedString).GetField("m_Key", BindingFlags.Instance | BindingFlags.NonPublic)!.SetValue(cue.Text, (string?)text["m_Key"] ?? "");
        if (text["Shared"] is JObject shared)
        {
            var asset = (SharedStringAsset)System.Runtime.Serialization.FormatterServices.GetUninitializedObject(typeof(SharedStringAsset));
            asset.String = new LocalizedString();
            typeof(LocalizedString).GetField("m_Key", BindingFlags.Instance | BindingFlags.NonPublic)!.SetValue(asset.String, (string)shared["stringkey"]!);
            cue.Text.Shared = asset;
        }
    }

    private sealed class ArchiveCondition : Condition
    {
        internal Func<bool> Holds = null!;
        protected override string GetConditionCaption() => "Native condition (archive fixture)";
        protected override bool CheckCondition() => Holds();
    }

    // The archive's checker as a function of the fixture world: EtudeStatus (Playing), CueSeen, QuestStatus (Completed) and
    // nested OrAndLogic, each with its Not, under And/Or. Anything else fails the test (the page's checkers drifted).
    private static Func<bool> ArchiveChecker(JObject checker, Func<string, bool> playing, Func<string, bool> seen, Func<string, bool> completed,
        Action<bool, string> check, string where)
    {
        bool and = (string)checker["Operation"]! == "And";
        var parts = new List<Func<bool>>();
        foreach (JObject condition in (JArray)checker["Conditions"]!)
        {
            string type = ((string)condition["$type"]!).Split(new[] { ", " }, StringSplitOptions.None).Last();
            bool not = (bool)condition["Not"]!;
            string Target(string field) => ((string)condition[field]!).Replace("!bp_", "");
            Func<bool> holds;
            switch (type)
            {
                case "EtudeStatus":   // the fixture's etudes are Playing (started and not completed), so Started|Playing reads the same
                    check((bool)condition["Playing"]! && !(bool)condition["Completed"]! && !(bool)condition["NotStarted"]! && !(bool)condition["CompletionInProgress"]!,
                        "Native checker reads an etude state other than Playing (or Started): " + where);
                    string etude = Target("m_Etude"); holds = () => playing(etude); break;
                case "FlagInRange": string flag = Target("m_Flag"); holds = () => playing(flag); break;   // the fixture holds the flag in range
                case "CueSeen": string cue = Target("m_Cue"); holds = () => seen(cue); break;
                case "QuestStatus":
                    check((string)condition["State"]! == "Completed", "Camellia native checker reads a quest state other than Completed: " + where);
                    string quest = Target("m_Quest"); holds = () => completed(quest); break;
                case "OrAndLogic": holds = ArchiveChecker((JObject)condition["ConditionsChecker"]!, playing, seen, completed, check, where); break;
                default: check(false, "Camellia native checker has an unmodelled condition " + type + ": " + where); holds = () => false; break;
            }
            parts.Add(() => holds() != not);
        }
        return and ? () => parts.All(p => p()) : () => parts.Any(p => p());
    }

    // E14d extension: Camellia's BookPage_0347 with the archive's eight cues and their real checkers; the shipped edits are
    // prepared and attached as Main does (Prepare, AttachGroup) and the suppressions guarded (Suppress). State by state, the
    // page shows what DialogController.PlayBookPage would: every cue whose checker passes, in page order.
    public static void RunCamellia(Story story, Dictionary<string, JObject> native, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        string[] Refs(JObject data, string field) => ((JArray)data[field]!).Select(v => ((string)v!).Replace("!bp_", "")).ToArray();
        string pageId = NativeEpilogueEdit.CamelliaPage;
        var pageCues = Refs(native[pageId], "Cues");
        check(pageCues.SequenceEqual(new[] { "84f892d388bba01489145ecd631f23a2", "c1b1da84c12d3ac448ec65b4342ce77f", "4ed8e9723359441dae10ad3068d3f2c7",
                "36a07840d25540eeac6b1c6631196bcc", "5011dfa46fbb0464ab624d78bcfbd483", "3617a648c06a45d1807fde65aedafb06", "430ce9767d3ede2479ff9d6aee432304",
                "e9a183135b8289544a3144dcf8151920" }), "BookPage_0347 cues drifted.");
        check(pageCues.All(c => NativeEpilogueEdit.Reviewed.TryGetValue(c, out var e) && e.Page == pageId && !e.DegradeOnRefusal),
            "A Camellia slide is not reviewed warning-only evidence.");
        const string TE1 = "6f95e268d337ddc45be43a11587bc0b6", TE2 = "aca88b6a3cc90c047925bbc0572c10dc", Q3 = "72d7618aeec2e134db7e9728e9fea90a",
            RomDefault = "0f98398a5ddf32e4cb8200f56e4cfbfc", RomTrue = "1454cf86d07cfdf4f8b5daee625cdc5b", Sacrifice = "381a296094804761af0893d2e70dc2df";
        var playing = new HashSet<string>(); var seen = new HashSet<string>(); var completed = new HashSet<string>();
        var etudesRead = new HashSet<string>();
        Snapshot? current = null;
        var cues = new Dictionary<string, BlueprintCue>();
        var checkers = new Dictionary<string, Func<bool>>();
        foreach (var guid in pageCues)
        {
            var cue = new BlueprintCue { AssetGuid = BlueprintGuid.Parse(guid), name = "CamelliaFixture_" + guid };
            checkers[guid] = ArchiveChecker((JObject)native[guid]["Conditions"]!, e => { etudesRead.Add(e); return playing.Contains(e); }, seen.Contains,
                completed.Contains, check, guid);
            cue.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = Array.Empty<Condition>() };
            LoadArchiveShape(cue, native[guid], check);
            cue.ShowOnce = (bool)native[guid]["ShowOnce"]!;
            cues[guid] = cue;
        }
        var page = new BlueprintBookPage { AssetGuid = BlueprintGuid.Parse(pageId), name = "CamelliaFixture_page" };
        page.Cues.AddRange(pageCues.Select(Ref));
        var sequence = new BlueprintCueSequence { AssetGuid = BlueprintGuid.Parse(NativeEpilogueEdit.Companions), name = "CamelliaFixture_companions" };
        sequence.Cues.AddRange(Refs(native[NativeEpilogueEdit.Companions], "Cues").Select(Ref));
        var fixtures = new Dictionary<string, SimpleBlueprint> { [pageId] = page, [NativeEpilogueEdit.Companions] = sequence };
        foreach (var pair in cues) fixtures[pair.Key] = pair.Value;
        SimpleBlueprint? Resolve(string g) => fixtures.TryGetValue(g, out var bp) ? bp : null;
        // A drifted continuation (Cue_0386 no longer into Cue_0387) is refused, warning-only.
        var drifted = new BlueprintCue { AssetGuid = BlueprintGuid.Parse("5011dfa46fbb0464ab624d78bcfbd483"), name = "CamelliaFixture_drift" };
        drifted.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = Array.Empty<Condition>() };
        LoadArchiveShape(drifted, native["5011dfa46fbb0464ab624d78bcfbd483"], check);
        drifted.Continue.Cues.Clear();
        check(NativeEpilogueEdit.Check("5011dfa46fbb0464ab624d78bcfbd483", story.NativeEpilogueEdits["5011dfa46fbb0464ab624d78bcfbd483"],
                g => g == "5011dfa46fbb0464ab624d78bcfbd483" ? drifted : Resolve(g), null) != null,
            "Cue_0386 without its reviewed continuation is accepted.");
        var byGuid = new Dictionary<BlueprintGuid, (BlueprintCue Cue, string Name, Func<bool> Native)>();
        foreach (var pair in cues) byGuid[pair.Value.AssetGuid] = (pair.Value, pair.Key, checkers[pair.Key]);
        foreach (var edit in story.NativeEpilogueEdits.Where(p => p.Value.Page == pageId))
        {
            check(NativeEpilogueEdit.Check(edit.Key, edit.Value, Resolve, null) == null, "The archive-shaped Camellia cue is refused: " + edit.Key);
            var variants = Rules.EditVariants(edit.Value);
            var group = new NativeEpilogueEdit.Group(edit.Value, () => current);
            var plans = new List<NativeEpilogueEdit.Plan>();
            var replacements = new Dictionary<NativeEpilogueEdit.Plan, BlueprintCue>();
            for (int v = 0; v < variants.Length; v++)
            {
                int variant = v;
                var replacement = new BlueprintCue { AssetGuid = id(Rules.NativeEditCueName(edit.Key, edit.Value, variant)), name = "CamelliaFixture_" + edit.Key + "_v" + variant };
                var plan = NativeEpilogueEdit.Prepare(edit.Key, edit.Value, cues[edit.Key], page, replacement, () => group.Selected() == variant, variant);
                foreach (var condition in replacement.Conditions.Conditions)
                { condition.Owner = replacement; condition.name = "$Applies$fixture" + variant; replacement.ElementsArray.Add(condition); }
                check(replacement.Continue.Cues.Count == 0, "A Camellia replacement continues (Cue_0387 must not follow it): " + edit.Key);
                plans.Add(plan);
                replacements[plan] = replacement;
                byGuid[replacement.AssetGuid] = (replacement, variants[variant].Replacement, checkers[edit.Key]);
            }
            NativeEpilogueEdit.AttachGroup(group, plans, plan => Ref(replacements[plan].AssetGuid.ToString()));
        }
        foreach (var suppression in story.NativeEpilogueSuppressions.Where(p => p.Value.Page == pageId))
        {
            check(NativeEpilogueEdit.Check(suppression.Key, suppression.Value, Resolve, null) == null, "The archive-shaped Camellia cue is refused: " + suppression.Key);
            var when = suppression.Value.When;
            NativeEpilogueEdit.Suppress(cues[suppression.Key], () => current != null && Rules.WhenHolds(when, current));
        }
        foreach (var cue in cues.Values)
            foreach (var condition in cue.Conditions.Conditions) { condition.Owner = cue; if (!cue.ElementsArray.Contains(condition)) cue.ElementsArray.Add(condition); }
        string[] Shown() => page.Cues.Select(reference => byGuid[reference.Guid])
            .Where(entry => entry.Native() && entry.Cue.Conditions.Conditions.All(c => c.Check())).Select(entry => entry.Name).ToArray();
        const string R = "camellia.trickster.returned", C = "camellia.committed", T = "camellia.trickster.terms_named", N = "camellia.trickster.epilogue.native_";
        var rows = new (string What, string[] Native, string[]? Flags, string[] Plays)[]
        {
            ("no romance, nothing returned", new string[0], new[] { "trickster.ever" }, new[] { "5011dfa46fbb0464ab624d78bcfbd483", "3617a648c06a45d1807fde65aedafb06" }),
            ("no romance, kept", new string[0], new[] { "trickster.ever", R, C }, new[] { N + "stayed_plain" }),
            ("no romance, kept, mod disabled", new string[0], null, new[] { "5011dfa46fbb0464ab624d78bcfbd483", "3617a648c06a45d1807fde65aedafb06" }),
            ("true romance, kept", new[] { RomTrue }, new[] { "trickster.ever", R, C }, new[] { N + "stayed" }),
            ("true romance, terms named", new[] { RomTrue }, new[] { "trickster.ever", R, T },
                new[] { "4ed8e9723359441dae10ad3068d3f2c7", "3617a648c06a45d1807fde65aedafb06" }),
            ("default romance, kept, closed", new[] { RomDefault }, new[] { "trickster.ever", R, C, "camellia.closed" },
                new[] { "4ed8e9723359441dae10ad3068d3f2c7", "3617a648c06a45d1807fde65aedafb06", "e9a183135b8289544a3144dcf8151920" }),
            ("romance, sacrifice, kept, Commander back", new[] { RomDefault, Sacrifice }, new[] { "trickster.ever", R, C, "sacrifice", "trickster.commander_back" },
                new[] { N + "threshold_waited" }),
            ("romance, sacrifice, kept, Commander dead", new[] { RomDefault, Sacrifice }, new[] { "trickster.ever", R, C, "sacrifice" },
                new[] { "36a07840d25540eeac6b1c6631196bcc", "3617a648c06a45d1807fde65aedafb06", "e9a183135b8289544a3144dcf8151920" }),
            ("TE, Q3 done, true romance, kept", new[] { RomTrue }, new[] { "trickster.ever", R, C }, new[] { N + "te_stayed" }),
            ("TE, Q3 open, kept", new string[0], new[] { "trickster.ever", R, C }, new[] { N + "te_own_path" }),
        };
        foreach (var row in rows)
        {
            playing.Clear(); seen.Clear(); completed.Clear();
            playing.UnionWith(row.Native);
            if (row.What.StartsWith("TE", StringComparison.Ordinal)) seen.Add(TE1);
            if (row.What.Contains("Q3 done")) completed.Add(Q3);
            if (row.Flags == null) current = null;
            else { current = new Snapshot { Chapter = 6 }; current.Flags.UnionWith(row.Flags); }
            var shown = Shown();
            check(shown.SequenceEqual(row.Plays), "Camellia slides, " + row.What + ": plays [" + string.Join(", ", shown) + "], expected [" + string.Join(", ", row.Plays) + "]");
        }
        check(new[] { RomDefault, RomTrue, Sacrifice }.All(etudesRead.Contains), "The Camellia fixture's etude GUIDs do not match the archive checkers.");
        var semidivine = page.Cues.Select(r => byGuid[r.Guid]).Single(e => e.Name == N + "te_stayed").Cue;
        check(semidivine.OnShow.Actions.Select(NativeEpilogueEdit.ImageOf).SequenceEqual(new[] { "df4a5da19a0a64542929dc8409b29bbe" }),
            "The kept semidivine slide lost the native picture action.");
        Console.WriteLine("PASS: E14d Camellia slides (BookPage_0347): archive checkers, replacements and suppressions, one lead per state.");
    }

    // E14i: the afterlogue dialog's Cue_0001 with the archive's seven account lines (Strategy First) and their own checkers; the
    // shipped Areelu lines are prepared and attached as Main does (PrepareInDialog, AttachGroup). The selected line is what
    // CueSelection.Select would pick: the first in Continue order whose checker passes. The replacement speaks as the original
    // and continues into Cue_0007 exactly as the original does.
    public static void RunAfterlogue(Story story, Dictionary<string, JObject> native, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        string[] Refs(JObject data, string field) => ((JArray)data[field]!).Select(v => ((string)v!).Replace("!bp_", "")).ToArray();
        string parentId = NativeEpilogueEdit.AfterlogueFirst, dialogId = NativeEpilogueEdit.AfterlogueDialog;
        check(Refs((JObject)native[parentId]["Continue"]!, "Cues").SequenceEqual(AfterlogueLines), "Afterlogue Cue_0001 continuation drifted.");
        var playing = new HashSet<string>();
        Snapshot? current = null;
        var parent = new BlueprintCue { AssetGuid = BlueprintGuid.Parse(parentId), name = "AfterlogueFixture_parent" };
        parent.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = Array.Empty<Condition>() };
        LoadArchiveShape(parent, native[parentId], check);
        var dialog = new BlueprintDialog { AssetGuid = BlueprintGuid.Parse(dialogId), name = "AfterlogueFixture_dialog" };
        dialog.FirstCue = new Kingmaker.DialogSystem.CueSelection { Cues = Refs((JObject)native[dialogId]["FirstCue"]!, "Cues").Select(Ref).ToList() };
        var cues = new Dictionary<string, BlueprintCue>();
        var byGuid = new Dictionary<BlueprintGuid, (BlueprintCue Cue, string Name, Func<bool> Native)>();
        foreach (var guid in AfterlogueLines)
        {
            var cue = new BlueprintCue { AssetGuid = BlueprintGuid.Parse(guid), name = "AfterlogueFixture_" + guid };
            var nativeCheck = ArchiveChecker((JObject)native[guid]["Conditions"]!, playing.Contains, _ => false, _ => false, check, guid);
            cue.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = Array.Empty<Condition>() };
            LoadArchiveShape(cue, native[guid], check);
            cue.Speaker = new Kingmaker.DialogSystem.DialogSpeaker();
            cues[guid] = cue;
            byGuid[cue.AssetGuid] = (cue, guid, nativeCheck);
        }
        var fixtures = new Dictionary<string, SimpleBlueprint> { [parentId] = parent, [dialogId] = dialog };
        foreach (var pair in cues) fixtures[pair.Key] = pair.Value;
        SimpleBlueprint? Resolve(string g) => fixtures.TryGetValue(g, out var bp) ? bp : null;
        var edits = story.NativeEpilogueEdits.Where(p => p.Value.Parent == parentId).ToArray();
        check(edits.Select(p => p.Key).OrderBy(k => k).SequenceEqual(new[] { "1b53c189b767412f921b8294b980a51c", "825786e8c5db4511ae30950bb286f0e9" }),
            "The afterlogue edits are not exactly Cue_0004 and Cue_0005.");
        // A drifted parent (no longer continuing into the cue) is refused, warning-only.
        var drifted = new BlueprintCue { AssetGuid = parent.AssetGuid, name = "AfterlogueFixture_drift" };
        drifted.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = Array.Empty<Condition>() };
        LoadArchiveShape(drifted, native[parentId], check);
        drifted.Continue.Cues.RemoveAll(r => r.Guid == BlueprintGuid.Parse(edits[0].Key));
        check(NativeEpilogueEdit.Check(edits[0].Key, edits[0].Value, g => g == parentId ? drifted : Resolve(g), null) != null
              && !NativeEpilogueEdit.DegradesOnRefusal(edits[0].Key), "A drifted afterlogue parent is accepted, or its refusal degrades.");
        foreach (var edit in edits)
        {
            check(NativeEpilogueEdit.Check(edit.Key, edit.Value, Resolve, null) == null, "The archive-shaped afterlogue cue is refused: " + edit.Key);
            var variants = Rules.EditVariants(edit.Value);
            var group = new NativeEpilogueEdit.Group(edit.Value, () => current);
            var plans = new List<NativeEpilogueEdit.Plan>();
            var replacements = new Dictionary<NativeEpilogueEdit.Plan, BlueprintCue>();
            for (int v = 0; v < variants.Length; v++)
            {
                int variant = v;
                var replacement = new BlueprintCue { AssetGuid = id(Rules.NativeEditCueName(edit.Key, edit.Value, variant)), name = "AfterlogueFixture_" + edit.Key + "_v" + variant };
                var plan = NativeEpilogueEdit.PrepareInDialog(edit.Key, edit.Value, cues[edit.Key], parent, replacement, () => group.Selected() == variant, variant);
                foreach (var condition in replacement.Conditions.Conditions)
                { condition.Owner = replacement; condition.name = "$Applies$fixture" + variant; replacement.ElementsArray.Add(condition); }
                check(replacement.Continue.Cues.Select(r => r.Guid).SequenceEqual(new[] { BlueprintGuid.Parse(NativeEpilogueEdit.AfterlogueAccount) })
                      && replacement.Continue.Strategy == Kingmaker.DialogSystem.Strategy.First && ReferenceEquals(replacement.Speaker, cues[edit.Key].Speaker)
                      && replacement.OnShow.Actions.Length == 0 && replacement.Answers.Count == 0,
                    "An afterlogue replacement does not speak as the original or does not continue into Cue_0007: " + edit.Key);
                plans.Add(plan);
                replacements[plan] = replacement;
                byGuid[replacement.AssetGuid] = (replacement, variants[variant].Replacement, byGuid[cues[edit.Key].AssetGuid].Native);
            }
            NativeEpilogueEdit.AttachGroup(group, plans, plan => Ref(replacements[plan].AssetGuid.ToString()));
        }
        foreach (var cue in cues.Values)
            foreach (var condition in cue.Conditions.Conditions) { condition.Owner = cue; if (!cue.ElementsArray.Contains(condition)) cue.ElementsArray.Add(condition); }
        string Selected() => parent.Continue.Cues.Select(reference => byGuid[reference.Guid])
            .FirstOrDefault(entry => entry.Native() && entry.Cue.Conditions.Conditions.All(c => c.Check())).Name ?? "(none)";
        const string Dead = "936af39436c74953b43a4165bfbcc9f9", Redeemed = "127e8a018a0840b080c276b4704e58a2", T = "areelu.trickster.";
        var common = new[] { "trickster.ever", T + "wager_struck", T + "bet_offered", T + "wager_on_screen", T + "late_committed" };
        var rewritten = common.Concat(new[] { "areelu.sacrifice_trickster", "areelu.dead_fight", T + "graft_drawn", T + "survives", T + "rewritten",
            "areelu.died_at_finale" }).ToArray();
        var spared = common.Concat(new[] { "sacrifice", "ending.trickster", "trickster.cheated_death", T + "survives" }).ToArray();
        var rows = new (string What, string[] Etudes, string[]? Flags, string Plays)[]
        {
            ("rewrite, late-committed", new[] { Dead }, rewritten, "areelu.trickster.afterlogue.mortal"),
            ("rewrite, mod disabled", new[] { Dead }, null, "1b53c189b767412f921b8294b980a51c"),
            ("rewrite, closed", new[] { Dead }, rewritten.Append("areelu.closed").ToArray(), "1b53c189b767412f921b8294b980a51c"),
            ("punchline, she lives", new string[0], spared, "areelu.trickster.afterlogue.spared"),
            ("punchline, mod disabled", new string[0], null, "825786e8c5db4511ae30950bb286f0e9"),
            ("punchline, declined", new string[0], spared.Append(T + "declined").ToArray(), "825786e8c5db4511ae30950bb286f0e9"),
            ("redeemed, flags of a live romance", new[] { Redeemed }, spared, "aa857d545e124ce9a5148221e07194b9"),
        };
        foreach (var row in rows)
        {
            playing.Clear();
            playing.UnionWith(row.Etudes);
            if (row.Flags == null) current = null;
            else { current = new Snapshot { Chapter = 6 }; current.Flags.UnionWith(row.Flags); }
            check(Selected() == row.Plays, "Afterlogue, " + row.What + ": plays " + Selected() + ", expected " + row.Plays);
        }
        Console.WriteLine("PASS: E14i afterlogue lines (Cue_0004, Cue_0005): archive checkers, Strategy First, replacement continues into Cue_0007.");
    }
}
