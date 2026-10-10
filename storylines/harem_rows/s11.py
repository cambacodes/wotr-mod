"""S11: authored challenged-mask acknowledgment and act-before-confession arc.

Group B supplies the base; Group D's later four-step optional contract governs
the extension. Native barks are voice evidence, never completion witnesses.
"""
from story_format import c, n, scene
from storylines import household

PREFIX = "household.pair.camellia_arueshalae."
PAIR = ("camellia", "arueshalae")
SCROLL = "89e10c3f21fa50c4b8719e004c7628d3"
SLOT = PREFIX + "choice.explicit.1"
# Ruling 03 shares witnessed work, never affection or S12 completion.
SHARED_CRAFT_WITNESS = "household.craft.method_witnessed"


def p(suffix):
    return PREFIX + suffix


def terminal(node, speaker, text, *flags):
    return n(node, speaker, text, c("[Continue.]", flags=tuple(p(f) for f in flags)))


def later():
    return c("[Later.]", abort=True)


def entry(step, title, nodes, requires=(), forbids=(), delay=0, optional=False):
    witness = p("settle.seen" if step.startswith("settle.") else
                "retry.seen" if step.startswith("retry.") else step + ".seen")
    negatives = ["fool_king.gone", "trickster.failed", "sacrifice",
                 "camellia.closed", "arueshalae.closed", "camellia.epoch_unavailable",
                 "arueshalae.epoch_unavailable", "camellia.returned_actor_lost",
                 "arueshalae.returned_actor_lost", "arueshalae_dead", "arueshalae.evil_dead",
                 "arueshalae.kicked_out", "arueshalae.kicked_out_evil", witness]
    overrides = {"sacrifice": "trickster.commander_back"}
    for a, b in (PAIR, PAIR[::-1]):
        key = household.enmity(a, b)
        negatives.append(key)
        overrides[key] = a + ".harem.reconciled." + b
    extra = dict(Relationship="household", InteractionHub=household.TABLE_HUB,
                 Areas=[household.DREZEN], Chapters=[5], Pair=list(PAIR),
                 Participants=list(PAIR), ParticipantWomen=[],
                 HouseholdCategory="pair" if optional else "protected",
                 RestAllowance="household.pair" if optional else "household.protected",
                 HouseholdWitness=witness, ForbidOverrides=overrides)
    if optional:
        extra.update(HouseholdArc=p("arc"), HouseholdArcStart=step == "company")
        negatives.append(p("arc.declined"))
    return scene(p(step), title, "Camellia", 5, "[" + title + "]", nodes,
                 requires=("trickster", household.PAGE_TAKEN, household.STANCE_ELIGIBLE,
                           household.KEPT, "camellia.harem.eligible", "arueshalae.harem.eligible",
                           "camellia.present_now", "arueshalae.present_now", p("body.camellia")) + tuple(requires),
                 forbids=tuple(negatives) + tuple(forbids), delay=delay, last=5, **extra)


BASE_DEEDS = ("deed.camellia_bait_named", "deed.arueshalae_answer_owned",
              "cost.camellia_harmless_cover_yielded", "cost.arueshalae_easy_answer_yielded",
              "cost.commander_cover_lost")
COMPANY = ("company.seen", "company.kept", "deed.a_company", "deed.b_company",
           "cost.a_company", "cost.b_company")
DESIRE = ("desire.seen", "desire.named", "deed.a_personal_answer", "deed.b_personal_answer",
          "cost.a_personal_answer", "cost.b_personal_answer")
FRIENDS = tuple(a + ".harem.attitude." + b + ".friend" for a, b in (PAIR, PAIR[::-1]))
RESPECT = tuple(a + ".harem.attitude." + b + ".respect" for a, b in (PAIR, PAIR[::-1]))


