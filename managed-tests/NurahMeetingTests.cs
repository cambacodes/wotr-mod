using System;
using System.Collections.Generic;
using System.Collections;
using System.Reflection;
using System.Runtime.Serialization;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.EntitySystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.UnitLogic;
using Kingmaker.View.Spawners;
using System.Linq;
using Kingmaker;
using Kingmaker.AreaLogic.Cutscenes;
using Kingmaker.Blueprints.Area;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Conditions;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.Designers.EventConditionActionSystem.NamedParameters;
using Kingmaker.ElementsSystem;
using Newtonsoft.Json;

internal static class NurahMeetingTests
{
    private const BindingFlags Members = BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;
    private static void Set(object value, string name, object data)
    {
        for (Type? type = value.GetType(); type != null; type = type.BaseType)
        {
            var field = type.GetField(name, Members | BindingFlags.DeclaredOnly);
            if (field == null) continue;
            field.SetValue(value, data); return;
        }
        throw new Exception("Missing native fixture field: " + name);
    }
    private static T Bare<T>() => (T)FormatterServices.GetUninitializedObject(typeof(T));

    internal static void Run(Action<bool, string> check)
    {
        var service = typeof(Tirabade.Main).Assembly.GetType("Tirabade.NurahMeeting", true)!;
        string Constant(string name) => (string)service.GetField(name, Members)!.GetRawConstantValue()!;
        SimpleBlueprint Resolve(string id) => id == Constant("Finale")
            ? (SimpleBlueprint)new BlueprintCue { AssetGuid = BlueprintGuid.Parse(id) }
            : new BlueprintEtude { AssetGuid = BlueprintGuid.Parse(id) };
        var observer = Activator.CreateInstance(service, Members, null,
            new object[] { new Func<string, SimpleBlueprint>(Resolve) }, null);
        check(observer != null, "Verified typed parent bindings did not construct observer");
        bool rejected = false;
        try { Activator.CreateInstance(service, Members, null, new object[] {
            new Func<string, SimpleBlueprint>(id => new BlueprintEtude { AssetGuid = BlueprintGuid.Parse(Constant("Romance")) }) }, null); }
        catch (TargetInvocationException error) { rejected = error.InnerException is InvalidOperationException; }
        check(rejected, "Resolver aliases were accepted as independent native bindings");
        var state = new SceneEntitiesState("DrezenCapital_Default_Mechanics");
        var states = new[] { state };
        var registry = new Dictionary<string, EntityDataBase>();
        bool loaded = true;
        string area = Constant("Capital");
        UnitEntityData? Inspect() => (UnitEntityData?)service.GetMethod("Inspect", Members)!.Invoke(null, new object[] {
            area, states, new Func<SceneEntitiesState, bool>(_ => loaded),
            new Func<string, EntityDataBase?>(id => registry.TryGetValue(id, out var value) ? value : null) });
        var spawner = Bare<UnitSpawnerBase.MyData>();
        Set(spawner, "<UniqueId>k__BackingField", Constant("Spawner"));
        Set(spawner, "<HoldingState>k__BackingField", state);
        state.AllEntityData.Add(spawner); registry[spawner.UniqueId] = spawner;
        check(Inspect() == null, "Never-spawned Nurah became correspondence evidence");
        spawner.HasSpawned = true;
        object reference = default(UnitReference);
        Set(reference, "m_UniqueId", "original-nurah");
        Set(spawner, "m_SpawnedUnit", reference);
        check(Inspect() == null, "Missing retained actor became correspondence evidence");
        UnitEntityData Unit(string id)
        {
            var actor = Bare<UnitEntityData>(); var descriptor = Bare<UnitDescriptor>(); var life = Bare<UnitState>();
            Set(actor, "<UniqueId>k__BackingField", id); Set(actor, "<HoldingState>k__BackingField", state);
            Set(actor, "<Descriptor>k__BackingField", descriptor); Set(descriptor, "<Unit>k__BackingField", actor);
            Set(descriptor, "<Blueprint>k__BackingField", new BlueprintUnit { AssetGuid = BlueprintGuid.Parse(Constant("Unit")) });
            Set(descriptor, "State", life); Set(life, "<LifeState>k__BackingField", UnitLifeState.Conscious);
            return actor;
        }
        var actor = Unit("original-nurah");
        state.AllEntityData.Add(actor); registry[actor.UniqueId] = actor;
        check(ReferenceEquals(Inspect(), actor), "Exact retained living actor was rejected");
        check(actor.View == null, "Fixture unexpectedly provided a physical Unity view");
        loaded = false; check(Inspect() == null, "Unloaded source granted access"); loaded = true;
        area = "wrong-area"; check(Inspect() == null, "Wrong area granted access"); area = Constant("Capital");
        spawner.HasDied = true; check(Inspect() == null, "Historical death silently became an authorized revival"); spawner.HasDied = false;
        Set(actor.State, "<LifeState>k__BackingField", UnitLifeState.Dead);
        check(Inspect() == null, "Current dead actor granted access"); Set(actor.State, "<LifeState>k__BackingField", UnitLifeState.Conscious);
        Set(actor.State, "<IsFinallyDead>k__BackingField", true);
        check(Inspect() == null, "Finally dead actor granted access"); Set(actor.State, "<IsFinallyDead>k__BackingField", false);
        Set(actor, "<DestroyMark>k__BackingField", true);
        check(Inspect() == null, "Removed actor granted access"); Set(actor, "<DestroyMark>k__BackingField", false);
        Set(spawner, "<DestroyMark>k__BackingField", true);
        check(Inspect() == null, "Removed spawner granted access"); Set(spawner, "<DestroyMark>k__BackingField", false);
        var duplicate = Unit("duplicate-nurah"); state.AllEntityData.Add(duplicate);
        check(Inspect() == null, "Second capital Nurah was silently ignored"); state.AllEntityData.Remove(duplicate);
        var secondSource = Bare<UnitSpawnerBase.MyData>(); Set(secondSource, "<UniqueId>k__BackingField", "second-source");
        Set(secondSource, "m_SpawnedUnit", reference); state.AllEntityData.Add(secondSource);
        check(Inspect() == null, "Ambiguous spawner provenance was accepted"); state.AllEntityData.Remove(secondSource);
        registry[actor.UniqueId] = duplicate;
        check(Inspect() == null, "Registry replacement was accepted"); registry[actor.UniqueId] = actor;
        states = new[] { state, state };
        check(Inspect() == null, "Duplicate source scene was accepted"); states = new[] { state };
        Set(actor.Descriptor, "<Blueprint>k__BackingField", new BlueprintUnit { AssetGuid = BlueprintGuid.Parse("c44d5c157091e7e46af1f11a4c79303d") });
        check(Inspect() == null, "War-camp representation substituted for capital actor");
        Set(actor.Descriptor, "<Blueprint>k__BackingField", new BlueprintUnit { AssetGuid = BlueprintGuid.Parse(Constant("Unit")) });
        check(ReferenceEquals(Inspect(), actor), "Rejected evidence mutated retained actor or source");

        Etude Playing() { var fact = Bare<Etude>(); Set(fact, "<IsActive>k__BackingField", true); return fact; }
        var romance = Playing(); var personality = Playing(); var personalities = new Etude?[] { personality, null, null };
        bool jailed = false, dead = false, seen = true;
        bool History() => (bool)service.GetMethod("HistoryPermits", Members)!.Invoke(null,
            new object?[] { romance, jailed, dead, personalities, seen })!;
        check(History(), "Accepted active parent romance with one personality was rejected");
        seen = false; check(!History(), "Romance alone substituted for accepted Book5 terminal"); seen = true;
        jailed = true; check(!History(), "Current imprisonment granted a free visit"); jailed = false;
        dead = true; check(!History(), "Recorded native death granted a visit"); dead = false;
        Set(romance, "m_IsCompleted", true); check(!History(), "Completed romance substituted for current relationship"); Set(romance, "m_IsCompleted", false);
        Set(romance, "m_CompletionInProgress", true); check(!History(), "Closing romance granted access"); Set(romance, "m_CompletionInProgress", false);
        Set(romance, "<IsActive>k__BackingField", false); check(!History(), "Dormant romance granted access"); Set(romance, "<IsActive>k__BackingField", true);
        personalities[1] = Playing(); check(!History(), "Conflicting personalities silently chose priority"); personalities[1] = null;
        personalities[0] = null; check(!History(), "Missing personality was accepted"); personalities[2] = personality;
        check(History(), "Alternate current personality was rejected");
        Set(personality, "m_CompletionInProgress", true); check(!History(), "Transitioning personality granted access");

        // Reproduce the native completion interval at the actual dictionary/fact adapter.
        var system = Bare<EtudesSystem>();
        var manager = new EntityFactsManager(system);
        Set(system, "Facts", manager);
        var tree = manager.EnsureFactProcessor<EtudesTree>();
        Set(system, "<Etudes>k__BackingField", tree);
        var savedField = typeof(EtudesSystem).GetField("m_EtudesData", Members)!;
        var saved = (IDictionary)Activator.CreateInstance(savedField.FieldType)!;
        var nativeStateType = savedField.FieldType.GetGenericArguments()[1];
        var nativePrison = new BlueprintEtude { AssetGuid = BlueprintGuid.Parse(Constant("Prison")) };
        saved.Add(nativePrison, Enum.Parse(nativeStateType, "Completed")); savedField.SetValue(system, saved);
        var prisonFact = Playing(); Set(prisonFact, "<Blueprint>k__BackingField", nativePrison);
        Set(prisonFact, "m_CompletionInProgress", true);
        var raw = (IList)typeof(EntityFactsManager).GetField("m_Facts", Members)!.GetValue(manager)!;
        raw.Add(prisonFact);
        check(ReferenceEquals(tree.GetFact(nativePrison), prisonFact), "Prison fixture did not reach actual native fact lookup");
        check(system.EtudeIsCompleted(nativePrison) && !system.EtudeIsStarted(nativePrison)
            && prisonFact.IsPlaying && prisonFact.CompletionInProgress && !prisonFact.IsCompleted,
            "Fixture did not reproduce native early-published completion");
        bool PrisonBlocks() => (bool)service.GetMethod("PrisonBlocks", Members)!.Invoke(null, new object[] { system, nativePrison })!;
        check(PrisonBlocks(), "Completed dictionary bypassed a playing/completing prison fact");
        Set(prisonFact, "<IsActive>k__BackingField", false);
        check(PrisonBlocks(), "Deactivated but still-completing prison granted release");
        Set(prisonFact, "m_CompletionInProgress", false);
        check(PrisonBlocks(), "Unfinished dormant prison fact granted release");
        Set(prisonFact, "m_IsCompleted", true);
        check(!PrisonBlocks(), "Fully finished historical imprisonment blocked released Nurah");
        Set(prisonFact, "<IsActive>k__BackingField", true);
        check(PrisonBlocks(), "Completed but still-playing prison fact granted release");
        Set(prisonFact, "<IsActive>k__BackingField", false);
        saved[nativePrison] = Enum.Parse(nativeStateType, "Started");
        check(PrisonBlocks(), "Started native prison history bypassed confinement");
        manager = new EntityFactsManager(system);
        Set(system, "Facts", manager);
        tree = manager.EnsureFactProcessor<EtudesTree>();
        Set(system, "<Etudes>k__BackingField", tree);
        check(tree.GetFact(nativePrison) == null && PrisonBlocks(), "Pending recorded prison without a live fact was ignored");
        saved[nativePrison] = Enum.Parse(nativeStateType, "Completed");
        check(!PrisonBlocks(), "Completed history without a retained prison fact blocked release");
        saved.Clear();
        check(!PrisonBlocks(), "Never-imprisoned native history was incorrectly treated as confinement");
        NurahPlacementTests.Run(check);

    }
}

