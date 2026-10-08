using System;
using System.Linq;
using System.Collections.Generic;
using Tirabade;

// J-A1: exact delivered surfaces, evaluated by production Rules. The literal
// histories are earned entry fixtures, not claims of full campaign progression.
internal static class ReferenceHistory
{
    internal const string Drezen = "2570015799edf594daf2f076f2f975d8";

    internal static Snapshot World(Story story, int chapter, params string[] history)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 1000, Area = Drezen,
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 1000, ["Favors"] = 1000 } };
        state.Flags.UnionWith(history);
        state.Flags.Add(chapter < 3 ? "chapter_one" : "chapter_later");
        Observe(story, state);
        foreach (var flag in state.Flags) state.Times[flag] = 0;
        return state;
    }

    internal static void Observe(Story story, Snapshot state)
    {
        state.Flags.ExceptWith(story.Derived.Keys.Concat(story.Counts.Keys));
        Rules.Complete(story, state);
    }

    internal static void Play(Story story, string id, Snapshot state,
        Action<bool, string> check, params (string node, int index, string? next)[] path)
    {
        var scene = story.Scenes.Single(s => s.Id == id);
        check(Rules.Available(story, scene, state), id + ": required entry unavailable");
        string? current = scene.Nodes[0].Id;
        bool completed = false;
        foreach (var step in path)
        {
            check(current == step.node, id + ": wrong predecessor for " + step.node);
            var node = scene.Nodes.Single(n => n.Id == current);
            Rules.EnterNode(node, state);
            Observe(story, state);
            var choice = node.Choices[step.index];
            check(Rules.ChoiceAvailable(choice, state), id + "/" + step.node + "[" + step.index + "]: reference blocked by unrelated loss");
            check(step.next == null ? choice.Next == null && choice.Check == null
                : Rules.NextNodes(choice).Contains(step.next), id + ": changed saved target");
            if (choice.Crusade != null)
            {
                var cost = choice.Crusade;
                check(Rules.ApplyCrusadeChange(cost, () => state.CrusadeResources![cost.Resource],
                    () => state.CrusadeResources![cost.Resource] += cost.Amount, warning => check(false, warning)),
                    id + ": existing payment did not apply");
            }
            Rules.RecordAvailabilityEvents(story, state, choice.Set);
            foreach (var flag in choice.Set)
                if (state.Flags.Add(flag)) state.Times[flag] = state.Hour;
            Observe(story, state);
            current = step.next;
            completed = current == null && !choice.Abort;
        }
        if (completed)
        {
            state.Flags.Add(id);
            state.Times[id] = state.Hour;
            Observe(story, state);
        }
    }

}

internal static class ElyankaReferenceAvailabilityTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var writ = ReferenceHistory.World(story, 5, "trickster", "elyanka.trickster.bier_seen", "iomedae.closed", "iomedae.returned_actor_lost");
        ReferenceHistory.Play(story, "elyanka.trickster.beat.writ", writ, check,
            ("start", 0, "writ"), ("writ", 0, "yard"), ("yard", 0, "oath"),
            ("oath", 0, "chaplain"), ("chaplain", 0, "upheld"),
            ("upheld", 0, "upheld2"), ("upheld2", 0, null));
        check(writ.Has("elyanka.trickster.writ.upheld"), "Lawful writ lost its receipt");
        var wards = ReferenceHistory.World(story, 5, "trickster", "elyanka.trickster.bier_seen", "iomedae.closed", "iomedae.returned_actor_lost");
        check(Rules.Available(story, story.Scenes.Single(s => s.Id == "elyanka.trickster.beat.wards"), wards),
            "A sword emblem requires the goddess's romance");
        var closed = ReferenceHistory.World(story, 5, "trickster", "elyanka.trickster.bier_seen", "elyanka.closed");
        check(!Rules.Available(story, story.Scenes.Single(s => s.Id == "elyanka.trickster.beat.writ"), closed),
            "Lawful writ reopened Elyanka's own closure");
    }
}

