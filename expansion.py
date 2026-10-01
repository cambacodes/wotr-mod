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
from storylines import aivu_campaign
from storylines import konomi_private_absence
from storylines import soana_later_progression, soana_late_campaign
from storylines import tirabade_chronology
from storylines import konomi_private_consequence, konomi_early_reciprocity
from storylines import aranka_continuation
from storylines import konomi_contact, konomi_political_consequence
from storylines import konomi_missed_contact
from storylines import konomi_retained_return
from storylines import konomi_return_invitation
from storylines import irabeth_return_invitation
from storylines import minagho_chivarro_continuation
from storylines import nocticula_continuation
from storylines import nocticula_trickster_acquisition
from storylines import nocticula_trickster_concession
from storylines import nocticula_trickster_harbor_join
from storylines import nocticula_acquired_harbor
from storylines import nurah_continuation
from storylines import anevia_independent, irabeth_independent, tirabade_independent_bridge
from storylines import arsinoe_campaign
from storylines import arsinoe_trickster, trickster_world
from storylines import irabeth_trickster
from storylines import anevia_trickster
from storylines import jerribeth_trickster
from storylines import konomi_trickster
from storylines import nocticula_trickster
from storylines import vellexia_trickster
from storylines import nurah_trickster
from storylines import kiana_trickster
from storylines import minagho_chivarro_trickster
from storylines import soana_trickster
from storylines import aranka_trickster
from storylines import gesmerha_trickster
from storylines import seelah_trickster
from storylines import dorgelinda_trickster, dorgelinda_ledger
from storylines import hepzamirah_trickster, hepzamirah_flesh
from storylines import camellia_trickster, camellia_masks, camellia_evenings, camellia_cards, camellia_days, camellia_last  # noqa: F401 (the others append to camellia_trickster.SCENES)
from storylines import targona_trickster
from storylines import eritrice_trickster, eritrice_minutes, eritrice_council
from storylines import areelu_trickster
from storylines import chadali_trickster, chadali_wagers, chadali_fortunes, chadali_sessions, chadali_hours
from storylines import arueshalae_trickster, arueshalae_treatment, arueshalae_rounds, arueshalae_chapel
from storylines import arueshalae_hours, arueshalae_notes
from storylines import devarra_trickster, devarra_tower
from storylines import delamere_trickster, delamere_woods, delamere_fire
from storylines import kaylessa_trickster, kaylessa_wasps, kaylessa_clearing
from storylines import mielarah_trickster, mielarah_deck
from storylines import nidalynn_trickster, nidalynn_kiln, nidalynn_salt
from storylines import shamira_trickster, shamira_mind, shamira_dream
from storylines import jannah_trickster, jannah_circle
from storylines import nenio_trickster, nenio_folios
from storylines import herrax_trickster, herrax_house
from storylines import terendelev_trickster, terendelev_watch
from storylines import eliandra_trickster, eliandra_stars
from storylines import galfrey_trickster, galfrey_kitrane
from storylines import horzalah_trickster, horzalah_guild
from storylines import elyanka_trickster, elyanka_hearse
from storylines import iomedae_trickster, iomedae_banner
from storylines import rrt_ui
from storylines import rrt_portraits
from storylines import scene_kinds
from storylines import lastcall
from storylines import household
from storylines import gesmerha_campaign
from storylines import gesmerha_late_campaign
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
        # Playing only in WintersunOutdoor (area link): the raw reader is a latch source; soana.bear_dead is its latch (trickster_world), so
        # her remote letters (soana.trickster.killed.knot) read the bear's death anywhere (18-ETUDE-BINDING-AUDIT follow-up).
        "soana.bear_dead.live": "995f0ac2951bbb041b062806c163fbf1",
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
    payload["Relationships"]["gesmerha"] = copy.deepcopy(gesmerha_opening.RELATIONSHIP)
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
    payload["Relationships"]["aivu"] = copy.deepcopy(aivu_opening.RELATIONSHIP)
    payload["Etudes"].update(aivu_opening.ETUDES)
    payload["Scenes"].extend(copy.deepcopy(aivu_campaign.SCENES))
    payload["CompletedQuests"].update(aivu_campaign.COMPLETED_QUESTS)
    payload["SeenCues"].update(aivu_campaign.SEEN_CUES)
    payload["Relationships"]["aivu"]["Guidance"] = (
        "Speak with Aivu in Drezen while she is your Azata companion. The map outings begin in Chapter 3, "
        "and the garden visits can continue after your return from the Abyss. If you missed the map outings, "
        "a separate garden introduction is available in Chapter 5. Leave time between outings. "
        "An established friendship also offers optional visits at the Nexus; support after her rescue "
        "requires completing her native rescue quest and having her back with you."
    )
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
        tirabade_independent_bridge.integrate(payload)
        payload["Scenes"].extend(copy.deepcopy(irabeth_return_invitation.SCENES))
    irabeth_independent.integrate(payload)
    tirabade_chronology.integrate_morale(payload)
    payload["Scenes"].extend(copy.deepcopy(arsinoe_campaign.SCENES))
    payload["Scenes"].extend(copy.deepcopy(arsinoe_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(gesmerha_campaign.SCENES))
    gesmerha_campaign.integrate(payload)
    payload["Scenes"].extend(copy.deepcopy(gesmerha_late_campaign.SCENES))
    gesmerha_late_campaign.integrate(payload)
    payload["Relationships"]["gesmerha"]["Guidance"] = (
        "After resolving Wintersun and reporting to Irabeth, speak to Gesmerha at her native trading dialogue. "
        "Keep the Chapter 3 visits while she is available. After returning from the Abyss, look for her in Wintersun "
        "to continue the relationship and help settle the things left to carry. Return between the later visits. "
        "Her possible audience in Drezen offers a separate reunion; it is not required for the later Wintersun visits."
    )
    payload["Etudes"].update(ember_campaign.ETUDES)
    payload["CompletedQuests"].update(ember_campaign.COMPLETED_QUESTS)
    payload["Scenes"].extend(copy.deepcopy(ember_campaign.SCENES))
    konomi_missed_contact.integrate(payload)
    payload["Relationships"]["konomi"] = copy.deepcopy(payload["Relationships"]["konomi"])
    payload["Relationships"]["konomi"]["Guidance"] += (
        " Before her council appointment begins, a Trickster can seek a personal introduction "
        "during a quiet rest in Drezen. Keep her reply and arrange the meeting she offers. "
        "A later council appointment pauses these private visits while she holds the office."
    )
    first_konomi = next(i for i, scene in enumerate(payload["Scenes"]) if scene.get("Relationship") == "konomi")
    payload["Scenes"][first_konomi:first_konomi] = copy.deepcopy(konomi_retained_return.SCENES)
    payload["Scenes"][first_konomi:first_konomi] = copy.deepcopy(konomi_return_invitation.SCENES)
    konomi_return_invitation.integrate(payload)
    payload["Revivals"].update(copy.deepcopy(konomi_retained_return.REVIVALS))
    payload["Relationships"]["konomi"]["UnavailableFlags"].append(konomi_retained_return.DEAD)
    payload["Relationships"]["konomi"]["Description"] = (
        "Lady Konomi's official duties and private choices do not always lead in the same direction. "
        "There may be more to learn in our conversations."
    )
    payload["Relationships"]["konomi"]["Guidance"] += (
        " If Konomi has died and her body remains in Drezen, a Trickster can investigate a possible return "
        "through the available events. After her return, allow half a day before sending a personal letter. "
        "Accept her reply to arrange the first visit. Visits require her to be well enough and available to meet. "
        "A return does not reverse an earlier refusal or restore her office."
    )
    minagho_chivarro_continuation.integrate(payload)
    payload["Scenes"].extend(copy.deepcopy(minagho_chivarro_continuation.SCENES))
    nocticula_continuation.integrate(payload)
    harbor = copy.deepcopy(nocticula_continuation.SCENES)
    for scene in harbor:
        scene["Forbids"].append("noct.join.harbor_variant_ready")
    payload["Scenes"].extend(harbor)
    payload["Scenes"].extend(copy.deepcopy(nocticula_acquired_harbor.SCENES))
    payload["Relationships"]["nocticula"]["Description"] = nocticula_acquired_harbor.RELATIONSHIP["Description"]
    payload["Relationships"]["nocticula"]["Guidance"] = (
        "An existing dream relationship can lead to this undertaking after accepting Nocticula's Chapter 5 offer. "
        "Rest in Drezen while she lives and her Profane Gift remains. "
        "A Trickster who missed or refused that offer can instead earn a separate invitation through personal correspondence. "
        + nocticula_acquired_harbor.RELATIONSHIP["Guidance"]
    )
    acquisition = nocticula_trickster_acquisition
    payload["Relationships"]["nocticula.acquisition"] = copy.deepcopy(acquisition.RELATIONSHIP)
    for key, bindings in (("Etudes", acquisition.ETUDES), ("CompletedEtudes", acquisition.COMPLETED_ETUDES),
                          ("SeenCues", acquisition.SEEN_CUES), ("SelectedAnswers", acquisition.SELECTED_ANSWERS)):
        for flag, binding in bindings.items():
            if flag in payload[key] and payload[key][flag] != binding:
                raise ValueError(f"Conflicting Nocticula binding: {flag}")
            payload[key][flag] = copy.deepcopy(binding)
    # The post-conflict draft has no verified lifecycle producer and is not deliverable yet.
    payload["Scenes"].extend(copy.deepcopy([s for s in acquisition.SCENES if s["Id"] != "noct.acq.after_the_council"]))
    payload["Scenes"].extend(copy.deepcopy(nocticula_trickster_concession.SCENES))
    payload["Scenes"].extend(copy.deepcopy(nocticula_trickster_harbor_join.SCENES))
    nurah_continuation.integrate(payload)
    nurah_scenes = copy.deepcopy(nurah_continuation.SCENES)
    for scene in nurah_scenes:
        if not scene.get("Remote", False):
            scene["InteractionHub"] = "nurah.arrival"
    payload["Scenes"].extend(nurah_scenes)
    payload["ParentEpilogueEdits"] = copy.deepcopy(minagho_chivarro_continuation.PARENT_EPILOGUE_EDITS)
    payload["ParentEpilogueLossRules"] = copy.deepcopy(minagho_chivarro_continuation.PARENT_EPILOGUE_LOSS_RULES)
    arsinoe_trickster.integrate(payload)
    if "irabeth" in payload["Relationships"]:
        payload["Scenes"].extend(copy.deepcopy(irabeth_trickster.SCENES))
        irabeth_trickster.integrate(payload)
    if "anevia" in payload["Relationships"]:
        payload["Scenes"].extend(copy.deepcopy(anevia_trickster.SCENES))
        anevia_trickster.integrate(payload)
    if "jerribeth" in payload["Relationships"]:
        payload["Scenes"].extend(copy.deepcopy(jerribeth_trickster.SCENES))
        jerribeth_trickster.integrate(payload)
    if "konomi" in payload["Relationships"]:
        payload["Scenes"].extend(copy.deepcopy(konomi_trickster.SCENES))
        konomi_trickster.integrate(payload)
    if "nocticula" in payload["Relationships"] and "nocticula.acquisition" in payload["Relationships"]:
        payload["Scenes"].extend(copy.deepcopy(nocticula_trickster.SCENES))
        nocticula_trickster.integrate(payload)
    if "vellexia" in payload["Relationships"]:
        payload["Scenes"].extend(copy.deepcopy(vellexia_trickster.SCENES))
        vellexia_trickster.integrate(payload)
    if "nurah" in payload["Relationships"]:
        payload["Scenes"].extend(copy.deepcopy(nurah_trickster.SCENES))
        nurah_trickster.integrate(payload)
    if "kiana" in payload["Relationships"]:
        payload["Scenes"].extend(copy.deepcopy(kiana_trickster.SCENES))
        kiana_trickster.integrate(payload)
    if "minagho_chivarro" in payload["Relationships"]:
        payload["Scenes"].extend(copy.deepcopy(minagho_chivarro_trickster.SCENES))
        minagho_chivarro_trickster.integrate(payload)
    if "soana" in payload["Relationships"]:
        payload["Scenes"].extend(copy.deepcopy(soana_trickster.SCENES))
        soana_trickster.integrate(payload)
    if "aranka" in payload["Relationships"]:
        payload["Scenes"].extend(copy.deepcopy(aranka_trickster.SCENES))
        aranka_trickster.integrate(payload)
    if "gesmerha" in payload["Relationships"]:
        payload["Scenes"].extend(copy.deepcopy(gesmerha_trickster.SCENES))
        gesmerha_trickster.integrate(payload)
    if "seelah" in payload["Relationships"]:
        payload["Scenes"].extend(copy.deepcopy(seelah_trickster.SCENES))
        seelah_trickster.integrate(payload)
    # Dorgelinda Stranglehold: a new relationship, opened only by the Trickster audit (dorgelinda_trickster).
    payload["Relationships"]["dorgelinda"] = copy.deepcopy(dorgelinda_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(dorgelinda_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(dorgelinda_ledger.SCENES))
    dorgelinda_trickster.integrate(payload)
    dorgelinda_ledger.integrate(payload)
    # Hepzamirah: a new relationship, opened only by the Trickster steal in her father's prison (hepzamirah_trickster).
    payload["Relationships"]["hepzamirah"] = copy.deepcopy(hepzamirah_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(hepzamirah_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(hepzamirah_flesh.SCENES))
    hepzamirah_trickster.integrate(payload)
    if "targona" in payload["Relationships"]:
        payload["Scenes"].extend(copy.deepcopy(targona_trickster.SCENES))
        targona_trickster.integrate(payload)
    # Camellia: a new native adapter, opened only by the Trickster's spoken death (camellia_trickster); the life around it is
    # camellia_masks. Registered after the routes whose Camellia reactions it lifts (G6(b)).
    payload["Relationships"]["camellia"] = copy.deepcopy(camellia_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(camellia_trickster.SCENES))
    camellia_trickster.integrate(payload)
    # Eritrice: a new relationship, opened only by the Trickster motion in her private audience (eritrice_trickster).
    payload["Relationships"]["eritrice"] = copy.deepcopy(eritrice_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(eritrice_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(eritrice_minutes.SCENES))
    payload["Scenes"].extend(copy.deepcopy(eritrice_council.SCENES))
    eritrice_trickster.integrate(payload)
    eritrice_minutes.integrate(payload)
    eritrice_council.integrate(payload)
    # Areelu has no registered route of her own: the Trickster wager (areelu-vorlesh.md) is the whole relationship.
    payload["Relationships"]["areelu"] = copy.deepcopy(areelu_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(areelu_trickster.SCENES))
    areelu_trickster.integrate(payload)
    # Chadali: a new relationship, opened only by the Trickster coin in her private audience (chadali_trickster).
    payload["Relationships"]["chadali"] = copy.deepcopy(chadali_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(chadali_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(chadali_wagers.SCENES))
    payload["Scenes"].extend(copy.deepcopy(chadali_fortunes.SCENES))
    payload["Scenes"].extend(copy.deepcopy(chadali_sessions.SCENES))
    payload["Scenes"].extend(copy.deepcopy(chadali_hours.SCENES))
    chadali_trickster.integrate(payload)
    chadali_wagers.integrate(payload)
    chadali_fortunes.integrate(payload)
    chadali_sessions.integrate(payload)
    chadali_hours.integrate(payload)
    # Arueshalae: a new native adapter (arueshalae.md); it reads ArueshalaeRomance and never starts or completes it.
    payload["Relationships"]["arueshalae"] = copy.deepcopy(arueshalae_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(arueshalae_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(arueshalae_treatment.SCENES))
    payload["Scenes"].extend(copy.deepcopy(arueshalae_rounds.SCENES))
    payload["Scenes"].extend(copy.deepcopy(arueshalae_chapel.SCENES))
    payload["Scenes"].extend(copy.deepcopy(arueshalae_hours.SCENES))
    payload["Scenes"].extend(copy.deepcopy(arueshalae_notes.SCENES))
    arueshalae_trickster.integrate(payload)
    arueshalae_treatment.integrate(payload)
    arueshalae_rounds.integrate(payload)
    arueshalae_chapel.integrate(payload)
    arueshalae_hours.integrate(payload)
    arueshalae_notes.integrate(payload)
    # Devarra: the draft (retired to reference/retired-drafts) is replaced by the Trickster "Clutch-mother" route
    # (devarra.md round 2) and its watchtower courtship on the Storyteller's hub (devarra_tower).
    payload["Relationships"]["devarra"] = copy.deepcopy(devarra_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(devarra_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(devarra_tower.SCENES))
    devarra_trickster.integrate(payload)
    devarra_tower.integrate(payload)
    # Delamere: a new relationship, opened only by the Trickster's stag call at her sarcophagus (delamere_trickster, 11 §2);
    # the courtship is delamere_woods and delamere_fire. Nothing is spawned for her (her native units share the undead prefab).
    payload["Relationships"]["delamere"] = copy.deepcopy(delamere_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(delamere_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(delamere_woods.SCENES))
    payload["Scenes"].extend(copy.deepcopy(delamere_fire.SCENES))
    delamere_trickster.integrate(payload)
    # Kaylessa: a new relationship (kaylessa.md; 11-ROSTER-PLAN-2 §2): Shyka's timeline trade in the dead worlds, the amulet
    # swap in the living one, and the courtship under the tailor's awning (kaylessa_wasps, kaylessa_clearing).
    payload["Relationships"]["kaylessa"] = copy.deepcopy(kaylessa_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(kaylessa_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(kaylessa_wasps.SCENES))
    payload["Scenes"].extend(copy.deepcopy(kaylessa_clearing.SCENES))
    kaylessa_trickster.integrate(payload)
    # Mielarah: the unregistered draft (retired to reference/retired-drafts) is replaced by the Trickster route "Zyphus
    # picks the nearest" (11 §2) and its Chapter 5 courtship on her presence in Drezen (mielarah_deck).
    payload["Relationships"]["mielarah"] = copy.deepcopy(mielarah_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(mielarah_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(mielarah_deck.SCENES))
    mielarah_trickster.integrate(payload)
    # Nidalynn: a new relationship (trickster/nidalynn.md; 11-ROSTER-PLAN-2 §2): the smallest of Devarra's eggs hidden from
    # the golems' count under soot (or from the vault clerk's), a silver dragon in a widow's dress, the kiln and the salt
    # (nidalynn_kiln, nidalynn_salt). Her door never depends on the Gold Dragon path.
    payload["Relationships"]["nidalynn"] = copy.deepcopy(nidalynn_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(nidalynn_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(nidalynn_kiln.SCENES))
    payload["Scenes"].extend(copy.deepcopy(nidalynn_salt.SCENES))
    nidalynn_trickster.integrate(payload)
    # Shamira: a new relationship (shamira.md hooks; 11-ROSTER-PLAN-2 §2 "Dreams for a body", revised 2026-09-29): at the
    # compulsory kill she flees into the one mind she was let into, the Commander's; a shell stolen in the Fleshmarkets, woken
    # on the Commander's dreams (shamira_mind); the game lost on purpose in her Harem (shamira_dream). Nothing is spawned for
    # her (no Shamira unit has a dialog), and nothing touches Areelu's flask, which is Last Call's.
    payload["Relationships"]["shamira"] = copy.deepcopy(shamira_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(shamira_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(shamira_mind.SCENES))
    payload["Scenes"].extend(copy.deepcopy(shamira_dream.SCENES))
    shamira_trickster.integrate(payload)
    shamira_mind.integrate(payload)
    shamira_dream.integrate(payload)
    # Jannah: a new relationship (jannah.md; 11-ROSTER-PLAN-2 §2): the Aldori forms at the Molten Scar cage in the killed
    # worlds, blood and tale in her cell in the living ones; the courtship at her cell (jannah_circle) and her challenge.
    payload["Relationships"]["jannah"] = copy.deepcopy(jannah_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(jannah_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(jannah_circle.SCENES))
    jannah_trickster.integrate(payload)
    # Nenio: a new relationship (nenio.md; 11-ROSTER-PLAN-2 §2 and its build sheet): the riddle in the Enigma, a name for a
    # name; the Sphinx's servant and the field report in the loss worlds; the dictation (nenio_folios) and her own test.
    payload["Relationships"]["nenio"] = copy.deepcopy(nenio_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(nenio_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(nenio_folios.SCENES))
    nenio_trickster.integrate(payload)
    # Herrax: a new relationship (herrax.md; 11-ROSTER-PLAN-2 §2, R3 build sheet): the coup on her schedule, sold to
    # Rokhorn on his own list; the night in her hall; her proposal at closing; the courtship in her house (herrax_house).
    payload["Relationships"]["herrax"] = copy.deepcopy(herrax_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(herrax_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(herrax_house.SCENES))
    herrax_trickster.integrate(payload)
    # Terendelev: a new relationship (trickster/terendelev.md; 11-ROSTER-PLAN-2 §2, R3 build sheet): restitution in the
    # Wound's blood at her burning bones at Iz (inline on Galfrey's or Irabeth's post-battle list), a late page, and the
    # courtship on her presence in Drezen (terendelev_watch). Distinct from the unregistered terendelev_continuation draft.
    payload["Relationships"]["terendelev"] = copy.deepcopy(terendelev_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(terendelev_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(terendelev_watch.SCENES))
    terendelev_trickster.integrate(payload)
    terendelev_watch.integrate(payload)
    # Eliandra: a new relationship (trickster/eliandra.md; 11-ROSTER-PLAN-2 §2, R4 build sheet): a sacrifice in her place,
    # made in her last rite at the star-heart of Pulura's Fall (inline on her Ch5 hub), her own offering, the first mile,
    # the shrine's last night, and the courtship on her presence in Drezen (eliandra_stars). Replaces the unregistered draft
    # eliandra_trickster_opening (never merged).
    payload["Relationships"]["eliandra"] = copy.deepcopy(eliandra_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(eliandra_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(eliandra_stars.SCENES))
    eliandra_trickster.integrate(payload)
    eliandra_stars.integrate(payload)
    # Galfrey: a new relationship (trickster/galfrey.md; 11-ROSTER-PLAN-2 §2, R4 build sheet): "The Queen dies; Kitrane walks
    # out", an offer she takes or refuses at her deathbed at Iz (inline on GalfreyOnTheEdge), and the courtship on her presence
    # in Drezen as a knight of the Green Crows (galfrey_kitrane). Where she lives, her native romance comes first: nothing here
    # starts or completes it. The unregistered galfrey_all_path_continuation draft stays unregistered.
    payload["Relationships"]["galfrey"] = copy.deepcopy(galfrey_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(galfrey_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(galfrey_kitrane.SCENES))
    galfrey_trickster.integrate(payload)
    galfrey_kitrane.integrate(payload)
    # Horzalah: a new relationship (trickster/horzalah.md; 11-ROSTER-PLAN-2 §2, R4 build sheet): the ear in the gift box, a
    # con on her own Guild offered at the mercy node (or in the Greybor-less night, or when the Guild circles); the collar
    # on her terms; the courtship on her presence by the Storyteller and her letters by knife (horzalah_guild).
    payload["Relationships"]["horzalah"] = copy.deepcopy(horzalah_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(horzalah_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(horzalah_guild.SCENES))
    horzalah_trickster.integrate(payload)
    # Elyanka Camilary: a new relationship (trickster/elyanka-camilary.md; 11-ROSTER-PLAN-2 §2, R5 build sheet): the only door
    # is the funeral Drezen held for the Commander; the Commander receives the Whispering Way's envoy veiled, as their own
    # executor, and sells her the corpse in advance; an exchange of claims; the courtship beats around the dead-house
    # (elyanka_hearse). Every scene is a rest-delivered visit: no presence, no entry on any native list but her reactors'.
    payload["Relationships"]["elyanka"] = copy.deepcopy(elyanka_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(elyanka_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(elyanka_hearse.SCENES))
    elyanka_trickster.integrate(payload)
    # Iomedae: a new relationship (trickster/iomedae.md, Build sheet R6; 11-ROSTER-PLAN-2 §2): veiled until the finale. The
    # courtship is her banner's memory and her herald (iomedae_banner), then her own voice after the Summit; the commit is a
    # formal disputation under her banner; the device is the banner carried into the Wound, which she may choose to answer.
    payload["Relationships"]["iomedae"] = copy.deepcopy(iomedae_trickster.RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(iomedae_trickster.SCENES))
    payload["Scenes"].extend(copy.deepcopy(iomedae_banner.SCENES))
    iomedae_trickster.integrate(payload)
    # Last Call (doc 04) and the Trickster's Ledger: after every route, so its pages and call-ins read the routes' flags.
    lastcall.integrate(payload)
    iomedae_trickster.integrate_joint(payload)     # ledger row 6: the Appointment empties the flask (after Last Call's pages)
    trickster_engine(payload)
    trickster_world.integrate(payload)
    # The household (08): the Table, stance hooks and the Ledger's household sections. After Last Call (its Ledger book)
    # and after the Trickster engine and world, whose late-commitment keys feed <rel>.harem.eligible.
    household.integrate(payload)
    # E15: the RRT book UI (glossary tooltips, the guide book).
    rrt_ui.integrate(payload)
    rrt_portraits.integrate(payload)
    # E15c: what each rest-delivered scene is (letter, visit, sending, memory, event), after every route and Last Call.
    scene_kinds.integrate(payload)
    normalize_trickster_access(payload)
    return payload


# Verified in blueprints.zip (2026-09-27): every GUID below is a BlueprintEtude.
TRICKSTER_ETUDES = {
    # World/Etudes/Common/WrathOfTheRighteous/MythicTrickster/TricksterStates/PlayerWasTrickster
    "trickster.was": "c820b3788f967e14f8bde3c17447157f",
    # World/Etudes/Common/WrathOfTheRighteous/Chapter06_Extra/Ending_Trickster ("Nirvana" finale)
    "ending.trickster": "db5375333382d044089475d256f19582",
    # .../Chapter06_Extra/Ending_Trickster_AllPlanes and _AllPlanesAndFW (started by Ending_TricksterFull)
    "ending.trickster_allplanes": "f7343e290a8d4ed887af8f04d1b3446b",
    "ending.trickster_allplanes_fw": "5f63f6d43c9b465f822db70af7d69b92",
    # .../Chapter06_Extra/Ending_TricksterFull
    "ending.trickster_full": "6ff418aeda24e6e48be844e6258e3c5a",
}


def normalize_trickster_access(payload):
    """E7: RELATIONSHIP["TricksterAccess"] = {state: {"detect": [...], "device": id, "returned": flag}} is authored in
    lower case; Story.json carries it as Detect/Device/Returned metadata for rrt_verify (the runtime ignores it)."""
    for rel in payload["Relationships"].values():
        access = rel.get("TricksterAccess")
        if access is None:
            continue
        rel["TricksterAccess"] = {state: {"Detect": list(entry.get("detect", entry.get("Detect", []))),
                                          "Device": entry.get("device", entry.get("Device")),
                                          "Returned": entry.get("returned", entry.get("Returned"))}
                                  for state, entry in access.items()}


def trickster_engine(payload):
    """Engine-level Trickster state shared by every device spec (02-TRICKSTER-ENGINE-API.md)."""
    for key, guid in TRICKSTER_ETUDES.items():
        if payload["Etudes"].get(key, guid) != guid:
            raise ValueError(f"Conflicting Trickster binding: {key}")
        payload["Etudes"][key] = guid
    # A started-then-completed state still counts as observed history.
    payload["PermanentEtudes"] = sorted(set(payload.get("PermanentEtudes", [])) | set(TRICKSTER_ETUDES))
    # TT-02: Chapter 4 can complete PlayerIsTrickster; the latch keeps device payoffs alive afterwards.
    payload.setdefault("Latches", {})["trickster.ever"] = ["trickster", "trickster.was"]
    # TT-22: the Trickster "punchline" finale sets Ending_PlayerSacrifice (sacrifice), yet the native rewrite page
    # says this Commander "found a way of cheating death". Epilogues may lift their sacrifice forbid with it.
    payload.setdefault("Derived", {})["trickster.cheated_death"] = [
        ["sacrifice", "trickster.ever", ending] for ending in
        ("ending.trickster", "ending.trickster_allplanes", "ending.trickster_allplanes_fw", "ending.trickster_full")]


if __name__ == "__main__":
    output = ROOT / "development/Story.json"
    output.parent.mkdir(exist_ok=True)
    payload = make_expansion()
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"INCOMPLETE DEVELOPMENT EXPORT: {len(payload['Scenes'])} scenes -> {output}")
