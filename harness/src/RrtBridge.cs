using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;

namespace RRT.TestHarness
{
    /// <summary>
    /// Reflection access to RanRomance.Tirabade internals. Pure: it names game types only as strings,
    /// so the offline self-test can validate it against the built RRT DLL without Unity.
    /// </summary>
    public sealed class RrtBridge
    {
        public const string AssemblyName = "RanRomance.Tirabade";
        const BindingFlags S = BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;
        const BindingFlags I = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;

        /// <summary>Every member the harness uses, with the type shape it expects ("*" = any).</summary>
        public static readonly (string Type, string Member, string Kind, string Shape)[] Expectations =
        {
            ("Tirabade.Main", "initialized", "static-field", "Boolean"),
            ("Tirabade.Main", "enabled", "static-field", "Boolean"),
            ("Tirabade.Main", "error", "static-field", "String"),
            ("Tirabade.Main", "degraded", "static-field", "HashSet<String>"),
            ("Tirabade.Main", "warnings", "static-field", "List<String>"),
            ("Tirabade.Main", "story", "static-field", "Story"),
            ("Tirabade.Main", "dialogs", "static-field", "Dictionary<String,BlueprintDialog>"),
            ("Tirabade.Main", "flags", "static-field", "Dictionary<String,BlueprintUnlockableFlag>"),
            ("Tirabade.Main", "State", "static-method()", "Snapshot"),
            ("Tirabade.Main", "Set", "static-method(String,Int32)", "Void"),
            ("Tirabade.Main", "PresenceReport", "static-method()", "String[]"),
            ("Tirabade.Main", "PresenceClick", "static-method(String)", "Boolean"),
            ("Tirabade.Main+RouteCondition", "CheckCondition", "instance-method()", "Boolean"),
            ("Tirabade.Main+RouteAction", "RunAction", "instance-method()", "Void"),
            ("Tirabade.Story", "Scenes", "field", "List<Scene>"),
            ("Tirabade.Story", "Relationships", "field", "Dictionary<String,Relationship>"),
            ("Tirabade.Relationship", "StartedFlag", "field", "String"),
            ("Tirabade.Scene", "Id", "field", "String"),
            ("Tirabade.Scene", "Relationship", "field", "String"),
            ("Tirabade.Scene", "Owner", "field", "String"),
            ("Tirabade.Scene", "Requires", "field", "String[]"),
            ("Tirabade.Scene", "RequiresAnyGroups", "field", "String[][]"),
            ("Tirabade.Scene", "MinChapter", "field", "Int32"),
            ("Tirabade.Scene", "MaxChapter", "field", "Int32"),
            ("Tirabade.Scene", "Nodes", "field", "List<Node>"),
            ("Tirabade.Scene", "ContactUnit", "field", "String"),
            ("Tirabade.Scene", "NativeReturnCue", "field", "String"),
            ("Tirabade.Node", "Id", "field", "String"),
            ("Tirabade.Node", "Choices", "field", "List<Choice>"),
            ("Tirabade.Choice", "Next", "field", "String"),
            ("Tirabade.Choice", "Abort", "field", "Boolean"),
            ("Tirabade.Choice", "Revive", "field", "String"),
            ("Tirabade.Choice", "Check", "field", "SkillCheck"),
            ("Tirabade.Choice", "Set", "field", "String[]"),
            ("Tirabade.Choice", "Requires", "field", "String[]"),
            ("Tirabade.Choice", "Forbids", "field", "String[]"),
            ("Tirabade.Snapshot", "Chapter", "field", "Int32"),
            ("Tirabade.Snapshot", "Hour", "field", "Int32"),
            ("Tirabade.Snapshot", "Area", "field", "String"),
            ("Tirabade.Snapshot", "Flags", "field", "HashSet<String>"),
            ("Tirabade.Snapshot", "AvailableContacts", "field", "HashSet<String>"),
            ("Tirabade.Snapshot", "Times", "field", "Dictionary<String,Int32>"),
            ("Tirabade.Rules", "Available", "static-method(Story,Scene,Snapshot)", "Boolean"),
            ("Tirabade.Rules", "ContactAvailable", "static-method(Story,Scene,Snapshot)", "Boolean"),
            ("Tirabade.Rules", "Match", "static-method(IEnumerable<String>,IEnumerable<String>,Snapshot)", "Boolean"),
            ("Tirabade.Rules", "IsRemote", "static-method(Scene)", "Boolean"),
        };

        public static string Shape(Type t)
        {
            if (t.IsArray) return Shape(t.GetElementType()!) + "[]";
            if (Nullable.GetUnderlyingType(t) is Type u) return Shape(u) + "?";
            if (!t.IsGenericType) return t.Name;
            string name = t.Name.Substring(0, t.Name.IndexOf('`'));
            return name + "<" + string.Join(",", t.GetGenericArguments().Select(Shape)) + ">";
        }