internal static class TargonaReferenceAvailabilityTests
{
    private static Snapshot Correspondence(Story story) => ReferenceHistory.World(story, 5,
        "trickster", "targona.free", "targona.ran_treatment_completed", "targona.ran_final_seen",
        "targona.ran_trickster", "areelu.closed", "areelu.dead", "areelu.returned_actor_lost", "irabeth.closed", "irabeth_dead", "irabeth.returned_actor_lost", "iomedae.closed", "iomedae.returned_actor_lost");

    internal static void Run(Story story, Action<bool, string> check)
    {
        var state = Correspondence(story);
        ReferenceHistory.Play(story, "targona.unasked_question", state, check,
            ("start", 0, "drawing"), ("drawing", 0, "exit"), ("exit", 0, "personal"),
            ("personal", 1, "friend"), ("friend", 0, null));
        state.Hour += 48;
        ReferenceHistory.Play(story, "targona.second_margin", state, check,
            ("start", 0, "anograt"), ("anograt", 0, "account"), ("account", 1, "private"), ("private", 0, null));
        state.Hour += 48;
        ReferenceHistory.Play(story, "targona.the_folded_room", state, check,
            ("start", 0, "study"), ("study", 0, "creased"), ("creased", 0, null));
        check(state.Has("targona.fold_failed"), "Targona failed fold lost its receipt");
        state.Hour += 48;
        ReferenceHistory.Play(story, "targona.an_unpromised_future", state, check,
            ("start", 1, "failed"), ("failed", 0, "account"), ("account", 1, "private"),
            ("private", 0, "question"), ("question", 0, null));
        foreach (var loss in new[] { "targona.closed", "targona.dead_lab", "targona.returned_actor_lost" })
        {
            var lost = Correspondence(story); lost.Flags.Add(loss); ReferenceHistory.Observe(story, lost);
            check(!Rules.Available(story, story.Scenes.Single(s => s.Id == "targona.unasked_question"), lost),
                "Historical drawing bypasses owner's loss: " + loss);
        }
        var unpaid = Correspondence(story); unpaid.Flags.Remove("targona.ran_final_seen"); ReferenceHistory.Observe(story, unpaid);
        check(!Rules.Available(story, story.Scenes.Single(s => s.Id == "targona.unasked_question"), unpaid),
            "Drawing bypasses the earned parent finale");

        var spent = ReferenceHistory.World(story, 3, "trickster", "targona.free", "iomedae.closed", "iomedae.returned_actor_lost");
        ReferenceHistory.Play(story, "targona.trickster.free.spent_light", spent, check,
            ("start", 1, "night_spent"), ("night_spent", 0, "report_hand"), ("report_hand", 0, null));
        var ward = ReferenceHistory.World(story, 3, "trickster", "targona.trickster.free.spark", "iomedae.closed", "iomedae.returned_actor_lost");
        ward.AvailableContacts.Add("81297c673b63b60448ef88a10db6bc78");
        ReferenceHistory.Play(story, "targona.trickster.after.ward", ward, check,
            ("start", 0, "dawn"), ("dawn", 1, "refused_dawn"), ("refused_dawn", 0, null));
        foreach (bool reported in new[] { false, true })
        foreach (int answer in new[] { 0, 2 })
        {
            var returned = ReferenceHistory.World(story, 5, "trickster", "targona.trickster.returned", "targona.trickster.cost.struck_down",
                "iomedae.closed", "iomedae.returned_actor_lost", "areelu.closed", "areelu.returned_actor_lost");
            if (reported) returned.Flags.Add("targona.trickster.cost.she_told_heaven");
            ReferenceHistory.Observe(story, returned);
            returned.AvailableContacts.Add("81297c673b63b60448ef88a10db6bc78");
            string page = reported ? "pikeman" : "pikeman_late";
            string target = answer == 0 ? "truth" : "lie";
            ReferenceHistory.Play(story, "targona.trickster.dead.furlough", returned, check,
                ("start", reported ? 0 : 1, page), (page, answer, target), (target, 0, null));
        }
        var yaniel = ReferenceHistory.World(story, 5, "trickster", "targona.trickster.met", "targona.free", "yaniel.trickster.returned",
            "areelu.closed", "areelu.dead", "areelu.returned_actor_lost");
        var reaction = story.Scenes.Single(s => s.Id == "targona.trickster.react.ix_a.yaniel");
        ReferenceHistory.Play(story, reaction.Id, yaniel, check, ("start", 0, null));
        var lostYaniel = Program.Copy(yaniel); lostYaniel.Flags.Remove(reaction.Id);
        lostYaniel.Flags.Add("yaniel.returned_actor_lost"); ReferenceHistory.Observe(story, lostYaniel);
        check(!Rules.Available(story, reaction, lostYaniel), "Historical Areelu discussion grants lost Yaniel");
        foreach (var (index, flag, target) in new[] {
            (0, "asked", "list"), (1, "tended", "tended"), (2, "unasked", "unasked") })
        {
            var names = ReferenceHistory.World(story, 5, "trickster", "targona.trickster.met", "targona.trickster.free.names_kept",
                "targona.trickster.free.names_" + flag, "iomedae.closed", "iomedae.returned_actor_lost");
            names.AvailableContacts.Add("81297c673b63b60448ef88a10db6bc78");
            var scene = story.Scenes.Single(s => s.Id == "targona.trickster.free.the_names");
            var absent = Program.Copy(names); absent.AvailableContacts.Clear();
            check(!Rules.Available(story, scene, absent), "Prayer reference grants absent Targona contact");
            ReferenceHistory.Play(story, scene.Id, names, check,
                ("start", index, target), (target, 0, null));
        }
    }
}