def settlement(branch, retry=False):
    evil = branch == "evil"
    step = ("retry." if retry else "settle.") + branch
    stamp = "retry" if retry else "settle"
    start = '''{n}Camellia has proposed an evening at the workbench, away from the troops preparing to march against the Worldwound. Arueshalae has left the chair beside her empty.{/n}
"Such a cold reception. I merely offered you a little company."'''
    answered = '''"Company? You made it sound delicious."
{n}Arueshalae smiles without disguising her interest in Camellia's throat.{/n}''' if evil else '''"You know what a touch can do. Why make it sound harmless?"
{n}Arueshalae pushes the empty chair back under the table.{/n}'''
    answer_c = '''"Because I dislike having my invitations mistaken for supper."
{n}Camellia's pleasant smile thins. She turns her chair to face Arueshalae.{/n}
"I know what you are. You need not pretend to be a charming guest. I shall stop pretending I invited one."'''
    answer_a = '''"Good. I was beginning to wonder how long you would keep that smile nailed on."
{n}Arueshalae takes the chair, keeping her hands to herself.{/n}
"You interest me, Camellia. That does not make me less hungry."''' if evil else '''"Then here is my answer: no. Not a kiss, not a little taste."
{n}Arueshalae leaves the chair empty, but stays beside the table.{/n}
"We have an operation to prepare for. I can help with that. Do not dress the other invitation up as kindness."'''
    choices = [c('"Let each name what she meant."' if retry else
                 '"Answer her without the polite cover."', "answered")]
    if not retry:
        choices.append(c('"Call it a harmless invitation."', "masked"))
    choices.extend([c('"Leave it."' if retry else '"Leave this unanswered."', "refused"), later()])
    nodes = [n("start", "Camellia", start, *choices),
             n("answered", "Arueshalae", answered, c("[Continue.]", "camellia")),
             n("camellia", "Camellia", answer_c, c("[Continue.]", "owned")),
             terminal("owned", "Arueshalae", answer_a,
                      stamp + ".seen", *(["retry.done"] if retry else []),
                      "settle.done", "settle." + branch + "_done", *BASE_DEEDS),
             terminal("refused", "Camellia", '''"How discreet of you."
{n}Camellia rises. Arueshalae watches her go; the empty chair remains between them.{/n}''',
                      stamp + ".seen", stamp + ".refused", "unsettled")]
    if not retry:
        nodes.append(terminal("masked", "Arueshalae", '''"Harmless? Ask her to sit closer, then."
{n}Camellia does not move. Neither woman takes up the work waiting at the bench.{/n}''',
                              "settle.seen", "settle.failed", "failed." + branch))
    # Ruling 21: the successful deed includes the proposed workbench inspection,
    # inside this protected host. No second preparation, roll or allowance.
    owned = next(node for node in nodes if node["Id"] == "owned")["Choices"][0]
    receipt = owned["Set"]
    owned["Set"] = []
    owned["Next"] = "inspection_camellia"
    nodes.extend([
        n("inspection_camellia", "Camellia",
          "[PROSE PENDING: Camellia - retain control of the exposed work / turn the existing sample toward Arueshalae for inspection / surrender the harmless cover without preparing another sample]",
          c("[Let Arueshalae inspect it.]", "inspection_arueshalae")),
        n("inspection_arueshalae", "Arueshalae",
          "[PROSE PENDING: fallen Arueshalae - keep her appetite / inspect Camellia's existing work without taking a taste / give up the easy feeding answer]" if evil else
          '''{n}Arueshalae bends over the workbench, keeping her hands clear of Camellia. She examines the sample beneath the lamp.{/n}
"This edge is uneven. There, beside your thumb."
{n}Camellia turns it to the light, then draws it back to her side. Arueshalae leaves the chair empty.{/n}
"I have seen the work. That was what we came here to do. The troops can have their preparations back."''',
          c("[Finish the inspection.]", flags=receipt + [p("deed.workbench_inspected")]))])
    requires = [p("ready." + branch)]
    forbids = []
    if not evil:
        forbids.append("arueshalae.corrupted")
    if retry:
        requires.extend([p("settle.failed"), p("failed." + branch)])
        forbids.extend([p("settle.done"), p("unsettled")])
    return entry(step, "An invitation with teeth", nodes, requires, forbids, 48 if retry else 0)


