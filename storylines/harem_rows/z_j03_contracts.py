"""Approved J03 rulings 01, 02, 04, 17–20; append-only contract integration.

All patrol/collector/concession staging and the retained confession are authored
additions, not native events or inventory blueprints. Native evidence and exact
costs are recorded in tools/route_packs/plans/j03-contracts.md. Edge prose belongs
to the voice owner; pending() labels only new beats, never edits locked text.
Runs after the individual row registrars and before J02 terminal publication.
"""
from copy import deepcopy

from story_format import c, n, scene
from storylines import foresight, household, contract_j01
from storylines.harem_rows import s04, s05, s08, s23, s35
from storylines import hepzamirah_trickster as hep
from storylines import horzalah_trickster as horzalah


def pending(node, woman, beat, *choices):
    return n(node, woman.capitalize(),
             "[PROSE PENDING: " + woman + " - " + beat + "]", *choices)


def flags(prefix, *names):
    return tuple(prefix + name for name in names)


def table(sid, title, nodes, requires=(), forbids=(), participants=(), women=(),
          contacts=None, witness=None, delay=0, overrides=None):
    return scene(sid, title, nodes[0]["Speaker"], 5, '[' + title + ']', nodes,
        requires=("trickster", "trickster.now", household.PAGE_TAKEN,
                  household.STANCE_ELIGIBLE, household.KEPT, *requires),
        forbids=(household.KING_GONE, "trickster.failed", "engine.l12.commander_unreturned",
                 *forbids), delay=delay, last=5, Relationship="household", Chapters=[5],
        Areas=[household.DREZEN], InteractionHub=household.TABLE_HUB,
        Participants=list(participants), ParticipantWomen=list(women),
        ParticipantContacts=contacts or {}, ForbidOverrides=overrides or {},
        RestAllowance="household.protected", HouseholdCategory="protected",
        HouseholdWitness=witness or sid + ".seen")


def append(payload, body):
    if not any(s["Id"] == body["Id"] for s in payload["Scenes"]):
        payload["Scenes"].append(body)
    foresight.CONSUMERS[body["Id"]] = household.PAGE_TAKEN
    payload.setdefault("ForesightConsumers", {})[body["Id"]] = household.PAGE_TAKEN


def respect(payload, key, prefix, *witnesses):
    payload.setdefault("Derived", {})[key] = [list(flags(prefix, "resolved", *witnesses))]


