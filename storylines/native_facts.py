"""Verified optional native history, never inferred from an authored romance.

README
======
key("eggs.manually_smashed") returns a read-only native.history.* predicate.
integrate(payload) binds all facts through existing SeenCues, SelectedAnswers,
Etudes and CompletedQuests readers. Each Fact lists native GUIDs, exactly what
observation sets it, archive paths and the originating CAN audit. A missing fact
means unobserved history, not proof that the opposite event happened. In
particular a visited cue is not current physical presence, a request is not its
success, and restoration is not reconciliation or a subsequent Heaven return.

conditioned(record, fact) adds Requires=[key(fact)]; neutral=True adds Forbids.
Use on a scene, choice, or EPILOGUE paragraph. Ordinary dialogue must branch to
separate nodes/choices; do not add conditional paragraphs there. For an existing
choice keep it at its index, condition its remembered branch, and APPEND the
fact-neutral choice returned by recollection_choices. Neither helper changes
availability until a route author explicitly uses it. This task changes no prose.

The seed covers optional native histories in the latest *hx* CAN defects plus
the supplied earlier egg-smashing, Nenio insult and herald findings. Authored
events (Galfrey's substituted burial, anatomy examinations, earned returns) stay
route predicates. AeonFinalWorld facts describe that rewritten world, not a
restored Trickster marriage. Current native status remains a separate reader.
"""
import copy
from dataclasses import dataclass
import json
from zipfile import ZipFile

from tools.game_blueprints import blueprint_type, game_dir

PREFIX = "native.history."
READER_TYPES = dict(SeenCues="BlueprintCue", SelectedAnswers="BlueprintAnswer",
                    Etudes="BlueprintEtude", CompletedQuests="BlueprintQuest",
                    UnlockableFlags="BlueprintUnlockableFlag")


@dataclass(frozen=True)
class Fact:
    reader: str
    guids: tuple
    how_set: str
    evidence: tuple
    audit: str


