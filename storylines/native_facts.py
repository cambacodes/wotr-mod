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
                    UnlockableFlags="BlueprintUnlockableFlag",
                    QuestObjectives="BlueprintQuestObjective")  # eng7-l02


@dataclass(frozen=True)
class Fact:
    reader: str
    guids: tuple
    how_set: str
    evidence: tuple
    audit: str
    state: str = ""  # eng7-l02: QuestObjectives pair state; never inferred from a project start.


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
            # eng7-l02: objective states are part of evidence, not arbitrary history flags.
            if (fact.reader == "QuestObjectives" and fact.state not in {"Started", "Completed", "Failed"}) or (fact.reader != "QuestObjectives" and fact.state):
                raise ValueError(f"NativeFact {name}: invalid objective state")
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
        # eng7-l02: retain the native objective's exact completed-state contract.
        value = ([fact.guids[0], fact.state] if fact.reader == "QuestObjectives" else
                 list(fact.guids) if fact.reader == "SeenCues" else fact.guids[0])
        readers = payload.setdefault(fact.reader, {})
        if flag in readers and readers[flag] != value:
            raise ValueError(f"NativeFact {name}: conflicting reader")
        readers[flag] = value
        if fact.reader == "Etudes":
            permanent.add(flag)  # historical started/playing OR completed, never a live-path power
    payload["PermanentEtudes"] = sorted(permanent)
    # eng7-l02: optional observations select wording, never become romance entry gates.
    inventory_consumers(payload)
    from tools.native_fact_inventory import verify_inventory
    verify_inventory(payload, archive)
    # eng7-l02 end


# eng7-l02: cited native witnesses added to q6b's single history registry.
FACTS.update({
    'arueshalae.first_dream': Fact('SeenCues', ('57ebbd804c32df74a866bba2f79b3acb',),
        'Hear her very first dream in DreamVisit_1-1 Cue_0002, not just a treatment morning.',
        ('World/Dialogs/Companions/CompanionQuests/Arueshalae/Q1/DreamVisit_1-1/Cue_0002.jbp',), 'arueshalae:007'),
    'ulbrig.powers_price': Fact('SeenCues', ('97d61a5c383b41639aacc800dc703252',),
        'Hear the optional powers/payment discussion in Cue_6 after Answer_0004; a greeting is insufficient.',
        ('World/Dialogs/DLC4_Shifter/Shifter_CompanionDialogue/Cue_6.jbp',), 'soana:002'),
    'nenio.bite_boast': Fact('SelectedAnswers', ('20a557207800252419c55049322943c4',),
        'Select the native bite boast, Answer_0132.',
        ('World/Dialogs/Companions/CompanionDialogues/Nenio/Answer_0132.jbp',), 'nenio:031-033'),
    'nenio.named_self': Fact('SelectedAnswers', ('9051b7f03a183094591ca0f729817283',),
        'Answer the void with the Commander name, FoxReveal Answer_0013.',
        ('World/Dialogs/Companions/CompanionQuests/Nenio/Q1MoreThanNothing/FoxReveal/Answer_0013.jbp',), 'nenio:037-039'),
    'nenio.lied_galfrey': Fact('SelectedAnswers', ('a70db7009a08bd94aab35660299712b6',),
        'Lie to the void as Galfrey, FoxReveal Answer_0014.',
        ('World/Dialogs/Companions/CompanionQuests/Nenio/Q1MoreThanNothing/FoxReveal/Answer_0014.jbp',), 'nenio:037-039'),
    'nenio.lied_deskari': Fact('SelectedAnswers', ('2b4e81f903934de4ca5f58baa3b9e87e',),
        'Lie to the void as Deskari, FoxReveal Answer_0015.',
        ('World/Dialogs/Companions/CompanionQuests/Nenio/Q1MoreThanNothing/FoxReveal/Answer_0015.jbp',), 'nenio:037-039'),
    'nenio.refused_void': Fact('SelectedAnswers', ('778303b3cff06cc4fba3a3645313eb5c',),
        'Refuse the void question, FoxReveal Answer_0009, not merely leave or ask a question.',
        ('World/Dialogs/Companions/CompanionQuests/Nenio/Q1MoreThanNothing/FoxReveal/Answer_0009.jbp',), 'nenio:037-039'),
    'kaylessa.letter_sent': Fact('Etudes', ('78fb64bf32f3f194ab077315650adf10',),
        'Kaylessa_Letter success starts KaylessaTomb; completed etude still proves sending, unlike live tomb availability.',
        ('World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/Kaylessa/KaylessaTomb.jbp',), 'kaylessa:004'),
    'kaylessa.message_resolved': Fact('QuestObjectives', ('e4b225860f1f1c947a6df5c80acf9872',),
        'Both Kaylessa_Letter and Kaylessa_Conceal complete Obj6_SendMessage. Combine with durable Letter evidence to distinguish them.',
        ('World/Quests/c1/HuntingKaylessa/Obj6_SendMessage.jbp',), 'kaylessa:004', 'Completed'),
    'minagho.prison_brand_heard': Fact('SeenCues', ('c5f918382f54e4342b40334c2d9f854f',),
        'Hear Baphomet explain Minagho seals in the Chapter 5 prison, not MinaghoTerrified in the Chapter 4 hideout.',
        ('World/Dialogs/c5/LabyrinthOfBaphometh/Prison_Baph/Cue_0123.jbp',), 'minagho-and-chivarro:003'),
})


