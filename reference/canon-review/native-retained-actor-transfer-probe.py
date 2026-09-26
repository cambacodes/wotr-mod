"""Read installed assemblies; reproduce why AddEntityData is not a transfer.

Only writes an isolated temporary project. Never loads or changes a game save.
The real native test object is spawner data, not a live Unity actor.
"""
from pathlib import Path
import hashlib
import subprocess
import tempfile
from xml.sax.saxutils import escape

GAME = Path('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure')
DOTNET = Path.home() / 'AppData/Local/RanRomanceTools/dotnet/dotnet.exe'
MANAGED = GAME / 'Wrath_Data/Managed'
work = Path(tempfile.mkdtemp(prefix='retained-transfer-probe-'))
project = '''<Project Sdk="Microsoft.NET.Sdk">
<PropertyGroup><OutputType>Exe</OutputType><TargetFramework>net48</TargetFramework><LangVersion>latest</LangVersion></PropertyGroup>
<ItemGroup><PackageReference Include="Microsoft.NETFramework.ReferenceAssemblies" Version="1.0.3" PrivateAssets="all" />
<Reference Include="{managed}/*.dll" Exclude="{managed}/System*.dll;{managed}/mscorlib.dll;{managed}/netstandard.dll" Private="false" /></ItemGroup>
</Project>'''
(work / 'Probe.csproj').write_text(project.format(managed=escape(str(MANAGED))), encoding='utf-8')
source = r'''using System;
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
    [MethodImpl(MethodImplOptions.NoInlining)]
    static void Inspect() {
        var source = new SceneEntitiesState("source");
        var target = new SceneEntitiesState("target");
        var data = (UnitSpawnerBase.MyData)FormatterServices.GetUninitializedObject(typeof(UnitSpawnerBase.MyData));
        typeof(EntityDataBase).GetField("<UniqueId>k__BackingField", BindingFlags.Instance | BindingFlags.NonPublic)
            .SetValue(data, "synthetic-observation-only");
        source.AddEntityData(data);
        if (!source.AllEntityData.Contains(data) || data.HoldingState != source)
            throw new Exception("Initial native add failed.");
        target.AddEntityData(data);
        if (!source.AllEntityData.Contains(data) || !target.AllEntityData.Contains(data) || data.HoldingState != target)
            throw new Exception("Native add semantics changed; rereview the implementation.");
        Console.WriteLine("PASS: same object remains in both states; AddEntityData is not a transfer.");
    }
}'''
(work / 'Probe.cs').write_text(source.replace('MANAGED_PATH', str(MANAGED).replace('"', '""')), encoding='utf-8')
subprocess.run([str(DOTNET), 'build', str(work / 'Probe.csproj'), '-c', 'Release', '-v', 'quiet'], check=True)
subprocess.run([str(work / 'bin/Release/net48/Probe.exe')], check=True)
print('Assembly-CSharp SHA256:', hashlib.sha256((MANAGED / 'Assembly-CSharp.dll').read_bytes()).hexdigest().upper())
print('Isolated witness:', work)