        static MemberInfo? Find(Type type, string member, string kind)
        {
            if (kind.Contains("field"))
                return type.GetField(member, kind.StartsWith("static") ? S : I | S);
            string paramList = kind.Substring(kind.IndexOf('(') + 1).TrimEnd(')');
            var wanted = paramList.Length == 0 ? new string[0] : paramList.Split(',');
            var flags = kind.StartsWith("static") ? S : I;
            return type.GetMethods(flags | BindingFlags.DeclaredOnly)
                .FirstOrDefault(m => m.Name == member && m.GetParameters().Select(p => Shape(p.ParameterType)).SequenceEqual(wanted));
        }

        /// <summary>Checks every expectation; returns human-readable problems (empty = all good).</summary>
        public static List<string> Validate(Assembly asm)
        {
            var problems = new List<string>();
            foreach (var e in Expectations)
            {
                Type? type;
                try { type = asm.GetType(e.Type, false); }
                catch (Exception ex) { problems.Add(e.Type + ": " + ex.Message); continue; }
                if (type == null) { problems.Add("missing type " + e.Type); continue; }
                MemberInfo? m;
                try { m = Find(type, e.Member, e.Kind); }
                catch (Exception ex) { problems.Add(e.Type + "." + e.Member + ": " + ex.Message); continue; }
                if (m == null) { problems.Add("missing " + e.Kind + " " + e.Type + "." + e.Member); continue; }
                string actual;
                try { actual = m is FieldInfo f ? Shape(f.FieldType) : Shape(((MethodInfo)m).ReturnType); }
                catch (Exception ex) { problems.Add(e.Type + "." + e.Member + " type unresolved: " + ex.Message); continue; }
                if (e.Shape != "*" && actual != e.Shape)
                    problems.Add(e.Type + "." + e.Member + " has type " + actual + ", expected " + e.Shape);
            }
            return problems;
        }

        // ---- runtime accessors -------------------------------------------------------------------

        public Assembly Assembly { get; }
        readonly Type main, rules, sceneT, nodeT, choiceT, snapshotT, storyT, relationshipT;
        readonly MethodInfo state, set, available, contactAvailable, match, isRemote, presenceReport, presenceClick;

        public RrtBridge(Assembly asm)
        {
            Assembly = asm;
            Type T(string n) => asm.GetType(n, true)!;
            main = T("Tirabade.Main"); rules = T("Tirabade.Rules"); sceneT = T("Tirabade.Scene");
            nodeT = T("Tirabade.Node"); choiceT = T("Tirabade.Choice"); snapshotT = T("Tirabade.Snapshot");
            storyT = T("Tirabade.Story"); relationshipT = T("Tirabade.Relationship");
            MethodInfo M(Type t, string name, string kind) => (MethodInfo)(Find(t, name, kind) ?? throw new MissingMethodException(t.FullName, name));
            state = M(main, "State", "static-method()");
            set = M(main, "Set", "static-method(String,Int32)");
            presenceReport = M(main, "PresenceReport", "static-method()");
            presenceClick = M(main, "PresenceClick", "static-method(String)");
            available = M(rules, "Available", "static-method(Story,Scene,Snapshot)");
            contactAvailable = M(rules, "ContactAvailable", "static-method(Story,Scene,Snapshot)");
            match = M(rules, "Match", "static-method(IEnumerable<String>,IEnumerable<String>,Snapshot)");
            isRemote = M(rules, "IsRemote", "static-method(Scene)");
        }

        public static Assembly? FindLoaded() =>
            AppDomain.CurrentDomain.GetAssemblies().FirstOrDefault(a => a.GetName().Name == AssemblyName);

        object? Static(string name) => main.GetField(name, S)!.GetValue(null);
        static object? Get(object o, string field) => o.GetType().GetField(field, I)!.GetValue(o);
        static T GetAs<T>(object o, string field) => (T)Get(o, field)!;

        public bool Initialized => (bool)Static("initialized")!;
        public bool Enabled => (bool)Static("enabled")!;
        public string? Error => (string?)Static("error");
        public List<string> Degraded => ((IEnumerable<string>?)Static("degraded") ?? Enumerable.Empty<string>()).OrderBy(x => x, StringComparer.Ordinal).ToList();
        public List<string> Warnings => ((IEnumerable<string>?)Static("warnings") ?? Enumerable.Empty<string>()).ToList();
        public object? Story => Static("story");
        public IDictionary Dialogs => (IDictionary)Static("dialogs")!;
        public IDictionary Flags => (IDictionary)Static("flags")!;

        public object State() => Invoke(state, null);
        /// <summary>E12: one line per returned presence ("key [mode] wanted; status"), for verifying a presence appears.</summary>
        public string[] PresenceReport() => (string[])Invoke(presenceReport, null);
        /// <summary>E12c: click a presence like the player; true when its RRT hub dialog started.</summary>
        public bool PresenceClick(string key) => (bool)Invoke(presenceClick, key);
        public void Set(string key, int value = 1) => Invoke(set, key, value);

