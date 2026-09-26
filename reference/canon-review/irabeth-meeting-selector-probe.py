"""Exercise installed native etude arbitration in detached managed fixtures.

Writes and builds only a fresh temporary project. No save or installed edit.
The full lifecycle boundary is diagnostic, not a passing actor-arrival result.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import tempfile
from zipfile import ZipFile
from xml.sax.saxutils import escape

GAME = Path("D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure")
MANAGED = GAME / "Wrath_Data/Managed"
DOTNET = Path.home() / "AppData/Local/RanRomanceTools/dotnet/dotnet.exe"
GROUP = "997d865aa6f17cc48b480bd62ba02841"
RECORDS = {
    "World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/IrabethNotInDrezen.jbp":
        ("99a03d4f02004b76a5e97c85ba0ec37e", 99),
    "World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/IrabethNotInDrezenCh5_WithGalfrey.jbp":
        ("260454e5186fbd34694a0393097f77b5", 400),
}
with ZipFile(GAME / "blueprints.zip") as archive:
    for path, (guid, priority) in RECORDS.items():
        raw = archive.read(path)
        record = json.loads(raw)
        assert record["AssetId"] == guid
        assert record["Data"]["Priority"] == priority
        assert record["Data"]["m_ConflictingGroups"] == ["!bp_" + GROUP]
        print("VERIFIED", guid, priority, hashlib.sha256(raw).hexdigest(), flush=True)
print("ASSEMBLY", hashlib.sha256((MANAGED / "Assembly-CSharp.dll").read_bytes()).hexdigest(), flush=True)
work = Path(tempfile.mkdtemp(prefix="irabeth-meeting-selector-"))
project = '''<Project Sdk="Microsoft.NET.Sdk">
<PropertyGroup><OutputType>Exe</OutputType><TargetFramework>net48</TargetFramework><LangVersion>latest</LangVersion></PropertyGroup>
<ItemGroup><PackageReference Include="Microsoft.NETFramework.ReferenceAssemblies" Version="1.0.3" PrivateAssets="all" />
<Reference Include="{managed}/*.dll" Exclude="{managed}/System*.dll;{managed}/mscorlib.dll;{managed}/netstandard.dll" Private="false" /></ItemGroup>
</Project>'''
(work / "Probe.csproj").write_text(project.format(managed=escape(str(MANAGED))), encoding="utf-8")
SOURCE = r'''
using System;
using System.IO;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Kingmaker.EntitySystem;
using Kingmaker.View.Spawners;
class Probe {
    static void Main() {
        AppDomain.CurrentDomain.AssemblyResolve += (sender, args) => {
            string name = new AssemblyName(args.Name).Name + ".dll";
            foreach (var directory in new[] { @"MANAGED_PATH", @"MANAGED_PATH/UnityModManager" }) {
                string file = Path.Combine(directory, name);
                if (File.Exists(file)) return Assembly.LoadFrom(file);
            }
            return null;
        };
        Inspect();
    }


    static readonly BindingFlags Inst=BindingFlags.Instance|BindingFlags.NonPublic|BindingFlags.Public;
    static FieldInfo Field(Type t,string n) { for(;t!=null;t=t.BaseType) {var f=t.GetField(n,Inst|BindingFlags.DeclaredOnly);if(f!=null)return f;}throw new Exception("Missing field "+n); }
    static void Set(object o,string n,object v) { Field(o.GetType(),n).SetValue(o,v); }
    static object Bare(Type t) { return FormatterServices.GetUninitializedObject(t); }
    [MethodImpl(MethodImplOptions.NoInlining)]
    static void Inspect() {
      typeof(Owlcat.Runtime.Core.Logging.Logger).GetField("s_Instance",BindingFlags.Static|BindingFlags.NonPublic).SetValue(null,new Owlcat.Runtime.Core.Logging.Logger {Enabled=true});
      var game=(Kingmaker.Game)Bare(typeof(Kingmaker.Game));
      var player=(Kingmaker.Player)Bare(typeof(Kingmaker.Player));
      var state=(Kingmaker.EntitySystem.PersistentState)Bare(typeof(Kingmaker.EntitySystem.PersistentState));
      Set(state,"PlayerState",player);Set(game,"State",state);
      typeof(Kingmaker.Game).GetField("s_Instance",BindingFlags.Static|BindingFlags.NonPublic).SetValue(null,game);
      var system=(Kingmaker.AreaLogic.Etudes.EtudesSystem)Bare(typeof(Kingmaker.AreaLogic.Etudes.EtudesSystem));
      Set(system,"m_HeldConflictingGroups",new System.Collections.Generic.Dictionary<Kingmaker.AreaLogic.Etudes.BlueprintEtudeConflictingGroup,Kingmaker.AreaLogic.Etudes.BlueprintEtude>());
      Set(player,"EtudesSystem",system);
      var manager=new Kingmaker.EntitySystem.EntityFactsManager(system);
      Set(system,"Facts",manager);
      var tree=manager.EnsureFactProcessor<Kingmaker.AreaLogic.Etudes.EtudesTree>();
      var group=new Kingmaker.AreaLogic.Etudes.BlueprintEtudeConflictingGroup {AssetGuid=Kingmaker.Blueprints.BlueprintGuid.Parse("997d865aa6f17cc48b480bd62ba02841"),name="Irabeth_fixture_group"};
      Func<string,int,Kingmaker.AreaLogic.Etudes.Etude> create=(id,prio)=> {
        var bp=new Kingmaker.AreaLogic.Etudes.BlueprintEtude {AssetGuid=Kingmaker.Blueprints.BlueprintGuid.Parse(id),name="fixture_"+prio};
        Set(bp,"Priority",prio);
        var gf=Field(bp.GetType(),"m_ConflictingGroups");
        var gs=(System.Collections.IList)Activator.CreateInstance(gf.FieldType);
        var reference=(Kingmaker.Blueprints.BlueprintReferenceBase)Activator.CreateInstance(gf.FieldType.GetGenericArguments()[0]);
        Set(reference,"deserializedGuid",group.AssetGuid);Set(reference,"<Cached>k__BackingField",group);gs.Add(reference);gf.SetValue(bp,gs);
        var e=(Kingmaker.AreaLogic.Etudes.Etude)Bare(typeof(Kingmaker.AreaLogic.Etudes.Etude));Set(e,"<Blueprint>k__BackingField",bp);
        ((System.Collections.Generic.List<Kingmaker.EntitySystem.EntityFact>)Field(manager.GetType(),"m_Facts").GetValue(manager)).Add(e);
        return e;
      };

      var departure=create("99a03d4f02004b76a5e97c85ba0ec37e",99);
      var meeting=create("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",100);
      var equal=create("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",100);
      var lower=create("cccccccccccccccccccccccccccccccc",0);
      var unknown=create("dddddddddddddddddddddddddddddddd",-10);
      var expedition=create("260454e5186fbd34694a0393097f77b5",400);
      var starts=(System.Collections.Generic.HashSet<Kingmaker.AreaLogic.Etudes.Etude>)Field(tree.GetType(),"m_StartingSet").GetValue(tree);
      var stops=(System.Collections.Generic.HashSet<Kingmaker.AreaLogic.Etudes.Etude>)Field(tree.GetType(),"m_StoppingSet").GetValue(tree);
      var filter=tree.GetType().GetMethod("FilterOnActors",Inst);
      int count=0;
      Action<bool,string> check=(ok,msg)=> { if(!ok)throw new Exception(msg);count++;Console.WriteLine("PASS "+msg); };
      Action<Kingmaker.AreaLogic.Etudes.Etude,Kingmaker.AreaLogic.Etudes.Etude[]> prepare=(held,pending)=> {
          starts.Clear();stops.Clear();system.SetConflictingGroupTask(group,held);
          foreach(var e in pending)starts.Add(e);
      };
      prepare(departure,new[]{meeting});filter.Invoke(tree,null);
      check(starts.Contains(meeting)&&stops.Contains(departure),"meeting100 schedules departure99 to stop");
      prepare(equal,new[]{meeting});filter.Invoke(tree,null);
      check(!starts.Contains(meeting)&&!stops.Contains(equal),"held native100 blocks equal meeting100");
      prepare(meeting,new[]{equal});filter.Invoke(tree,null);
      check(!starts.Contains(equal)&&!stops.Contains(meeting),"held meeting100 blocks equal native100 without withdrawal");
      prepare(expedition,new[]{meeting});filter.Invoke(tree,null);
      check(!starts.Contains(meeting)&&!stops.Contains(expedition),"queen expedition400 blocks meeting100");
      prepare(unknown,new[]{meeting});filter.Invoke(tree,null);
      check(starts.Contains(meeting)&&stops.Contains(unknown),"native filter would steal unknown lower-priority holder");
      prepare(meeting,new[]{lower});filter.Invoke(tree,null);
      check(!starts.Contains(lower),"held meeting100 suppresses pending event0");
      prepare(meeting,new[]{lower});stops.Add(meeting);filter.Invoke(tree,null);
      check(!starts.Contains(lower),"scheduled stop alone does not release held claim in this filter pass");
      tree.RemoveFromPlaying(meeting);
      check(system.GetConflictingGroupTask(group)==null,"native RemoveFromPlaying releases only actual meeting holder");
      starts.Clear();stops.Clear();starts.Add(lower);filter.Invoke(tree,null);
      check(starts.Contains(lower),"event0 becomes selectable after actual claim release");
      tree.AddToPlaying(lower);
      check(object.ReferenceEquals(system.GetConflictingGroupTask(group),lower.Blueprint),"native AddToPlaying commits the same event claim");
      tree.RemoveFromPlaying(meeting);
      check(object.ReferenceEquals(system.GetConflictingGroupTask(group),lower.Blueprint),"stale meeting release preserves replacement event holder");
      tree.RemoveFromPlaying(lower);starts.Clear();stops.Clear();starts.Add(departure);starts.Add(lower);filter.Invoke(tree,null);
      check(starts.Contains(departure)&&!starts.Contains(lower),"eligible native departure99 still outranks event0 after meeting release");
      tree.AddToPlaying(departure);
      check(object.ReferenceEquals(system.GetConflictingGroupTask(group),departure.Blueprint)&&!departure.IsCompleted,"release restores exact original departure claim without completion");
      prepare(departure,new[]{meeting});filter.Invoke(tree,null);tree.RemoveFromPlaying(departure);tree.AddToPlaying(meeting);
      check(object.ReferenceEquals(system.GetConflictingGroupTask(group),meeting.Blueprint)&&!meeting.IsCompleted,"same meeting object can reacquire after another native selection");
      tree.RemoveFromPlaying(meeting);starts.Clear();stops.Clear();starts.Add(equal);filter.Invoke(tree,null);
      check(starts.Contains(equal),"native100 becomes selectable after meeting claim release");
      prepare(null,new[]{lower,meeting});filter.Invoke(tree,null);
      check(starts.Contains(meeting)&&!starts.Contains(lower),"native filter sorts pending priorities rather than insertion order");
      Console.WriteLine("PASS "+count+" actual native arbitration and claim assertions; no actor or full activation execution.");
      try {
        Set(meeting,"Children",new System.Collections.Generic.List<Kingmaker.AreaLogic.Etudes.Etude>());
        Set(meeting,"<Manager>k__BackingField",manager);
        Set(meeting,"Components",new System.Collections.Generic.List<Kingmaker.EntitySystem.EntityFactComponent>());
        ((System.Collections.Generic.List<Kingmaker.AreaLogic.Etudes.Etude>)Field(tree.GetType(),"m_Roots").GetValue(tree)).Add(meeting);
        meeting.Blueprint.ActivationCondition=new Kingmaker.ElementsSystem.ConditionsChecker {Conditions=new Kingmaker.ElementsSystem.Condition[0]};
        var linked=Field(meeting.Blueprint.GetType(),"m_LinkedCampaigns");linked.SetValue(meeting.Blueprint,Activator.CreateInstance(linked.FieldType));
        tree.GetType().GetMethod("SelectPlayingEtudes",Inst).Invoke(tree,null);
        foreach(var entry in (System.Collections.Generic.LinkedList<Owlcat.Runtime.Core.Logging.LogInfo>)Field(typeof(Owlcat.Runtime.Core.Logging.Logger),"m_RecentMessages").GetValue(Owlcat.Runtime.Core.Logging.Logger.Instance)) if(entry.IsException) Console.WriteLine("NATIVE CAUGHT EXCEPTION: "+entry.Message);
        Console.WriteLine("FULL SELECTOR OBSERVATION: starts="+starts.Count+", IsActive="+meeting.IsActive+", IsPlaying="+meeting.IsPlaying+", held="+(system.GetConflictingGroupTask(group)?.name ?? "none"));
        typeof(Kingmaker.AreaLogic.Etudes.Etude).GetMethod("OnActivate",Inst).Invoke(meeting,null);
      } catch(Exception error) {
        while(error is TargetInvocationException && error.InnerException!=null)error=error.InnerException;
        Console.WriteLine("FULL SELECTOR BOUNDARY: "+error.GetType().FullName+": "+error.Message+"\n"+error.StackTrace);
      }

    }
}
'''
(work / 'Program.cs').write_text(SOURCE.replace('MANAGED_PATH', str(MANAGED)), encoding='utf-8')
print('TEMP', work, flush=True)
subprocess.run([str(DOTNET), 'build', str(work / 'Probe.csproj'), '--nologo', '-v', 'quiet'], check=True)
subprocess.run([str(work / 'bin/Debug/net48/Probe.exe')], check=True)