internal static class NurahPlacementTests
{
    private const BindingFlags Members = BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;
    private static FieldInfo Field(Type type, string name)
    {
        for(Type? t=type;t!=null;t=t.BaseType) {var f=t.GetField(name,Members|BindingFlags.DeclaredOnly);if(f!=null)return f;}
        throw new Exception(name);
    }
    private static void Set(object target,string name,object value)=>Field(target.GetType(),name).SetValue(target,value);
    private static object Bare(Type type)=>FormatterServices.GetUninitializedObject(type);
    private static T Reference<T>(SimpleBlueprint bp) where T:BlueprintReferenceBase,new()
    {var r=new T();Set(r,"deserializedGuid",bp.AssetGuid);Set(r,"<Cached>k__BackingField",bp);return r;}
    internal static void Run(Action<bool,string> check)
    {
        var service=typeof(Tirabade.Main).Assembly.GetType("Tirabade.NurahMeeting",true)!;
        string C(string name)=>(string)service.GetField(name,Members)!.GetRawConstantValue()!;
        var map=new Dictionary<string,SimpleBlueprint>();
        var group=new BlueprintEtudeConflictingGroup{AssetGuid=BlueprintGuid.Parse(C("Group"))};map[C("Group")]=group;
        var ktc=new BlueprintEtudeConflictingGroup{AssetGuid=BlueprintGuid.Parse(C("CapitalKtc"))};map[C("CapitalKtc")]=ktc;
        map[C("Capital")]=new BlueprintArea{AssetGuid=BlueprintGuid.Parse(C("Capital"))};
        map[C("Finale")]=new BlueprintCue{AssetGuid=BlueprintGuid.Parse(C("Finale"))};
        BlueprintEtude B(string id,int priority=0,BlueprintEtudeConflictingGroup? g=null)
        {
            var b=new BlueprintEtude{AssetGuid=BlueprintGuid.Parse(id),Priority=priority,
                ActivationCondition=new ConditionsChecker{Conditions=Array.Empty<Condition>()},
                CompletionCondition=new ConditionsChecker{Conditions=Array.Empty<Condition>()},ComponentsArray=Array.Empty<BlueprintComponent>()};
            Set(b,"m_Parent",new BlueprintEtudeReference());
            Set(b,"m_ConflictingGroups",g==null?new List<BlueprintEtudeConflictingGroupReference>():new List<BlueprintEtudeConflictingGroupReference>{Reference<BlueprintEtudeConflictingGroupReference>(g)});
            map[id]=b;return b;
        }
        B(C("Romance"));B(C("Prison"));
        var deathIds=(string[])service.GetField("Deaths",Members)!.GetValue(null)!;
        foreach(string id in deathIds.Concat((string[])service.GetField("Personalities",Members)!.GetValue(null)!))B(id);
        var parent=B(C("HiddenParent"));var hidden=B(C("Hidden"),-100,group);Set(hidden,"m_Parent",Reference<BlueprintEtudeReference>(parent));
        var death=new EtudeStatus{Playing=true};Set(death,"m_Etude",Reference<BlueprintEtudeReference>(map[deathIds[0]]));
        EntityReference E(string id)=>new EntityReference{UniqueId=id,SceneAssetGuid=C("SceneAsset")};
        var hide=new HideUnit{Target=new UnitFromSpawner{Spawner=E(C("Spawner"))},Unhide=false};
        var trigger=new EtudePlayTrigger{Conditions=new ConditionsChecker{Conditions=new Condition[]{new OrAndLogic{Not=true,
            ConditionsChecker=new ConditionsChecker{Operation=Operation.Or,Conditions=new Condition[]{death}}}}},
            Actions=new ActionList{Actions=new GameAction[]{hide}}};hidden.ComponentsArray=new BlueprintComponent[]{trigger};
        var nativeShow=new HideUnit{Target=new NamedParameterUnit{Parameter="Unit"},Unhide=true};
        var nativeMove=new TranslocateUnit{Unit=new NamedParameterUnit{Parameter="Unit"},translocatePosition=E(C("Locator"))};Set(nativeMove,"m_CopyRotation",true);
        var command=new CommandAction{AssetGuid=BlueprintGuid.Parse(C("VisitorCommand")),EntryCondition=new ConditionsChecker{Conditions=Array.Empty<Condition>()},
            Action=new ActionList{Actions=new GameAction[]{nativeShow,nativeMove}}};map[C("VisitorCommand")]=command;
        var meeting=B("f28f50a099c3498b95285b1eeb960c2a",0,group);string? request=null;bool throws=false;
        object Build()=>Activator.CreateInstance(service,Members,null,new object[]{meeting,new Func<string?>(()=>throws?throw new Exception("consent failure"):request),new Func<string,SimpleBlueprint>(id=>map[id])},null)!;
        var instance=Build();
        check(meeting.Priority==-90&&meeting.ConflictingGroups.Count()==1&&meeting.ConflictingGroups.Single().Get()==group,"Meeting must claim only Nurah's group, never Capital_KTC");
        check(meeting.Parent.IsEmpty()&&!meeting.StartsParent&&!meeting.CompletesParent,"Meeting writes native parent history");
        check(ReferenceEquals(command.Action.Actions[0],nativeShow)&&ReferenceEquals(command.Action.Actions[1],nativeMove)
            &&nativeShow.Target is NamedParameterUnit&&nativeMove.Unit is NamedParameterUnit,"Shared native actions were retargeted");
        check(ReferenceEquals(Field(service,"show").GetValue(instance) is HideUnit ownShow?ownShow.Owner:null,meeting),"Authored action lacks authored owner");
        check(!(bool)service.GetMethod("Eligible",Members)!.Invoke(instance,null)!&&!(bool)service.GetMethod("Arrived",Members)!.Invoke(instance,null)!,"Missing native world produced positive placement proof");
        check(service.GetMethod("ArrivedActor", Members)!.Invoke(instance, null) == null,
            "Missing native world supplied an interaction actor");
        request="nurah.private/0";
        check((string?)service.GetProperty("CurrentRequest",Members)!.GetValue(instance)==request,"Stable consent episode lost");
        throws=true;check(service.GetProperty("CurrentRequest",Members)!.GetValue(instance)==null,"Failed callback retained consent");throws=false;
        void Reject(Action mutate,Action restore,string message){mutate();try{Build();check(false,message);}catch(TargetInvocationException e){check(e.InnerException is InvalidOperationException,message);}finally{restore();}}
        Reject(()=>nativeMove.translocatePosition.SceneAssetGuid="wrong",()=>nativeMove.translocatePosition.SceneAssetGuid=C("SceneAsset"),"Changed locator scene accepted");
        Reject(()=>((NamedParameterUnit)nativeMove.Unit).Parameter="Other",()=>((NamedParameterUnit)nativeMove.Unit).Parameter="Unit","Changed native target accepted");
        Reject(()=>hide.Unhide=true,()=>hide.Unhide=false,"Fallback now unhides but still approved");
        Reject(()=>death.Completed=true,()=>death.Completed=false,"Expanded native fallback death semantics accepted");
        Reject(()=>hidden.Priority=-80,()=>hidden.Priority=-100,"Changed fallback priority accepted");
        // Actual native dictionary and fact collection, with separate groups.
        var system=(EtudesSystem)Bare(typeof(EtudesSystem));Set(system,"m_HeldConflictingGroups",new Dictionary<BlueprintEtudeConflictingGroup,BlueprintEtude>());
        var manager=new EntityFactsManager(system);Set(system,"Facts",manager);var tree=manager.EnsureFactProcessor<EtudesTree>();Set(system,"<Etudes>k__BackingField",tree);
        var raw=(IList)Field(typeof(EntityFactsManager),"m_Facts").GetValue(manager)!;
        Etude Fact(BlueprintEtude b){var f=(Etude)Bare(typeof(Etude));Set(f,"<Blueprint>k__BackingField",b);raw.Add(f);return f;}
        var meetingFact=Fact(meeting);var hiddenFact=Fact(hidden);var native=Fact(B("21a061de3610732438072d2b975b6f43",0,group));
        var privateEvent=Fact(B("28c0e7ec749d8eb45b617f5a7342d203",100,ktc));
        var lower=Fact(B("ee09072e5b464c9b92e4fe92f01dbd30",-95,group));var ready=new HashSet<Etude>();
        bool Claims()=>(bool)service.GetMethod("ClaimsPermit",Members)!.Invoke(null,new object[]{system,meeting,hidden,group,ktc,new Func<Etude,bool>(ready.Contains)})!;
        system.SetConflictingGroupTask(group,hiddenFact);check(Claims(),"Free generic private point denied fallback displacement");
        system.SetConflictingGroupTask(ktc,privateEvent);check(!Claims(),"Current KTC did not defer private appointment");
        system.RemoveConflictingGroupTask(ktc,privateEvent);ready.Add(privateEvent);check(!Claims(),"Pending ready KTC was starved");
        ready.Clear();check(Claims(),"Finished KTC permanently disqualified standing invitation");
        system.SetConflictingGroupTask(group,meetingFact);ready.Add(lower);check(!Claims(),"Lower-priority real Nurah claim was ignored");
        ready.Clear();system.SetConflictingGroupTask(group,native);check(!Claims(),"Current prison claim was stolen");
        system.SetConflictingGroupTask(group,hiddenFact);check(Claims()&&!privateEvent.IsCompleted&&!native.IsCompleted,"Arbitration changed native history");
        var oldGame=Field(typeof(Game),"s_Instance").GetValue(null);
        try
        {
            var game=(Game)Bare(typeof(Game));var player=(Player)Bare(typeof(Player));var state=(PersistentState)Bare(typeof(PersistentState));
            Set(state,"PlayerState",player);Set(game,"State",state);Set(player,"EtudesSystem",system);Field(typeof(Game),"s_Instance").SetValue(null,game);
            var loadingField = Field(typeof(Game), "<LoadingSave>k__BackingField");
            loadingField.SetValue(game, Bare(loadingField.FieldType));
            var previousError = service.GetProperty("LastError", Members)!.GetValue(instance);
            service.GetMethod("Tick", Members)!.Invoke(instance, null);
            check(game.IsLoadingSave && ReferenceEquals(service.GetProperty("LastError", Members)!.GetValue(instance), previousError),
                "Loading Tick reached native start/evaluation instead of returning before mutation");
            check(!(bool)service.GetMethod("Eligible", Members)!.Invoke(instance, null)!, "Loading admitted physical placement");
            loadingField.SetValue(game, null);
            game.IsUnloading = true;
            service.GetMethod("Tick", Members)!.Invoke(instance, null);
            check(ReferenceEquals(service.GetProperty("LastError", Members)!.GetValue(instance), previousError)
                && !(bool)service.GetMethod("Eligible", Members)!.Invoke(instance, null)!, "Unloading entered native start or admitted physical placement");
            game.IsUnloading = false;
            var pendingParent=Fact(B("1e0b0f84af7f04c49bd96eb4fe0de384"));
            Set(privateEvent,"<SourceFact>k__BackingField",pendingParent);
            Set(privateEvent.Blueprint,"m_Parent",Reference<BlueprintEtudeReference>(pendingParent.Blueprint));
            var noOtherKtc=new AnotherEtudeOfGroupIsPlaying{Not=true,Owner=privateEvent.Blueprint};
            Set(noOtherKtc,"m_Group",Reference<BlueprintEtudeConflictingGroupReference>(ktc));
            // Populated ConditionsChecker invokes Unity ProfileScope and cannot execute standalone.
            // Exercise actual parent readiness with an empty checker and the native condition separately.
            privateEvent.Blueprint.ActivationCondition=new ConditionsChecker{Conditions=Array.Empty<Condition>()};
            var readiness=typeof(Tirabade.Main).Assembly.GetType("Tirabade.IrabethMeeting",true)!.GetMethod("ReadyUnderPlayingParents",Members)!;
            bool NativeReady()=>(bool)readiness.Invoke(null,new object?[]{privateEvent,null,null})! && noOtherKtc.Check();
            bool NativeClaims()=>(bool)service.GetMethod("ClaimsPermit",Members)!.Invoke(null,new object[]{system,meeting,hidden,group,ktc,new Func<Etude,bool>(f=>ReferenceEquals(f,privateEvent)&&NativeReady())})!;
            system.SetConflictingGroupTask(group,meetingFact);
            check(noOtherKtc.Check(),"Nurah actor-only ownership blocked native KTC condition");
            check(!NativeReady()&&NativeClaims(),"Dormant native KTC parent permanently blocked appointment");
            Set(pendingParent,"<IsActive>k__BackingField",true);
            check(NativeReady()&&!NativeClaims(),"Ready native KTC with playing parent failed to defer meeting");
            system.SetConflictingGroupTask(ktc,privateEvent);
            check(noOtherKtc.Check()&&!NativeClaims(),"Native self-owned KTC lost its original condition semantics");
            system.RemoveConflictingGroupTask(ktc,privateEvent);Set(pendingParent,"<IsActive>k__BackingField",false);
            check(NativeClaims(),"Native parent withdrawal required a new invitation");
            var starts=(HashSet<Etude>)Field(typeof(EtudesTree),"m_StartingSet").GetValue(tree)!;
            var stops=(HashSet<Etude>)Field(typeof(EtudesTree),"m_StoppingSet").GetValue(tree)!;
            Set(pendingParent,"<IsActive>k__BackingField",true);
            starts.Add(privateEvent);
            typeof(EtudesTree).GetMethod("FilterOnActors",Members)!.Invoke(tree,null);
            check(starts.Contains(privateEvent)&&!stops.Contains(meetingFact),"Separate-group fixture must demonstrate explicit KTC eligibility deferral is necessary");
        }
        finally{Field(typeof(Game),"s_Instance").SetValue(null,oldGame);}
        var runtime=((IRuntimeEntityFactComponentProvider)meeting.ComponentsArray.Single()).CreateRuntimeFactComponent();
        runtime.Setup(meeting.ComponentsArray.Single());
        check(runtime.GetType().Name=="EtudeBracketRuntime","Authored placement did not construct native bracket runtime");
        Lifecycle(check,system,manager,meetingFact,hiddenFact,group,runtime);
        var dataType=service.GetNestedType("MeetingData",Members)!;var data=Activator.CreateInstance(dataType)!;Set(data,"ActorId","original");Set(data,"Request","nurah.private/0");
        var allows=service.GetMethod("RequestAllows",Members)!;bool Allows(string episode)=>(bool)allows.Invoke(null,new object[]{data,episode,"original"})!;
        var attempt=service.GetMethod("AttemptPlacement",Members)!;bool Attempt(Func<bool> run)=>(bool)attempt.Invoke(null,new object[]{data,run})!;
        check(Allows("nurah.private/0"),"Fresh accepted request rejected");
        check(!Attempt(()=>false)&&!Allows("nurah.private/0"),"Nonthrowing partial failure repeated same episode");
        check(Allows("nurah.private/1"),"Explicit retry rejected");
        check(Attempt(()=>!(bool)Field(dataType,"Failed").GetValue(data)!)&&Allows("nurah.private/0"),"Verification self-invalidated while attempt active");
        try{Attempt(()=>throw new Exception("native failure"));check(false,"Throwing attempt swallowed");}catch(TargetInvocationException){check(!Allows("nurah.private/0"),"Thrown partial failure lost saved latch");}
        Set(data,"Placed",true);var restored=JsonConvert.DeserializeObject(JsonConvert.SerializeObject(data),dataType)!;
        check((bool)Field(dataType,"Failed").GetValue(restored)!&&!(bool)Field(dataType,"Placed").GetValue(restored)!,"Save trusted stale placement or lost failure");
        check(!(bool)allows.Invoke(null,new object[]{data,"nurah.private/1","replacement"})!,"Retry authorized a replacement actor");
        ObservedPlacement(check, service);
    }