        static object Invoke(MethodInfo m, params object?[]? args)
        {
            try { return m.Invoke(null, args)!; }
            catch (TargetInvocationException ex) when (ex.InnerException != null)
            {
                System.Runtime.ExceptionServices.ExceptionDispatchInfo.Capture(ex.InnerException).Throw();
                throw;
            }
        }

        public bool Available(object scene, object snapshot) => (bool)Invoke(available, Story, scene, snapshot);
        public bool ContactAvailable(object scene, object snapshot) => (bool)Invoke(contactAvailable, Story, scene, snapshot);
        public bool Match(IEnumerable<string> requires, IEnumerable<string> forbids, object snapshot) => (bool)Invoke(match, requires, forbids, snapshot);
        public bool IsRemote(object scene) => (bool)Invoke(isRemote, scene);

        public IList Scenes => GetAs<IList>(Story!, "Scenes");
        public static string SceneId(object scene) => GetAs<string>(scene, "Id");
        public static string SceneRelationship(object scene) => GetAs<string>(scene, "Relationship");
        public static string SceneOwner(object scene) => GetAs<string>(scene, "Owner");
        public static string[] SceneRequires(object scene) => GetAs<string[]>(scene, "Requires");
        public static string[][] SceneRequiresAnyGroups(object scene) => GetAs<string[][]>(scene, "RequiresAnyGroups");
        public static int SceneMinChapter(object scene) => GetAs<int>(scene, "MinChapter");
        public static int SceneMaxChapter(object scene) => GetAs<int>(scene, "MaxChapter");
        public static string? SceneContactUnit(object scene) => (string?)Get(scene, "ContactUnit");
        public static IList SceneNodes(object scene) => GetAs<IList>(scene, "Nodes");
        public static string NodeId(object node) => GetAs<string>(node, "Id");
        public static IList NodeChoices(object node) => GetAs<IList>(node, "Choices");

        public string? StartedFlag(string relationship)
        {
            var map = GetAs<IDictionary>(Story!, "Relationships");
            return map.Contains(relationship) ? GetAs<string>(map[relationship]!, "StartedFlag") : null;
        }

        public sealed class ChoiceInfo
        {
            public object Scene = null!;
            public object Choice = null!;
            public string SceneId = "", NodeId = "";
            public int Index;
            public string? Next, Revive;
            public bool Abort, HasCheck;
            public string[] Set = new string[0], Requires = new string[0], Forbids = new string[0];
            public bool Terminal => Next == null && !HasCheck && !Abort;
            public string Label => SceneId + "/" + NodeId + "/" + Index;
        }

        /// <summary>Map of RRT answer blueprint names ("RRT_answer.&lt;scene&gt;.&lt;node&gt;.&lt;i&gt;", see Main.BuildScene) to story choices.</summary>
        public Dictionary<string, ChoiceInfo> ChoiceIndex()
        {
            var map = new Dictionary<string, ChoiceInfo>(StringComparer.Ordinal);
            foreach (var scene in Scenes)
            {
                string sid = SceneId(scene!);
                foreach (var node in SceneNodes(scene!))
                {
                    string nid = NodeId(node!);
                    var choices = NodeChoices(node!);
                    for (int i = 0; i < choices.Count; i++)
                    {
                        var c = choices[i]!;
                        map["RRT_answer." + sid + "." + nid + "." + i] = new ChoiceInfo
                        {
                            Scene = scene!, Choice = c, SceneId = sid, NodeId = nid, Index = i,
                            Next = (string?)Get(c, "Next"), Revive = (string?)Get(c, "Revive"),
                            Abort = (bool)Get(c, "Abort")!, HasCheck = Get(c, "Check") != null,
                            Set = GetAs<string[]>(c, "Set"), Requires = GetAs<string[]>(c, "Requires"), Forbids = GetAs<string[]>(c, "Forbids"),
                        };
                    }
                }
            }
            return map;
        }

        public static SnapshotData ToData(object snapshot)
        {
            var d = new SnapshotData
            {
                Chapter = GetAs<int>(snapshot, "Chapter"),
                Hour = GetAs<int>(snapshot, "Hour"),
                Area = GetAs<string>(snapshot, "Area") ?? "",
                Flags = GetAs<IEnumerable<string>>(snapshot, "Flags").OrderBy(x => x, StringComparer.Ordinal).ToList(),
                AvailableContacts = GetAs<IEnumerable<string>>(snapshot, "AvailableContacts").OrderBy(x => x, StringComparer.Ordinal).ToList(),
            };
            foreach (var kv in GetAs<IDictionary<string, int>>(snapshot, "Times")) d.Times[kv.Key] = kv.Value;
            return d;
        }

        public static HashSet<string> FlagSet(object snapshot) =>
            new HashSet<string>(GetAs<IEnumerable<string>>(snapshot, "Flags"), StringComparer.Ordinal);
    }
}
