"""Compile production rules and scenario metadata in system temp; check every integrated scripted contract."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SystemScenarioTests(unittest.TestCase):
    def test_scenario_contracts_against_production_rules(self):
        with tempfile.TemporaryDirectory(prefix="rrt-hcov-contract-") as directory:
            temp = Path(directory)
            newtonsoft = Path(os.environ.get("RRT_GAME_DIR", "/wrath")) / "Wrath_Data/Managed/Newtonsoft.Json.dll"
            project = temp / "Contracts.csproj"
            project.write_text('''<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><OutputType>Exe</OutputType>
<TargetFramework>net8.0</TargetFramework><Nullable>enable</Nullable></PropertyGroup><ItemGroup>
''' + f'<Compile Include="{ROOT / "src/Story.cs"}" /><Compile Include="{ROOT / "harness/src/SystemScenarios.cs"}" />'
                + f'<Reference Include="Newtonsoft.Json"><HintPath>{newtonsoft}</HintPath></Reference>'
                + '</ItemGroup></Project>', encoding="utf-8")
            (temp / "Program.cs").write_text('''using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using Newtonsoft.Json;
using Tirabade;
using RRT.TestHarness;
var story = JsonConvert.DeserializeObject<Story>(File.ReadAllText(args[0]))!;
var cases = SystemCases.Parse(File.ReadAllText(args[1]));
int checkedCases=0, missing=0;
foreach (var c in cases.Cases) {
    if (c.FixtureFlags == null) { missing++; continue; }
    var state = new Snapshot { Chapter=c.Chapter, Hour=10000, Flags=new HashSet<string>(c.FixtureFlags) };
    foreach(var step in c.Steps) {
        var scene=story.Scenes.Single(s=>s.Id==step.Scene);
        state.Area=scene.Areas.FirstOrDefault() ?? "";
        if(scene.ContactUnit!=null) state.AvailableContacts.Add(scene.ContactUnit);
        state.AvailableContacts.UnionWith(scene.AdditionalContactUnits);
        var probe=JsonConvert.DeserializeObject<Snapshot>(JsonConvert.SerializeObject(state))!;
        probe.Flags.ExceptWith(step.Remove); probe.Flags.UnionWith(step.Add);
        foreach(var p in step.RestSpent) probe.RestSpent[p.Key]=p.Value;
        if(step.RestSucceeded.HasValue) Rules.RestFinished(probe,step.RestSucceeded.Value);
        Rules.Complete(story,probe);
        bool available=Rules.Available(story,scene,probe);
        if(available!=step.Available || step.Table && Rules.TableEntries(story,probe).Contains(scene)!=step.Available)
            throw new Exception(c.Id+": availability mismatch for "+step.Scene+" expected="+step.Available+" actual="+available+" missing="+string.Join(",",scene.Requires.Where(f=>!probe.Flags.Contains(f)))+" forbids="+string.Join(",",scene.Forbids.Where(probe.Flags.Contains))+" contact="+Rules.ContactAvailable(story,scene,probe));
        var entries=Rules.BookVisible(story.Books["trickster.ledger"],probe).Select(e=>e.Id).ToArray();
        if(step.LedgerEntries.Any(e=>!entries.Contains(e)) || step.HiddenLedgerEntries.Any(entries.Contains))
            throw new Exception(c.Id+": W5 reader mismatch");
        if(!step.Available || step.ProbeOnly) continue;
        Rules.Complete(story,state);
        var node=scene.Nodes[0];
        foreach(var answer in step.Answers) {
            Rules.Complete(story,state);
            var bits=answer.Split('/');
            if(node.Id!=bits[1]) throw new Exception(c.Id+": path diverged at "+answer);
            var choice=node.Choices[int.Parse(bits[2])];
            if(!Rules.ChoiceAvailable(choice,state)) throw new Exception(c.Id+": scripted answer hidden: "+answer);
            foreach(var flag in choice.Set) state.Flags.Add(flag);
            if(choice.Next==null) { Rules.SpendRestAllowance(story,scene,state); state.Flags.Add(scene.Id); }
            else node=scene.Nodes.Single(n=>n.Id==choice.Next);
        }
        if(step.ExpectFlags.Any(f=>!state.Flags.Contains(f)) || step.ExpectRestSpent.Any(p=>!state.RestSpent.TryGetValue(p.Key,out int n) || n!=p.Value))
            throw new Exception(c.Id+": effect/allowance mismatch");
    }
    checkedCases++;
}
Console.WriteLine($"PASS {checkedCases} integrated contracts; {missing} explicitly missing integration contracts");
''', encoding="utf-8")
            env = dict(os.environ)
            env.pop("BaseIntermediateOutputPath", None)
            env.pop("BaseOutputPath", None)
            result = subprocess.run(["dotnet", "run", "--project", str(project), "-c", "Release", "--",
                                     str(ROOT / "development/Story.json"), str(ROOT / "harness/system-scenarios.json")],
                                    cwd=temp, env=env, capture_output=True, text=True)
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_all_interaction_variants_are_explicit(self):
        import sys
        sys.path.insert(0, str(ROOT / "tools"))
        import harness_system_cases as generator
        cases = json.loads((ROOT / "harness/system-scenarios.json").read_text(encoding="utf-8"))["Cases"]
        scripted = {step["Scene"] for c in cases for step in c["Steps"]}
        self.assertTrue(set(generator.IX_A + generator.IX_B).issubset(scripted))
        self.assertEqual({"household-pairs", "pair-w5", "w4-ensemble", "w4-knowledge", "partner-stance", "lastcall", "lastcall-entitlement", "ix-a", "ix-b"},
                         {c["System"] for c in cases})


if __name__ == "__main__":
    unittest.main()
