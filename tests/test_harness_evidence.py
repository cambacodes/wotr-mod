"""H09: fixture execution does not certify earning or unavailable live cases."""
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from tools.harness_evidence import evaluate


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.report = {'Status': 'complete', 'Plan': {'Force': True},
            'Init': {'RrtVersion': '1.2.3'}, 'Summary': {'Passed': True, 'Skipped': []},
            'Saves': [{'ResolvedPath': 'finale-copy.zks', 'LoadOk': True,
                       'State': {'Chapter': 6, 'Area': 'native-area', 'AvailableContacts': ['woman']},
                       'Runs': [{'Scene': 'fixture', 'Forced': True, 'Passed': True, 'Result': 'completed',
                                 'Inline': {'Dialog': 'native-host', 'NavPath': ['cue: answer']}}]}]}
        self.requirement = dict(case='fixture', kind='synthetic fixture', save='finale-copy.zks',
            area='native-area', chapter=6, mod_version='1.2.3', host='native-host', path=['cue: answer'],
            placement='native-area', contacts=['woman'], owner='coordinator')

    def test_same_supplied_fixture_executes_but_cannot_close_earning(self):
        fixture = evaluate(self.report, [self.requirement])
        self.assertTrue(fixture['execution_passed'])
        self.assertTrue(fixture['acceptance_passed'])
        earning = dict(self.requirement, kind='earned campaign')
        actual = evaluate(self.report, [earning])
        self.assertFalse(actual['acceptance_passed'])
        self.assertIn('evidence kind unproved: earned campaign', actual['requirements'][0]['remaining'])

    def test_real_save_and_rendered_evidence_stay_distinct(self):
        self.report['Plan']['Force'] = False
        self.report['Plan']['ForceSetRequires'] = True  # inert unless Force is selected
        run = self.report['Saves'][0]['Runs'][0]
        run['Forced'] = False
        self.assertTrue(evaluate(self.report, [dict(self.requirement, kind='real save')])['acceptance_passed'])
        self.assertFalse(evaluate(self.report, [dict(self.requirement, kind='rendered')])['acceptance_passed'])
        run['Screenshots'] = ['bound-page.png']
        self.assertTrue(evaluate(self.report, [dict(self.requirement, kind='rendered')])['acceptance_passed'])
        self.report['Plan']['SeenCues'] = ['injected-native-history']
        self.assertFalse(evaluate(self.report, [dict(self.requirement, kind='real save')])['acceptance_passed'])

    def test_wrong_path_missing_contact_version_skip_and_truncation_leave_open(self):
        mutations = [lambda r: r['Saves'][0]['State'].update(Area='azata-only-area'),
                     lambda r: r['Saves'][0]['State'].update(AvailableContacts=[]),
                     lambda r: r['Init'].pop('RrtVersion'),
                     lambda r: r['Saves'][0]['Runs'][0].update(Result='skipped-forbidden'),
                     lambda r: r['Saves'][0].update(InventoryTruncated=True),
                     lambda r: r['Saves'][0]['Runs'][0]['Inline'].update(NavPath=['wrong answer']),
                     lambda r: r.update(Status='aborted')]
        for mutate in mutations:
            report = copy.deepcopy(self.report)
            mutate(report)
            self.assertFalse(evaluate(report, [self.requirement])['acceptance_passed'])

    def test_empty_or_missing_inventory_and_owner_remain_open(self):
        self.assertFalse(evaluate(self.report, [])['acceptance_passed'])
        requirement = dict(self.requirement)
        requirement.pop('owner')
        self.assertFalse(evaluate(self.report, [requirement])['acceptance_passed'])
        self.report['Saves'][0]['Runs'] = []
        self.assertFalse(evaluate(self.report, [self.requirement])['acceptance_passed'])

    def test_public_receipt_includes_identity_and_keeps_earning_open(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory(prefix='rrt-h09-') as directory:
            directory = Path(directory)
            report = directory / 'report.json'
            requirements = directory / 'requirements.json'
            out = directory / 'receipt.json'
            report.write_text(json.dumps(self.report))
            requirements.write_text(json.dumps([dict(self.requirement, kind='earned campaign')]))
            result = subprocess.run([sys.executable, str(root / 'tools/harness_evidence.py'), str(report),
                '--requirements', str(requirements), '--out', str(out), '--source-hash', 'a' * 64,
                '--export-hash', 'b' * 64], capture_output=True, text=True, timeout=10)
            self.assertEqual(2, result.returncode, result.stderr)
            receipt = json.loads(out.read_text())
            self.assertEqual('a' * 64, receipt['source_hash'])
            self.assertEqual('b' * 64, receipt['export_hash'])
            self.assertEqual(64, len(receipt['policy_hash']))
            self.assertFalse(receipt['acceptance_passed'])

    def test_live_report_skip_counts_and_truncation_offline(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory(prefix='rrt-h09-report-') as directory:
            temp = Path(directory)
            newtonsoft = Path(os.environ.get('RRT_GAME_DIR', '/wrath')) / 'Wrath_Data/Managed/Newtonsoft.Json.dll'
            (temp / 'Report.csproj').write_text('<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup>'
                '<OutputType>Exe</OutputType><TargetFramework>net8.0</TargetFramework><Nullable>enable</Nullable>'
                '</PropertyGroup><ItemGroup><Compile Include="' + str(root / 'harness/src/HarnessReport.cs') + '" />'
                '<Reference Include="Newtonsoft.Json"><HintPath>' + str(newtonsoft) + '</HintPath></Reference>'
                '</ItemGroup></Project>')
            (temp / 'Models.cs').write_text('''namespace RRT.TestHarness {
public class HarnessPlan { public string? SystemCasesJson; public bool NativeEpilogueSpike; }
public class NativeSlideResult { public string Case="",Result=""; public bool Passed; public System.Collections.Generic.List<string> Findings=new(); }
public class SystemCoverage { public string Scenario="",Result=""; public bool Passed; public System.Collections.Generic.List<string> Findings=new(); }
public class ResidenceSpikeResult { public bool Passed; public System.Collections.Generic.List<string> Findings=new(); }
public class PresenceSpikeResult { public bool Passed; public System.Collections.Generic.List<string> Findings=new(); }
}''')
            (temp / 'Program.cs').write_text('''using System; using RRT.TestHarness;
var r=new HarnessReport {Status="complete"}; r.Init.Initialized=true; r.Init.RrtModFound=true; r.Init.RrtVersion="v";
var save=new SaveReport {LoadOk=true}; r.Saves.Add(save);
var run=new SceneRun {Scene="fixture",Result="skipped-forbidden",Passed=true}; save.Runs.Add(run);
r.ComputeSummary();
if (!r.Summary.Passed || r.Summary.RunsPassed!=0 || r.Summary.AcceptanceComplete) throw new Exception("skip counted as pass");
run.Result="completed"; r.ComputeSummary();
if (r.Summary.RunsPassed!=1 || !r.Summary.AcceptanceComplete) throw new Exception("completed coverage missing");
save.InventoryTruncated=true; r.ComputeSummary();
if(r.Summary.AcceptanceComplete) throw new Exception("truncated counted as pass");
save.InventoryTruncated=false; r.Init.RrtVersion=null; r.ComputeSummary();
if(r.Summary.AcceptanceComplete) throw new Exception("missing mod version counted as pass");
Console.WriteLine("PASS offline live report coverage");''')
            env = dict(os.environ)
            env.pop('RRT_TEST_BUILD_ROOT', None)
            result = subprocess.run(['dotnet', 'run', '--project', str(temp / 'Report.csproj'), '-c', 'Release'],
                                    cwd=temp, env=env, capture_output=True, text=True, timeout=90)
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