FACTS = {
    'eggs.manually_smashed': Fact('SeenCues', ('757a3b2e19b4f8f4d8d438ba15db1d76',),
        'DragonEggs/Cue_0006 is played after the manual smash answer; the shared destruction etude alone does not identify the actor.',
        ('World/Dialogs/c3/IvorySanctum/DragonEggs/Cue_0006.jbp',), 'devarrahx2.json'),
    'eggs.golem_wrong_password': Fact('SeenCues', ('07404e9374e3d004db0f6397f1a7f2b6',),
        'Golems Cue_0017 is played after any wrong password (Answers 0010/0011/0013/0014/0015); its OnStop plays GolemsDestroyEggs.',
        ('World/Dialogs/c3/IvorySanctum/Golems_DragonEggs/Cue_0017.jbp',), 'devarrahx3.json'),
    'eggs.commanded_destruction': Fact('SelectedAnswers', ('6f9afd4cc981ce3468fb9b7ec5aa3082',),
        'Select Golems Answer_0022, Destruction, after the correct password; distinct from a wrong password or passive watching.',
        ('World/Dialogs/c3/IvorySanctum/Golems_DragonEggs/Answer_0022.jbp',), 'devarrahx3.json'),
    'eggs.watched_crushing': Fact('SelectedAnswers', ('dcea2a05e317aa04285fadd6185d531e',),
        'Select Golems Answer_0005, See what happens next; not a wrong-password observation.',
        ('World/Dialogs/c3/IvorySanctum/Golems_DragonEggs/Answer_0005.jbp',), 'devarrahx3.json'),
    'eggs.deactivation_requested': Fact('SelectedAnswers', ('008eb2ba4b80de7469524ffb7f1934ab',),
        'Select Golems Answer_0021, Deactivation; records the request, not every later egg fate.',
        ('World/Dialogs/c3/IvorySanctum/Golems_DragonEggs/Answer_0021.jbp',), 'adjacent:devarrahx3.json'),
    'eggs.dialog_unlocked': Fact('UnlockableFlags', ('b88c56313ded5e0409bbd04334add635',),
        'Native EnableEggDialog is unlocked after deactivation; its positive value enables the separate egg dialogue. It does not record a destruction cause.',
        ('World/Encounters/IvorySanctum/UnlockableFlags/EnableEggDialog.jbp',), 'adjacent:devarrahx2.json'),
    'camellia.soana_murder_request': Fact('SeenCues', ('f505392f3d7c18348b178da457b4272e', 'b2e418443ec73974faa09a5496564d03', '2fb85dd5779e8c141b15ec119d889fd3'),
        'Any of Camelia Cue_0136 or SoanaAfterBear Cue_0065/Cue_0069 was heard; merely killing Soana proves none of these requests.',
        ('World/Dialogs/Companions/CompanionDialogues/Camelia/Cue_0136.jbp', 'World/Dialogs/c3/Wintersun/SoanaAfterBear/Cue_0065.jbp', 'World/Dialogs/c3/Wintersun/SoanaAfterBear/Cue_0069.jbp'), 'soanahx2.json'),
    'areelu.impostor_freed_encounter': Fact('SeenCues', ('b618fff15d921894e84b9b2fe9efaa39',),
        'Hear FakeYaniel_ToAreelu Cue_0006, the reveal acknowledging the freed impostor; not inferred from reaching Drezen.',
        ('World/Dialogs/c2_vs/DrezenSiege/FakeYaniel_ToAreelu/Cue_0006.jbp',), 'yanielhx2.json'),
    'areelu.impostor_refused_encounter': Fact('SeenCues', ('f1a82798065c27b45aa1d17d9db80dc6',),
        'Hear FakeYaniel_ToAreelu Cue_0014, which acknowledges refusing the prisoner; native SecretPassageShowsItself replaces the guide encounter.',
        ('World/Dialogs/c2_vs/DrezenSiege/FakeYaniel_ToAreelu/Cue_0014.jbp',), 'yanielhx2.json'),
    'nenio.kenabres_insult': Fact('SeenCues', ('41aa8d9d2d0ad874b8370d1dd4679da0',),
        'Hear NenioJoin Cue_0046 after asking whether she calls the Commander mediocre; records her Yes, not recruitment.',
        ('World/Dialogs/c1/MeetNenioSE/NenioJoin/Cue_0046.jbp',), 'neniohx.json'),
    'nenio.kenabres_insult_protested': Fact('SelectedAnswers', ('4e460d9de7451b54cba28ed8961ff848',),
        'Select NenioJoin Answer_0049, Do not dare call me stupid; distinguishes the protest from merely hearing her insult.',
        ('World/Dialogs/c1/MeetNenioSE/NenioJoin/Answer_0049.jbp',), 'adjacent:neniohx.json'),
    'nenio.shouted_name': Fact('SeenCues', ('45450b2f327797e41bce701b91118cb4',),
        'Hear FoxReveal Cue_0023; her shouted name is optional witnessed history, not a lifetime quietness claim.',
        ('World/Dialogs/Companions/CompanionQuests/Nenio/Q1MoreThanNothing/FoxReveal/Cue_0023.jbp',), 'neniohx2.json'),
    'nenio.threshold_farewell': Fact('SeenCues', ('240e6a0b130026a4d8558897b53e7f4d',),
        'Hear NenioFarewell Cue_0007 at Threshold; proves this encounter, not her continuous or current physical presence.',
        ('World/Dialogs/c6/ThresholdExterior/CompanionFarewells/NenioFarewell/Cue_0007.jbp',), 'neniohx2.json'),
    'herald.heart_restored': Fact('SeenCues', ('55ab2d8561d68ad4aae145e4798b43d4',),
        'Hear Labyrinth Herald Cue_0021 after restoring his heart; does not establish Heaven or exile.',
        ('World/Dialogs/c5/LabyrinthOfBaphometh/Herald/Cue_0021.jbp',), 'iomedaehx2.json'),
    'herald.returned_to_heaven': Fact('SeenCues', ('6a9482523b5ac1646823a4866485f0ab',),
        'Hear Labyrinth Herald Cue_0028, reached by the Angel-only return answer; this is distinct from restoring his heart.',
        ('World/Dialogs/c5/LabyrinthOfBaphometh/Herald/Cue_0028.jbp',), 'iomedaehx2.json'),
    'herald.exiled': Fact('SeenCues', ('58565f5d678283e4b94874f5a07bdbc2',),
        'Hear Labyrinth Herald Cue_0031, his exile farewell, accessible to a Trickster after restoring his heart.',
        ('World/Dialogs/c5/LabyrinthOfBaphometh/Herald/Cue_0031.jbp',), 'iomedaehx2.json'),
    'herald.died_in_labyrinth': Fact('SeenCues', ('c241ccdbc3b178b41b7161d17ff43b17', '1f0fef1fbc666cc42a213671d6b171a2'),
        'Hear Labyrinth Herald Cue_0020 or Cue_0026; records death without substituting it for restoration or exile.',
        ('World/Dialogs/c5/LabyrinthOfBaphometh/Herald/Cue_0020.jbp', 'World/Dialogs/c5/LabyrinthOfBaphometh/Herald/Cue_0026.jbp'), 'adjacent:iomedaehx2.json'),
    'aeon.irabeth_solitary': Fact('SeenCues', ('924904a1b8400324894cb6119b44325b',),
        'Hear AeonFinalWorld Cue_0024, which says Irabeth never started a family in the rewritten world.',
        ('World/Dialogs/Epilogues/Cue_0024.jbp',), 'irabethhx3.json'),
    'aeon.anevia_died': Fact('SeenCues', ('f8a5d88cf76a2134e8e3f3b8a617e2c1',),
        'Hear AeonFinalWorld Cue_0021, Anevia died in the River Kingdoms in the rewritten history.',
        ('World/Dialogs/Epilogues/Cue_0021.jbp',), 'irabethhx3.json'),
    'aeon.terendelev_spared': Fact('Etudes', ('6b98ec3e704599149b99fe70b5f793ab',),
        'The native Aeon intervention etude was started/playing or completed; a historical intervention, not current Aeon power.',
        ('World/Etudes/Common/WrathOfTheRighteous/MythicAeon/AeonStates/TerendelevWasNotKilled.jbp',), 'adjacent:irabethhx3.json'),
    'nocticula.audience_witnessed': Fact('SeenCues', ('e7aeebbcb6d08ac46bdb731fbd601348',),
        'Hear Nocticula_main Cue_0074, her appearance at the first palace audience; no departure or permission is inferred.',
        ('World/Dialogs/c4/Nocticula_main/Cue_0074.jbp',), 'herraxhx3.json'),
    'nocticula.permitted_city_return': Fact('SeenCues', ('30469883ce1583743a6b4228d24778bc',),
        'Hear Nocticula_main Cue_0022, permission to enjoy the city and return for business; does not mean Colyphyr was visited.',
        ('World/Dialogs/c4/Nocticula_main/Cue_0022.jbp',), 'herraxhx3.json'),
    'fool_king.accepted': Fact('SeenCues', ('fb5dd1021f76e314ba12a1a2067886cd',),
        'KTC_FoolKingArrives Cue_0022 gives the coronation objectives and starts FoolKingAvailable; acceptance is distinct from crowning.',
        ('World/Dialogs/c3/Mythic_Trickster/KTC_FoolKingArrives/Cue_0022.jbp',), 'iomedaehx3.json'),
    'fool_king.rejected': Fact('SelectedAnswers', ('6d30d2b547164d14e919e23d7813ed14',),
        'Select KTC_FoolKingArrives Answer_0006, throw the drunkard out.',
        ('World/Dialogs/c3/Mythic_Trickster/KTC_FoolKingArrives/Answer_0006.jbp',), 'iomedaehx3.json'),
    'fool_king.rejected_after_claim': Fact('SelectedAnswers', ('81b075f17dabe9e4598f8fed92b3cf5b',),
        'Select KTC_FoolKingArrives Answer_0020, throw the impostor out after his claim.',
        ('World/Dialogs/c3/Mythic_Trickster/KTC_FoolKingArrives/Answer_0020.jbp',), 'iomedaehx3.json'),
    'fool_king.crowned': Fact('Etudes', ('cc76b7abcda591f438d0f24972dafddc',),
        'FoolKingCoronated was started/playing or completed by the coronation; rejected arrival answers cannot establish this.',
        ('World/Etudes/Common/WrathOfTheRighteous/MythicTrickster/PlayerIsTrickster/FoolKing/FoolKingCoronated.jbp',), 'iomedaehx3.json'),
    'arsinoe.souls_vision_heard': Fact('SeenCues', ('a473e5412ffd0f54fbf395770a80a008',),
        'Hear ktc_ElanCalls Cue_0019 describing the vision of Gravestone Rock; locating souls is not recovering them.',
        ('World/Dialogs/Companions/CompanionQuests/Seelah/Q3_WeightOfMySword/ktc_ElanCalls/Cue_0019.jbp',), 'kianahx2.json'),
    'seelah.souls_returned': Fact('CompletedQuests', ('5a5a533c9ce630a48b877f9a194840cb',),
        'Native Seelah Q3 completes; separate from an authored ransom and from merely locating the gems.',
        ('World/Quests/Companions/Seelah/Q3_WeightOfMySword/WeightOfMySword_SeelahQ3_quest.jbp',), 'adjacent:kianahx2.json'),
    'konomi.dismissed': Fact('SelectedAnswers', ('73c5728c4c6658344bedcc1b666e598c',),
        'Select Diplomacy_6 Answer_0070 dismissing the Royal Council; missed contact or completed office alone does not prove dismissal.',
        ('World/Crusade/RankUps/Diplomacy/Diplomacy_6/Answer_0070.jbp',), 'konomihx2.json'),
    'vellexia.slaves_released_before_kill': Fact('SeenCues', ('6906a289597ab6e41873e79b71f96c95',),
        'Hear Cue_0095, the living release; the general SlavesFreed etude also covers the later execution and cannot establish chronology.',
        ('World/Dialogs/c4/RaptureOfRupture/Velexia_Third_Date/Cue_0095.jbp',), 'vellexiahx3.json'),
    'irabeth.encouraged': Fact('Etudes', ('8b0924efc23df3540b4d8b5fbffd522f',),
        'Native Irabeth encouragement ending etude was started/playing or completed; native Cue_0308 keeps the Tirabades in service for years.',
        ('World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/Irabeth/IrabethEncouraged_Chapter03.jbp',), 'irabethhx3.json'),
    'irabeth.broken': Fact('Etudes', ('7a038ff7b70e91844954407b18e8feb6',),
        'Native Irabeth broken ending etude was started/playing or completed; native Cue_0566 retires the Tirabades to the River Kingdoms.',
        ('World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/Irabeth/IrabethBroken_Chapter03.jbp',), 'irabethhx3.json'),
    'galfrey.native_romance_finished': Fact('Etudes', ('133f3b1b38f04fa44be3200b786e437f',),
        'Native Galfrey romance-finished etude was started/playing or completed; native Cue_0249 records abdication, not a retained crown.',
        ('World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/Galfrey/GalfreyRomance/GalfreyRomance_Finished.jbp',), 'galfreyhx4.json'),
    'guild.headquarters_moved_heard': Fact('SeenCues', ('35c428d079c243c4a88a92b0cc1b35c9',),
        'Hear Yozz_HailNewLord Cue_0007 describing Horzalah moving the Guild to her fathers realm; not a return to Alushinyrra.',
        ('World/Dialogs/c5/Mythic_Demon/Demons_InTheDrezen/Yozz_HailNewLord/Cue_0007.jbp',), 'horzalahhx.json'),
    'minagho.hideout_terror': Fact('SeenCues', ('99854f97811aa0b4eac54ccd352decbc',),
        'Hear MinaghoAfterCombat Cue_0029 in the Chapter 4 hideout; MinaghoTerrified does not prove a Chapter 5 prison visit.',
        ('World/Dialogs/c4/Minagho_Desperation/MinaghoAfterCombat/Cue_0029.jbp',), 'minagho-and-chivarrohx.json'),
}


