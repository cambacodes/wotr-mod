using System;
using System.IO;
using System.Reflection;
using System.Collections;
using System.Collections.Generic;

public static class ManagedProbe
{
    public static int Main(string[] args)
    {
        string managed = args[0];
        AppDomain.CurrentDomain.AssemblyResolve += delegate(object sender, ResolveEventArgs e)
        {
            string filename = new AssemblyName(e.Name).Name + ".dll";
            foreach (string dir in new[] { managed, Path.Combine(managed, "UnityModManager") })
            {
                string path = Path.Combine(dir, filename);
                if (File.Exists(path)) return Assembly.LoadFrom(path);
            }
            return null;
        };
        try
        {
            Assembly game = Assembly.LoadFrom(Path.Combine(managed, "Assembly-CSharp.dll"));
            foreach (string name in new[] {
                "Kingmaker.Blueprints.SimpleBlueprint",
                "Kingmaker.DialogSystem.Blueprints.BlueprintAnswer",
                "Kingmaker.DialogSystem.Blueprints.BlueprintAnswersList",
                "Kingmaker.DialogSystem.Blueprints.BlueprintBookPage",
                "Kingmaker.DialogSystem.Blueprints.BlueprintDialog",
                "Kingmaker.Localization.LocalizationPack" })
            {
                object instance = Activator.CreateInstance(game.GetType(name, true));
                MethodInfo enable = instance.GetType().GetMethod("OnEnable");
                if (enable != null) enable.Invoke(instance, null);
                Console.WriteLine("CREATED " + name);
            }
            Type localization = game.GetType("Kingmaker.Localization.LocalizationManager", true);
            localization.GetField("CurrentPack").SetValue(null,
                Activator.CreateInstance(game.GetType("Kingmaker.Localization.LocalizationPack", true)));
            Console.WriteLine("SET LocalizationManager.CurrentPack");
            object cache = game.GetType("Kingmaker.Blueprints.ResourcesLibrary", true)
                .GetField("BlueprintsCache").GetValue(null);
            Console.WriteLine("CACHE " + cache.GetType().FullName);
            if (args.Length > 2)
            {
                Assembly umm = Assembly.LoadFrom(Path.Combine(managed, "UnityModManager/UnityModManager.dll"));
                Type infoType = umm.GetType("UnityModManagerNet.UnityModManager+ModInfo", true);
                object info = Activator.CreateInstance(infoType);
                infoType.GetField("Id").SetValue(info, "ManagedProbe");
                infoType.GetField("Version").SetValue(info, "1.0.0");
                infoType.GetField("ManagerVersion").SetValue(info, "0.27.11");
                object entry = Activator.CreateInstance(umm.GetType("UnityModManagerNet.UnityModManager+ModEntry", true), info, Path.GetDirectoryName(args[1]));
                Console.WriteLine("CREATED real ModEntry and ModLogger");
                Assembly mod = Assembly.LoadFrom(args[1]);
                Type main = mod.GetType("Tirabade.Main", true);
                Type storyType = mod.GetType("Tirabade.Story", true);
                Type json = Assembly.LoadFrom(Path.Combine(managed, "Newtonsoft.Json.dll")).GetType("Newtonsoft.Json.JsonConvert", true);
                object story = json.GetMethod("DeserializeObject", new[] { typeof(string), typeof(Type) })
                    .Invoke(null, new object[] { File.ReadAllText(args[2]), storyType });
                main.GetField("entry", BindingFlags.NonPublic | BindingFlags.Static).SetValue(null, entry);
                main.GetField("story", BindingFlags.NonPublic | BindingFlags.Static).SetValue(null, story);
                Type guidType = game.GetType("Kingmaker.Blueprints.BlueprintGuid", true);
                MethodInfo parse = guidType.GetMethod("Parse", new[] { typeof(string) });
                MethodInfo add = cache.GetType().GetMethod("AddCachedBlueprint");
                var seeded = new HashSet<string>();
                Action<string, string> seed = delegate(string guid, string typename)
                {
                    if (!seeded.Add(guid)) return;
                    object bp = Activator.CreateInstance(game.GetType(typename, true));
                    object id = parse.Invoke(null, new object[] { guid });
                    bp.GetType().GetField("AssetGuid").SetValue(bp, id);
                    bp.GetType().GetField("name").SetValue(bp, "Fixture_" + guid);
                    add.Invoke(cache, new[] { id, bp });
                };
                MethodInfo targets = mod.GetType("Tirabade.Rules", true).GetMethod("EntryTargets");
                foreach (object scene in (IEnumerable)storyType.GetField("Scenes").GetValue(story))
                    foreach (string guid in (IEnumerable)targets.Invoke(null, new[] { scene }))
                        seed(guid, "Kingmaker.DialogSystem.Blueprints.BlueprintAnswersList");
                foreach (DictionaryEntry pair in (IDictionary)storyType.GetField("Etudes").GetValue(story))
                    seed((string)pair.Value, "Kingmaker.AreaLogic.Etudes.BlueprintEtude");
                foreach (string guid in new[] { "ed4baeaf69394754902344f0598d7e5a", "ced82f299d246f448b48afa0b630dd70" })
                    seed(guid, "Kingmaker.DialogSystem.Blueprints.BlueprintCueSequence");
                Console.WriteLine("Seeded actual blueprint types: " + seeded.Count);
                main.GetMethod("Build", BindingFlags.NonPublic | BindingFlags.Static).Invoke(null, null);
                Console.WriteLine("BUILD initialized=" + main.GetField("initialized", BindingFlags.NonPublic | BindingFlags.Static).GetValue(null));
                Console.WriteLine("BUILD error=" + main.GetField("error", BindingFlags.NonPublic | BindingFlags.Static).GetValue(null));
                if (!(bool)main.GetField("initialized", BindingFlags.NonPublic | BindingFlags.Static).GetValue(null)) return 2;
            }
            foreach (string name in new[] { "Kingmaker.UnitLogic.UnitDescriptor", "Kingmaker.EntitySystem.Entities.UnitEntityData", "Kingmaker.EntitySystem.EntityService", "Kingmaker.View.Spawners.UnitSpawnerBase" })
            {
                Type type = game.GetType(name);
                if (type == null) continue;
                foreach (MethodInfo method in type.GetMethods(BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static))
                    if (method.Name.Contains("Resurrect") || method.Name.Contains("Faction") || method.Name.Contains("GetEntity") || method.Name.Contains("Respawn"))
                        Console.WriteLine(name + " " + method);
            }
            return 0;
        }
        catch (Exception ex)
        {
            while (ex.InnerException != null) ex = ex.InnerException;
            Console.WriteLine(ex.GetType().FullName + ": " + ex.Message);
            Console.WriteLine(ex.StackTrace);
            return 1;
        }
    }
}