def optional_scenes():
    fallen = ("arueshalae.corrupted", p("ready.evil"), p("settle.evil_done"))
    company = entry("company", "The work under the smile", [
        n("start", "Camellia", '''{n}At the Table, Camellia sets a stoppered poison bottle beside the map of the Worldwound approaches. Arueshalae leans over it; Camellia puts a finger on the stopper.{/n}
"The workroom is ready. She insists on inspecting my work. How flattering."''',
          c('"Let her inspect the work."', "workbench", forbids=(SHARED_CRAFT_WITNESS,)),
          c('"Keep this to business."', "declined"), later(),
          c("[PROSE PENDING: choice - leave them company over the already witnessed work]", "witnessed_company",
            requires=(SHARED_CRAFT_WITNESS,))),
        n("workbench", "Camellia", '''{n}In the workroom, Camellia draws a strip of linen across a blade. Arueshalae reaches for the bottle. Camellia slides it out of reach and offers the blade instead.{/n}
"You may look. I am not giving lessons."
{n}She turns the treated edge toward the lamp, exposing her work to the succubus's scrutiny.{/n}''', c("[Continue.]", "kept")),
        terminal("kept", "Arueshalae", '''"You missed a patch. Such a pity if the cultist lived long enough to scream."
{n}Arueshalae points beside the hilt. Camellia examines the blade, then takes the linen to it again.{/n}
"There. I would rather watch your hands than eat you tonight."
{n}Camellia stops wiping. Then she smiles and lays a second blade under the lamp. Arueshalae stays to examine it.{/n}''', *COMPANY),
        terminal("declined", "Camellia", '"Very well. I have work to finish."',
                 "company.seen", "company.declined", "arc.declined"),
        terminal("witnessed_company", "Camellia",
                 "[PROSE PENDING: Camellia - seek Arueshalae's company / keep her beside the already inspected work and receive her personal answer / spend private time without repeating the preparation]",
                 *COMPANY),
    ], fallen + (p("settle.done"),) + RESPECT, optional=True)
    desire = entry("desire", "Courtesy set aside", [
        n("start", "Camellia", '''{n}Camellia brings two cups to the Table. The blades for the Worldwound march are packed; the workroom key lies beside her wine.{/n}
"I have no more work to show her. She may come anyway."''',
          c('"Leave them their invitation."', "camellia_answer"),
          c('"Keep it company."', "declined"), later()),
        n("camellia_answer", "Camellia", '''"I asked for you, Arueshalae. The soldiers may think you came to inspect the equipment. You need not."
{n}Camellia pushes the second cup toward her.{/n}
"I should be very annoyed if you made me say it twice."''', c("[Continue.]", "arueshalae_answer")),
        n("arueshalae_answer", "Arueshalae", '''"And what shall I tell them when they ask why you keep inviting a succubus?"
{n}Arueshalae takes the cup, watching Camellia over its rim.{/n}
"I'll come for you, Cami. Your bottles bore me. But you'll have to do your own lying."''', c("[Continue.]", "named")),
        terminal("named", "Camellia", '''"How fortunate that I am better at it."
{n}Camellia leaves the key between them and drinks.{/n}''', *DESIRE),
        terminal("declined", "Arueshalae", '"Company, then. She can keep her pretty excuses."',
                 "desire.seen", "desire.declined", "arc.declined"),
    ], fallen + (p("company.kept"),), delay=48, optional=True)
    contact = entry("choice", "No harmless invitation", [
        n("start", "Camellia", '''{n}At the Table, Camellia sets down the key to the workroom. Arueshalae traps it beneath one finger. Outside, soldiers are being called to their posts.{/n}
"Seven minutes under the ward, then I have blades to deliver."''',
          c('"Leave them alone."', "camellia_yes", requires=("arueshalae.ward_held",)),
          c('"Keep it friendship."', "declined"), later()),
        n("camellia_yes", "Camellia", '''"I said company. Do try to distinguish an invitation from a serving dish."
{n}Camellia looks directly at Arueshalae.{/n}
"Come with me. I want you there."''', c("[Continue.]", "arueshalae_yes")),
        n("arueshalae_yes", "Arueshalae", '''"You were very careful to make both sound alike."
{n}Arueshalae lifts her finger from the key.{/n}
"Yes, Cami. Tonight I want the woman who asked. Keep your poison corked."''', c("[Continue.]", "ward_application")),
        n("ward_application", "Narrator", '''{n}The shrine chaplain unrolls the Scroll of Death Ward. Camellia stands before him while Arueshalae waits clear of her. The ward must be read over Camellia before they leave together.{/n}''',
          c("[Have the ward read over Camellia.]", "cut", requires=("arueshalae.ward_held",),
            remove_item=SCROLL, flags=(p("choice.ward_spent"), p("ward.applied_camellia"))),
          c('"Keep their company; leave the rest tonight."', "declined")),
        n("cut", "Narrator", '''{n}You leave them in the workroom and shut the door. Camellia pushes the corked bottles aside, catches Arueshalae by the collar and kisses her. The succubus grips her waist and answers. Camellia draws her against the cleared bench; Arueshalae's fingers catch at the fastenings of her clothes.{/n}
{n}Camellia does not bother with patience. She has the succubus's bodice open with one tug and her own coat off with the other, and she sets her teeth to Arueshalae's throat hard enough to leave a mark, because she can, because for seven minutes the one thing in this room that kills by touch, the drain behind the succubus's kiss, cannot take a breath from her. Arueshalae gasps and laughs and arches into it, wings flaring wide to knock a rack of vials rattling. Her hands are all over the mortal's body, hungry, reverent, unashamed: ribs, hips, the long muscle of the thigh. Camellia hoists her up onto the bench by the backs of her knees and stands between them, breathing hard, bare to the waist, her expression the one she wears over a good kill. \"Say it,\" she mutters. \"Say what you want.\" Arueshalae answers by pulling her down by the hair.{/n}''',
          c("[Continue.]", SLOT)),
        n(SLOT, "Camellia", '{n}Their shadows move across the workbench in the lamplight.{/n}\n"You will not tell them I asked."',
          c("[Continue.]", "kept_warded")),
        terminal("kept_warded", "Arueshalae", '''{n}Camellia straightens her clothes and steps away before the ward expires. Arueshalae laughs from the other side of the bench.{/n}
"You did ask. Shall I tell them how sweetly?"
{n}Camellia turns back, one fastening still undone.{/n}
"Oh, I know. You wanted me. Next time, you can say it before you kiss me."
{n}They leave separately for their own quarters.{/n}''',
                 "choice.seen", "choice.both_yes", "deed.a_chose", "deed.b_chose", "choice.ward_spent",
                 "ward.applied_camellia"),
        terminal("declined", "Camellia", '"Keep the wine, then. I shall keep the key."',
                 "choice.seen", "choice.declined", "arc.declined"),
    ], fallen + FRIENDS + tuple(p(x) for x in COMPANY[1:] + DESIRE[1:]), delay=48, optional=True)
    morning = entry("morning", "Who kept the key", [
        n("start", "Camellia", '''{n}At the Table the next morning, Camellia snaps a case of treated blades shut. Arueshalae has brought her bow and the workroom key. Outside, the troops are assembling for the Worldwound march.{/n}
"You have brought that back very publicly."''',
          c('"Whose invitation was it?"', "cover"), later()),
        n("cover", "Camellia", '''"Mine. You may stop looking so pleased about it."
{n}Camellia presses her palm over the case's latch.{/n}
"Next time, I shall come to you. You can explain my visit for a change."''', c("[Continue.]", "done")),
        terminal("done", "Arueshalae", '''"To me? With that sweet little smile? They'll think you've come to be eaten."
{n}Arueshalae slides the key across the Table and shoulders her bow without touching Camellia.{/n}
"Wear it anyway. I like knowing what you hide behind it."
{n}Camellia leaves with her case; Arueshalae follows the troops toward the gate.{/n}''',
                 "morning.seen", "morning.done", "deed.a_returned_to_duty", "deed.b_returned_to_duty"),
    ], fallen + (p("choice.both_yes"),), delay=8, optional=True)
    return [company, desire, contact, morning]