def faith(payload):
    p = s04.P
    body = next(s for s in payload["Scenes"] if s["Id"] == p + "settle")
    if any(node["Id"] == "confession_record" for node in body["Nodes"]):
        return
    root = body["Nodes"][0]["Choices"]
    root[0]["Requires"] = []
    root[0]["Next"] = None
    root[0]["Check"] = dict(Skill="SkillLoreReligion", DC=30, CommanderOnly=True,
                            Success="reasoned", Failure="missed")
    root[1]["Requires"] = list(flags(p, "confession_kept", "seelah_confession_heard"))
    root[1]["Next"] = "evidence"
    root[2]["Requires"].remove(s04.BLOCKERS[2])
    # No source-independent evidence: this records what the Commander actually
    # heard, then discloses it to the already-current Seelah on page.
    root.append(c('[Retain Camellia\'s confession and tell Seelah.]', "confession_record",
                  requires=("camellia.mireya_unmasked",),
                  forbids=(p + "confession_kept",)))
    root.append(c('[Unfinished argument.]', "awaiting", forbids=("trickster.now",)))
    deeds = flags(p, "settle.seen", "resolved", "seelah_blessing_withheld",
                  "camellia_cover_limited", "cost.seelah_company_kept", "cost.camellia_public_cover")
    body["Nodes"].extend([
        n("confession_record", "Seelah",
          '{n}You write down Camellia\'s admission that Mireya never existed and put it beside the crusader\'s shield. Seelah reads it twice.{/n}\n'
          '"So that was a lie, too. Leave this with me. I won\'t call murder holy because we need another blade on the walls."',
          c('[Keep the admission with Seelah\'s account.]', "evidence",
            flags=flags(p, "confession_kept", "seelah_confession_heard"))),
        pending("reasoned", "camellia", "want useful public cover / accept an unblessed place beside Seelah while Seelah completes the dead crusader's prayer / lose religious cover, Seelah keeps dangerous company",
                c('Continue', flags=deeds + flags(p, "method.religion"))),
        pending("evidence", "camellia", "want her admission contained / face the actual retained confession and Seelah's refusal to bless murder / public cover lost, Seelah retains useful dangerous company",
                c('Continue', flags=deeds + flags(p, "method.confession"))),
        n("missed", "Seelah", '"That doesn\'t make it a blessing I can give. Bring me something better than an argument."\n'
          '{n}She sets the unlit candle beside the shield. Beyond the tavern door, the sentries change.{/n}',
          c('Continue', flags=flags(p, "settle.seen", "settle.failed"))),
    ])
    for key in s04.BLOCKERS:
        payload["PendingHooks"].remove(key)
    retry = deepcopy(body)
    retry["Id"] = p + "retry"
    retry["DelayHours"] = 48
    retry["Requires"].append(p + "settle.failed")
    retry["Forbids"] = [f for f in retry["Forbids"] if f != p + "settle.seen"]
    retry["Forbids"].extend(flags(p, "retry.seen", "resolved", "permanent_refusal"))
    retry["HouseholdWitness"] = p + "retry.seen"
    # The retry repeats only retained evidence or the same existing Word.
    # Keep all copied IDs/destinations; retire unavailable approaches by gating.
    retry["Nodes"][0]["Choices"][0]["Forbids"].append("trickster.now")
    retry["Nodes"][0]["Choices"][5]["Forbids"].append("trickster.now")
    for node in retry["Nodes"]:
        if node["Id"] in ("start", "word", "refused"):
            node["Text"] = "[PROSE PENDING: camellia - want public cover / repeat the limited prayer dispute with Seelah / keep the blessing withheld and dangerous company explicit]"
        for choice in node["Choices"]:
            choice["Set"] = [p + "retry.seen" if f == p + "settle.seen" else f for f in choice["Set"]]
    body["Forbids"].extend(flags(p, "resolved", "permanent_refusal"))
    append(payload, retry)
    for a, b, deed, cost in (
        ("seelah", "camellia", "camellia_cover_limited", "cost.camellia_public_cover"),
        ("camellia", "seelah", "seelah_blessing_withheld", "cost.seelah_company_kept")):
        respect(payload, a + ".harem.attitude." + b + ".respect", p, deed, cost)


