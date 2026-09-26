"""Build the incomplete expansion into development/, never into the installed mod."""
import copy
import json
from pathlib import Path

from story import make_story
from storylines import kiana_followthrough, seelah_late_campaign, tirabade_reckoning
from storylines import jerribeth_counteroffer
from storylines import seelah_return, seelah_progression, kiana_progression
from storylines import tirabade_after_roads, tirabade_progression, jerribeth_progression
from storylines import arsinoe_opening, konomi_political
from storylines import jerribeth_fate
from storylines import arsinoe_continuation, soana_continuation
from storylines import targona_opening, kiana_further
from storylines import kiana_reconciliation, gesmerha_opening
from storylines import vellexia_opening, konomi_ordinary_expansion
from storylines import aivu_opening
from storylines import konomi_private_absence
from storylines import soana_later_progression, soana_late_campaign
from storylines import tirabade_chronology
from storylines import konomi_private_consequence, konomi_early_reciprocity
from storylines import aranka_continuation
from storylines import konomi_contact, konomi_political_consequence
from storylines import anevia_independent, irabeth_independent, tirabade_independent_bridge
from storylines import arsinoe_campaign
from storylines import gesmerha_campaign
from storylines import ember_campaign
from storylines import vellexia_campaign
from storylines import tirabade_later, tirabade_campaign, seelah, seelah_later, seelah_fate, seelah_abyss, seelah_aftermath, konomi, konomi_history, konomi_private, konomi_distance, konomi_future, konomi_private_hearing, jerribeth, jerribeth_consequences, kiana, kiana_consequences, ember, ember_afternoons, soana_opening

ROOT = Path(__file__).parent