    private static void ObservedPlacement(Action<bool, string> check, Type service)
    {
        var occupantType = service.GetNestedType("Occupant", Members)!;
        var location = service.GetMethods(Members).Single(m => m.Name == "LocationFree" && m.IsStatic);
        var actor = (UnitEntityData)Bare(typeof(UnitEntityData));
        var other = (UnitEntityData)Bare(typeof(UnitEntityData));
        object Occupant()
        {
            var value = Activator.CreateInstance(occupantType)!;
            Set(value, "Actor", other);
            foreach (var flag in new[] { "InGame", "Loaded", "Active", "OwnView" }) Set(value, flag, true);
            Set(value, "Position", new UnityEngine.Vector3(2.99f, 0, 0));
            return value;
        }
        bool Free(params object[] values)
        {
            var array = Array.CreateInstance(occupantType, values.Length);
            for (int i = 0; i < values.Length; i++) array.SetValue(values[i], i);
            return (bool)location.Invoke(null, new object[] { actor, UnityEngine.Vector3.zero, array })!;
        }
        check(Free(), "Empty observed appointment point was blocked");
        var occupant = Occupant();
        check(!Free(occupant), "Visible nonparty occupant inside three units did not defer");
        Set(occupant, "Position", new UnityEngine.Vector3(3, 0, 0));
        check(Free(occupant), "Exact three-unit boundary differs from native placement policy");
        Set(occupant, "Position", new UnityEngine.Vector3(3.01f, 0, 0));
        check(Free(occupant), "Distant nonparty occupant blocked the point");
        occupant = Occupant(); Set(occupant, "Actor", actor);
        check(Free(occupant), "Retained actor counted as its own obstruction");
        occupant = Occupant(); Set(occupant, "PartyOrPet", true);
        check(Free(occupant), "Party/pet exclusion did not permit the observed point");
        foreach (string flag in new[] { "InGame", "Loaded", "Active" })
        {
            occupant = Occupant(); Set(occupant, flag, false);
            check(Free(occupant), "Absent/inactive observation blocked point: " + flag);
        }
        foreach (string flag in new[] { "Dummy", "Removed" })
        {
            occupant = Occupant(); Set(occupant, flag, true);
            check(Free(occupant), "Unusable actor observation blocked point: " + flag);
        }
        occupant = Occupant(); Set(occupant, "OwnView", false);
        Set(occupant, "Position", new UnityEngine.Vector3(100, 0, 0));
        check(!Free(occupant), "Mismatched view owner was accepted even though its position is untrustworthy");

        var dataType = service.GetNestedType("MeetingData", Members)!;
        var data = Activator.CreateInstance(dataType)!;
        var place = service.GetMethod("PlaceObserved", Members)!;
        var events = new List<string>();
        string? request = "nurah.private/0";
        string identity = "retained";
        bool permission = true, held = true, occupied = false, viewValid = true, arrival = true;
        object view = new object();
        object expectedView = view;
        Action? afterPreflight = null, afterShow = null;
        bool Run() => (bool)place.Invoke(null, new object?[] { data, request, identity,
            new Func<bool>(() => permission && held && !occupied && identity == "retained"),
            new Action(() => { events.Add("preflight"); afterPreflight?.Invoke(); }),
            new Action(() => { events.Add("unhide"); afterShow?.Invoke(); }),
            new Func<bool>(() => { events.Add("reread"); return viewValid && ReferenceEquals(view, expectedView); }),
            new Action(() => events.Add("move")),
            new Func<bool>(() => { events.Add("verify"); return arrival; }) })!;
        bool Failed() => (bool)Field(dataType, "Failed").GetValue(data)!;
        void Reset()
        {
            data = Activator.CreateInstance(dataType)!; events.Clear(); request = "nurah.private/0";
            identity = "retained"; permission = held = viewValid = arrival = true; occupied = false;
            view = expectedView = new object(); afterPreflight = afterShow = null;
        }
        permission = false;
        check(!Run() && events.Count == 0 && !Failed(), "Missing consent mutated before permission");
        Reset(); held = false;
        check(!Run() && events.Count == 0 && !Failed(), "Missing claim mutated before ownership");
        Reset(); request = null;
        check(!Run() && events.Count == 0 && !Failed(), "Missing request entered native protocol");
        Reset(); occupied = true;
        check(!Run() && events.Count == 0 && !Failed() && Field(dataType, "Request").GetValue(data) == null,
            "Occupancy deferral consumed or failed accepted episode");
        occupied = false;
        check(Run() && string.Join(",", events) == "preflight,unhide,reread,move,verify" && !Failed(),
            "Removing occupant did not resume unchanged invitation through complete protocol");
        Reset(); afterPreflight = () => held = false;
        check(!Run() && events.SequenceEqual(new[] { "preflight" }) && !Failed(), "Claim loss during preflight performed a partial placement");
        Reset(); afterShow = () => permission = false;
        check(!Run() && Failed() && events.SequenceEqual(new[] { "preflight", "unhide" }), "Consent withdrawal after unhide did not stop mutation");
        permission = true; events.Clear(); afterShow = null;
        check(!Run() && events.Count == 0 && Failed(), "Same failed episode replayed native operations");
        request = "nurah.private/1";
        check(Run() && !Failed(), "Explicit new retry could not use the same retained actor");
        Reset(); afterShow = () => held = false;
        check(!Run() && Failed() && !events.Contains("move"), "KTC/actor claim lost after unhide still moved actor");
        Reset(); afterShow = () => identity = "replacement";
        check(!Run() && Failed() && !events.Contains("reread"), "Actor identity changed after unhide without stopping placement");
        Reset();
        // The native permitted callback also compares its captured request; model that observation explicitly.
        afterShow = () => { request = "nurah.private/1"; permission = false; };
        check(!Run() && Failed() && !events.Contains("move"), "Changed consent episode after unhide moved actor");
        Reset(); afterShow = () => viewValid = false;
        check(!Run() && Failed() && events.Contains("reread") && !events.Contains("move"), "Missing/dummy/unusable current view was not reread");
        Reset(); afterShow = () => view = new object();
        check(!Run() && Failed() && !events.Contains("move"), "Unowned replacement view reached movement");
        Reset(); afterShow = () => view = expectedView = new object();
        check(Run() && !Failed(), "Fresh valid post-unhide view was rejected by a cached old view");
        Reset(); arrival = false;
        check(!Run() && Failed() && events.Last() == "verify", "Failed contact/distance verification became successful placement");
        Reset(); afterShow = () => throw new InvalidOperationException("native unhide failure");
        try { Run(); check(false, "Native operation failure was swallowed"); }
        catch (TargetInvocationException error)
        {
            check(error.InnerException is InvalidOperationException && Failed() && !events.Contains("move"),
                "Native operation exception did not preserve partial-mutation failure");
        }
        Reset(); afterPreflight = () => throw new InvalidOperationException("missing locator");
        try { Run(); check(false, "Missing locator continued placement"); }
        catch (TargetInvocationException error)
        {
            check(error.InnerException is InvalidOperationException && !events.Contains("unhide"), "Locator preflight exception mutated actor");
        }
    }
    private static void Lifecycle(Action<bool, string> check, EtudesSystem system, EntityFactsManager manager,
        Etude fact, Etude fallback, BlueprintEtudeConflictingGroup group, EntityFactComponent runtime)
    {
        var gameField = Field(typeof(Game), "s_Instance");
        var loggerField = Field(typeof(Owlcat.Runtime.Core.Logging.Logger), "s_Instance");
        var rootReference = ResourcesLibrary.RootRef;
        var cachedRoot = Field(rootReference.GetType(), "<Cached>k__BackingField");
        var oldGame = gameField.GetValue(null);
        var oldLogger = loggerField.GetValue(null);
        var oldRoot = cachedRoot.GetValue(rootReference);
        try
        {
            var game = (Game)Bare(typeof(Game));
            var player = (Player)Bare(typeof(Player));
            var state = (PersistentState)Bare(typeof(PersistentState));
            Set(state, "PlayerState", player);
            Set(game, "State", state);
            Set(game, "TimeController", Bare(typeof(Kingmaker.Controllers.TimeController)));
            Set(player, "EtudesSystem", system);
            gameField.SetValue(null, game);
            var root = new Kingmaker.Blueprints.Root.BlueprintRoot();
            var calendar = (CalendarRoot)Bare(typeof(CalendarRoot));
            Set(calendar, "m_Initialized", true);
            Set(calendar, "m_StartDate", new DateTime(2020, 1, 1));
            root.Calendar = calendar;
            cachedRoot.SetValue(rootReference, root);
            var logger = new Owlcat.Runtime.Core.Logging.Logger { Enabled = true };
            loggerField.SetValue(null, logger);
            Set(system, "EtudeChangedEvent", Activator.CreateInstance(Field(typeof(EtudesSystem), "EtudeChangedEvent").FieldType)!);
            Set(fact, "<Manager>k__BackingField", manager);
            Set(fact, "Children", new List<Etude>());
            Set(runtime, "<Fact>k__BackingField", fact);
            Set(fact, "Components", new List<EntityFactComponent> { runtime });
            system.RemoveConflictingGroupTask(group, fact);
            fact.Activate();
            check(fact.IsPlaying && ReferenceEquals(system.GetConflictingGroupTask(group), fact.Blueprint),
                "Actual native activation acquires the meeting claim.");
            fact.Deactivate();
            check(!fact.IsPlaying && system.GetConflictingGroupTask(group) == null && !fact.IsCompleted,
                "Actual native deactivation releases the claim without completing history.");
            fact.Activate();
            check(fact.IsPlaying && ReferenceEquals(system.GetConflictingGroupTask(group), fact.Blueprint) && !fact.IsCompleted,
                "The same native fact reacquires through activation without historical completion.");
            // Actual native selection with explicit eligibility observations instead of Unity ProfileScope.
            // A nonempty all-null OR checker returns false without invoking any native condition.
            var original = fact.Blueprint.ActivationCondition;
            var originalArea = Field(typeof(BlueprintEtude), "m_LinkedAreaPart").GetValue(fact.Blueprint)!;
            var roots = (IList)Field(typeof(EtudesTree), "m_Roots").GetValue(system.Etudes)!;
            var oldRoots = roots.Cast<object>().ToArray();
            try
            {
                Set(fact.Blueprint, "m_LinkedAreaPart", new BlueprintAreaPartReference());
                Set(fallback, "<Manager>k__BackingField", manager);
                Set(fallback, "Children", new List<Etude>());
                // The fallback's actual HideUnit requires Unity; selection is the boundary here.
                Set(fallback, "Components", new List<EntityFactComponent>());
                roots.Clear(); roots.Add(fact); roots.Add(fallback);
                fact.Blueprint.ActivationCondition = new ConditionsChecker { Operation = Operation.Or, Conditions = new Condition[] { null! } };
                system.Etudes.SelectPlayingEtudes();
                check(!fact.IsPlaying && system.GetConflictingGroupTask(group) == null,
                    "Native selection did not withdraw the now-ineligible meeting");
                // Native CheckBlockConflicts still sees the old holder during the withdrawal pass.
                system.Etudes.SelectPlayingEtudes();
                check(!fact.IsPlaying && fallback.IsPlaying && ReferenceEquals(system.GetConflictingGroupTask(group), fallback.Blueprint)
                    && !fact.IsCompleted && !fallback.IsCompleted,
                    "Native selection did not withdraw an ineligible meeting and restore hidden fallback ownership: meeting="
                    + fact.IsPlaying + ", fallback=" + fallback.IsPlaying + ", holder=" + system.GetConflictingGroupTask(group)?.AssetGuid);
                fact.Blueprint.ActivationCondition = new ConditionsChecker { Conditions = Array.Empty<Condition>() };
                system.Etudes.SelectPlayingEtudes();
                check(fact.IsPlaying && !fallback.IsPlaying && ReferenceEquals(system.GetConflictingGroupTask(group), fact.Blueprint)
                    && !fact.IsCompleted, "Native selection did not resume eligible standing meeting over fallback");
            }
            finally
            {
                fact.Blueprint.ActivationCondition = original;
                Set(fact.Blueprint, "m_LinkedAreaPart", originalArea);
                roots.Clear(); foreach (var previous in oldRoots) roots.Add(previous);
                if (fact.IsPlaying) fact.Deactivate();
                if (fallback.IsPlaying) fallback.Deactivate();
            }
        }
        finally
        {
            cachedRoot.SetValue(rootReference,oldRoot);
            loggerField.SetValue(null,oldLogger);
            gameField.SetValue(null,oldGame);
        }
    }
}