def power(payload):
    p = s08.PREFIX
    for body in s08.draft_scenes():
        retry = ".retry." in body["Id"]
        step = "retry" if retry else "settle"
        root = body["Nodes"][0]["Choices"]
        favour = root[0 if retry else 1]
        # A favour owed TO the queen never becomes credit against her.
        favour["Forbids"].append("trickster.now")
        check = dict(Skill="CheckDiplomacy", DC=37, CommanderOnly=True,
                     Success="held", Failure="failed")
        if retry:
            root.append(c('[Diplomacy: present the same renunciation.]', check=check))
            body["Nodes"].append(pending("failed", "nocticula",
                "want rank acknowledged / reject the repeated renunciation / public claim remains disputed",
                c('Continue', flags=flags(p, "retry.seen", "permanent_refusal", "unsettled"))))
        else:
            root[0]["Check"] = check
        for node in body["Nodes"]:
            if node["Id"] in ("held", "failed") or body["Id"].endswith("corrupted"):
                if not node["Text"].startswith("[PROSE PENDING:"):
                    woman = "nocticula" if node["Id"] in ("held", "failed") else "arueshalae"
                    beat = {
                        "start": "want her own name / publicly dictate renunciation over the crusade map / defy her former mistress",
                        "held": "want rank without conceding the throne / answer through the acquired seal, acknowledge Arueshalae's name / limit this claim, no summons",
                        "answer": "want freedom from ownership / answer the queen in her own name and sign / public defiance",
                        "failed": "want obedience / return a sealed rejection / ownership claim remains disputed",
                        "refused": "want the crusade or her own appetite / withhold the renunciation / leave the claim disputed",
                    }[node["Id"]]
                    node["Text"] = "[PROSE PENDING: " + woman + " - " + beat + "]"
        body["ParticipantContacts"] = {"nocticula": contract_j01.authenticated_reply(
            ["noct.acq.renewed_agreement", "noct.acq.seal_received", "noct.acq.an_answer_of_her_own_done"],
            ["noct.closed", "noct.acq.closed", "noct.acq.council_fight"])}
        # Pair is an engine declaration of two bodily participant routes. The
        # queen is an independently checked correspondent, not a second body.
        body.pop("Pair", None)
        body["Forbids"].append("engine.l12.commander_unreturned")
        append(payload, body)
    for (a, b, stage), witnesses in s08.LADDER.items():
        payload.setdefault("Derived", {})[a + ".harem.attitude." + b + "." + stage] = [witnesses]


def flesh_guards(woman):
    required = [woman + ".present_now"]
    forbidden = [woman + ".epoch_unavailable", woman + ".returned_actor_lost"]
    if woman == "hepzamirah":
        required.append(hep.RET)
        forbidden.extend([hep.CLOSED, hep.CONFINED, hep.PRESENCE_FAILED])
    elif woman in ("minagho", "chivarro"):
        required.append("participant." + woman + ".available")
        forbidden.extend(["minachiv.closed", "minagho_chivarro.trickster." + (
            "declined_minagho" if woman == "minagho" else "chivarro_declined")])
        if woman == "chivarro":
            forbidden.append("minagho_chivarro.trickster.chivarro_sent_back")
    else:
        forbidden.extend([woman + ".closed", horzalah.DEAD, horzalah.LEFT_FREE, horzalah.PRESENCE_FAILED])
    return required, forbidden


