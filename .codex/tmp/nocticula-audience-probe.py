import json
from pathlib import Path
from zipfile import ZipFile

root = Path(__file__).resolve().parents[2]
with ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip') as archive:
    native = {}
    for name in archive.namelist():
        if '/c5/Mythic_Trickster/Nocticula/' in name and name.endswith('.jbp'):
            item = json.loads(archive.read(name))
            native[item['AssetId']] = item['Data']
cue = native['20451daada07f744b9d7f3e14a37a864']
answers = native['2729c49e2bf20c64caa4f54b352e03f6']
answer = native['fd4f6c1d6397fa94db7aaf08de7dfeca']
reward = native['bb552fe4e21cb874fa3c98c2cc328186']
departure = native['19a0d2e4bae6246469852a4abf7705e6']
assert not cue['OnShow']['Actions'] and not cue['OnStop']['Actions']
assert not cue['ShowOnce'] and not cue['Conditions']['Conditions']
assert cue['Answers'] == ['!bp_2729c49e2bf20c64caa4f54b352e03f6']
assert '!bp_fd4f6c1d6397fa94db7aaf08de7dfeca' in answers['Answers']
assert answer['NextCue']['Cues'] == ['!bp_bb552fe4e21cb874fa3c98c2cc328186']
assert reward['Continue']['Cues'] == ['!bp_19a0d2e4bae6246469852a4abf7705e6']
assert answer['OnSelect']['Actions'][0]['Etude'] == '!bp_8ee3df5466722b94091a3b867b33063a'
assert [a['$type'].split(', ')[-1] for a in departure['OnStop']['Actions']] == ['TeleportParty','HideMapObject']
managed = (root / '.codex/tmp/nocticula-dialogcontroller.cs').read_text()
select = managed[managed.index('public void SelectAnswer('):managed.index('public bool NextCueHasNewAnswers')]
assert select.index('answer.OnSelect.Run()') < select.index('SelectNextCue(answer)') < select.index('StopDialog()')
clear = managed[managed.index('private void Clear()'):managed.index('private void TurnOffSpeakerHighlight()')]
assert 'Dialog = null;' in clear and 'm_Answers.Clear();' in clear
# This is a graph/action-order replay, not execution of DialogController or Unity.
old_trace = ['native selection recorded','addon Queue','empty NextCue','StopDialog','Clear native cue and answers','native FinishActions','queued addon starts','addon terminal empty NextCue','StopDialog']
bridge_trace = ['addon entry NextCue -> inline history','addon local choices','terminal -> native Cue_0006','native answers rebuilt','player chooses native Answer_0011','native StartEtude','native Cue_0016 OnShow','native Cue_0019 OnShow','departure OnStop TeleportParty','departure OnStop HideMapObject']
print(json.dumps({'kind':'native JSON and freshly decompiled managed-source graph probe','old_trace':old_trace,'recommended_trace':bridge_trace,'executed_native_controller':False},indent=2))