def register(payload, scenes, refs):
    pending = payload.setdefault("PendingHooks", [])
    for a, b in (PAIR, PAIR[::-1]):
        for key in (household.enmity(a, b), a + ".harem.reconciled." + b):
            if key not in pending:
                pending.append(key)
    derived = payload.setdefault("Derived", {})
    derived[p("body.camellia")] = [[p("body.camellia.native")],
                                   ["camellia.trickster.coffin_life"]]
    derived[p("body.camellia.native")] = [["camellia.present_now"]]
    payload.setdefault("DerivedForbids", {})[p("body.camellia.native")] = [
        "camellia.killed", "camellia.dead", "camellia.kicked_out"]
    payload["DerivedForbids"][p("body.camellia")] = ["camellia.presence.failed"]
    for branch, personality, body in (("good", "redeemed", "arueshalae.in_party"),
                                      ("evil", "corrupted", "arueshalae.evil_recruited")):
        derived[p("ready." + branch)] = [["camellia.harem.eligible", "arueshalae.harem.eligible",
                                          "camellia.present_now", "arueshalae.present_now",
                                          p("body.camellia"), "arueshalae." + personality, body]]
    # Registration owns Derived views; choices write only deed/cost witnesses.
    # Current personality filters old fallen friendship without deleting history.
    for a, b in (PAIR, PAIR[::-1]):
        stage = a + ".harem.attitude." + b + "."
        derived[stage + "rival"] = [[p("settle.seen")]]
        derived[stage + "respect"] = [[p(x) for x in BASE_DEEDS[:4]]]
        who = "b" if a == "camellia" else "a"
        derived[stage + "friend"] = [[p("settle.evil_done"), p("company.kept"),
                                      p("deed." + who + "_company"), p("cost." + who + "_company"),
                                      "arueshalae.corrupted"]]
        derived[stage + "lover"] = [[p("settle.evil_done"), "arueshalae.corrupted"] +
                                     [p(x) for x in COMPANY[1:] + DESIRE[1:]] +
                                     [p(x) for x in ("choice.both_yes", "deed.a_chose", "deed.b_chose",
                                                    "choice.ward_spent", "ward.applied_camellia")]]
    additions = [settlement(branch, retry) for retry in (False, True) for branch in ("good", "evil")]
    additions.extend(optional_scenes())
    craft = derived.setdefault(SHARED_CRAFT_WITNESS, [])
    # The old company inspection is also a legitimate source; no S12 receipt
    # is manufactured by either of these S11 acts.
    for group in ([p("deed.workbench_inspected")], [p(x) for x in COMPANY]):
        if group not in craft:
            craft.append(group)
    existing = {s["Id"] for s in scenes}
    scenes.extend(s for s in additions if s["Id"] not in existing)
    household.CONSUMERS.update({s["Id"]: household.PAGE_TAKEN for s in additions})
