"""eng7-f1: export/runtime policy equivalence and paid-history answer replacements."""
import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from storylines import kiana_native, native_overrides
from tools import native_answer_policy, native_q3_policy
from tools.game_blueprints import find_bindings, game_dir

ROOT = Path(__file__).resolve().parents[1]


class NativeAnswerContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        expected = dict(native_q3_policy.TYPES)
        for target, policy in native_answer_policy.contracts().items():
            expected[target] = "BlueprintAnswer"
            expected[policy["AnswerList"]] = "BlueprintAnswersList"
        cls.found = find_bindings(game_dir() / "blueprints.zip", expected)

    def test_shipped_answers_match_runtime_whitelist(self):
        self.assertEqual(set(kiana_native.NATIVE_ANSWER_EDITS), set(native_answer_policy.contracts()))
        for target, spec in kiana_native.NATIVE_ANSWER_EDITS.items():
            native_answer_policy.check(target, spec, self.found)
            self.assertEqual(spec["When"], kiana_native.HOME_WORLDS)

    def test_behavior_drift_is_rejected_by_class(self):
        for target, spec in kiana_native.NATIVE_ANSWER_EDITS.items():
            cases = dict(ShowOnce=True, ShowOnceCurrentDialog=True, DebugMode=True, AddToHistory=False,
                RequireValidCue=True, Components=[{}], MythicRequirement="Trickster", AlignmentRequirement="Good",
                Experience="NormalExperience", ShowCheck=dict(Type="Diplomacy", DC=1), FakeChecks=[{}],
                CharacterSelection=dict(SelectionType="Manual", ComparisonStats=[]),
                ShowConditions=dict(Operation="Or", Conditions=[]), SelectConditions=dict(Operation="Or", Conditions=[]),
                NextCue=dict(Strategy="First", Cues=[]), OnSelect=dict(Actions=[{}]),
                AlignmentShift=dict(Direction="ChaoticEvil", Value=1))
            for field, value in cases.items():
                with self.subTest(target=target, field=field):
                    found = copy.deepcopy(self.found)
                    found[target]["data"][field] = value
                    with self.assertRaisesRegex(ValueError, "runtime policy"):
                        native_answer_policy.check(target, spec, found)
            found = copy.deepcopy(self.found)
            found[spec["AnswerList"]]["data"]["Answers"].append("!bp_" + target)
            with self.assertRaisesRegex(ValueError, "runtime policy"):
                native_answer_policy.check(target, spec, found)

    def test_declaration_forbids_behavior_fields_and_unknown_policy(self):
        target, spec = next(iter(kiana_native.NATIVE_ANSWER_EDITS.items()))
        for edited in (dict(spec, NextCue="anything"), dict(spec, AnswerList="0" * 32)):
            payload = {}
            with self.assertRaises(ValueError):
                native_overrides.declare(payload, source="test", target=target, target_type="answer", action="REPLACE", spec=edited)
            self.assertFalse(payload)

    def test_q3_declaration_and_both_action_sites_match_runtime(self):
        spec = kiana_native.NATIVE_GATES["kiana.q3_recovery"]
        native_q3_policy.check(spec, self.found)
        for target, field in ((native_q3_policy.FINAL, "Components"), (native_q3_policy.VERDICT, "OnStop"),
                              (native_q3_policy.COMPLETION, "Action")):
            found = copy.deepcopy(self.found)
            if field == "Components":
                found[target]["data"][field][0]["Actions"]["Actions"].pop()
            else:
                found[target]["data"][field]["Actions"].pop()
            with self.subTest(site=target), self.assertRaisesRegex(ValueError, "action sites"):
                native_q3_policy.check(spec, found)

    def test_actual_managed_runtime_contract_and_two_q3_branches(self):
        if shutil.which("dotnet") is None:
            self.skipTest("dotnet unavailable")
        managed = game_dir() / "Wrath_Data/Managed"
        self.assertTrue((managed / "Assembly-CSharp.dll").exists(), "runtime contract needs installed managed assemblies")
        with tempfile.TemporaryDirectory(prefix="rrt-eng7-f1-") as directory:
            temp = Path(directory)
            for name in ("fixtures", "runtime"):
                shutil.copyfile(ROOT / ("tests/native_f1_" + name + ".cs.txt"), temp / (name + ".cs"))
            (temp / "native.json").write_text(json.dumps({g: record["data"] for g, record in self.found.items()}))
            sources = ("Story.cs", "NativeAnswerEdit.cs", "NativeEpilogueEdit.cs", "NativeQ3Recovery.cs", "NativeGate.cs", "ParentEndingGuard.cs")
            links = ''.join(f'<Compile Include="{ROOT / "src" / name}" />' for name in sources)
            references = ''.join(f'<Reference Include="{p.stem}"><HintPath>{p}</HintPath><Private>false</Private></Reference>'
                for p in managed.glob("*.dll") if not p.name.startswith(("System", "mscorlib", "netstandard")))
            harmony = managed / "UnityModManager/0Harmony.dll"
            references += f'<Reference Include="0Harmony"><HintPath>{harmony}</HintPath><Private>false</Private></Reference>'
            project = temp / "Runtime.csproj"
            project.write_text('<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><OutputType>Exe</OutputType>'
                '<TargetFramework>net8.0</TargetFramework><Nullable>enable</Nullable></PropertyGroup><ItemGroup>'
                + links + references + '</ItemGroup></Project>')
            result = subprocess.run(["dotnet", "run", "--project", str(project), "-c", "Release", "--", str(game_dir()), str(temp / "native.json")],
                cwd=temp, env=dict(os.environ, DOTNET_CLI_TELEMETRY_OPTOUT="1"), text=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn("PASS eng7-f1", result.stdout)


if __name__ == "__main__":
    unittest.main()