def key(name):
    if name not in FACTS:
        raise ValueError(f"Unknown native-history fact: {name}")
    return PREFIX + name


def conditioned(record, fact, *, neutral=False):
    """Copy a predicate-bearing record; do not mutate the caller's save layout."""
    result = copy.deepcopy(record)
    field = "Forbids" if neutral else "Requires"
    flag = key(fact)
    result[field] = list(result.get(field, []))
    if flag not in result[field]:
        result[field].append(flag)
    return result


def recollection_choices(remembered, neutral, fact):
    """Return disjoint choices: retain the old choice index, append the neutral."""
    return conditioned(remembered, fact), conditioned(neutral, fact, neutral=True)


def verify(archive=None, facts=None):
    """Validate every static GUID/type/path citation before exporting readers."""
    table = FACTS if facts is None else facts
    with ZipFile(archive or game_dir() / "blueprints.zip") as z:
        for name, fact in table.items():
            if fact.reader not in READER_TYPES or not fact.guids or len(fact.guids) != len(fact.evidence):
                raise ValueError(f"NativeFact {name}: invalid reader or evidence list")
            if fact.reader != "SeenCues" and len(fact.guids) != 1:
                raise ValueError(f"NativeFact {name}: {fact.reader} needs exactly one GUID; use separate facts")
            if not fact.how_set or not fact.audit:
                raise ValueError(f"NativeFact {name}: missing setting/audit evidence")
            for guid, path in zip(fact.guids, fact.evidence):
                try:
                    record = json.loads(z.read(path))
                except KeyError as ex:
                    raise ValueError(f"NativeFact {name}: missing evidence path {path}") from ex
                if record["AssetId"] != guid or blueprint_type(record["Data"]) != READER_TYPES[fact.reader]:
                    raise ValueError(f"NativeFact {name}: GUID/type mismatch for {guid} at {path}")
                if fact.reader == "SelectedAnswers" and not record["Data"].get("AddToHistory", False):
                    raise ValueError(f"NativeFact {name}: answer {guid} is not recorded in native history; use its observed cue")


def integrate(payload, archive=None):
    verify(archive)
    permanent = set(payload.get("PermanentEtudes", []))
    for name, fact in FACTS.items():
        flag = key(name)
        value = list(fact.guids) if fact.reader == "SeenCues" else fact.guids[0]
        readers = payload.setdefault(fact.reader, {})
        if flag in readers and readers[flag] != value:
            raise ValueError(f"NativeFact {name}: conflicting reader")
        readers[flag] = value
        if fact.reader == "Etudes":
            permanent.add(flag)  # historical started/playing OR completed, never a live-path power
    payload["PermanentEtudes"] = sorted(permanent)
