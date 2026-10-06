using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng7-l01: keep physical observations separate from saved progress.
// A predicate checkpoint is labelled; it never proves a return producer.
internal sealed class InventoryWorldBuilder
{
    internal static InventoryWorldBuilder? LastObserved;
    internal sealed class Actor
    {
        public string Unit = "", Area = "", Presence = "";
        public bool Alive = true, Hidden, AtPosition = true, Destroyed, Retained;
        internal Actor Copy() => (Actor)MemberwiseClone();
    }
    private sealed class Record
    {
        public bool Submitted, Unhidden, Native, NativeContact, OriginalHidden, OriginalAtPosition, Lost;
        internal Record Copy() => (Record)MemberwiseClone();
    }
    internal readonly Story Story;
    internal Snapshot State;
    internal readonly List<string> Trace = new List<string>();
    internal readonly List<string> Rendered = new List<string>();
    internal readonly List<string> Payments = new List<string>();
    internal readonly Dictionary<string, int> Spent = new Dictionary<string, int>();
    internal readonly List<Actor> Actors = new List<Actor>();
    private readonly Dictionary<string, Record> records = new Dictionary<string, Record>();
    private readonly HashSet<string> missingAnchors = new HashSet<string>();
    private readonly HashSet<string> observedLocators = new HashSet<string>();
    internal bool CompleteEnabled = true, PlacementEnabled = true;
    internal string? WithheldProducer, WithheldNative;