internal static class NidalynnReferenceAvailabilityTests
{
    private const string Nidalynn = "e24a8cb4f83960748b5bead99d58a36e";
    internal static void Run(Story story, Action<bool, string> check)
    {
        foreach (int index in new[] { 0, 1 })
        foreach (string outcome in new[] { "taken", "fist" })
        {
            var egg = ReferenceHistory.World(story, 3, "trickster", "devarra.dead", "devarra.closed", "devarra.returned_actor_lost");
            ReferenceHistory.Play(story, "nidalynn.trickster.eggs.lamp_black", egg, check,
                ("look", index, outcome), (outcome, 0, "held"), ("held", 0, "rock"),
                ("rock", 0, "packed"), ("packed", outcome == "fist" ? 1 : 0, null));
            check(egg.Has("nidalynn.trickster.primed"), "Ancestry acquisition lost its receipt");
        }
        var offPath = ReferenceHistory.World(story, 3, "trickster", "trickster.failed");
        check(!Rules.Available(story, story.Scenes.Single(s => s.Id == "nidalynn.trickster.eggs.lamp_black"), offPath),
            "Egg rescue fires off current Trickster");
        var straw = ReferenceHistory.World(story, 3, "trickster", "nidalynn.trickster.eggs_given", "devarra.dead", "devarra.closed", "devarra.returned_actor_lost");
        ReferenceHistory.Play(story, "nidalynn.trickster.eggs.straw", straw, check,
            ("chit", 0, "vault"), ("vault", 0, "signed"), ("signed", 0, "carry"), ("carry", 0, null));
        check(straw.Has("nidalynn.trickster.cost.slate") && straw.Has("nidalynn.trickster.egg_owed"),
            "Straw rescue lost its existing liability");
        var hatch = ReferenceHistory.World(story, 3, "trickster", "nidalynn.trickster.kiln", "iomedae.closed", "iomedae.returned_actor_lost",
            "devarra.trickster.returned", "devarra.returned_actor_lost");
        hatch.AvailableContacts.Add(Nidalynn);
        var hatching = story.Scenes.Single(s => s.Id == "nidalynn.trickster.kiln.hatching");
        var absent = Program.Copy(hatch); absent.AvailableContacts.Clear();
        check(!Rules.Available(story, hatching, absent), "Prayer grants an absent Nidalynn");
        ReferenceHistory.Play(story, hatching.Id, hatch, check,
            ("boy", 0, "kiln"), ("kiln", 0, "out"), ("out", 0, "bite"), ("bite", 0, "torches"),
            ("torches", 0, "crowd"), ("crowd", 1, "her"), ("her", 0, "confess"), ("confess", 0, "chaplain"),
            ("chaplain", 2, "said"), ("said", 0, null));
        check(hatch.Has("nidalynn.trickster.hatched") && hatch.Has("nidalynn.trickster.confessed"),
            "Hatching did not earn its existing confession");
        var mother = hatching.Nodes.Single(n => n.Id == "chaplain");
        check(!Rules.ChoiceAvailable(mother.Choices[0], hatch), "Ancestry exemption stages a lost mother");
        check(Rules.ChoiceAvailable(mother.Choices[2], hatch), "Lost mother has no existing absence continuation");
        foreach (var (index, target) in new[] { (0, "hers"), (1, "pray"), (2, "leave") })
        {
            var path = new List<(string, int, string?)> {
                ("kiln", 0, "report"), ("report", 0, "why"), ("why", 0, "want"), ("want", index, target) };
            if (index < 2) path.AddRange(new (string, int, string?)[] { (target, 0, "prayer"), ("prayer", 0, "after_prayer"), ("after_prayer", 0, "end") });
            else path.Add(("leave", 0, "end"));
            path.Add(("end", 0, null));
            ReferenceHistory.Play(story, "nidalynn.trickster.kiln.the_chaplain", PrayerWorld(story), check, path.ToArray());
        }
        var lost = PrayerWorld(story); lost.AvailableContacts.Clear();
        check(!Rules.Available(story, story.Scenes.Single(s => s.Id == "nidalynn.trickster.kiln.the_chaplain"), lost),
            "Chaplain prayer grants an absent Nidalynn");
        var demon = ReferenceHistory.World(story, 5, "trickster", "nidalynn.trickster.snowfield", "iomedae.closed", "iomedae.returned_actor_lost");
        demon.AvailableContacts.Add("3191b154bbed71b4595a5154ad067e90");
        ReferenceHistory.Play(story, "nidalynn.trickster.after.first_demon", demon, check,
            ("wall", 0, "her"), ("her", 1, "look"), ("look", 0, "fed"),
            ("fed", 3, "house"), ("house", 2, "end"), ("end", 0, null));
    }

