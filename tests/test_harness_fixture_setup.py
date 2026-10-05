"""Offline fixture isolation: build game-free plan/probe policy in system temp."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class HarnessFixtureSetupTests(unittest.TestCase):
    def test_plan_normalization_and_production_negative_controls(self):
        with tempfile.TemporaryDirectory(prefix="rrt-f7-harness-") as temp:
            temp = Path(temp)
            project = temp / "Fixture.csproj"
            sources = ("HarnessPlan.cs", "PresenceSpikeModel.cs", "ResidenceSpikeModel.cs", "WalkableProbe.cs", "ProductionPresenceProbe.cs")
            # Compile only the policy half of the runtime probe, without Unity/game types.
            probe = (ROOT / "harness/src/ProductionPresenceProbe.cs").read_text().split("    internal sealed partial class HarnessRunner")[0]
            probe = "\n".join(line for line in probe.splitlines() if not line.startswith("using Kingmaker") and line != "using UnityEngine;") + "\n}\n"
            (temp / "ProductionPolicy.cs").write_text(probe)
            # F5 adds case validation to HarnessPlan; compile its real game-free
            # model alongside the F7 policy, rather than stubbing the dependency.
            cases = (ROOT / 'harness/Probes/NativeEpilogueInventoryProbe.cs').read_text(encoding='utf-8')
            cases = cases[cases.index('namespace RRT.TestHarness'):cases.index('    public sealed class NativeSlideRow')]
            (temp / 'SlideCases.cs').write_text('using System;\nusing System.Collections.Generic;\nusing System.Linq;\nusing Newtonsoft.Json;\n' + cases + '}\n', encoding='utf-8')
            links = "".join(f'<Compile Include="{ROOT / "harness/src" / file}" />' for file in sources[:-1])
            game_candidates = [Path(os.environ.get("RRT_GAME_DIR") or
                                    r"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure"),
                               Path("/wrath")]
            newtonsoft = next((p / "Wrath_Data/Managed/Newtonsoft.Json.dll" for p in game_candidates
                               if (p / "Wrath_Data/Managed/Newtonsoft.Json.dll").exists()), None)
            self.assertIsNotNone(newtonsoft, "installed game Newtonsoft.Json.dll required (RRT_GAME_DIR)")
            project.write_text('<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><OutputType>Exe</OutputType>'
                               '<TargetFramework>net8.0</TargetFramework><Nullable>enable</Nullable></PropertyGroup>'
                               '<ItemGroup>' + links + '<Reference Include="Newtonsoft.Json"><HintPath>'
                               + str(newtonsoft) + '</HintPath></Reference></ItemGroup></Project>')
            (temp / "Program.cs").write_text('''using System;
using System.Linq;
using RRT.TestHarness;
var plan = HarnessPlan.Parse("{\\\"setFlags\\\":[\\\"a,b\\\",\\\" a \\\"],\\\"startEtudes\\\":[\\\"9F486A9C-0C9A-BFC4-A952-BB22E88A7E96\\\"]}");
if (!plan.SetFlags.SequenceEqual(new[] {"a", "b"}) || plan.StartEtudes.Single() != "9f486a9c0c9abfc4a952bb22e88a7e96") throw new Exception("normalization");
bool invalid = false;
try { HarnessPlan.Parse("{\\\"startEtudes\\\":[\\\"bad\\\"]}"); } catch (FormatException) { invalid = true; }
if (!invalid) throw new Exception("invalid GUID accepted");
var key = HarnessPlan.Parse("{\\\"spike\\\":\\\"presence\\\",\\\"presence\\\":{\\\"key\\\":\\\"galfrey.presence\\\"}}");
if (key.Presence!.Key != "galfrey.presence") throw new Exception("production selection");
var p = new ProductionPresenceProbe { Key="fixture", Wanted=true, ActorId="same", WalkableGap=0.2f, Drift=0.1f, ApproachDistance=1.8f, Clickable=true };
if (p.Failures().Any()) throw new Exception("positive production fixture");
p.Wanted=false;
if (!p.Failures().Any()) throw new Exception("unwanted production actor accepted");
p.Wanted=true; p.Clickable=false;
if (!p.Failures().Any()) throw new Exception("unclickable accepted");
p.Clickable=true; p.Crowding.Add("blocked");
if (!p.Failures().Any()) throw new Exception("occupied accepted");
var r = new PresenceSpikeResult { Production=p, ProductionReloadRequired=true };
r.Evaluate();
if (r.Passed || !r.Findings.Contains("production presence was not checked after reload")) throw new Exception("missing reload accepted");
p.Crowding.Clear(); r.ProductionAfterReload=p; r.Evaluate();
if (!r.Passed) throw new Exception("matching reload rejected");
r.ProductionAfterReload=new ProductionPresenceProbe { Wanted=true, ActorId="different", WalkableGap=0.1f, Drift=0.1f, ApproachDistance=1f, Clickable=true };
r.Evaluate(); if (r.Passed) throw new Exception("changed actor accepted");
Console.WriteLine("PASS fixture setup and production observation controls");
''')
            env = dict(os.environ)
            env.pop("BaseIntermediateOutputPath", None)
            env.pop("BaseOutputPath", None)
            result = subprocess.run(["dotnet", "run", "--project", str(project), "-c", "Release"],
                                    cwd=temp, env=env, capture_output=True, text=True)
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