    internal InventoryWorldBuilder(Story story, int chapter, string area, int finances = 10000)
    {
        Story = story;
        State = new Snapshot { Chapter = chapter, Area = area, Hour = 5000,
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = finances, ["Favors"] = 10000, ["Materials"] = 10000 } };
    }
    internal InventoryWorldBuilder Copy()
    {
        var copy = new InventoryWorldBuilder(Story, State.Chapter, State.Area) { State = Program.Copy(State),
            CompleteEnabled = CompleteEnabled, PlacementEnabled = PlacementEnabled,
            WithheldProducer = WithheldProducer, WithheldNative = WithheldNative };
        copy.State.SceneContacts = new HashSet<string>(State.SceneContacts);
        copy.Trace.AddRange(Trace); copy.Rendered.AddRange(Rendered);
        copy.Payments.AddRange(Payments);
        foreach (var p in Spent) copy.Spent[p.Key] = p.Value;
        copy.Actors.AddRange(Actors.Select(a => a.Copy()));
        foreach (var p in records) copy.records[p.Key] = p.Value.Copy();
        copy.missingAnchors.UnionWith(missingAnchors);
        copy.observedLocators.UnionWith(observedLocators);
        return copy;
    }
    internal void Native(string key)
    {
        Require(Rules.NativeKeys(Story).Contains(key), "Not a native reader input: " + key);
        if (WithheldNative == key) { Trace.Add("withheld native " + key); return; }
        // Read all aliases of the observed blueprint (ascend_areelu / areelu.ascended).
        if (Story.Etudes.TryGetValue(key, out var guid)) ObserveEtude(guid);
        else { Set(key); Trace.Add("native reader " + key); }
        Refresh();
    }
    internal void ObserveEtude(string guid)
    {
        var keys = Story.Etudes.Where(p => p.Value == guid).Select(p => p.Key).ToArray();
        Require(keys.Length > 0, "Unbound native etude " + guid);
        foreach (var key in keys) if (key != WithheldNative) Set(key);
        Trace.Add("native etude " + guid + " -> " + string.Join(",", keys));
        Refresh();
    }
    internal void ObserveCue(string guid)
    {
        var keys = Story.SeenCues.Where(p => p.Value.Contains(guid)).Select(p => p.Key).ToArray();
        Require(keys.Length > 0, "Unbound native cue " + guid);
        foreach (var key in keys) if (key != WithheldNative) Set(key);
        Trace.Add("native cue " + guid + " -> " + string.Join(",", keys));
        Refresh();
    }
    internal void Checkpoint(string label, params string[] flags)
    {
        foreach (var flag in flags)
        {
            Require(!Story.Derived.ContainsKey(flag) && !Story.Counts.ContainsKey(flag)
                && !flag.EndsWith(".failed", StringComparison.Ordinal)
                && !flag.Contains("returned") && !flag.EndsWith(".ascended", StringComparison.Ordinal),
                "Checkpoint fabricates an outcome/observation: " + flag);
            Set(flag); State.Times[flag] = State.Hour - 1000;
        }
        Trace.Add("checkpoint (predicate setup only): " + label + " -> " + string.Join(",", flags));
        Refresh();
    }
    internal Actor ObserveActor(string unit, bool alive = true, bool hidden = false, bool atPosition = true, bool retained = false)
    {
        var actor = Actors.FirstOrDefault(a => a.Unit == unit && a.Area == State.Area && a.Presence == "" && !a.Destroyed);
        if (actor == null) { actor = new Actor { Unit = unit, Area = State.Area }; Actors.Add(actor); }
        actor.Alive = alive; actor.Hidden = hidden; actor.AtPosition = atPosition; actor.Retained = retained;
        Trace.Add("actor " + unit + ": alive=" + alive + ", hidden=" + hidden + ", atPosition=" + atPosition);
        Refresh();
        return actor;
    }
    internal void MissingAnchor(string key)
    {
        missingAnchors.Add(key);
        var p = Story.Presences[key];
        // F10: a fallback that shares the primary's anchor unit (Shamira: primary and awning both use the tailor) must keep
        // that actor, or the "primary cannot be placed" scenario would also destroy the fallback's anchor.
        if (p.At?.NearUnit is string unit && !Story.Presences.Any(o => o.Key != key && o.Value.Unit == p.Unit && o.Value.At?.NearUnit == unit))
            foreach (var actor in Actors.Where(a => a.Unit == unit && a.Area == p.Area && a.Presence == "")) actor.Destroyed = true;
        Refresh();
    }
    internal void Anchor(string key)
    {
        var p = Story.Presences[key];
        if (p.At?.NearUnit is string unit) ObserveActor(unit);
        if (p.At?.Locator is string locator) observedLocators.Add(p.Area + "/" + locator);
        Trace.Add("observed anchor " + key);
        Refresh();
    }
    internal void RouteAnchors(string relationship)
    {
        foreach (var key in Story.Presences.Keys.Where(k => Rules.PresenceRelationship(k) == relationship)) Anchor(key);
    }
    internal void Advance(int hours) { State.Hour += hours; Refresh(); }
    internal void Travel(int chapter, string area)
    {
        State.Chapter = chapter; State.Area = area;
        Trace.Add("travel " + chapter + "/" + area);
        Refresh();
    }
    // Reload retains saved progress, actors and presence records, and rebuilds all observations.
    internal InventoryWorldBuilder Reload()
    {
        var copy = Copy();
        copy.State = JsonSerializer.Deserialize<Snapshot>(JsonSerializer.Serialize(State,
            new JsonSerializerOptions { IncludeFields = true }), new JsonSerializerOptions { IncludeFields = true })!;
        copy.Trace.Add("save/load; rebuild observations");
        copy.Refresh();
        return copy;
    }
    internal PresenceObservation Observe(string key)
    {
        var p = Story.Presences[key];
        var native = Rules.SingleUsable(Actors.Where(a => a.Unit == p.Unit && a.Area == p.Area && a.Presence == ""),
            a => a.Alive && !a.Destroyed, a => !a.Alive || a.Destroyed);
        var copy = Actors.FirstOrDefault(a => a.Presence == key && a.Area == p.Area && !a.Destroyed);
        records.TryGetValue(key, out var record);
        bool anchor = p.At == null || p.At.NearUnit != null && Actors.Any(a => a.Unit == p.At.NearUnit
            && a.Area == p.Area && a.Alive && !a.Hidden && !a.Destroyed && a.Presence == "")
            || p.At.Locator != null && observedLocators.Contains(p.Area + "/" + p.At.Locator);
        return new PresenceObservation { AreaLoaded = State.Area == p.Area, AnchorResolved = anchor && !missingAnchors.Contains(key),
            NativeAlive = native != null, NativeHidden = native?.Hidden ?? false, NativeAtPosition = native?.AtPosition ?? true,
            NativeCount = Actors.Count(a => a.Unit == p.Unit && a.Area == p.Area && a.Presence == "" && a.Alive && !a.Destroyed),
            NativeUsable = native != null && !native.Hidden,
            NativeManageable = native != null,
            RecordedNative = record?.Native ?? false, RecordedNativeContact = record?.NativeContact ?? false,
            CopyFound = copy != null, CopyAlive = copy?.Alive ?? false, Recorded = record != null,
            Submitted = record?.Submitted ?? false, RecordedUnhide = record?.Unhidden ?? false };
    }
    internal PresenceStep[] Tick(string key)
    {
        Refresh();
        var p = Story.Presences[key]; var seen = Observe(key);
        if (Rules.RecordPresenceFailure(Story, key, State, seen))
            Set(Story.PresenceFailureReceipts[key].Flag);
        if (records.TryGetValue(key, out var record) && seen.AreaLoaded
            && (seen.CopyFound && !seen.CopyAlive || (record.Native || record.NativeContact)
                && Actors.Any(a => a.Unit == p.Unit && a.Area == p.Area && a.Presence == "" && !a.Alive && !a.Destroyed)))
            record.Lost = true;
        bool wanted = Rules.PresenceWanted(p, State);
        var steps = Rules.PlanPresence(p, wanted, seen);
        Trace.Add("placement " + key + ": wanted=" + wanted + ", native=" + seen.NativeAlive
            + ", hidden=" + seen.NativeHidden + ", anchor=" + seen.AnchorResolved + ", steps=" + string.Join(",", steps));
        if (PlacementEnabled)
        foreach (var step in steps)
        {
            var native = Actors.FirstOrDefault(a => a.Unit == p.Unit && a.Area == p.Area && a.Presence == "" && a.Alive && !a.Destroyed);
            var copy = Actors.FirstOrDefault(a => a.Presence == key && !a.Destroyed);
            if (step == PresenceStep.Spawn)
            {
                Actors.Add(new Actor { Unit = p.Unit, Area = p.Area, Presence = key });
                records[key] = new Record { Submitted = true };
            }
            if (step == PresenceStep.Adopt && native != null)
                records[key] = new Record { Native = true, OriginalHidden = native.Hidden, OriginalAtPosition = native.AtPosition };
            if (step == PresenceStep.RecordNativeContact) records[key] = new Record { NativeContact = true };
            if (step == PresenceStep.RestoreNative && native != null)
            {
                var prior = records[key]; native.Hidden = prior.OriginalHidden; native.AtPosition = prior.OriginalAtPosition;
                records.Remove(key);
            }
            if (step == PresenceStep.Unhide && native != null)
            {
                native.Hidden = false;
                if (!records.TryGetValue(key, out var adopted) || !adopted.Native) records[key] = new Record { Unhidden = true };
            }
            if (step == PresenceStep.Move && native != null) native.AtPosition = true;
            if (step == PresenceStep.Hide && native != null) { native.Hidden = true; records.Remove(key); }
            if (step == PresenceStep.Remove && copy != null) { copy.Destroyed = true; records.Remove(key); }
            if (step == PresenceStep.Forget) records.Remove(key);
        }
        Refresh();
        return steps;
    }
    internal void TickRoute(string relationship)
    {
        Refresh();
        foreach (var key in Story.Presences.Keys.Where(k => Rules.PresenceRelationship(k) == relationship)
            .OrderBy(k => Rules.PresenceWanted(Story.Presences[k], State)).ToArray()) Tick(key);
    }
    internal void Refresh()
    {
        LastObserved = this;
        State.Flags.ExceptWith(Story.Derived.Keys.Concat(Story.Counts.Keys).Concat(Rules.WordMadeTrueKeys));
        State.Flags.Remove("chapter_one"); State.Flags.Remove("chapter_later");
        State.Flags.Remove("ascended"); State.Flags.Remove("inhuman");
        if (new[] { "ascend_all", "ascend_alone", "ascend_areelu", "ascend_companions" }.Any(State.Has)) State.Flags.Add("ascended");
        if (State.Has("swarm") || State.Has("true_lich")) State.Flags.Add("inhuman");
        State.Flags.Add(State.Chapter == 1 ? "chapter_one" : "chapter_later");
        for (int chapter = 0; chapter <= 6; chapter++)
            if (Rules.ChapterFlag(chapter) is string oldChapter) State.Flags.Remove(oldChapter);
        if (Rules.ChapterFlag(State.Chapter) is string chapterFlag) State.Flags.Add(chapterFlag);
        foreach (var revival in Story.Revivals)
        {
            string key = "revive." + revival.Key + ".available";
            State.Flags.Remove(key);
            if (Actors.Any(a => a.Unit == revival.Value.Unit && !a.Alive && !a.Destroyed && a.Presence == "" && a.Retained))
                State.Flags.Add(key);
        }
        foreach (var key in Story.Presences.Keys) State.Flags.Remove(Rules.PresenceFailedFlag(key));
        if (State.Flags.Contains("wenduag.trickster.returned")
            && records.Any(p => Rules.PresenceRelationship(p.Key) == "wenduag" && p.Value.Lost))
            State.Flags.Add(Rules.WenduagEchoPrefix + "unavailable");
        // Mirror Main's original-body and saved visitor observations.
        foreach (var pair in Story.DepartureEpochs)
        {
            State.Flags.Remove(pair.Key + ".native_alive");
            if (Story.Revivals.TryGetValue(pair.Key, out var revival)
                && Actors.Any(a => a.Unit == revival.Unit && a.Retained && a.Alive && !a.Destroyed && a.Presence == ""))
                State.Flags.Add(pair.Key + ".native_alive");
            if (records.Any(p => Rules.PresenceRelationship(p.Key) == pair.Value.Relationship && p.Value.Lost
                && (pair.Value.Relationship != "minagho_chivarro" || p.Key.EndsWith("." + pair.Key, StringComparison.Ordinal))))
                State.Flags.Add(pair.Key + ".returned_actor_lost");
        }
        if (CompleteEnabled) Rules.Complete(Story, State);
        foreach (var p in Story.Presences)
            if (Rules.PresenceFailed(p.Value, Rules.PresenceWanted(p.Value, State,
                p.Value.Forbids.Contains(Rules.PresenceFailedFlag(p.Key)) ? Rules.PresenceFailedFlag(p.Key) : null), Observe(p.Key)))
                State.Flags.Add(Rules.PresenceFailedFlag(p.Key));
        State.Flags.ExceptWith(Story.Derived.Keys.Concat(Story.Counts.Keys).Concat(Rules.WordMadeTrueKeys));
        if (CompleteEnabled) Rules.Complete(Story, State);
        State.AvailableContacts.Clear();
        foreach (var group in Actors.Where(a => a.Area == State.Area).GroupBy(a => a.Unit))
            if (Rules.SingleUsable(group, a => a.Alive && !a.Hidden && !a.Destroyed,
                a => !a.Alive || a.Destroyed) != null) State.AvailableContacts.Add(group.Key);
    }
    internal Scene Scene(string id) => Story.Scenes.Single(s => s.Id == id);
    internal bool Available(string id) { Refresh(); return Rules.Available(Story, Scene(id), State); }
    internal List<InventoryWorldBuilder> Walk(string id, string? stopAt = null)
    {
        Refresh();
        var scene = Scene(id);
        Require(Rules.Available(Story, scene, State), "Required positive cannot open " + id
            + "; missing=[" + string.Join(",", scene.Requires.Where(k => !State.Has(k))) + "]"
            + "; held forbids=[" + string.Join(",", scene.Forbids.Where(State.Has)) + "]"
            + "; contact=" + Rules.ContactAvailable(Story, scene, State) + "\n" + string.Join("\n", Trace));
        var ends = new List<InventoryWorldBuilder>();
        void Visit(string nodeId, InventoryWorldBuilder world, HashSet<string> visited)
        {
            Require(visited.Add(nodeId), "Cycle " + id + "/" + nodeId);
            world.Refresh();
            var node = scene.Nodes.Single(n => n.Id == nodeId);
            // eng7-integ: OnShow effects precede affordability and payment exits.
            foreach (var flag in node.EnterSet) if (flag != world.WithheldProducer) world.Set(flag);
            world.Refresh();
            world.Rendered.Add(id + "/" + nodeId + ": " + node.Text + " "
                + string.Join(" ", Rules.VisibleParagraphs(node, world.State).Select(p => p.Text)));
            if (nodeId == stopAt) { ends.Add(world); return; }
            var choices = node.Choices.Where(c => Rules.ChoiceAvailable(c, world.State)).ToArray();
            // Main.AddPaymentExit inserts an abort on a payment page with no affordable answer.
            if (choices.Length == 0 && node.Choices.Any(c => c.Crusade?.Amount < 0))
            { world.Trace.Add(id + "/" + nodeId + ": generated payment exit (abort; no completion)");
                ends.Add(world); return; }
            Require(choices.Length > 0, "Page has no selectable answers: " + id + "/" + nodeId);
            foreach (var choice in choices)
            foreach (var target in choice.Check == null ? new[] { choice.Next } : new[] { choice.Check.Success, choice.Check.Failure })
            {
                var next = world.Copy();
                next.Trace.Add(id + "/" + nodeId + "[" + node.Choices.IndexOf(choice) + "] " + choice.Text
                    + (choice.Check == null ? "" : " check=" + (target == choice.Check.Success ? "success" : "failure")));
                if (choice.Crusade != null)
                {
                    var cost = choice.Crusade;
                    next.State.CrusadeResources![cost.Resource] += cost.Amount;
                    next.Spent.TryGetValue(cost.Resource, out int spent);
                    next.Spent[cost.Resource] = spent - cost.Amount;
                    next.Payments.Add(id + "/" + nodeId + "[" + node.Choices.IndexOf(choice) + "] " + cost.Resource + "=" + cost.Amount);
                }
                if (choice.Revive != null)
                {
                    var unit = Story.Revivals[choice.Revive].Unit;
                    var dead = next.Actors.Single(a => a.Unit == unit && !a.Alive && !a.Destroyed && a.Presence == "");
                    dead.Alive = true; dead.Hidden = false;
                    next.State.Flags.Remove(Story.Revivals[choice.Revive].DeathFlag);
                    next.Trace.Add("native revival applied to observed corpse " + unit);
                }
                foreach (var flag in choice.Set) if (flag != next.WithheldProducer) next.Set(flag);
                Rules.RecordAvailabilityEvents(Story, next.State, choice.Set.Where(f => f != next.WithheldProducer));
                if (choice.RemoveItem != null)
                    next.State.Flags.ExceptWith(Story.InventoryItems.Concat(Story.PartyItems).Where(p => p.Value == choice.RemoveItem).Select(p => p.Key));
                if (choice.StartEtude != null) next.ObserveEtude(choice.StartEtude);
                next.Refresh();
                if (target != null) Visit(target, next, new HashSet<string>(visited));
                else
                {
                    if (!choice.Abort) next.Set(id);
                    next.Refresh(); ends.Add(next);
                }
            }
        }
        Visit(scene.Nodes[0].Id, Copy(), new HashSet<string>());
        return ends;
    }
    internal InventoryWorldBuilder Earn(string scene, string flag)
    {
        var end = Walk(scene).FirstOrDefault(w => w.State.Has(scene) && w.State.Has(flag));
        Require(end != null, "No played producer for " + flag + " in " + scene);
        end!.Refresh();
        return end;
    }
    internal void Report(string scenario, string status = "executed")
    {
        Console.WriteLine(JsonSerializer.Serialize(new { scenario, status, producer_trace = Trace,
            rendered_output = Rendered, payments = Payments, spent = Spent,
            finances = State.CrusadeResources, contacts = State.AvailableContacts.OrderBy(k => k) }));
    }
    private void Set(string flag) { if (State.Flags.Add(flag)) State.Times[flag] = State.Hour; }
    internal static void Require(bool result, string message) { if (!result) throw new InvalidOperationException(message); }
}