def history_variant(scene, node_id, fact, neutral_text):
    """Keep old node/choice indices; append neutral twins for every incoming edge."""
    # Placement twins share nested choice lists in their source templates.
    # Isolate this scene before adding a history requirement to an incoming edge.
    scene['Nodes'] = copy.deepcopy(scene['Nodes'])
    nodes = scene['Nodes']
    old = next(n for n in nodes if n['Id'] == node_id)
    neutral = copy.deepcopy(old)
    neutral['Id'] = node_id + '.history_neutral'
    neutral['Text'] = neutral_text
    nodes.append(neutral)
    for node in nodes[:-1]:
        appended = []
        for choice in node['Choices']:
            if choice.get('Next') != node_id:
                continue
            twin = copy.deepcopy(choice)
            choice.setdefault('Requires', []).append(fact)
            twin['Next'] = neutral['Id']
            twin.setdefault('Forbids', []).append(fact)
            appended.append(twin)
        node['Choices'].extend(appended)


def reaction_variant(payload, scene, fact, neutral_text):
    """Reactions keep their one-page contract; append a disjoint neutral scene."""
    neutral = copy.deepcopy(scene)
    neutral['Id'] = scene['Id'] + '.history_neutral'
    neutral['Nodes'][0]['Text'] = neutral_text
    neutral['Forbids'].extend([fact, scene['Id']])
    # Completing either version consumes the same existing one-time reaction.
    for choice in neutral['Nodes'][0]['Choices']:
        choice['Set'].append(scene['Id'])
    scene['Requires'].append(fact)
    payload['Scenes'].append(neutral)


