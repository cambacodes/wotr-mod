using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// eng7-l01: required delivery checks. Predicate matrices remain in the route suites;
// these witnesses must earn the tested outcome and acquire an actor before opening it.
internal static class InventoryFixtureMutationTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private static void Need(bool result, string message) => InventoryWorldBuilder.Require(result, message);
    internal static void RunMutationSentinels(Action<bool, string> check) => Mutations(check);

    internal static void Run(Story story, Action<bool, string> check)
    {
        var failures = new List<string>();
        int executed = 0;
        void Case(string id, Action action)
        {
            executed++;
            InventoryWorldBuilder.LastObserved = null;
            try { action(); Console.WriteLine("PASS: E-Q7-12 " + id); }
            catch (Exception ex)
            {
                failures.Add(id + ": " + ex.Message);
                InventoryWorldBuilder.LastObserved?.Report(id, "failed");
                Console.Error.WriteLine("FAIL: E-Q7-12 " + id + ": " + ex.Message);
                Console.Error.WriteLine(ex.StackTrace);
            }
        }
        Case("six mutation sentinels", () => Mutations(check));
        foreach (var native in new[] { "ascend_areelu", "ascend_all", "ascend_alone", "ascend_companions" })
        {
            string input = native;
            Case("areelu:007/" + input, () => AreeluAscent(story, input));
        }
        Case("areelu:008/extraction continuity", () => AreeluExtraction(story));
        Case("arsinoe:002/interrupted failed haggle", () => Arsinoe(story));
        foreach (bool fallback in new[] { false, true })
        {
            bool missing = fallback;
            Case("camellia:041/" + (missing ? "missing anchor" : "spawn"), () => Camellia(story, missing));
        }
        Case("camellia:042/battlefield return then native execution", () => CamelliaSecondDeath(story));
        Case("camellia:042/refused then subsequent death", () => CamelliaRefused(story));
        foreach (bool fallback in new[] { false, true })
        foreach (bool blind in new[] { false, true })
        {
            bool missing = fallback;
            bool scarred = blind;
            Case("galfrey:007/" + (missing ? "stall" : "curio") + "/blind=" + scarred, () => Galfrey(story, missing, scarred));
        }
        Case("gesmerha:009/hidden capital native", () => Gesmerha(story, false));
        foreach (string ending in new[] { "living", "fatal", "Last Call" })
        {
            string finale = ending;
            Case("gesmerha:010/failure survives travel/" + finale, () => GesmerhaFallback(story, finale));
        }
        Case("hepzamirah:006/confinement and physical remote areas", () => Hepzamirah(story));
        foreach (string device in new[] { "primed", "late toast", "dug out", "raised" })
        {
            string name = device;
            Case("irabeth:010/hidden reporting actor/" + name, () => Irabeth(story, name));
        }
        Case("irabeth:011/survivor native slide", () => IrabethSlides(story));
        foreach (var phase in new[] { "cells", "back", "standing" })
        foreach (var observation in new[] { "hidden", "displaced", "absent" })
        {
            string name = phase;
            string actor = observation;
            Case("jannah:004/" + name + "/" + actor, () => Jannah(story, name, actor));
        }
        Case("kaylessa:002/paid return", () => Kaylessa(story));
        foreach (var observation in new[] { "hidden", "displaced", "absent", "dead" })
        {
            string name = observation;
            Case("kiana:007/" + name, () => Kiana(story, name));
        }
        Case("kiana:007/observed missing anchor fallback", () => KianaFallback(story));
        foreach (bool arcade in new[] { false, true })
        {
            bool alternate = arcade;
            Case("mielarah:024/recruitment arcade=" + alternate, () => Mielarah(story, alternate));
        }
        Case("mielarah:024/departure after dispatch", () => MielarahDeparture(story));
        foreach (bool arcade in new[] { false, true })
        {
            bool alternate = arcade;
            Case("mielarah:024/market discovery arcade=" + alternate, () => MielarahMarket(story, alternate));
        }
        Case("minagho-and-chivarro:036/paid solo contacts", () => Minagho(story));
        Case("minagho-and-chivarro:036/solo Chivarro", () => Chivarro(story));
        Case("minagho-and-chivarro:036/paid before RET_M", () => MinaghoBeforeReturn(story));
        Case("minagho-and-chivarro:037/parent terminal and reunion", () => PairContinuation(story));
        Case("nocticula:020/completed coda snapshot", () => Nocticula(story));
        foreach (bool recruited in new[] { false, true })
        {
            bool pawn = recruited;
            Case("nurah:004/chapter 5 recruited=" + pawn, () => Nurah(story, pawn, false));
        }
        Case("nurah:004/chapter 3 pardon carried", () => Nurah(story, false, true));
        foreach (var observation in new[] { "hidden", "visible", "absent", "dead" })
        foreach (var anchor in new[] { "tavern", "awning", "king gone" })
        {
            string name = observation;
            string place = anchor;
            Case("shamira:015/" + name + "/" + place, () => Shamira(story, name, place));
        }
        Case("wenduag:054/dead original and living copy reload", () => Wenduag(story, false));
        Case("wenduag:055/ending and household loss matrix", () => Wenduag(story, true));
        Case("binding contexts/unearned and closed negatives", () => Unearned(story));
        Console.WriteLine("E-Q7-12: " + executed + " scenarios executed; " + failures.Count + " failed.");
        check(failures.Count == 0, "E-Q7-12 required integration failures:\n" + string.Join("\n", failures));
    }

    private static InventoryWorldBuilder World(Story story, int chapter = 5)
    {
        var w = new InventoryWorldBuilder(story, chapter, Drezen);
        w.Native("trickster");
        // Explicit world geometry/actors; eligibility alone never fabricates a contact.
        foreach (string route in new[] { "camellia", "galfrey", "gesmerha", "hepzamirah", "irabeth", "jannah",
            "kaylessa", "kiana", "mielarah", "minagho_chivarro", "nurah", "shamira", "wenduag" }) w.RouteAnchors(route);
        return w;
    }

    private static InventoryWorldBuilder AreeluWager(Story story)
    {
        var w = World(story, 6);
        w = w.Earn("areelu.trickster.wager.unprimed", "areelu.trickster.wager_struck");
        return w.Walk("areelu.trickster.wager.raised")
            .First(r => r.State.Has("areelu.committed") && !r.State.Has("areelu.trickster.term.life"));
    }

    private static void AreeluAscent(Story story, string native)
    {
        var w = AreeluWager(story);
        w.Native(native);
        bool shared = native == "ascend_all" || native == "ascend_areelu";
        Need(w.Available("areelu.trickster.finale.ascended") == shared,
            "Native " + native + " selected the wrong committed ascension page.");
        if (shared)
        {
            var endings = w.Walk("areelu.trickster.finale.ascended");
            foreach (string node in new[] { "asc_night", "asc_morning", "asc_stopped" })
                Need(endings.Any(r => r.Trace.Any(t => t.StartsWith("areelu.trickster.finale.ascended/" + node + "["))),
                    "Native " + native + " lost the post-ascent night, morning or refusal: " + node);
            w = endings.First();
        }
        w.Report("areelu:007/" + native);
    }

    private static void AreeluExtraction(Story story)
    {
        var w = AreeluWager(story);
        w.Native("areelu.siphon.council");
        w = w.Earn("areelu.trickster.wager.collect", "areelu.trickster.graft_drawn");
        // q6b provides the registry; the existing runtime selects NativeEpilogueEdits.
        // Cue names/paths are verified in blueprints.zip, not inferred from rendered romance text.
        var targets = new[] {
            ("a9510daab8a04163933d9ecaeffac563", "TE_Final/Cue_3"),
            ("f8d2b851faecddf448fe18db41e17120", "TE_Final/Cue_0017"),
            ("1c8a6796436a7164fa9d63ec79e0395a", "TE_Final/Cue_0020"),
            ("0fa64f1d24f706d41b09dee83acf621d", "GrandFinal/Cue_0088_TricksterAree1")
        };
        var errors = new List<string>();
        const string introduction = "5b567bdd747e497cb9f6984b1ca1dfc8";
        foreach (string input in new[] { "ascend_areelu", "ascend_all", "ascend_alone", "ascend_companions", "areelu.dead_fight",
            "areelu.incinerated", "areelu.sacrifice_wound", "areelu.sacrifice_before", "areelu.sacrifice_trickster", "sacrifice" })
        {
            var end = w.Copy(); end.Native(input);
            string text = string.Join(" ", story.Scenes.Where(s => s.Relationship == "areelu" && s.Owner == "Epilogue"
                && Rules.Available(story, s, end.State)).SelectMany(s => s.Nodes)
                .SelectMany(n => new[] { n.Text }.Concat(Rules.VisibleParagraphs(n, end.State).Select(p => p.Text))));
            end.Rendered.Add("selected finale: " + text);
            end.Report("areelu:008/" + input);
            if ((input == "ascend_areelu" || input == "ascend_all")
                && !end.Available("areelu.trickster.finale.ascended")) errors.Add(input + " has no ascension page");
            if (!story.NativeEpilogueEdits.TryGetValue(introduction, out var intro))
            { errors.Add(input + ": no executable corrected introduction"); continue; }
            var introVariants = Rules.EditVariants(intro);
            var introScenes = Rules.EditScenes(story, introVariants);
            int selectedIntro = Rules.SelectNativeEditVariant(story, introVariants, introScenes, end.State);
            if (selectedIntro < 0) errors.Add(input + ": extraction retained the native half-demon introduction");
            else end.Rendered.Add("corrected introduction: " + end.Scene(introVariants[selectedIntro].Replacement).Nodes[0].Text);
            var unextracted = AreeluWager(story); unextracted.Native(input);
            if (Rules.SelectNativeEditVariant(story, introVariants, introScenes, unextracted.State) >= 0)
                errors.Add(input + ": unextracted introduction changed");
            var former = end.Copy(); former.Native("trickster.failed");
            if (Rules.SelectNativeEditVariant(story, introVariants, introScenes, former.State) >= 0)
                errors.Add(input + ": off-path introduction changed");
            end.Report("areelu:008/introduction/" + input);
        }
        // Exact targets are from blueprints.zip. Both the rewritten and untouched worlds
        // select against the executable registry, not registry metadata or a text substring.
        foreach (var target in targets)
        {
            if (!story.NativeEpilogueEdits.TryGetValue(target.Item1, out var edit))
            { errors.Add("No executable post-extraction replacement for " + target.Item2 + " (" + target.Item1 + ")"); continue; }
            var variants = Rules.EditVariants(edit);
            int selected = Rules.SelectNativeEditVariant(story, variants, Rules.EditScenes(story, variants), w.State);
            if (selected < 0) errors.Add("Extracted world retained " + target.Item2);
            else w.Rendered.Add("native replacement " + target.Item2 + ": " + w.Scene(variants[selected].Replacement).Nodes[0].Text);
            var untouched = AreeluWager(story);
            if (Rules.SelectNativeEditVariant(story, variants, Rules.EditScenes(story, variants), untouched.State) >= 0)
                errors.Add("Unextracted world changed " + target.Item2);
            var offPath = w.Copy(); offPath.Native("trickster.failed");
            if (Rules.SelectNativeEditVariant(story, variants, Rules.EditScenes(story, variants), offPath.State) >= 0)
                errors.Add("Off-path world changed " + target.Item2);
        }
        w.Report("areelu:008/extraction");
        Need(errors.Count == 0, string.Join("; ", errors));
    }

    private static void Arsinoe(Story story)
    {
        var w = World(story);
        w.Native("arsinoe.capital"); w.Native("council.cauldron_given");
        w.ObserveActor("a609ed9b2205d034bb3bb04d2a255681");
        const string scene = "arsinoe.trickster.cauldron.lease";
        w.State.CrusadeResources!["Finances"] = 500;
        var failure = w.Walk(scene).First(r => r.Trace.Any(t => t.Contains("check=failure")));
        Need(!failure.State.Has(scene) && !failure.State.Has("arsinoe.trickster.primed")
            && failure.Trace.Any(t => t.Contains("generated payment exit")), "Failed haggle did not exercise the payment exit.");
        // Reopen with enough for both the base price and the still-owed surcharge.
        failure.State.CrusadeResources!["Finances"] = 700;
        var reopened = failure.Walk(scene).Where(r => r.State.Has("arsinoe.trickster.primed")).ToArray();
        Need(reopened.Length > 0, "Paid interrupted lease cannot resume.");
        foreach (var result in reopened)
        {
            result.Report("arsinoe:002/reopened failed haggle");
            Need(result.State.Has("arsinoe.trickster.cost.rent_raised")
                && result.Spent["Finances"] == 700,
                "Agreement/reroll erased the failed haggle surcharge or charged the base rent twice.");
        }
    }

    private static InventoryWorldBuilder Camellia(Story story, bool missing)
    {
        var w = World(story, 3);
        w.Native("camellia.killed");
        w.Native("camellia.dead"); // The observed execution holds both native etudes.
        w.ObserveActor(story.Presences["camellia.presence"].Unit, alive: false);
        w = w.Earn("camellia.trickster.killed.late_curtain", "camellia.trickster.raised");
        w.Advance(missing ? 168 : 72);
        if (missing) w.MissingAnchor("camellia.presence");
        var steps = w.Tick("camellia.presence");
        Need(missing ? steps.Contains(PresenceStep.Blocked) : steps.Contains(PresenceStep.Spawn),
            "Paid Camellia ritual did not plan the expected placement.");
        string id = "camellia.trickster.killed.performance" + (missing ? "_letter" : "");
        w = w.Earn(id, "camellia.trickster.returned");
        w.Report("camellia:041/" + (missing ? "letter" : "spawn"));
        return w;
    }

    private static void CamelliaSecondDeath(Story story)
    {
        var w = World(story, 3);
        w.Native("camellia.dead");
        w.ObserveActor(story.Revivals["camellia"].Unit, alive: false, retained: true);
        w = w.Earn("camellia.trickster.dead.overacting", "camellia.trickster.returned");
        w.Checkpoint("committed household/card predicate prehistory; battlefield return above is played",
            "camellia.committed", "camellia.harem.seated", "camellia.trickster.masks.game", "camellia.trickster.beat.grave");
        // Camelia Q3 execution co-holds Killed, Dead and KickedOut (native etude readers).
        w.Native("camellia.killed"); w.Native("camellia.kicked_out");
        foreach (var a in w.Actors) a.Alive = false;
        w.Advance(200);
        var errors = new List<string>();
        foreach (int chapter in new[] { 3, 5, 6 })
        {
            w.Travel(chapter, chapter == 6 ? "" : Drezen);
            if (Rules.RouteOpen(story.Relationships["camellia"], w.State)) errors.Add("Battlefield return lifts a subsequent execution in Chapter " + chapter);
            if (w.State.Has("camellia.harem.eligible")) errors.Add("Household eligibility after execution");
            foreach (var scene in story.Scenes.Where(s => s.Relationship == "camellia"
                && (s.Id.Contains(".cards.") || s.Id.Contains(".react.") || s.Id == "camellia.trickster.epilogue.knife")))
                if (Rules.Available(story, scene, w.State)) errors.Add("Living consumer after execution: " + scene.Id);
        }
        try { AssertAbsent(story, w, "camellia"); } catch (InvalidOperationException ex) { errors.Add(ex.Message); }
        w.Report("camellia:042/subsequent execution");
        Need(errors.Count == 0, string.Join("; ", errors));
    }

    private static void CamelliaRefused(Story story)
    {
        var w = World(story, 3); w.Native("camellia.dead");
        w.ObserveActor(story.Revivals["camellia"].Unit, alive: false, retained: true);
        w = w.Earn("camellia.trickster.dead.overacting", "camellia.trickster.returned");
        w.Checkpoint("prior conversation predicate; return is played", "camellia.trickster.beat.lesson");
        w.Advance(48);
        w = w.Earn("camellia.trickster.returned.terms_camp", "camellia.closed");
        // A later battlefield death is observed on the same native actor; no new return is played.
        foreach (var a in w.Actors.Where(a => a.Unit == story.Revivals["camellia"].Unit)) a.Alive = false;
        w.Native("camellia.dead"); w.Travel(6, "");
        var refused = w.Scene("camellia.trickster.epilogue.refused");
        Need(w.Available(refused.Id), "Commander-only refusal consequences disappeared after her death.");
        Need(!Rules.ParagraphVisible(refused.Nodes.Single().Paragraphs[2], w.State),
            "Refused page retains living murder after a subsequent unreturned death.");
        w.Report("camellia:042/refused and subsequently dead");
    }

    private static void Galfrey(Story story, bool missing, bool blind)
    {
        var w = World(story);
        w.Native("galfrey.dying_seen");
        w = w.Walk("galfrey.trickster.iz.offer").First(r => r.State.Has("galfrey.trickster.kitrane_taken")
            && r.State.Has("galfrey.trickster.blind") == blind);
        w.Native("galfrey.dead"); w.Advance(40);
        // eng8-q8d: pending-device delivery belongs to the living sergeant;
        // the returned woman's market hubs must still be unavailable.
        if (missing) w.MissingAnchor("galfrey.presence.sergeant");
        w.TickRoute("galfrey");
        w = w.Earn("galfrey.trickster.iz.eulogy" + (missing ? "_stall" : ""), "galfrey.trickster.cost.eulogy");
        w.Native("coronation.after"); w.Advance(96);
        if (missing) w.MissingAnchor("galfrey.presence");
        w.TickRoute("galfrey");
        Need(story.Presences.Count(p => (p.Key == "galfrey.presence" || p.Key == "galfrey.presence.stall")
            && Rules.PresenceWanted(p.Value, w.State)) == 0, "Pending Kitrane visit must not stage an unreturned market actor.");
        string ret = w.State.Has("galfrey.trickster.cost.rent_scar") ? "galfrey.trickster.return.kitrane_scarred" : "galfrey.trickster.return.kitrane";
        w = w.Earn(ret + (missing ? "_stall" : ""), "galfrey.trickster.returned");
        // end eng8-q8d
        w.Advance(6); w.TickRoute("galfrey");
        w = w.Earn("galfrey.trickster.after.first_morning" + (missing ? "_stall" : ""), "galfrey.trickster.first_morning");
        // Subsequent acts are played when available; no commitment prerequisites are fabricated.
        for (int i = 0; i < 20 && !w.State.Has("galfrey.committed"); i++)
        {
            w.Advance(48); w.TickRoute("galfrey");
            var next = story.Scenes.FirstOrDefault(s => s.Relationship == "galfrey" && !s.Owner.EndsWith("Epilogue")
                && s.Id.StartsWith("galfrey.trickster.kitrane.", StringComparison.Ordinal) && Rules.Available(story, s, w.State));
            if (next == null) break;
            w = w.Walk(next.Id).First(r => r.State.Has(next.Id));
        }
        w.Advance(48); w.TickRoute("galfrey");
        w = w.Earn("galfrey.trickster.commit.oath" + (missing ? "_stall" : ""), "galfrey.committed");
        w.Report("galfrey:007/" + (missing ? "stall" : "curio"));
    }

    private static InventoryWorldBuilder GesmerhaReturn(Story story)
    {
        var w = World(story, 3);
        w.Native("gesmerha.dead");
        w.Checkpoint("pre-death commission (tested separately)", "gesmerha.trickster.primed");
        w.Advance(72);
        return w.Earn("gesmerha.trickster.dead.unfinished_work", "gesmerha.trickster.returned");
    }
    private static void Gesmerha(Story story, bool fallback)
    {
        var w = GesmerhaReturn(story);
        // BlindCarver_Gesmerha_DefaultActor bd304d5930ed4d9bb09a024b1e648bb6
        // hides the living native capital placeholder (blueprints.zip).
        if (!fallback) w.ObserveActor(story.Presences["gesmerha.presence"].Unit, hidden: true);
        else w.MissingAnchor("gesmerha.presence");
        w.Advance(24); w.Tick("gesmerha.presence");
        if (!fallback)
        {
            Need(w.State.AvailableContacts.Contains(story.Presences["gesmerha.presence"].Unit),
                "Hidden living native placeholder prevented a usable returned actor.");
            w = w.Walk("gesmerha.trickster.returned.yard").First(r => r.State.Has("gesmerha.trickster.yard_seen"));
        }
        else
        {
            Need(w.State.Has("gesmerha.presence.failed"), "Missing anchor did not produce observed failure.");
            w.Travel(6, "threshold"); w = w.Reload();
            Need(w.Available("gesmerha.trickster.epilogue.commit"), "Earned fallback disappeared on travel/reload.");
            w = w.Walk("gesmerha.trickster.epilogue.commit").First();
        }
        w.Report("gesmerha:" + (fallback ? "010" : "009"));
    }

    private static void Hepzamirah(Story story)
    {
        var w = World(story);
        w.Checkpoint("Colyphyr prepared steal (predicate prehistory)", "hepzamirah.trickster.primed");
        w.Advance(48);
        w = w.Earn("hepzamirah.trickster.ghost.body", "hepzamirah.trickster.returned");
        var errors = new List<string>();
        foreach (string area in new[] { "3538511f16d45f44f8249ff710777e2d", "unrelated-area" })
        {
            var away = w.Copy(); away.Travel(5, area); away.Advance(48);
            foreach (string id in new[] { "hepzamirah.trickster.ghost.body", "hepzamirah.trickster.body.hounds" })
            {
                var beforeBody = id.EndsWith(".body") ? World(story) : away;
                if (id.EndsWith(".body")) beforeBody.Checkpoint("prepared steal", "hepzamirah.trickster.primed");
                beforeBody.Travel(5, area); beforeBody.Advance(48);
                if (beforeBody.Available(id)) errors.Add(id + " available in " + area);
            }
        }
        w.Advance(48); w.TickRoute("hepzamirah");
        // Courtship prerequisites are played through their actual scenes.
        w = w.Earn("hepzamirah.trickster.flesh.first_morning", "hepzamirah.trickster.flesh.first_morning");
        w.Advance(24); w.TickRoute("hepzamirah");
        w = w.Walk("hepzamirah.trickster.flesh.the_pick").First(r => r.State.Has("hepzamirah.trickster.armed"));
        w.Advance(24); w.TickRoute("hepzamirah");
        var jailed = w.Earn("hepzamirah.trickster.flesh.chaplains", "hepzamirah.trickster.cost.confined");
        foreach (int h in new[] { 0, 36, 71 })
        {
            var at = jailed.Copy(); at.Advance(h); at.TickRoute("hepzamirah");
            if (story.Presences.Any(p => p.Key.StartsWith("hepzamirah.presence") && Rules.PresenceWanted(p.Value, at.State)))
                errors.Add("forge presence during confinement at " + h);
            if (at.Available("hepzamirah.trickster.body.hounds")) errors.Add("courier during confinement at " + h);
            Need(!at.Available("hepzamirah.trickster.flesh.released"), "Release before 72 hours.");
        }
        jailed.Advance(72); jailed.TickRoute("hepzamirah");
        var released = jailed.Walk("hepzamirah.trickster.flesh.released").First();
        released.TickRoute("hepzamirah");
        Need(released.State.AvailableContacts.Contains(story.Presences["hepzamirah.presence"].Unit), "Release did not restore forge contact.");
        released.Report("hepzamirah:006");
        Need(errors.Count == 0, string.Join("; ", errors));
    }

    private static void GesmerhaFallback(Story story, string ending)
    {
        var w = World(story, 3);
        w.Checkpoint("paid commission prehistory (predicate)", "gesmerha.trickster.primed", "gesmerha.trickster.cost.advance_paid");
        w.Native("gesmerha.dead"); w.Advance(48);
        w = w.Earn("gesmerha.trickster.dead.unfinished_work", "gesmerha.trickster.returned");
        w.Travel(5, Drezen); w.MissingAnchor("gesmerha.presence"); w.Tick("gesmerha.presence");
        Need(w.State.Has("gesmerha.presence.failed") && w.State.Has("gesmerha.trickster.late_committed"),
            "Drezen failure did not establish the fallback before departure.");
        w.Travel(6, "threshold"); w = w.Reload();
        Need(!w.State.Has("gesmerha.presence.failed"), "Travel retained a transient area observation.");
        if (ending == "fatal") w.Native("sacrifice");
        if (ending == "Last Call")
        {
            w.Native("lastcall.flask_taken"); w.Native("lastcall.flask_held");
            w = w.Earn("trickster.lastcall.threshold", "trickster.lastcall.open");
            w = w.Earn("gesmerha.lastcall.call", "gesmerha.lastcall.called");
            w = w.Earn("trickster.lastcall.last_joke", "trickster.lastcall.taken");
            w.Native("ending.trickster");
        }
        string page = ending == "Last Call" ? "gesmerha.lastcall.page"
            : "gesmerha.trickster.epilogue." + (ending == "fatal" ? "commit_mourned" : "commit");
        w = w.Walk(page).First();
        Need(w.State.Has("gesmerha.trickster.late_committed"), "Durable earned fallback vanished on departure.");
        w.Report("gesmerha:010/" + ending);
    }

    private static InventoryWorldBuilder IrabethReturn(Story story, string device)
    {
        var w = World(story);
        string scene = "irabeth.trickster.dead.relieved_not_dismissed";
        if (device == "primed")
        {
            w.Native("irabeth.deathbed");
            w = w.Earn("irabeth.trickster.dead.setup", "irabeth.trickster.primed");
        }
        w.Native("irabeth_dead"); w.Advance(24);
        if (device == "primed") w = w.Earn("irabeth.trickster.dead.raise_list", "irabeth.trickster.cost.vell");
        else if (device == "late toast") w = w.Earn("irabeth.trickster.dead.late_order", "irabeth.trickster.cost.vell");
        else
        {
            w.Native("anevia.irabeth_killed_by_commander");
            if (device == "dug out")
            {
                w.Checkpoint("prepared pre-execution drill (predicate)", "irabeth.trickster.drilled");
                w = w.Earn("irabeth.trickster.killed.dig", "irabeth.trickster.cost.dug_out");
            }
            else { w.Advance(24); w = w.Earn("irabeth.trickster.killed.late_step", "irabeth.trickster.raised_on_record"); }
            scene = "irabeth.trickster.killed.blow_missed";
        }
        w.Native("coronation.after"); w.Advance(24);
        w.ObserveActor(story.Presences["irabeth.presence"].Unit, hidden: true);
        var steps = w.Tick("irabeth.presence");
        Need(steps.Contains(PresenceStep.Unhide), "Paid reporting history did not unhide the native capital actor.");
        return w.Earn(scene, "irabeth.trickster.returned");
    }
    private static void Irabeth(Story story, string device)
    {
        var w = IrabethReturn(story, device);
            var closed = w.Copy(); closed.Checkpoint("explicit closure", "irabeth.closed"); closed.Tick("irabeth.presence");
            Need(!closed.State.AvailableContacts.Contains(story.Presences["irabeth.presence"].Unit), "Closed Irabeth reporting actor was not withdrawn.");
        w.Report("irabeth:010/" + device);
    }

    private static void IrabethSlides(Story story)
    {
        var errors = new List<string>();
        foreach (string device in new[] { "raised", "dug out" })
        {
            var survivor = World(story);
            survivor.Native("irabeth_dead"); survivor.Native("anevia.irabeth_killed_by_commander");
            survivor.Native("coronation.after");
            survivor.Advance(24);
            if (device == "dug out")
            {
                survivor.Checkpoint("pre-execution prepared drill (predicate prehistory)", "irabeth.trickster.drilled");
                survivor = survivor.Earn("irabeth.trickster.killed.dig", "irabeth.trickster.cost.dug_out");
            }
            else survivor = survivor.Earn("irabeth.trickster.killed.late_step", "irabeth.trickster.raised_on_record");
            Need(!survivor.State.Has("irabeth.trickster.returned"), "Survivor matrix accidentally walked the later reporting return.");
            foreach (bool aneviaBack in new[] { false, true })
            foreach (string finale in new[] { "survival", "sacrifice", "ascend_all" })
            foreach (bool refused in new[] { false, true })
            {
                var w = survivor.Copy();
                w.Native("anevia_gone");
                if (aneviaBack)
                {
                    w.Checkpoint("Anevia's paid pre-departure wardrobe", "anevia.trickster.primed");
                    w.Advance(200);
                    w = w.Earn("anevia.trickster.gone.wardrobe", "anevia.trickster.returned");
                }
                if (refused) w.Checkpoint("explicit reconciliation refusal (predicate row)", "irabeth.trickster.declined");
                w.Travel(6, "");
                if (finale != "survival") w.Native(finale);
                var edit = story.NativeEpilogueEdits["3a3e561c6b05a284d93eb3bff7b712a6"];
                var variants = Rules.EditVariants(edit);
                int selected = Rules.SelectNativeEditVariant(story, variants, Rules.EditScenes(story, variants), w.State);
                string selectedId = selected < 0 ? "native Cue_0311" : variants[selected].Replacement;
                w.Rendered.Add("native slide selected: " + selectedId + (selected < 0 ? "" : " " + w.Scene(selectedId).Nodes[0].Text));
                string row = device + "/AneviaBack=" + aneviaBack + "/" + finale + "/refused=" + refused;
                w.Report("irabeth:011/" + row);
                if (selected < 0 || selectedId.Contains("widow")) errors.Add(row + " treats a paid survivor as dead: " + selectedId);
            }
        }
        var pending = World(story, 6); pending.Native("irabeth_dead"); pending.Native("anevia_gone");
        var nativeVariants = Rules.EditVariants(story.NativeEpilogueEdits["3a3e561c6b05a284d93eb3bff7b712a6"]);
        Need(Rules.SelectNativeEditVariant(story, nativeVariants, Rules.EditScenes(story, nativeVariants), pending.State) < 0,
            "Pending unearned report replaced the native widow slide.");
        pending.Report("irabeth:011/pending native negative");
        Need(errors.Count == 0, string.Join("; ", errors));
    }

    private static void Jannah(Story story, string phase, string observation)
    {
        var w = World(story); w.Native("coronation.after"); w.Advance(24);
        w = w.Earn("jannah.trickster.alive.letter", "jannah.trickster.alive.in_cells");
        w.Advance(12);
        if (observation != "absent") w.ObserveActor(story.Presences["jannah.presence"].Unit,
            hidden: observation == "hidden", atPosition: observation != "displaced");
        w.TickRoute("jannah");
        Need(w.State.AvailableContacts.Contains(story.Presences["jannah.presence"].Unit), "Jannah cells phase produced no usable actor.");
        if (phase != "cells")
        {
            w = w.Earn("jannah.trickster.alive.stories", "jannah.trickster.alive.posted");
            w.Advance(36); w.TickRoute("jannah");
            Need(w.State.AvailableContacts.Contains(story.Presences["jannah.presence"].Unit), "Jannah back phase produced no usable actor.");
            if (phase == "standing") w = w.Earn("jannah.trickster.alive.wagon", "jannah.trickster.returned");
        }
        w = w.Reload(); w.TickRoute("jannah");
        Need(w.State.AvailableContacts.Contains(story.Presences["jannah.presence"].Unit), "Jannah contact lost on reload.");
        Need(w.Actors.Any(a => a.Unit == story.Presences["jannah.presence"].Unit && !a.Hidden
            && a.Alive && !a.Destroyed && a.AtPosition), "Jannah's displaced native actor was not placed at the phase anchor.");
        w.Report("jannah:004/" + phase + "/" + observation);
        var closed = w.Copy(); closed.Checkpoint("explicit native withdrawal", "jannah.closed"); closed.TickRoute("jannah");
        Need(!story.Presences.Where(p => p.Key.StartsWith("jannah.presence", StringComparison.Ordinal))
            .Any(p => Rules.PresenceWanted(p.Value, closed.State)) && !closed.Actors.Any(a => a.Presence.StartsWith("jannah.presence", StringComparison.Ordinal) && !a.Destroyed),
            "Jannah phase copy was not withdrawn after closure.");
        if (observation != "absent")
        {
            var original = closed.Actors.Single(a => a.Unit == story.Presences["jannah.presence"].Unit && a.Presence == "");
            Need(original.Hidden == (observation == "hidden") && original.AtPosition == (observation != "displaced"),
                "Jannah's original native state was not restored after closure.");
        }
    }

    private static void Kaylessa(Story story)
    {
        var w = World(story, 3); w.Native("kaylessa.dead");
        w = w.Earn("kaylessa.trickster.dead.borrow", "kaylessa.trickster.primed");
        w.Advance(12); w.Tick("kaylessa.presence");
        Need(w.State.AvailableContacts.Contains(story.Presences["kaylessa.presence"].Unit), "Paid Kaylessa window acquired no contact.");
        w = w.Earn("kaylessa.trickster.dead.soldier", "kaylessa.trickster.returned");
        w.Report("kaylessa:002");
    }

    private static void Kiana(Story story, string observed)
    {
        var w = World(story);
        w.Native("kiana.possessed");
        w = w.Earn("kiana.trickster.possessed.fake_gem", "kiana.trickster.returned");
        w.Advance(24);
        if (observed != "absent") w.ObserveActor(story.Presences["kiana.presence"].Unit,
            alive: observed != "dead", hidden: observed == "hidden", atPosition: observed != "displaced");
        var steps = w.Tick("kiana.presence");
        Need(w.State.AvailableContacts.Contains(story.Presences["kiana.presence"].Unit),
            "Placement left Kiana unusable: " + observed + " steps=[" + string.Join(",", steps) + "]");
        w = w.Earn("kiana.trickster.after.temple", "kiana.trickster.met");
        w.Advance(24); w.Tick("kiana.presence");
        w = w.Walk("kiana.trickster.ward_rounds").First(r => r.State.Has("kiana.trickster.ward_rounds"));
        w.Report("kiana:007/" + observed);
    }
    private static void KianaFallback(Story story)
    {
        var w = World(story); w.Native("kiana.possessed");
        w = w.Earn("kiana.trickster.possessed.fake_gem", "kiana.trickster.returned");
        w.MissingAnchor("kiana.presence"); w.Advance(24); w.Tick("kiana.presence");
        Need(w.State.Has("kiana.presence.failed") && !w.State.AvailableContacts.Contains(story.Presences["kiana.presence"].Unit),
            "Missing anchor did not yield observed failure without contact.");
        w = w.Earn("kiana.trickster.after.letter", "kiana.trickster.met");
        Need(!w.Available("kiana.trickster.after.temple"), "Letter fallback also delivered the physical pivot.");
        w.Report("kiana:007/missing anchor fallback");
    }

    private static void Mielarah(Story story, bool arcade)
    {
            var w = World(story);
            w.Checkpoint("earned dispatch/deck prehistory (predicate)", "mielarah.trickster.landfall",
                "mielarah.started", "mielarah.deck.docked", "mielarah.deck.reckoned");
            if (arcade) w.MissingAnchor("mielarah.presence");
            w.TickRoute("mielarah");
            string scene = "mielarah.deck.best_job" + (arcade ? ".arcade" : "");
            var without = w.Walk(scene);
            bool absentCorrect = without.All(r => !r.Rendered.Any(t => t.Contains("/lann_new:") || t.Contains("/lann:")));
            without[0].Report("mielarah:024/absent Lann/arcade=" + arcade);
            w.Native("lann.in_party");
            w = w.Walk(scene).First(r => r.State.Has("mielarah.deck.flown"));
            Need(w.Rendered.Any(t => t.Contains("/lann_new:")), "Available recruited Lann has no visit.");
            w.Report("mielarah:024/arcade=" + arcade);
            Need(absentCorrect, "Lann visits without recruitment/presence.");
    }
    private static void MielarahDeparture(Story story)
    {
        var w = World(story, 4);
        w.Native("mielarah.dead"); w.Native("mielarah.voyage_begun"); w.Advance(72);
        w = w.Earn("mielarah.trickster.raid.overboard", "mielarah.trickster.cost.herald_debt");
        w.Native("trickster.failed"); w.Travel(5, Drezen); w.Advance(72);
        Need(!w.Available("mielarah.trickster.raid.ashore"), "Dispatched rescue performs a new return after leaving Trickster.");
        w.Report("mielarah:024/off-path dispatch negative");
    }
    private static void MielarahMarket(Story story, bool arcade)
    {
        var w = World(story, 4); w.Native("mielarah.hired");
        w.Checkpoint("read curse arithmetic (predicate prehistory)", "mielarah.trickster.primed.pattern");
        w = w.Earn("mielarah.trickster.tavern.minder", "mielarah.trickster.minder.lied");
        w.Native("mielarah.arrived");
        w = w.Walk("mielarah.trickster.colyphyr.landfall")
            .First(r => r.State.Has("mielarah.trickster.landfall") && !r.State.Has("trickster.secret.mielarah_oskel.known.mielarah"));
        w.Travel(5, Drezen);
        if (arcade) w.MissingAnchor("mielarah.presence");
        w.TickRoute("mielarah");
        string suffix = arcade ? ".arcade" : "";
        w = w.Earn("mielarah.deck.cargo" + suffix, "mielarah.deck.docked");
        w.Advance(24); w.TickRoute("mielarah");
        w = w.Walk("mielarah.deck.nearest" + suffix)
            .First(r => r.State.Has("mielarah.deck.reckoned") && !r.State.Has("trickster.secret.mielarah_oskel.known.mielarah"));
        Need(w.Rendered.Any(t => t.Contains("/believed:")), "Continued lie did not traverse the cabin's believed answer.");
        w.Advance(24); w.TickRoute("mielarah");
        w = w.Earn("mielarah.deck.best_job" + suffix, "mielarah.deck.flown");
        w.Advance(24); w.TickRoute("mielarah");
        w = w.Earn("mielarah.deck.correction" + suffix, "mielarah.deck.corrected");
        w.Advance(24); w.TickRoute("mielarah");
        w = w.Earn("mielarah.deck.market" + suffix, "trickster.secret.mielarah_oskel.known.mielarah");
        Need(w.Rendered.Any(t => t.Contains("/worked_out:")), "Market discovery was not played.");
        w.Advance(12); w.TickRoute("mielarah");
        w = w.Earn("mielarah.deck.oskel" + suffix, "mielarah.deck.oskel_spoke");
        Need(w.State.Has("mielarah.deck.oskel_settled"), "Played settlement did not complete the Oskel debt.");
        w.Advance(48); w.TickRoute("mielarah");
        w = w.Earn("mielarah.deck.wheel" + suffix, "mielarah.committed");
        w.Report("mielarah:024/market discovery/arcade=" + arcade);
    }

    private static void Minagho(Story story)
    {
        var w = World(story);
        w.Native("minagho.dead"); w.Native("baphomet.parley");
        w.Checkpoint("paid native parley prehistory", "minagho_chivarro.trickster.cost.baphomet_debtor");
        w.Advance(48);
        w = w.Earn("minagho_chivarro.trickster.minagho_dead.collateral", "minagho_chivarro.trickster.returned_minagho");
        w.Advance(24); w.TickRoute("minagho_chivarro");
        Need(w.State.AvailableContacts.Contains(story.Presences["minagho_chivarro.presence.minagho"].Unit), "Solo Minagho earned no contact.");
        Need(!w.State.AvailableContacts.Contains(story.Presences["minagho_chivarro.presence.chivarro"].Unit), "Unrecovered Chivarro acquired contact.");
        w.Report("minagho-and-chivarro:036/solo");
    }
    private static void MinaghoBeforeReturn(Story story)
    {
        var w = World(story, 3); w.Native("minagho.brand_told_c3");
        w = w.Earn("minagho_chivarro.trickster.minagho_dead.setup_c3", "minagho_chivarro.trickster.primed");
        w.Travel(5, Drezen); w.Native("minagho.dead"); w.Native("baphomet.parley");
        w = w.Earn("minagho_chivarro.trickster.react.baphomet", "minagho_chivarro.trickster.collateral_delivered");
        Need(!w.State.Has("minagho_chivarro.trickster.returned_minagho") && w.State.Has("minagho_chivarro.trickster.collateral_delivered"),
            "Pre-return acceptance did not stop at the paid delivery.");
        w.Advance(24); w.TickRoute("minagho_chivarro");
        w = w.Earn("minagho_chivarro.trickster.minagho_dead.brand", "minagho_chivarro.trickster.returned_minagho");
        w.Report("minagho-and-chivarro:036/pre RET_M");
    }
    private static void Chivarro(Story story)
    {
        var w = World(story, 4); w.Native("herrax.asked_kill_chivarro");
        w = w.Earn("minagho_chivarro.trickster.chivarro_dead.deposit", "minagho_chivarro.trickster.chivarro_deposit");
        w.Native("chivarro.dead"); w.Native("chivarro.exile_objective_done"); w.Native("minagho.dead"); w.Travel(5, Drezen); w.Advance(48);
        w = w.Walk("minagho_chivarro.trickster.chivarro_dead.bought")
            .First(r => r.State.Has("minagho_chivarro.trickster.returned_chivarro") && r.State.Has("minagho_chivarro.trickster.chivarro_owned"));
        w.Advance(24); w.TickRoute("minagho_chivarro");
        Need(w.State.AvailableContacts.Contains(story.Presences["minagho_chivarro.presence.chivarro"].Unit), "Paid solo Chivarro has no usable contact.");
        Need(!w.State.AvailableContacts.Contains(story.Presences["minagho_chivarro.presence.minagho"].Unit), "Unrecovered Minagho acquired a contact.");
        w = w.Earn("minagho_chivarro.trickster.chivarro_dead.the_bill", "minagho_chivarro.trickster.bill_burned");
        w.Report("minagho-and-chivarro:036/solo Chivarro");
    }
    private static void PairContinuation(Story story)
    {
        var w = World(story);
        // Actual parent Book3 terminal, then the authored closet reunion.
        w.ObserveCue("4dbb41f1fb134b90ab3900dc05488e8f");
        w.Native("minagho.ran_complete");
        w.Native("minagho.ran_freed"); w.Native("minagho.ran_romance");
        w.Native("minagho.spared_c4");
        w.Advance(24); w.TickRoute("minagho_chivarro");
        w = w.Earn("minagho_chivarro.trickster.spared.brand", "minagho_chivarro.trickster.minagho_in");
        w.Native("closets.known");
        w = w.Earn("minagho_chivarro.trickster.reunion.wardrobe", "minagho_chivarro.trickster.reunited");
        w.Advance(24);
        w = w.Earn("minachiv.two_answers", "minachiv.invitation_kept");
        w.Advance(24);
        w = w.Earn("minachiv.her_own_arrival", "minachiv.arrival_kept");
        w.Advance(24); w = w.Walk("minachiv.the_remaining_customers").First(r => r.State.Has("minachiv.the_remaining_customers"));
        w.Report("minagho-and-chivarro:037");
    }
    private static void Nocticula(Story story)
    {
        var w = World(story, 6);
        w.Checkpoint("accepted Nocticula completed campaign and paid Last Call (predicate)",
            "noct.complete", "nocticula.trickster.said_yes", "trickster.lastcall.taken");
        w.Native("ending.trickster");
        Need(w.State.Has("nocticula.lastcall.route_open"), "Completed coda lacks derived route state.");
        w = w.Walk("nocticula.lastcall.page").First();
        w.Report("nocticula:020/living");
        var dead = World(story, 6);
        dead.Checkpoint("accepted completed campaign", "noct.complete", "nocticula.trickster.said_yes");
        dead.Native("sacrifice");
        Need(!dead.Available("nocticula.lastcall.page"), "Uncalled fatal finale gets a living coda.");
        dead.Report("nocticula:020/fatal without call");
    }
    private static void Nurah(Story story, bool recruited, bool carry)
    {
        var w = World(story, carry ? 3 : 5); w.Native("nurah.prison");
        if (recruited) w.Native("nurah.trickster_recruited");
        var prisoner = w.ObserveActor(Rules.NurahContact, hidden: true);
        if (carry)
        {
            // Chapter 3 actor is the actual native cell conversant, visible during this dialog.
            prisoner.Hidden = false; w.Refresh();
            w = w.Earn("nurah.trickster.prison.pardon", "nurah.trickster.primed");
            w.Travel(5, Drezen);
            w.Actors.Single(a => a.Unit == Rules.NurahContact && a.Presence == "").Hidden = true; w.Refresh();
        }
        w.Tick("nurah.presence.cell");
        Need(w.State.AvailableContacts.Contains(Rules.NurahContact), "Prison bootstrap did not acquire the hidden cell actor.");
        if (!carry) w = w.Earn("nurah.trickster.prison.pardon_late", "nurah.trickster.primed");
        w.Advance(24); w.Tick("nurah.presence.cell");
        w = w.Earn("nurah.trickster.prison.night_out_late", "nurah.trickster.released");
        w.Advance(72); w.Tick("nurah.presence.cell");
        w = w.Walk("nurah.trickster.prison.proofs_late").First(r => r.State.Has("nurah.trickster.proofs_seen"));
        w.Advance(72); w.Tick("nurah.presence.cell");
        w = w.Earn("nurah.trickster.prison.terms_late", story.Relationships["nurah"].CommittedFlag);
        w.Report("nurah:004/recruited=" + recruited + "/carry=" + carry);
    }
    private static void Shamira(Story story, string observation, string anchor)
    {
        var w = World(story);
        w.Checkpoint("paid mind/body preparation (predicate)", "shamira.trickster.fuel_set", "shamira.trickster.shell");
        // Earn the mind return through the late road, then embody through waking.
        w.Native("shamira.killed");
        w = w.Earn("shamira.trickster.killed.drowning", "shamira.trickster.returned");
        w.Advance(24);
        w = w.Earn("shamira.trickster.mind.waking", "shamira.trickster.embodied");
        if (observation != "absent") w.ObserveActor(story.Presences["shamira.presence"].Unit,
            alive: observation != "dead", hidden: observation == "hidden");
        if (anchor == "king gone") w.Native("fool_king.gone");
        if (anchor == "awning") w.MissingAnchor("shamira.presence");
        w.TickRoute("shamira");
        Need(w.State.Has("shamira.presence.failed") == (anchor == "awning"),
            "Shamira anchor failure observation disagrees with the actual actor observation.");
        Need(w.State.AvailableContacts.Contains(story.Presences["shamira.presence"].Unit),
            "Embodied Shamira has no usable actor: " + observation);
        w.Report("shamira:015/" + observation + "/" + anchor);
    }
    private static InventoryWorldBuilder WenduagReturn(Story story)
    {
        var w = World(story, 3);
        w = w.Earn("wenduag.trickster.killed.stage", "wenduag.trickster.staged");
        w.Native("wenduag.killed"); w.Advance(2);
        w = w.Earn("wenduag.trickster.killed.cairn", "wenduag.trickster.cairn_built");
        w.Advance(72); return w.Earn("wenduag.trickster.killed.back", "wenduag.trickster.returned");
    }
    private static void Wenduag(Story story, bool ending)
    {
        var w = WenduagReturn(story); w.Travel(5, Drezen);
        w.ObserveActor(story.Presences["wenduag.presence"].Unit, alive: false);
        w.Tick("wenduag.presence"); w = w.Reload(); w.Tick("wenduag.presence");
        Need(w.State.AvailableContacts.Contains(story.Presences["wenduag.presence"].Unit), "Dead original masked the returned live copy.");
        w.Checkpoint("courtship predicate prehistory (not contact evidence)", "wenduag.trickster.proved", "wenduag.trickster.gate_seen");
        w = w.Earn("wenduag.trickster.court.claim", "wenduag.committed");
        if (ending)
        {
            w.Travel(6, "");
            var errors = new List<string>();
            foreach (string lost in new[] { "wenduag.dead_any", "wenduag.kicked_out" })
            {
                var absent = World(story, 6);
                absent.Checkpoint("unclaimed predicate prehistory", "wenduag.started");
                absent.Native(lost); AssertAbsent(story, absent, "wenduag");
                if (absent.Available("wenduag.trickster.epilogue.unclaimed")
                    || absent.Available("wenduag.trickster.epilogue.pack")) errors.Add(lost + " selected a living page");
                absent.Report("wenduag:055/unreturned/" + lost);
            }
            var former = w.Copy(); former.Native("trickster.failed"); former.Refresh();
            // eng8-q8b begin: this nominated legacy copy requires current power;
            // its earned receipt and native fate survive conversion as history.
            Need(former.State.Has("wenduag.trickster.returned") && former.State.Has("wenduag.killed"),
                "Legacy conversion erased the return receipt or native fate.");
            Need(!former.State.Has("wenduag.life.available") && !Rules.RouteOpen(story.Relationships["wenduag"], former.State),
                "Current-path legacy copy survived path departure.");
            foreach (string page in new[] { "pack", "unclaimed", "dead", "refused" })
                Need(!former.Available("wenduag.trickster.epilogue." + page), "Off-path legacy ending selected " + page);
            former.Report("wenduag:055/former Trickster legacy copy withheld");
            // eng8-q8b end
            var ascended = w.Copy(); ascended.Native("ascend_all");
            var edit = story.NativeEpilogueEdits["4bb3706172f1ed54ca11db96254c4638"]; // blueprints.zip Epilogues/Cue_0580
            var variants = Rules.EditVariants(edit);
            int selected = Rules.SelectNativeEditVariant(story, variants, Rules.EditScenes(story, variants), ascended.State);
            Need(selected >= 0, "Native Cue_0580 ignored the earned live Wenduag state.");
            ascended.Rendered.Add("Cue_0580: " + ascended.Scene(variants[selected].Replacement).Nodes[0].Text);
            ascended.Report("wenduag:055/native Cue_0580");
            // Household eligibility is earned before the subsequent loss is applied.
            var household = w.Copy(); household.Travel(5, Drezen);
            household.Tick("wenduag.presence");
            Need(household.State.Has("wenduag.harem.eligible"), "Commitment has no household eligibility before the loss.");
            household.Native("wenduag.dead_any");
            foreach (var actor in household.Actors.Where(a => a.Unit == story.Presences["wenduag.presence"].Unit)) actor.Alive = false;
            household.Tick("wenduag.presence"); // idle runtime records the observed copy death before travel
            household.Refresh(); household.Travel(6, "");
            if (household.State.Has("wenduag.harem.eligible")) errors.Add("Household eligibility survived a subsequent unreturned death");
            household.Report("wenduag:055/post-eligibility death");
            Need(errors.Count == 0, string.Join("; ", errors));
        }
        w.Report("wenduag:" + (ending ? "055" : "054"));
    }
    private static void AssertAbsent(Story story, InventoryWorldBuilder w, string route)
    {
        Need(!w.State.Has(route + ".harem.eligible"), route + " remains household-eligible after unreturned loss.");
        foreach (var page in story.Scenes.Where(s => (s.Id == route + ".lastcall.page"
            || s.Id == route + ".lastcall.call" || s.Id == "guest." + route)))
            Need(!Rules.Available(story, page, w.State), "Unreturned loss still selects " + page.Id);
        foreach (var presence in story.Presences.Where(p => Rules.PresenceRelationship(p.Key) == route))
            Need(!Rules.PresenceWanted(presence.Value, w.State), "Unreturned loss still wants " + presence.Key);
    }
    private static void Unearned(Story story)
    {
        foreach (var row in new[] {
            ("camellia", "camellia.killed", "camellia.trickster.killed.performance"),
            ("galfrey", "galfrey.dead", "galfrey.trickster.return.kitrane"),
            ("gesmerha", "gesmerha.dead", "gesmerha.trickster.returned.yard"),
            ("irabeth", "irabeth_dead", "irabeth.trickster.dead.relieved_not_dismissed"),
            ("kaylessa", "kaylessa.dead", "kaylessa.trickster.dead.soldier"),
            ("jannah", "jannah.dead", "jannah.trickster.alive.stories"),
            ("nurah", "nurah.prison", "nurah.trickster.prison.proofs_late"),
            ("shamira", "shamira.killed", "shamira.trickster.harem"),
            ("wenduag", "wenduag.dead_any", "wenduag.trickster.court.claim")
        })
        {
            var w = World(story); w.Native(row.Item2); w.Advance(500); w.TickRoute(row.Item1);
            Need(!w.Available(row.Item3), "Unearned world selected " + row.Item3);
            w.Report("negative/unearned/" + row.Item1);
            var closed = w.Copy();
            closed.Checkpoint("explicit route closure", story.Relationships[row.Item1].ClosedFlag);
            closed.TickRoute(row.Item1);
            Need(!closed.Available(row.Item3), "Closed world selected " + row.Item3);
            closed.Report("negative/closed/" + row.Item1);
            var offPath = w.Copy(); offPath.Native("trickster.failed"); offPath.TickRoute(row.Item1);
            Need(!offPath.Available(row.Item3), "Unearned former Trickster selected " + row.Item3);
            offPath.Report("negative/off-path unearned/" + row.Item1);
        }
    }

    private static void Mutations(Action<bool, string> check)
    {
        // Small integration contract: a paid producer -> placed contact -> native ascension -> completed page.
        Story Fixture()
        {
            var s = new Story();
            s.Relationships["fixture"] = new Relationship { ClosedFlag = "fixture.closed" };
            s.Etudes["ascend_all"] = "07ad18ffb08145b69522f8eee0230857";
            s.Derived["fixture.ready"] = new[] { new[] { "fixture.returned", "ascend_all" } };
            s.Presences["fixture.presence"] = new Presence { Unit = "fixture-unit", Area = Drezen, Mode = "spawn-copy",
                At = new PresenceAnchor { Locator = "fixture-anchor" }, Requires = new[] { "fixture.returned" } };
            s.Scenes.Add(new Scene { Id = "fixture.producer", Relationship = "fixture", Owner = "Memory", Remote = true,
                Nodes = new List<Node> { new Node { Id = "pay", Text = "A paid return.", Choices = new List<Choice> {
                    new Choice { Text = "Pay.", Set = new[] { "fixture.returned" }, Crusade = new CrusadeChoice { Resource = "Finances", Amount = -500 } } } } } });
            s.Scenes.Add(new Scene { Id = "fixture.page", Relationship = "fixture", Owner = "Witness", ContactUnit = "fixture-unit",
                Requires = new[] { "fixture.ready" }, Nodes = new List<Node> { new Node { Id = "page", Text = "The witness arrived.",
                    Choices = new List<Choice> { new Choice { Text = "Continue." } } } } });
            s.Scenes.Add(new Scene { Id = "fixture.fallback", Relationship = "fixture", Owner = "Memory", Remote = true,
                Requires = new[] { "fixture.presence.failed" }, Nodes = new List<Node> { new Node { Id = "letter", Text = "An earned letter.",
                    Choices = new List<Choice> { new Choice { Text = "Keep.", Set = new[] { "fixture.fallback_earned" } } } } } });
            s.Scenes.Add(new Scene { Id = "fixture.finale", Relationship = "fixture", Owner = "Epilogue",
                MaxChapter = 99,
                Requires = new[] { "fixture.fallback_earned" }, Nodes = new List<Node> { new Node { Id = "page", Text = "The earned letter still matters.",
                    Choices = new List<Choice> { new Choice { Text = "Continue." } } } } });
            return s;
        }
        InventoryWorldBuilder Positive(Action<InventoryWorldBuilder>? mutate = null)
        {
            var w = new InventoryWorldBuilder(Fixture(), 5, Drezen, 500);
            w.Anchor("fixture.presence");
            mutate?.Invoke(w);
            w = w.Earn("fixture.producer", "fixture.returned"); w.Native("ascend_all"); w.Tick("fixture.presence");
            w = w.Walk("fixture.page").First();
            Need(w.State.Has("fixture.page"), "Positive delivered no page.");
            return w;
        }
        var baseline = Positive(); baseline.Report("mutation/baseline");
        void Reject(string id, Action action, string reason)
        {
            bool caught = false;
            try { action(); } catch (InvalidOperationException ex) { caught = ex.Message.Contains(reason); }
            check(caught, "Mutation did not invalidate its positive witness: " + id);
            Console.WriteLine("PASS: mutation " + id + " rejected by " + reason);
        }
        Reject("remove return producer", () => Positive(w => w.WithheldProducer = "fixture.returned"), "No played producer");
        Reject("disable placement", () => Positive(w => w.PlacementEnabled = false), "Required positive cannot open");
        Reject("withhold native ascend_all", () => Positive(w => w.WithheldNative = "ascend_all"), "Required positive cannot open");
        Reject("skip Complete", () => Positive(w => w.CompleteEnabled = false), "Required positive cannot open");
        Reject("unaffordable payment", () => Positive(w => w.State.CrusadeResources!["Finances"] = 499), "No played producer");
        var failed = new InventoryWorldBuilder(Fixture(), 5, Drezen, 500).Earn("fixture.producer", "fixture.returned");
        failed.MissingAnchor("fixture.presence"); failed.Tick("fixture.presence");
        var retained = failed.Earn("fixture.fallback", "fixture.fallback_earned");
        retained.Travel(6, "threshold");
        Need(retained.State.Has("fixture.fallback_earned") && !retained.State.Has("fixture.presence.failed"),
            "Fallback test retained a transient failure observation as saved evidence.");
        retained = retained.Walk("fixture.finale").First();
        retained.Report("mutation/fallback survives travel");
        Reject("clear failure on travel (transient consumer mutation)", () => {
            // Mutate only the consumer contract, so it incorrectly relies on the cleared
            // observation rather than on the receipt earned by the played letter.
            var lost = retained.Copy();
            lost.State.Flags.Remove("fixture.finale");
            lost.Scene("fixture.finale").Requires = new[] { "fixture.presence.failed" };
            lost.Walk("fixture.finale");
        }, "Required positive cannot open");
        // Negative worlds pass by withholding the actual outcome, with the same code path executed.
        var noFunds = new InventoryWorldBuilder(Fixture(), 5, Drezen, 499);
        var exits = noFunds.Walk("fixture.producer");
        check(exits.Count == 1 && !exits[0].State.Has("fixture.returned") && !exits[0].State.Has("fixture.producer"),
            "Unpaid negative fixture fabricated an outcome.");
        exits[0].Report("mutation/negative unpaid");
    }
}
