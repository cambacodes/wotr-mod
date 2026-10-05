using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng7-l05: E-Q7-04. Exercise the exported consumers with the real rules, including UI visibility.
internal static class ParticipantInventoryTests
{
    // Main builds a fresh snapshot on each observation. Authored history survives; computed keys do not.
    private static void Observe(Story story, Snapshot state)
    {
        state.Flags.ExceptWith(story.Derived.Keys.Concat(story.Counts.Keys));
        Rules.Complete(story, state);
    }
    internal static Snapshot World(Story story, Scene scene, params string[] extra)
    {
        var state = new Snapshot { Chapter = scene.Chapters.FirstOrDefault(scene.MinChapter), Hour = 10000,
            Area = scene.Areas.FirstOrDefault() ?? "" };
        state.Flags.Add(state.Chapter >= 3 ? "chapter_later" : "chapter_one");
        var visited = new HashSet<string>();
        void Earn(string flag)
        {
            if (!visited.Add(flag)) return;
            if (story.Derived.TryGetValue(flag, out var groups))
                foreach (var input in groups[0]) Earn(input);
            else state.Flags.Add(flag);
        }
        foreach (var flag in Program.Prerequisites(scene).Concat(extra)) Earn(flag);
        foreach (var contact in scene.AdditionalContactUnits.Concat(new[] { scene.ContactUnit }).Where(c => c != null))
            state.AvailableContacts.Add(contact!);
        Observe(story, state);
        return state;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        if (!story.Derived.ContainsKey("participant.lann.available")) return; // legacy standalone export
        using var doc = JsonDocument.Parse(File.ReadAllText(Path.Combine("tools", "participant_inventory_contracts.json")));
        var contract = doc.RootElement;
        var native = new Dictionary<string, string[]> {
            ["lann"] = new[] { "lann.dead", "lann.kicked_out", "lann.plot_absent" },
            ["woljif"] = new[] { "woljif.dead", "woljif.kicked_out", "woljif.plot_absent" },
            ["regill"] = new[] { "regill.dead", "regill.kicked_out", "regill.left_plot" },
            ["greybor"] = new[] { "greybor.dead", "greybor.kicked_out", "greybor.away" },
            ["arueshalae"] = new[] { "arueshalae_dead", "arueshalae.kicked_out", "arueshalae.plot_absent", "arueshalae.evil_recruited" }
        };
        var emptyScene = new Scene { MinChapter = 5 };
        foreach (var (who, losses) in native)
        {
            string key = "participant." + who + ".available";
            var state = World(story, emptyScene);
            check(!state.Has(key), who + " is available without recruitment.");
            state.Flags.Add(who + ".in_party");
            Observe(story, state);
            check(state.Has(key), who + " current recruitment cannot establish presence.");
            foreach (var loss in losses)
            {
                var lost = Program.Copy(state);
                lost.Flags.Add(loss); // earlier contact remains recorded
                Observe(story, lost);
                check(!lost.Has(key), who + " current reader ignores " + loss);
            }
        }

        // Every nominated scene/choice/paragraph is evaluated with current sources removed and history retained.
        int consumers = 0;
        foreach (var entry in contract.GetProperty("consumers").EnumerateArray())
        {
            string id = entry.GetProperty("scene").GetString()!;
            string key = entry.TryGetProperty("reader_override", out var ro) ? ro.GetString()! : entry.GetProperty("reader").GetString()!;
            string kind = entry.GetProperty("kind").GetString()!;
            var scenes = story.Scenes.Where(s => s.Id == id || entry.TryGetProperty("include_twins", out var twins)
                && twins.GetBoolean() && s.Id.StartsWith(id + "_", StringComparison.Ordinal));
            foreach (var scene in scenes)
            {
                consumers++;
                var live = World(story, scene, key);
                if (kind == "paragraph")
                    live = World(story, scene, scene.Nodes.SelectMany(n => n.Paragraphs)
                        .First(p => p.Requires.Contains(entry.GetProperty("match").GetString()!) && p.Requires.Contains(key)).Requires);
                if (entry.TryGetProperty("match", out var match)) live.Flags.Add(match.GetString()!);
                if (entry.TryGetProperty("extra", out var extra))
                    foreach (var flag in extra.EnumerateArray()) live.Flags.Add(flag.GetString()!);
                Observe(story, live);
                check(live.Has(key), id + " positive current-participant fixture did not earn its reader.");
                var absent = Program.Copy(live);
                string woman = key == "chadali.trickster.eritrice_available" ? "eritrice" : key.Split('.')[1];
                if (native.ContainsKey(woman)) absent.Flags.Remove(woman + ".in_party");
                else if (woman == "chivarro") absent.Flags.Add("minagho_chivarro.trickster.chivarro_sent_back");
                else absent.Flags.Add(woman + ".closed");
                Observe(story, absent);
                check(!absent.Has(key), id + " absence fixture retained current presence.");
                // eng8-q8e: the nominated physical Vellexia host retires its remembered opening by a scene guard.
                if (kind == "scene" || entry.TryGetProperty("eng8-q8e", out var q8e) && q8e.GetProperty("availability").GetString() == "scene")
                {
                    check(Rules.Available(story, scene, live), id + " is not available with its intended participant.");
                    check(!Rules.Available(story, scene, absent), id + " advertises an absent participant.");
                    // Mutation: removing this guard really exposes the defect, rather than testing JSON shape alone.
                    var requires = scene.Requires;
                    scene.Requires = requires.Where(f => f != key).ToArray();
                    check(Rules.Available(story, scene, absent), id + " mutation failed to reproduce the advertised ghost.");
                    scene.Requires = requires;
                }
                else if (kind == "paragraph")
                {
                    var blocks = scene.Nodes.SelectMany(n => n.Paragraphs).Where(p => p.Requires.Contains(key)
                        && p.Requires.Contains(entry.GetProperty("match").GetString()!)).ToArray();
                    check(blocks.Length > 0 && blocks.Any(p => Rules.ParagraphVisible(p, live)), id + " intended participant paragraph is unreachable.");
                    check(blocks.All(p => !Rules.ParagraphVisible(p, absent)), id + " portrays an absent participant.");
                }
                else
                {
                    var edges = scene.Nodes.SelectMany(n => n.Choices).Where(c => c.Requires.Contains(key)).ToArray();
                    check(edges.Length > 0, id + " has no current participant edge.");
                    check(edges.All(c => !Rules.ChoiceAvailable(c, absent)), id + " permits an absent participant continuation.");
                    // Check reachability and selectable absence fallbacks without suppressing the owner's whole scene.
                    check(Rules.Available(story, scene, absent), id + " absence incorrectly blocks the owner scene.");
                    Program.Walk(scene, absent, (nodeId, state) => {
                        check(!new[] { "sister", "sister_here", "lann", "lann_new", "mine", "here", "promised" }.Contains(nodeId),
                            id + " absence path entered participant node " + nodeId);
                    });
                }
            }
        }
        check(consumers >= 22, "Too few nominated participant consumers exercised: " + consumers);

        var hep = World(story, emptyScene, "trickster.now", "hepzamirah.trickster.returned");
        var presence = story.Presences["hepzamirah.presence"];
        hep.Area = presence.Area;
        hep.Flags.Add("hepzamirah.trickster.cost.confined");
        hep.Times["hepzamirah.trickster.cost.confined"] = hep.Hour;
        Observe(story, hep);
        check(!hep.Has("participant.hepzamirah.available") && !Rules.PresenceWanted(presence, hep), "Confined Hepzamirah is in the yard.");
        hep.Hour += 71;
        check(!Rules.PresenceWanted(presence, hep), "Confinement releases a body before three nights.");
        hep.Hour++;
        check(Rules.PresenceWanted(presence, hep), "The release encounter cannot acquire Hepzamirah at 72 hours.");
        var hounds = story.Scenes.Single(s => s.Id == "hepzamirah.trickster.body.hounds");
        check(!Rules.Available(story, hounds, hep), "Unreleased prisoner performs the courier visit.");
        hep.Flags.Add("hepzamirah.trickster.flesh.released");
        Observe(story, hep);
        check(hep.Has("participant.hepzamirah.available") && Rules.Available(story, hounds, hep), "Earned release fails to restore courier/current presence.");
        hep.Flags.Add("hepzamirah.closed");
        Observe(story, hep);
        check(!hep.Has("participant.hepzamirah.available"), "Returned then departed Hepzamirah remains available.");

        foreach (var who in new[] { "arueshalae", "vellexia" })
        {
            var back = World(story, emptyScene, "trickster.now", who + ".trickster.returned");
            if (who == "vellexia") back.Flags.Add("vellexia.trickster.cost.diminished");
            back.Flags.Add(who == "arueshalae" ? "arueshalae_dead" : "vellexia.dead");
            Observe(story, back);
            check(back.Has("participant." + who + ".available"), who + " earned return rejected by bare native death.");
            back.Flags.Add(who + ".closed");
            Observe(story, back);
            check(!back.Has("participant." + who + ".available"), who + " closure lifted by old return.");
        }
        var departed = World(story, emptyScene, "trickster.now", "vellexia.trickster.cost.diminished", "vellexia.parted");
        check(!departed.Has("participant.vellexia.available"), "Vellexia's historical body survives parting as current presence.");

        var lucky = story.Scenes.Single(s => s.Id == "chadali.trickster.epilogue.lucky_night");
        foreach (var fight in new[] { "council.fought", "council.fought_nocta_allied" })
        {
            var council = World(story, lucky, fight, "chadali.trickster.returned", "chadali.hours.first_sight", "council.epilogue_convened");
            var ongoing = lucky.Nodes.SelectMany(n => n.Paragraphs).Single(p => p.Requires.Contains("participant.eritrice.available")
                && p.Requires.Contains("council.epilogue_convened"));
            check(Rules.Available(story, lucky, council) && !Rules.ParagraphVisible(ongoing, council), fight + " returned Chadali brings unreturned Eritrice to Council.");
            check(lucky.Nodes.SelectMany(n => n.Paragraphs).Any(p => p.Forbids.Contains("participant.eritrice.available") && Rules.ParagraphVisible(p, council)),
                fight + " erases the old Council minutes instead of recollecting them.");
            council.Flags.Add("eritrice.trickster.returned");
            Observe(story, council);
            check(Rules.ParagraphVisible(ongoing, council), fight + " earned Eritrice return cannot restore ongoing minutes.");
            council.Flags.Add("eritrice.closed");
            Observe(story, council);
            check(!Rules.ParagraphVisible(ongoing, council), fight + " old return bypasses Eritrice closure.");
        }

        const string prefix = "minagho_chivarro.trickster.";
        var solo = World(story, emptyScene, "trickster.now", "minachiv.complete", prefix + "minagho_in", prefix + "chivarro_in",
            prefix + "returned_chivarro", prefix + "chivarro_walked", prefix + "chivarro_sent_back", "chivarro.dead");
        var ledger = story.Books["trickster.ledger"];
        bool Entry(string id, Snapshot state) => Rules.BookEntryVisible(ledger.Entries.Single(e => e.Id == id), state);
        check(solo.Has("participant.minagho.available") && !solo.Has("participant.chivarro.available"), "Solo Minagho inherits departed Chivarro.");
        check(!Entry("guest.minagho_chivarro", solo) && Entry("guest.minagho_chivarro.minagho", solo)
            && !Entry("guest.minagho_chivarro.chivarro", solo), "Guest List misreports solo membership.");
        var named = new Scene { Participants = new[] { "minagho_chivarro" }, ParticipantWomen = new[] { "minagho" } };
        check(Rules.ParticipantsAvailable(story, named, solo), "Legitimate solo Minagho seat suppressed.");
        named.ParticipantWomen = new[] { "chivarro" };
        check(!Rules.ParticipantsAvailable(story, named, solo), "Chivarro's empty seat counts as a participant.");
        solo.Flags.Remove(prefix + "chivarro_sent_back");
        solo.Flags.Add(prefix + "cost.won_back");
        Observe(story, solo);
        check(solo.Has("participant.chivarro.available") && Entry("guest.minagho_chivarro", solo), "Earned walkout reconciliation cannot restore the pair.");
        Console.WriteLine("participant inventory: " + consumers + " nominated consumers; recruitment, loss, confinement, earned return and solo UI histories passed.");
    }
}