def inventory_consumers(payload):
    """E-Q7-10 wiring only: no costs, closures, permissions or new outcome requirements."""
    scenes = {s['Id']: s for s in payload['Scenes']}
    derived = payload.setdefault('Derived', {})
    derived['native.history.nenio.lied_void'] = [[key('nenio.lied_galfrey')], [key('nenio.lied_deskari')]]
    derived['minachiv.reunion_history'] = [['chivarro.searching'], ['minagho_chivarro.trickster.reunited']]
    derived['native.history.fool_king.resident'] = [[key('fool_king.crowned')]]
    derived['native.history.fool_king.engaged'] = [[key('fool_king.accepted')], [key('fool_king.crowned')]]
    payload.setdefault('DerivedForbids', {})['native.history.fool_king.resident'] = ['fool_king.gone']
    # The parent's completed Book 3 is still required; an earned authored reunion supplies its own provenance.
    for scene in scenes.values():
        if scene['Id'].startswith('minachiv.') and 'chivarro.searching' in scene.get('Requires', []):
            scene['Requires'] = ['minachiv.reunion_history' if f == 'chivarro.searching' else f for f in scene['Requires']]

    scene = scenes['arueshalae.treatment.nightmare']
    start = scene['Nodes'][0]
    start['Text'] = '{n}She has woken you with a cry. When you get to her she is sitting bolt upright on her bedroll with her wings half open and her nails dug into her own arms.{/n}'
    history_variant(scene, 'dream', key('arueshalae.first_dream'),
        '"I remembered them. The priestess. The sergeant. Everyone." {n}She is shaking.{/n} "All those faces. I shut my eyes and there they were, waiting for me to feed. I could not make them go away."')
    history_variant(scene, 'price', key('arueshalae.first_dream'),
        '{n}She lowers her hands and looks at you.{/n} "You are here." {n}She takes a fistful of your shirt and does not let go.{/n} "Stay till it is light. Not every night. This one."')

    scene = scenes['herrax.house.the_glowworm']
    text = next(n['Text'] for n in scene['Nodes'] if n['Id'] == 'joke')
    history_variant(scene, 'joke', key('nocticula.permitted_city_return'),
        text.replace('the mortal the Lady let walk out of her palace', 'the mortal leading the crusade'))
    scene = scenes['horzalah.trickster.beat.storyteller']
    text = next(n['Text'] for n in scene['Nodes'] if n['Id'] == 'me')
    history_variant(scene, 'me', 'native.history.fool_king.resident',
        text.replace(' That a king of fools in this very city drinks to your health every night.', ''))
    scene = scenes['iomedae.trickster.dream.mortal']
    text = next(n['Text'] for n in scene['Nodes'] if n['Id'] == 'properly')
    history_variant(scene, 'properly', 'native.history.fool_king.engaged',
        text.replace(', and on a king who calls a tavern his throne room', ''))

    for suffix in ('', '_visitor', '_arcade'):
        scene = scenes['nenio.folio.teeth' + suffix]
        text = next(n['Text'] for n in scene['Nodes'] if n['Id'] == 'direct')
        history_variant(scene, 'direct', 'nenio.told_bite',
            text.replace('a subject who has claimed it could be considerable', 'a willing subject with a useful set of teeth'))
        # The shipped who_are_you is hub-only; visitor/arcade were already removed
        # from generation before this inventory. Do not recreate historical twins.
        if 'nenio.folio.who_are_you' + suffix not in scenes:
            continue
        scene = scenes['nenio.folio.who_are_you' + suffix]
        opening = scene['Nodes'][0]
        for choice, fact in zip(opening['Choices'], (key('nenio.named_self'), 'native.history.nenio.lied_void', key('nenio.refused_void'))):
            choice['Requires'].append(fact)
        opening['Choices'].append(dict(Text='"I would rather talk about what it asked you."', Next='question', Set=[], Requires=[], Forbids=[], Abort=False))
        # The shout is optional too; keep this class neutral at every sibling callback.
        opening['Text'] = opening['Text'].replace(' Then I shouted it. It was still not enough, and it took my face off and showed me the fox under it.', ' It took my face off and showed me the fox under it.')
        for node in scene['Nodes']:
            if node['Id'] == 'silent':
                node['Text'] = node['Text'].replace('I shouted my name at it like a fishwife', 'I gave it my name')
            if node['Id'] == 'question':
                for choice in node['Choices']:
                    choice['Text'] = choice['Text'].replace('you, shouting at it', 'you, facing it')

    scene = scenes['soana.trickster.epilogue.by_your_hand']
    paragraphs = scene['Nodes'][0]['Paragraphs']
    request = key('camellia.soana_murder_request')
    original = next(p for p in paragraphs if 'I asked you so nicely' in p['Text'])
    neutral = copy.deepcopy(original)
    original['Requires'].append(request)
    neutral['Forbids'].append(request)
    neutral['Text'] = neutral['Text'].replace('I asked you so nicely for her, my friend, and you simply took her. ', '')
    paragraphs.append(neutral)
    scene = scenes['soana.trickster.react.ulbrig_knot']
    text = scene['Nodes'][0]['Text']
    reaction_variant(payload, scene, key('ulbrig.powers_price'),
        text.replace('I asked you once what these new powers want in return, warchief. Now we know.', 'So that is what these new powers want in return, warchief.'))

    scene = scenes['kiana.trickster.react_arsinoe_souls_home']
    text = scene['Nodes'][0]['Text']
    observed = text.replace('*The stolen souls: no results yet.*', '*The stolen souls: Gravestone Rock.*').replace(
        'If anyone asks me about the stolen souls and I give them that page, stop me. I have read it out every morning since the wedding. My mouth has not caught up with my ledger.',
        'I saw the souls beneath Gravestone Rock. Locating them did not bring them home. Your money did that. I have entered both in the ledger.')
    reaction_variant(payload, scene, key('arsinoe.souls_vision_heard'), text)
    scene['Nodes'][0]['Text'] = observed

    scene = scenes['kaylessa.wasps.last_words']
    sent, resolved = key('kaylessa.letter_sent'), key('kaylessa.message_resolved')
    for choice in scene['Nodes'][0]['Choices']:
        if choice.get('Next') == 'tomb':
            choice['Requires'] = [sent if f == 'kaylessa.tomb' else f for f in choice['Requires']]
        if choice.get('Next') == 'nocame':
            choice['Forbids'] = [sent if f == 'kaylessa.tomb' else f for f in choice['Forbids']]
    nocame = next(n for n in scene['Nodes'] if n['Id'] == 'nocame')
    nocame['Text'] = '"I asked you to send a letter to Avennara at the border. I remember asking." {n}She watches you.{/n} "What did you do with it, soldier?"'
    for choice in nocame['Choices']:
        if choice.get('Next') == 'sold':
            choice['Requires'].append(resolved)
            choice['Forbids'].append(sent)
        else:
            choice['Forbids'].append(resolved)

    # Only the retained-crown partnership earns the crown paragraph; the native romance abdicates.
    scene = scenes['galfrey.lastcall.page']
    paragraphs = scene['Nodes'][0]['Paragraphs']
    crown = next(p for p in paragraphs if 'kept her crown and her Commander' in p['Text'])
    crown['Requires'] = ['galfrey.trickster.alive.committed']
    crown['Forbids'].append('galfrey.romance_finished')
    abdicated = copy.deepcopy(crown)
    abdicated['Requires'] = ['galfrey.romance_finished']
    abdicated['Forbids'] = []
    abdicated['Text'] = 'Galfrey laid down the crown after the war. She stayed with the Commander, and let Mendev find its own answer to that.'
    paragraphs.append(abdicated)
# eng7-l02 end
