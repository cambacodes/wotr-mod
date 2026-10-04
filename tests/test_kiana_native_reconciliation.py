"""eng7-f6b: archive contracts and original-identity runtime delivery."""
import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from storylines import kiana_native
from tools import kiana_native_policy
from tools.game_blueprints import find_bindings, game_dir
from tools.crossroute_checks import other_woman
from tools.crossroute_checks.common import Proof, blocks, verify

ROOT = Path(__file__).resolve().parents[1]


class KianaNativeArchiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contracts = kiana_native_policy.contracts()
        cls.found = find_bindings(game_dir() / 'blueprints.zip', kiana_native_policy.expected())

    def test_every_cue_dependency_has_archive_and_runtime_policy(self):
        self.assertEqual(len(self.contracts), 21)
        for target in self.contracts:
            with self.subTest(target=target):
                kiana_native_policy.check(target, kiana_native.NATIVE_EPILOGUE_EDITS[target], self.found)

    def test_verifier_allows_only_the_reviewed_sequence_parents(self):
        sequence_targets = []
        for target, policy in self.contracts.items():
            spec = kiana_native.NATIVE_EPILOGUE_EDITS[target]
            allowed = kiana_native_policy.parent_type(target, spec)
            self.assertEqual('BlueprintCueSequence' in allowed, policy['ParentType'] == 'BlueprintCueSequence')
            if policy['ParentType'] == 'BlueprintCueSequence':
                sequence_targets.append(target)
                self.assertNotIn('BlueprintCueSequence', kiana_native_policy.parent_type(target, dict(spec, Parent='0' * 32)))
        self.assertEqual(len(sequence_targets), 2)
        self.assertNotIn('BlueprintCueSequence', kiana_native_policy.parent_type('0' * 32, {}))

    def test_action_continuation_and_parent_drift_refuse_by_class(self):
        for target, policy in self.contracts.items():
            spec = kiana_native.NATIVE_EPILOGUE_EDITS[target]
            for field, value in dict(ShowOnce=True, Components=[{}], Continue=dict(Cues=[], Strategy='Random'),
                                     OnStop=dict(Actions=[{'$type': 'fixture, CompleteEtude', 'Etude': '!bp_' + '0' * 32}])).items():
                with self.subTest(target=target, field=field):
                    found = copy.deepcopy(self.found)
                    found[target]['data'][field] = value
                    with self.assertRaisesRegex(ValueError, 'runtime policy'):
                        kiana_native_policy.check(target, spec, found)
            for parent in [policy['Parent'], *policy['AlsoParents']]:
                found = copy.deepcopy(self.found)
                d = found[parent]['data']
                for field in ['Continue', 'NextCue', 'FirstCue']:
                    if '!bp_' + target in d.get(field, {}).get('Cues', []):
                        d[field]['Cues'].remove('!bp_' + target)
                if '!bp_' + target in d.get('Cues', []):
                    d['Cues'].remove('!bp_' + target)
                with self.subTest(target=target, parent=parent), self.assertRaises(ValueError):
                    kiana_native_policy.check(target, spec, found)

    def test_installed_managed_cue_presentation_keeps_native_identity(self):
        self.assertIsNotNone(shutil.which('dotnet'), 'managed native contract gate requires dotnet')
        managed = game_dir() / 'Wrath_Data/Managed'
        with tempfile.TemporaryDirectory(prefix='rrt-eng7-f6b-native-') as directory:
            temp = Path(directory)
            shutil.copyfile(ROOT / 'tests/native_f6b_runtime.cs.txt', temp / 'Runtime.cs')
            (temp / 'native.json').write_text(json.dumps({g: r['data'] for g, r in self.found.items()}))
            (temp / 'story.json').write_text(json.dumps(dict(Scenes=kiana_native.SCENES,
                Relationships={'kiana': dict(StartedFlag='kiana.started', ClosedFlag='kiana.closed', CommittedFlag='kiana.committed')},
                NativeEpilogueEdits=kiana_native.NATIVE_EPILOGUE_EDITS,
                Derived={'trickster.now': [['trickster', '!legend']]})))
            sources = ['Story.cs', 'NativeEpilogueEdit.cs', 'NativeCueTextEdit.cs', 'NativeQ3Recovery.cs', 'ParentEndingGuard.cs']
            links = ''.join(f'<Compile Include="{ROOT / "src" / name}" />' for name in sources)
            refs = ''.join(f'<Reference Include="{p.stem}"><HintPath>{p}</HintPath><Private>false</Private></Reference>'
                           for p in managed.glob('*.dll') if not p.name.startswith(('System', 'mscorlib', 'netstandard')))
            harmony = managed / 'UnityModManager/0Harmony.dll'
            refs += f'<Reference Include="0Harmony"><HintPath>{harmony}</HintPath><Private>false</Private></Reference>'
            project = temp / 'Runtime.csproj'
            project.write_text('<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><OutputType>Exe</OutputType>'
                              '<TargetFramework>net8.0</TargetFramework><Nullable>enable</Nullable></PropertyGroup><ItemGroup>'
                              + links + refs + '</ItemGroup></Project>')
            result = subprocess.run(['dotnet', 'run', '--project', str(project), '-c', 'Release', '--', str(game_dir()),
                                     str(temp / 'native.json'), str(temp / 'story.json')], cwd=temp,
                                    env=dict(os.environ, DOTNET_CLI_TELEMETRY_OPTOUT='1'), text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn('PASS eng7-f6b', result.stdout)

    def test_lint_inherits_only_reviewed_native_conversation(self):
        target = '82213327a06db644fb2b5bb1410d4654'
        spec = kiana_native.NATIVE_EPILOGUE_EDITS[target]
        scene = next(s for s in kiana_native.SCENES if s['Id'] == spec['Replacement'])
        def relationship(woman):
            return dict(StartedFlag=woman + '.started', ClosedFlag=woman + '.closed', CommittedFlag=woman + '.committed',
                        UnavailableFlags=[woman + '.dead', woman + '.gone'])
        def run(payload):
            model = verify.Model(payload)
            return other_woman.check(model, list(blocks(model)), Proof(model))
        story = dict(Relationships={w: relationship(w) for w in ['kiana', 'seelah', 'jannah', 'areelu', 'arsinoe']},
                     Scenes=[copy.deepcopy(scene)], NativeEpilogueEdits={target: copy.deepcopy(spec)},
                     NativeOverrides=[dict(Target=target, Field='NativeEpilogueEdits', Action='REPLACE', RuntimeKey=target)])
        self.assertEqual(run(story), [])  # Seelah's original quest speech survives romance closure.
        for target, contract in self.contracts.items():
            if not contract.get('SpeakerSource'):
                continue
            spec = kiana_native.NATIVE_EPILOGUE_EDITS[target]
            scene = next(s for s in kiana_native.SCENES if s['Id'] == spec['Replacement'])
            inherited = copy.deepcopy(story)
            inherited.update(Scenes=[copy.deepcopy(scene)], NativeEpilogueEdits={target: copy.deepcopy(spec)},
                NativeOverrides=[dict(Target=target, Field='NativeEpilogueEdits', Action='REPLACE', RuntimeKey=target)])
            with self.subTest(target=target):
                self.assertEqual(run(inherited), [])
                inherited['Scenes'][0]['Nodes'][0]['Text'] += ' {n}Arsinoe stands beside her.{/n}'
                self.assertIn('arsinoe:physical', {f['subject'] for f in run(inherited)})
                drift = copy.deepcopy(self.found)
                drift[contract['SpeakerSource']]['data']['Speaker']['m_Blueprint'] = '!bp_' + '0' * 32
                with self.assertRaises(ValueError):
                    kiana_native_policy.check(target, spec, drift)
        target = '82213327a06db644fb2b5bb1410d4654'

        wrong = copy.deepcopy(story)
        wrong['NativeEpilogueEdits'][target]['Parent'] = '0' * 32
        self.assertIn('seelah:physical', {f['subject'] for f in run(wrong)})
        invented = copy.deepcopy(story)
        invented['Scenes'][0]['Nodes'][0]['Text'] += ' {n}Areelu stands beside her.{/n}'
        self.assertIn('areelu:physical', {f['subject'] for f in run(invented)})
        extra_actor = copy.deepcopy(story)
        extra_actor['Scenes'][0]['Nodes'][0]['Text'] += ' {n}Jannah stands beside her.{/n}'
        self.assertIn('jannah:physical', {f['subject'] for f in run(extra_actor)})


if __name__ == '__main__':
    unittest.main()