    private static Snapshot PrayerWorld(Story story)
    {
        var state = ReferenceHistory.World(story, 3, "trickster", "nidalynn.trickster.confessed", "nidalynn.trickster.hatched",
            "iomedae.closed", "iomedae.returned_actor_lost");
        state.AvailableContacts.Add(Nidalynn);
        return state;
    }
}

internal static class HerraxReferenceAvailabilityTests
{
    private static Snapshot House(Story story, params string[] receipts) => ReferenceHistory.World(story, 4,
        new[] { "trickster", "herrax.madam", "herrax.met", "minachiv.closed", "chivarro.dead", "chivarro.returned_actor_lost",
            "noct.closed", "noct.dead", "nocticula.returned_actor_lost", "minagho.dead", "minagho.returned_actor_lost" }.Concat(receipts).ToArray());

    internal static void Run(Story story, Action<bool, string> check)
    {
        foreach (int reply in new[] { 0, 1, 2 })
        {
            var courier = ReferenceHistory.World(story, 5, "trickster", "herrax.committed", "noct.closed", "noct.dead", "nocticula.returned_actor_lost");
            ReferenceHistory.Play(story, "herrax.letters.the_courier", courier, check,
                ("start", 0, "letter"), ("letter", 3, "letter_end"), ("letter_end", reply, "b_healers"),
                ("b_healers", 0, "b_healers2"), ("b_healers2", 1, "b_lady"), ("b_lady", 0, "b_news"),
                ("b_news", 2, "b_news_empty"), ("b_news_empty", 0, "b_gift"), ("b_gift", 0, "b_gift_letter"),
                ("b_gift_letter", 3, "b_gift_end"), ("b_gift_end", 0, "b_last"), ("b_last", 0, "b_last2"),
                ("b_last2", 0, "reply"), ("reply", 0, "b_offer"), ("b_offer", 0, "b_offer2"),
                ("b_offer2", 0, "b_refused"), ("b_refused", 0, null));
        }
        var lady = House(story, "herrax.house.labyrinth");
        ReferenceHistory.Play(story, "herrax.house.the_lady", lady, check,
            ("start", 1, "lady"), ("lady", 0, "willodus"), ("willodus", 1, "patronless"), ("patronless", 0, "knows"), ("knows", 0, null));
        var wants = House(story, "herrax.house.the_lady");
        ReferenceHistory.Play(story, "herrax.house.what_she_wants", wants, check,
            ("start", 0, "have"), ("have", 0, "long"), ("long", 0, "end"), ("end", 0, null));
        var packet = ReferenceHistory.World(story, 5, "trickster", "herrax.letters.rokhorns_offer", "noct.closed", "noct.dead", "nocticula.returned_actor_lost");
        ReferenceHistory.Play(story, "herrax.letters.the_ladys_people", packet, check,
            ("start", 0, "letter"), ("letter", 1, "answer"), ("answer", 0, "ask"), ("ask", 0, "sent"), ("sent", 0, null));
        ReferenceHistory.Play(story, "herrax.house.the_chair", House(story, "herrax.house.predecessor"), check,
            ("start", 0, "had"), ("had", 0, "rokhorn"), ("rokhorn", 0, "end"), ("end", 0, null));
        ReferenceHistory.Play(story, "herrax.house.labyrinth", House(story, "herrax.house.first_price"), check,
            ("start", 0, "doors"), ("doors", 0, "cultists"), ("cultists", 1, "asset_empty"),
            ("asset_empty", 0, "dais"), ("dais", 1, "dais_end"), ("dais_end", 0, null));
        ReferenceHistory.Play(story, "herrax.house.the_lesson_room", House(story, "herrax.house.forgotten_things"), check,
            ("start", 0, "thief"), ("thief", 2, "hers"), ("hers", 0, "end"), ("end", 0, null));
        ReferenceHistory.Play(story, "herrax.house.last_night", House(story, "herrax.committed"), check,
            ("start", 0, "say"), ("say", 0, "agreed"), ("agreed", 0, null));
        ReferenceHistory.Play(story, "herrax.house.the_glowworm", House(story, "herrax.house.first_price"), check,
            ("start", 2, "joke.history_neutral"), ("joke.history_neutral", 1, "joke_before_audience"),
            ("joke_before_audience", 0, "end"), ("end", 0, "you"), ("you", 0, null));
        ReferenceHistory.Play(story, "herrax.house.the_glowworm", House(story, "herrax.house.first_price",
            "native.history.nocticula.permitted_city_return"), check,
            ("start", 0, "joke"), ("joke", 1, "joke_before_audience"),
            ("joke_before_audience", 0, "end"), ("end", 0, "you"), ("you", 0, null));
        ReferenceHistory.Play(story, "herrax.house.predecessor", House(story, "herrax.house.first_price"), check,
            ("start", 3, "unasked"), ("unasked", 0, "riches"), ("riches", 0, "enemies"), ("enemies", 0, null));
        ReferenceHistory.Play(story, "herrax.house.eye.two", House(story, "herrax.house.eye.one"), check,
            ("start", 0, "caught"), ("caught", 0, null));
        ReferenceHistory.Play(story, "herrax.house.eve", House(story, "herrax.trickster.bait_taken"), check,
            ("start", 0, "sold"), ("sold", 0, "where"), ("where", 0, "think"), ("think", 0, null));
        ReferenceHistory.Play(story, "herrax.house.the_sinners", House(story, "herrax.house.arena"), check,
            ("start", 0, "sinners"), ("sinners", 0, "work"), ("work", 0, "end"), ("end", 0, null));
        ReferenceHistory.Play(story, "herrax.house.the_coin", House(story, "herrax.house.first_price", "herrax.coin_held"), check,
            ("start", 1, "how_many"), ("how_many", 0, null));
        ReferenceHistory.Play(story, "herrax.house.a_night_late", House(story, "herrax.trickster.knife_restored"), check,
            ("start", 0, "cut"), ("cut", 0, "after"), ("after", 0, "said"), ("said", 0, null));
        ReferenceHistory.Play(story, "herrax.house.her_rooms", House(story, "herrax.committed"), check,
            ("start", 1, "rooms_first"), ("rooms_first", 0, "expected"), ("expected", 1, "beside"), ("beside", 0, null));
        foreach (int index in new[] { 0, 1 })
            ReferenceHistory.Play(story, "herrax.trickster.madam.schedule", House(story, "herrax.rokhorn_confessed", "herrax.coin_held"), check,
                ("start", 0, "chair"), ("chair", index, "lesson"), ("lesson", 0, "plan"), ("plan", 0, "named"), ("named", 0, null));
        foreach (int index in new[] { 0, 1, 3, 4, 5, 6 })
        {
            var sale = House(story, "herrax.trickster.primed", "herrax.coin_held");
            bool client = index == 1 || index == 4 || index == 6;
            if (client) sale.Flags.Add("herrax.rokhorn_client");
            if (index == 3 || index == 4) sale.Flags.Add("herrax.trickster.lie.spite");
            if (index == 5 || index == 6) sale.Flags.Add("herrax.trickster.lie.hunger");
            ReferenceHistory.Observe(story, sale);
            var path = new List<(string, int, string?)> { ("start", client ? 1 : 0, client ? "client" : "wary") };
            if (client) path.Add(("client", 0, "wary"));
            path.AddRange(new (string, int, string?)[] { ("wary", index, "blown"), ("blown", 0, "loud") });
            path.Add(("loud", 0, null));
            ReferenceHistory.Play(story, "herrax.trickster.madam.sell_the_night", sale, check, path.ToArray());
            check(sale.Has("herrax.trickster.cost.con_blown"), "Failed con loses its existing cost");
        }
        ReferenceHistory.Play(story, "herrax.trickster.madam.the_night", House(story, "herrax.trickster.bait_taken"), check,
            ("start", 0, "arch"), ("arch", 0, "arch2"), ("arch2", 0, "arch3"), ("arch3", 0, "knife"),
            ("knife", 2, "stayed"), ("stayed", 0, "stayed2"), ("stayed2", 0, "stayed_coin"), ("stayed_coin", 0, null));
        foreach (bool restored in new[] { false, true })
        foreach (int index in new[] { 0, 1 })
        {
            var path = new List<(string, int, string?)>();
            if (restored) path.AddRange(new (string, int, string?)[] { ("closing", 0, "restored"), ("restored", 0, "offer") });
            else path.Add(("closing", 4, "offer"));
            path.AddRange(new (string, int, string?)[] { ("offer", 0, "desire"), ("desire", 0, "thumb"), ("thumb", 0, "threshold"),
                ("threshold", 0, "threshold2"), ("threshold2", index, "cut") });
            ReferenceHistory.Play(story, "herrax.trickster.madam.reachable" + (restored ? "_restored" : ""),
                House(story, "herrax.trickster.lesson_given", "herrax.trickster.knife_restored", "herrax.house.a_night_late"), check, path.ToArray());
        }
        var owed = ReferenceHistory.World(story, 5, "trickster", "herrax.trickster.primed", "herrax.coin_held",
            "minachiv.closed", "chivarro.dead", "chivarro.returned_actor_lost");
        ReferenceHistory.Play(story, "herrax.trickster.owed.night", owed, check,
            ("start", 0, "unsold"), ("unsold", 0, "ask"), ("ask", 0, "promised"), ("promised", 0, null));
        ReferenceHistory.Play(story, "herrax.trickster.late.next_move", ReferenceHistory.World(story, 5, "trickster", "herrax.madam", "herrax.met",
            "minachiv.closed", "chivarro.dead", "chivarro.returned_actor_lost"), check,
            ("start", 0, "met"), ("met", 0, "ask"), ("ask", 0, "door"), ("door", 0, "why"), ("why", 0, "earnest"),
            ("earnest", 0, "earnest_taken"), ("earnest_taken", 0, "promised"), ("promised", 0, null));
        ReferenceHistory.Play(story, "herrax.trickster.late.next_move", ReferenceHistory.World(story, 5, "trickster",
            "minachiv.closed", "chivarro.returned_actor_lost"), check,
            ("start", 2, "stranger_house"), ("stranger_house", 0, "ask_house"), ("ask_house", 0, "door"), ("door", 3, "why_senior"),
            ("why_senior", 2, "earnest_senior"), ("earnest_senior", 0, "earnest_taken"), ("earnest_taken", 0, "promised"), ("promised", 0, null));
        var arue = House(story, "herrax.trickster.morning_served", "arueshalae.in_party");
        var morning = story.Scenes.Single(s => s.Id == "herrax.trickster.react.arueshalae_morning_unheard");
        ReferenceHistory.Play(story, morning.Id, arue, check, ("start", 0, null));
        var lostArue = Program.Copy(arue); lostArue.Flags.Remove(morning.Id);
        lostArue.Flags.Add("arueshalae_dead"); ReferenceHistory.Observe(story, lostArue);
        check(!Rules.Available(story, morning, lostArue), "Former employer reference stages dead Arueshalae");
        ReferenceHistory.Play(story, "herrax.house.rehearsal", House(story, "herrax.trickster.primed"), check,
            ("start", 0, "greed"), ("greed", 0, "greed2"), ("greed2", 0, "done"), ("done", 0, null));
        foreach (int index in new[] { 0, 1 })
            ReferenceHistory.Play(story, "herrax.house.the_girl_upstairs", House(story, "herrax.house.eye.three"), check,
                ("start", index, index == 0 ? "ask_girl" : "drink"), (index == 0 ? "ask_girl" : "drink", 0, "after"), ("after", 0, null));
        foreach (int index in new[] { 0, 1, 2 })
            ReferenceHistory.Play(story, "herrax.house.the_lesson_room", House(story, "herrax.house.forgotten_things"), check,
                ("start", 0, "thief"), ("thief", index, index == 0 ? "finger" : index == 1 ? "street" : "hers"),
                (index == 0 ? "finger" : index == 1 ? "street" : "hers", 0, "end"), ("end", 0, null));
        foreach (int index in new[] { 0, 1 })
            ReferenceHistory.Play(story, "herrax.house.the_one_who_left", House(story, "herrax.house.labyrinth", "arueshalae_dead", "arueshalae.kicked_out"), check,
                ("start", index, index == 0 ? "meant" : "house"), (index == 0 ? "meant" : "house", 0, "end"), ("end", 0, null));
        var closed = House(story, "herrax.house.predecessor", "herrax.closed");
        check(!Rules.Available(story, story.Scenes.Single(s => s.Id == "herrax.house.the_chair"), closed), "Historical chair reopens Herrax");
        var departed = House(story, "herrax.house.predecessor", "herrax.returned_actor_lost");
        check(!Rules.Available(story, story.Scenes.Single(s => s.Id == "herrax.house.the_chair"), departed), "Inherited cushions stage a lost Herrax");

        // Historical possessions are independent of Chivarro; the packet's
        // actual guest still needs her own current body, even after a return.
        var scene = story.Scenes.Single(s => s.Id == "herrax.letters.the_courier");
        var guest = ReferenceHistory.World(story, 5, "trickster", "herrax.committed", "herrax.asked_kill_chivarro",
            "minagho_chivarro.trickster.returned_chivarro");
        var edge = scene.Nodes.Single(n => n.Id == "reply").Choices[2];
        check(Rules.ChoiceAvailable(edge, guest), "Chivarro live participant control unavailable");
        guest.Flags.Add("chivarro.returned_actor_lost"); ReferenceHistory.Observe(story, guest);
        check(!Rules.ChoiceAvailable(edge, guest), "Reference exemption admits lost Chivarro to the packet");
    }
}