def deed_contract(payload, p, primary, title, women, accepts, deeds, costs,
                  failure_names, counter_moves, root_choices=None, check=None):
    """One guarded primary and one retry; both acts precede the shared terminal.

    The choices expose the approved handling/counter-move failures. Neutral
    mishandling is pending on the first attempt and never names a random woman.
    """
    requires, forbids = [], []
    for woman in women:
        req, no = flesh_guards(woman)
        requires.extend(req)
        forbids.extend(no)
    participants = ["minagho_chivarro" if w in ("minagho", "chivarro") else w for w in women]
    overrides = {hep.CONFINED: hep.RELEASED} if "hepzamirah" in women else {}
    for step in (primary, "retry"):
        success = flags(p, step + ".seen", "resolved", *deeds, *costs)
        final = flags(p, step + ".seen", "permanent_refusal", "unsettled")
        failed = flags(p, step + ".seen", "unsettled") if step == "retry" else flags(p, step + ".seen", primary + ".failed")
        nodes = [pending("start", women[0], accepts[0],
                         c('[Carry their terms.]', "second"), c('[Leave it unsettled.]', "refused"),
                         c('[Later.]', abort=True)),
                 pending("second", women[1], accepts[1],
                         c('[Carry out the agreed task.]', "held"),
                         c('[Mishandle the relay.]', "missed")),
                 pending("held", women[1], accepts[2], c('Continue', flags=success)),
                 pending("missed", women[0], "want the task done / reject the botched relay / neither promised deed is completed",
                         c('Continue', flags=failed)),
                 pending("refused", women[0], "want her own advantage / leave the limited bargain unsigned / dispute remains",
                         c('Continue', flags=final))]
        for woman, failure, counter_move in zip(women, failure_names, counter_moves):
            node_id = "broken_" + woman
            nodes[1]["Choices"].append(c('[Let ' + woman.capitalize() + ' break her own term.]', node_id))
            terminal = (final + flags(p, failure)) if step == "retry" else (
                flags(p, step + ".seen", primary + ".failed", "attempt." + failure))
            nodes.append(pending(node_id, woman, counter_move,
                                 c('Continue', flags=terminal)))
        if root_choices is not None and step == primary:
            nodes[0]["Choices"] = deepcopy(root_choices)
        if check:
            # The screen is Minagho's exposed move. Both successful approaches
            # still require her act and Hepzamirah's strike/yielded credit.
            if step == primary:
                nodes[0]["Choices"][1]["Check"] = dict(check, Success="second", Failure="screen_failed")
                nodes[0]["Choices"][1]["Next"] = None
            nodes.append(pending("screen_failed", "minagho",
                "want the collector screened / lose face when the approach sees through the screen / no strike or yielded credit",
                c('Continue', flags=(final + flags(p, "minagho_final_failed")) if step == "retry" else
                  flags(p, step + ".seen", primary + ".failed", "attempt.minagho_final_failed"))))
        body = table(p + step, title, nodes,
            requires=(*requires, *((p + primary + ".failed",) if step == "retry" else ())),
            forbids=(*forbids, p + step + ".seen", p + "resolved", p + "permanent_refusal"),
            participants=participants, women=[w for w in women if w in ("minagho", "chivarro")],
            witness=p + step + ".seen",
            delay=48 if step == "retry" else 0, overrides=overrides)
        if "hepzamirah" in women:
            body["ParticipantContacts"]["hepzamirah"] = dict(Kind="body", Requires=[hep.RET],
                Forbids=[], Options=[dict(Units=[hep.BODY_UNIT], Requires=[], Forbids=[])])
            # Reuse the actual presence hunt window, including on continuation.
            # J01's live contact inventory excludes her absent copy during it.
        append(payload, body)


def sisters(payload):
    p = "household.pair.horzalah_hepzamirah."
    deed_contract(payload, p, "truce", "The patrol's warning", ("horzalah", "hepzamirah"), (
        "want Guild leverage / give the approaching crusade patrol one real warning instead of selling it / lose that sale",
        "want dominance / accept Horzalah's control of this warning and leave her agent unmolested / yield this interception and Guild claim",
        "want a useful patrol alive / warning reaches the patrol, agent departs unmolested, each sister acknowledges her kept term / lost sale and lost domination"),
        ("horzalah_terms_kept", "hepzamirah_terms_kept"),
        ("cost.horzalah_concession", "cost.hepzamirah_concession"),
        ("horzalah_term_broken", "hepzamirah_term_broken"), (
            "want the warning's sale price / sell this warning instead of delivering it to the patrol / break her own Guild-warning concession",
            "want mastery of the Guild warning / intercept Horzalah's agent and seize this warning / break her own noninterception concession"))
    respect(payload, "horzalah.harem.attitude.hepzamirah.respect", p,
            "hepzamirah_terms_kept", "cost.hepzamirah_concession")
    respect(payload, "hepzamirah.harem.attitude.horzalah.respect", p,
            "horzalah_terms_kept", "cost.horzalah_concession")