def make_expansion(*, independent_tirabade=True):
    payload = copy.deepcopy(make_story())
    # Explicit legacy metadata also lets older authored Story.json files keep using
    # the C# defaults while this larger export carries independent relationships.
    payload["Relationships"] = {
        "tirabade": dict(
            Title="Three at the Table",
            Description="There is room for more than military reports in my conversations with Anevia and Irabeth. What we make of that time is another matter.",
            Objective="Make time for Anevia and Irabeth",
            Guidance="Speak to each woman at headquarters. Private conversations develop over the campaign, with time between meetings. In the Abyss, there may be time to write during a quiet rest.",
            StartedFlag="started", ClosedFlag="closed", CommittedFlag="committed",
            UnavailableFlags=["anevia_dead", "irabeth_dead", "anevia_gone", "irabeth_gone", "swarm", "true_lich"],
            FailureFlags=["loss", "inhuman"],
        ),
        "seelah": seelah.RELATIONSHIP,
        "konomi": konomi.RELATIONSHIP,
        "jerribeth": jerribeth.RELATIONSHIP,
        "kiana": kiana.RELATIONSHIP,
        "ember": ember.RELATIONSHIP,
        "soana": soana_opening.RELATIONSHIP,
        "arsinoe": arsinoe_opening.RELATIONSHIP,
    }
    etudes = json.loads((ROOT / "reference/expansion/etudes.json").read_text(encoding="utf-8"))
    companion = "World/Etudes/Common/WrathOfTheRighteous/Companions/SeelahCompanion/"
    payload["Etudes"].update({
        "konomi.present": "b5f301fbc4c44535a6309d610d5bd28a",
        "ember.present": "3a708ad53771a2d44ac506361fb7aafc",
        "ember_dead": "fcbd1ad00e1c7044b8485d7feda8b9b7",
        "ember_gone": "787273d702a87884e9f14cfb7ef91180",
        "ember.absent": "79519b75e04ffc744b9bb72a2b369786",
        "seelah_dead": etudes[companion + "SeelahNotInParty_Dead.jbp"],
        "seelah_gone": etudes[companion + "SeelahNotInParty_KickedOut.jbp"],
        "seelah.elan_dead": "148423f1d35917946a5ebeeb4f19246c",
        "seelah.ending_moderate": "2bb1f6f30ca9bb1408f720d6f10c5c05",
        "seelah.ending_bad": "e438007efc4f1474eb447031d4b5a60e",
        "jerribeth.unavailable": "cd8666952065ce74d94d960a23482133",
        "jerribeth.patron_lost": "72e423c719ed9d44fa432a6b9629babd",
        "soana.after_quest": "fccdd316924af204da00c99f01c0e222",
        "soana.old_defender": "c97882cbc65c4c546aed1810627a5b81",
        "soana.bear_dead": "995f0ac2951bbb041b062806c163fbf1",
        "soana.forest_dead": "ff0d7227c56b2b0488b006893b96040e",
        "soana.dead": "d4b624463e52e21438da6f4870320fee",
        "soana.killed_by_camellia": "f102a4d0677148f4cab007f901a5ed3c",
    })
    payload["CompletedQuests"] = {
        "seelah.souls_returned": "5a5a533c9ce630a48b877f9a194840cb",
    }
    payload["SelectedAnswers"] = {
        "konomi.dismissed": "73c5728c4c6658344bedcc1b666e598c",
    }
    payload["CompletedEtudes"] = {
        "konomi.office_completed": "b5f301fbc4c44535a6309d610d5bd28a",
    }
    payload["Revivals"] = {
        "seelah": dict(Relationship="seelah", Unit="54be53f0b35bf3c4592a97ae335fe765", DeathFlag="seelah_dead"),
    }
    payload["SeenCues"] = {
        "kiana.aftermath_seen": ["81109ea8fb20dbc478cf67116740f4a1", "aebbc1845e827dd4da4e28014e7b4162"],
        "jerribeth.met": ["666c827662e8af14798009a98c5aae52", "8a632a5249b3c2541a1381111cae9e37", "3857231db61891944999387a4154e9fb", "a1f97de9145c3574ebd2d7f75c3d39c9"],
        "jerribeth.wintersun_known": ["b2997124f3662e147a029a6f73e13468"],
        "jerribeth.xanthir_known": ["bf1542830cfa01d4c9db04546681084d"],
        "jerribeth.refuge_known": ["edeeb17ba4f3d124890d22bdd2d8901d"],
    }
    payload["Scenes"].extend(copy.deepcopy(seelah.SCENES))
    payload["Scenes"].extend(copy.deepcopy(tirabade_later.SCENES))
    payload["Scenes"].extend(copy.deepcopy(tirabade_campaign.SCENES))
    payload["Scenes"].extend(copy.deepcopy(seelah_later.SCENES))
    payload["Scenes"].extend(copy.deepcopy(seelah_fate.SCENES))
    payload["Scenes"].extend(copy.deepcopy(seelah_abyss.SCENES))
    payload["Scenes"].extend(copy.deepcopy(seelah_aftermath.SCENES))
    payload["Scenes"].extend(copy.deepcopy(konomi.SCENES))
    payload["Scenes"].extend(copy.deepcopy(konomi_history.SCENES))
    payload["Scenes"].extend(copy.deepcopy(konomi_private.SCENES))
    payload["Scenes"].extend(copy.deepcopy(konomi_distance.SCENES))
    payload["Scenes"].extend(copy.deepcopy(konomi_future.SCENES))
    payload["Scenes"].extend(copy.deepcopy(konomi_private_hearing.SCENES))
    payload["Scenes"].extend(copy.deepcopy(jerribeth.SCENES))
    payload["Scenes"].extend(copy.deepcopy(jerribeth_consequences.SCENES))
    payload["Scenes"].extend(copy.deepcopy(kiana.SCENES))
    payload["Scenes"].extend(copy.deepcopy(kiana_consequences.SCENES))
    payload["Scenes"].extend(copy.deepcopy(kiana_followthrough.SCENES))
    payload["Scenes"].extend(copy.deepcopy(ember.SCENES))
    payload["Scenes"].extend(copy.deepcopy(ember_afternoons.SCENES))
    payload["Scenes"].extend(copy.deepcopy(soana_opening.SCENES))
    payload["Scenes"].extend(copy.deepcopy(seelah_late_campaign.SCENES))
    payload["Scenes"].extend(copy.deepcopy(tirabade_reckoning.SCENES))
    payload["Scenes"].extend(copy.deepcopy(jerribeth_counteroffer.SCENES))
    payload["Scenes"].extend(copy.deepcopy(seelah_return.SCENES))
    payload["Scenes"].extend(copy.deepcopy(seelah_progression.SCENES))
    payload["Scenes"].extend(copy.deepcopy(kiana_progression.SCENES))
    payload["Scenes"].extend(copy.deepcopy(tirabade_after_roads.SCENES))
    payload["Scenes"].extend(copy.deepcopy(tirabade_progression.SCENES))
    payload["Scenes"].extend(copy.deepcopy(jerribeth_progression.SCENES))
    payload["Etudes"].update(arsinoe_opening.ETUDES)
    payload["Scenes"].extend(copy.deepcopy(arsinoe_opening.SCENES))
    payload["Scenes"].extend(copy.deepcopy(konomi_political.SCENES))
    payload["Scenes"].extend(copy.deepcopy(jerribeth_fate.SCENES))
    payload["Scenes"].extend(copy.deepcopy(arsinoe_continuation.SCENES))
    payload["Scenes"].extend(copy.deepcopy(soana_continuation.SCENES))
    tirabade_progression.integrate(payload)
    konomi_political.integrate(payload)
    jerribeth_fate.integrate(payload)
    payload["Scenes"].extend(copy.deepcopy(targona_opening.SCENES))
    payload["Relationships"]["targona"] = targona_opening.RELATIONSHIP
    payload["Etudes"].update(targona_opening.ETUDES)
    payload["CompletedQuests"].update(targona_opening.COMPLETED_QUESTS)
    payload["SeenCues"].update(targona_opening.SEEN_CUES)
    payload["Scenes"].extend(copy.deepcopy(kiana_further.SCENES))
    kiana_further.integrate(payload)
    payload["Scenes"].extend(copy.deepcopy(kiana_reconciliation.SCENES))
    kiana_reconciliation.integrate(payload)
    payload["Scenes"].extend(copy.deepcopy(gesmerha_opening.SCENES))
    payload["Relationships"]["gesmerha"] = gesmerha_opening.RELATIONSHIP
    payload["Etudes"].update(gesmerha_opening.ETUDES)
    payload["CompletedQuests"].update(gesmerha_opening.COMPLETED_QUESTS)
    payload["Scenes"].extend(copy.deepcopy(vellexia_opening.SCENES))
    payload["Relationships"]["vellexia"] = copy.deepcopy(vellexia_opening.RELATIONSHIP)
    payload["Etudes"].update(vellexia_opening.ETUDES)
    payload["SeenCues"].update(vellexia_opening.SEEN_CUES)
    payload["CompletedQuests"].update(vellexia_opening.COMPLETED_QUESTS)
    payload["Scenes"].extend(copy.deepcopy(vellexia_campaign.SCENES))
    vellexia_campaign.integrate(payload)
    payload["Relationships"]["vellexia"]["Guidance"] = (
        "Complete the gallery interlude and its two follow-up visits before accepting Vellexia's Battlebliss invitation. "
        "All eight visits take place in her manor without a required wait. "
        "After she offers the echo shell, complete her native dates and leave peacefully when she dismisses you. "
        "The correspondence can then continue at the Nexus, and later in Drezen after your return from the Abyss. "
        "Her native dates remain separate. The shell carries her voice and image; it does not bring her to you."
    )
    payload["Scenes"].extend(copy.deepcopy(konomi_ordinary_expansion.SCENES))
    konomi_ordinary_expansion.integrate(payload)
    payload["Scenes"].extend(copy.deepcopy(aivu_opening.SCENES))
    payload["Relationships"]["aivu"] = aivu_opening.RELATIONSHIP
    payload["Etudes"].update(aivu_opening.ETUDES)
    payload["Scenes"].extend(copy.deepcopy(konomi_private_absence.SCENES))
    konomi_private_absence.integrate(payload)
    payload["Scenes"].extend(copy.deepcopy(soana_later_progression.SCENES))
    tirabade_chronology.integrate(payload)
    payload["Scenes"].extend(copy.deepcopy(konomi_private_consequence.SCENES))
    konomi_private_consequence.integrate(payload)
    payload["Scenes"].extend(copy.deepcopy(konomi_early_reciprocity.SCENES))
    konomi_early_reciprocity.integrate(payload)
    payload["Scenes"].extend(copy.deepcopy(aranka_continuation.SCENES))
    payload["Relationships"]["aranka"] = aranka_continuation.RELATIONSHIP
    payload["Etudes"].update(aranka_continuation.ETUDES)
    payload["SeenCues"].update(aranka_continuation.SEEN_CUES)
    payload["CompletedQuests"].update(aranka_continuation.COMPLETED_QUESTS)
    payload["Scenes"].extend(copy.deepcopy(konomi_political_consequence.SCENES))
    konomi_political_consequence.integrate(payload)
    konomi_contact.integrate(payload)
    for scene in payload["Scenes"]:
        if scene.get("Relationship") == "konomi":
            for node in scene["Nodes"]:
                if node.get("Speaker") == "Narrator" and not node.get("Portrait"):
                    node["Portrait"] = "Konomi"
    payload["Scenes"].extend(copy.deepcopy(soana_late_campaign.SCENES))
    if independent_tirabade:
        for who, module in (("anevia", anevia_independent), ("irabeth", irabeth_independent)):
            payload["Relationships"][who] = copy.deepcopy(module.RELATIONSHIP)
            payload["Scenes"].extend(copy.deepcopy(module.SCENES))
        payload["Etudes"].update(anevia_independent.ETUDES)
        irabeth_independent.integrate(payload)
        tirabade_independent_bridge.integrate(payload)
    payload["Scenes"].extend(copy.deepcopy(arsinoe_campaign.SCENES))
    payload["Scenes"].extend(copy.deepcopy(gesmerha_campaign.SCENES))
    gesmerha_campaign.integrate(payload)
    payload["Etudes"].update(ember_campaign.ETUDES)
    payload["CompletedQuests"].update(ember_campaign.COMPLETED_QUESTS)
    payload["Scenes"].extend(copy.deepcopy(ember_campaign.SCENES))
    return payload


if __name__ == "__main__":
    output = ROOT / "development/Story.json"
    output.parent.mkdir(exist_ok=True)
    payload = make_expansion()
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"INCOMPLETE DEVELOPMENT EXPORT: {len(payload['Scenes'])} scenes -> {output}")