def collector(payload):
    p = "household.pair.hepzamirah_minagho."
    if any(s["Id"] == p + "job" for s in payload["Scenes"]):
        return
    roots = [c('[Use the existing Baphomet terms.]', "second", forbids=("trickster.now",)),
             c('[Misdirect the hostile approach.]'),
             c('[Carry out the common-enemy job.]', "exposure"),
             c('"Claim your own victories, then."', "refused"), c('[Later.]', abort=True)]
    deed_contract(payload, p, "job", "The collector at the approach", ("minagho", "hepzamirah"), (
        "want the current Baphomet collector off her trail / screen his threatening approach to the returned women / stake her own face on the screen",
        "want her own glory / strike this collector and accept Minagho's sole credit for the job / yield the credit",
        "want the collector dead / show Minagho's completed screen, Hepzamirah's strike and yielded credit / both named operational concessions"),
        ("job_held", "minagho_screened", "hepzamirah_struck"),
        ("cost.minagho_screen", "cost.hepzamirah_credit"),
        ("minagho_final_failed", "hepzamirah_final_failed"), (
            "want the screen credited to her / fail to screen the collector's approach and lose face / leave Hepzamirah without the promised opening",
            "want sole glory for herself / explicitly refuse the promised strike with yielded credit / leave Minagho's screen unanswered"), roots,
        dict(Skill="SkillThievery", DC=28, CommanderOnly=True))
    for body in payload["Scenes"]:
        if body["Id"] in (p + "job", p + "retry"):
            # Retry's old remedy index remains the direct common-enemy job;
            # append the same approved screen, never a Baphomet favour.
            if body["Id"].endswith("retry"):
                body["Nodes"][0]["Choices"][0]["Next"] = "exposure"
                body["Nodes"][0]["Choices"].append(c('[Misdirect the same hostile approach.]', check=dict(
                    Skill="SkillThievery", DC=28, CommanderOnly=True, Success="second", Failure="screen_failed")))
            body["Nodes"].append(n("exposure", "Narrator",
                '{n}You take the exposed approach yourself, drawing the collector\'s attention while Minagho screens the women\'s way to him.{/n}',
                c('[Hold his attention for Hepzamirah\'s strike.]', "second")))
            # Publish exposure cost only with the completed two-woman deed.
            direct = next(node for node in body["Nodes"] if node["Id"] == "exposure")
            direct["Choices"][0]["Set"] = [p + "cost.commander_exposure"]
    respect(payload, "hepzamirah.harem.attitude.w.minagho.respect", p,
            "minagho_screened", "cost.minagho_screen")
    respect(payload, "minagho_chivarro.harem.attitude.minagho.hepzamirah.respect", p,
            "hepzamirah_struck", "cost.hepzamirah_credit")


def precedence(payload):
    p = s05.P
    body = next(s for s in payload["Scenes"] if s["Id"] == p + "precedence")
    if any(s["Id"] == p + "precedence.live" for s in payload["Scenes"]):
        return
    req = ("nocticula.reachable_by_letter", "noct.acq.renewed_agreement", "noct.acq.seal_received",
           "noct.acq.an_answer_of_her_own_done", "shamira.reachable_by_letter")
    no = ("noct.closed", "noct.acq.closed", "noct.acq.council_fight", "nocticula.epoch_unavailable",
          "shamira.closed", "shamira.epoch_unavailable", "shamira.trickster.cost.kept_captive",
          "shamira.trickster.cast_out", "shamira.trickster.declined")
    # A separately guarded wrapper shares the old exhaustion/allowance. This
    # keeps the original no-reply account accessible after either channel loss,
    # while live continuation rechecks both channels before showing any speech.
    live = table(p + "precedence.live", "Two claims beside the throne", [
        n("start", "Narrator", '{n}Beside the reports from the Worldwound lie two sheets, each bearing its own seal.{/n}',
          c('[Carry each title exactly as she gives it.]', "queen_reply"),
          c('[Keep only the old account.]', "history"), c('[Later.]', abort=True)),
        deepcopy(body["Nodes"][1]),
        pending("queen_reply", "nocticula", "want court precedence / separately answer through her acquired seal and assert her priority / tolerate her lover's public counterclaim",
                c('Continue', "shamira_reply")),
        pending("shamira_reply", "shamira", "want her own court rank / freely send her distinct correspondence claiming precedence beside Nocticula / acknowledge the queen's bounded counterclaim",
                c('Continue', flags=flags(p, "precedence.seen", "resolved", "nocticula_claim_answered",
                  "shamira_title_answered", "cost.nocticula_counterclaim_public", "cost.shamira_rank_bounded"))),
    ], requires=(s05.LOVERS_SEEN, *req), forbids=(p + "precedence.seen", *no),
       contacts={"nocticula": contract_j01.authenticated_reply(req[:4], no[:4]),
                 "shamira": dict(Kind="letter", Requires=["shamira.reachable_by_letter"],
                                  Forbids=list(no[4:]), Options=[])}, witness=p + "precedence.seen")
    append(payload, live)
    # Unsupported coup/recovery and body slots stay inert; no exposure alias.


def turf(payload):
    p = s23.PREFIX
    body = next(s for s in payload["Scenes"] if s["Id"] == p + "turf")
    if any(s["Id"] == p + "turf.live" for s in payload["Scenes"]):
        return
    req = ("herrax.reachable_by_letter", "household.pair.herrax_minagho.herrax_channel")
    no = ("herrax.closed", "herrax.epoch_unavailable", "herrax.returned_actor_lost")
    # Preserve the original account and all its saved references. Its older
    # present-tense Herrax mention receives a cross-route life guard from the
    # classifier. A historical wrapper supplies no Herrax speech/action and
    # shares the original exhaustion; no blanket life override is needed.
    history = deepcopy(body)
    history["Id"] = p + "turf.history"
    history["Entry"] = '[Recall the earlier kill request.]'
    history["Forbids"] = [f for f in history["Forbids"] if f != "crossroute.herrax.unavailable"]
    history["Nodes"] = [
        pending("start", "chivarro", "want her current own-house trade / recall the actually heard earlier kill request / hostility remains, no respondent reply",
                c('[Keep the earlier account.]', "historical"), c('[Later.]', abort=True)),
        pending("historical", "chivarro", "want the old threat remembered / retain her own account of the earlier request / no new concession or reply",
                c('Continue', flags=flags(p, "turf.seen", "historical"))),
    ]
    append(payload, history)
    # The live wrapper and
    # retry guard the respondent at entry and every continuation, share turf.seen
    # and consume no new preparation, letter emission or incident allocation.
    body = deepcopy(body)
    body["Id"] = p + "turf.live"
    body["Requires"].extend(req)
    body["Forbids"].extend(no)
    body.setdefault("ParticipantContacts", {})["herrax"] = dict(Kind="letter", Requires=list(req), Forbids=list(no), Options=[])
    for node in body["Nodes"]:
        node["Text"] = "[PROSE PENDING: chivarro - want her current own-house business / name Herrax's actual disputed offer / old chair remains Herrax's, no reinstatement]"
    body["Nodes"][0]["Choices"].extend([
        c('[Carry their separate claims.]', "herrax_reply", requires=req, forbids=no),
        c('[Leave the offer unsettled.]', "unsettled"),
    ])
    deeds = ("resolved", "herrax_turf_terms_kept", "chivarro_house_terms_kept",
             "cost.herrax_turf_concession", "cost.chivarro_claim_concession")
    body["Nodes"].extend([
        pending("herrax_reply", "herrax", "want the Delights / send her own current message keeping the Delights, decline to recruit Chivarro's present contacts through this offer / withhold this recruiting claim",
                c('[Carry Herrax\'s actual claim to Chivarro.]', "chivarro_reply", requires=req, forbids=no),
                c('[Leave the reply owed.]', abort=True)),
        pending("chivarro_reply", "chivarro", "want her present own-house trade / answer Herrax separately, give up the old chair through this offer / withhold this chair claim",
                c('[Deliver both named claims.]', "terms_kept", requires=req, forbids=no),
                c('[Mishandle the names.]', "names_missed"),
                c('[Leave the offer unsettled.]', "unsettled")),
        pending("terms_kept", "chivarro", "want her own business / inspect Herrax's delivered recruiting concession and send her own chair concession / both bounded claims withheld, no reinstatement",
                c('Continue', flags=flags(p, "turf.seen", *deeds), requires=req, forbids=no),
                c('[Leave the reply owed.]', abort=True)),
        pending("names_missed", "chivarro", "want her own named claim / reject the muddled messages / no concession delivered",
                c('Continue', flags=flags(p, "turf.seen", "turf.failed"))),
        pending("unsettled", "chivarro", "want her own house / keep the offer disputed / no terms kept",
                c('Continue', flags=flags(p, "turf.seen", "permanent_refusal", "unsettled"))),
    ])
    retry = deepcopy(body)
    retry["Id"] = p + "retry"
    retry["DelayHours"] = 48
    retry["Requires"].append(p + "turf.failed")
    retry["Forbids"] = [f for f in retry["Forbids"] if f != p + "turf.seen"]
    retry["Forbids"].extend(flags(p, "retry.seen", "resolved", "permanent_refusal"))
    retry["HouseholdWitness"] = p + "retry.seen"
    # A corrected retry may remain owed on missing reply; it is never blamed
    # on either woman. Only her explicit counter-move supplies a final owner.
    retry["Nodes"][0]["Choices"] = [
        c('[Deliver the corrected claims.]', "herrax_reply", requires=req, forbids=no),
        c('[Leave the offer unsettled.]', "unsettled"), c('[Later.]', abort=True),
        c('[Old account.]', "historical", forbids=("trickster.now",))]
    for woman, failure, beat in (
            ("herrax", "herrax_term_broken", "want Chivarro's present contacts / explicitly renew recruiting those contacts through this offer / break her own recruiting concession"),
            ("chivarro", "chivarro_term_broken", "want her old chair / explicitly renew claiming the Delights chair through this offer / break her own chair concession")):
        retry["Nodes"][0]["Choices"].append(c('[Let ' + woman.capitalize() + ' break her term.]', failure,
                                                    requires=req, forbids=no))
        retry["Nodes"].append(pending(failure, woman, beat,
            c('Continue', flags=flags(p, "retry.seen", "permanent_refusal", "unsettled", failure))))
    for node in retry["Nodes"]:
        for choice in node["Choices"]:
            choice["Set"] = [p + "retry.seen" if f == p + "turf.seen" else f for f in choice["Set"]]
            if p + "turf.failed" in choice["Set"]:
                choice["Set"] = list(flags(p, "retry.seen", "unsettled"))
    body["Forbids"].extend(flags(p, "resolved", "permanent_refusal"))
    append(payload, body)
    append(payload, retry)
    respect(payload, "herrax.harem.attitude.w.chivarro.respect", p,
            "chivarro_house_terms_kept", "cost.chivarro_claim_concession")
    respect(payload, "minagho_chivarro.harem.attitude.chivarro.herrax.respect", p,
            "herrax_turf_terms_kept", "cost.herrax_turf_concession")


def register(payload, scenes, refs):
    faith(payload)
    power(payload)
    sisters(payload)
    collector(payload)
    precedence(payload)
    turf(payload)
    for a, b, deed, cost in (
        ("arsinoe", "nurah", "nurah_author_named", "cost.nurah_forgery_exposed"),
        ("nurah", "arsinoe", "arsinoe_flaw_named", "cost.arsinoe_claim_limited")):
        respect(payload, a + ".harem.attitude." + b + ".respect", s35.PREFIX, deed, cost)
    for body in scenes:
        if any(body["Id"].startswith("household.pair." + pair + ".") for pair in (
                "seelah_camellia", "arueshalae_nocticula", "horzalah_hepzamirah",
                "nocticula_shamira", "herrax_chivarro", "hepzamirah_minagho", "arsinoe_nurah")):
            if "trickster.now" not in body["Requires"]:
                body["Requires"].append("trickster.now")
            if "engine.l12.commander_unreturned" not in body["Forbids"]:
                body["Forbids"].append("engine.l12.commander_unreturned")
