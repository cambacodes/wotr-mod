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
        n("start", "Camellia", '''{n}Camellia lays out a stoppered bottle and a strip of linen. The equipment is intended for the next operation against the demons. Arueshalae watches her hands rather than the bottle.{/n}
"She wishes to inspect my work. How flattering."''',
          c('"Let her inspect the work."', "workbench"), c('"Keep this to business."', "declined"), later()),
        n("workbench", "Camellia", '''{n}Camellia draws the linen across a blade, then leaves the blade on the bench for inspection.{/n}
"The edge, not the handle. And the bottles stay where I put them."
{n}She does not hide the treated strip when Arueshalae bends over it.{/n}''', c("[Continue.]", "kept")),
        terminal("kept", "Arueshalae", '''"Careful work. You would hate to waste it on the wrong throat."
{n}Arueshalae points out a missed patch near the hilt. Camellia takes the strip back and corrects it.{/n}
"I came to see how you do it. If I wanted a meal, I would not be standing here talking about your knife."''', *COMPANY),
        terminal("declined", "Camellia", '"Very well. I have work to finish."',
                 "company.seen", "company.declined", "arc.declined"),
    ], fallen + (p("settle.done"),) + RESPECT, optional=True)
    desire = entry("desire", "Courtesy set aside", [
        n("start", "Camellia", '''{n}The blades for the Worldwound march have been packed away. Camellia has kept back a chair and a cup of wine.{/n}
"Not everything at this bench is meant for the army."''',
          c('"Leave them their invitation."', "camellia_answer"),
          c('"Keep it company."', "declined"), later()),
        n("camellia_answer", "Camellia", '''"I asked for you, Arueshalae. Not an inspection. Not an audience."
{n}Camellia leaves the second cup in plain sight.{/n}
"I should be very annoyed if you made me say it twice."''', c("[Continue.]", "arueshalae_answer")),
        n("arueshalae_answer", "Arueshalae", '''"You want something dangerous at your elbow. And you want everyone else to think it wandered there by accident."
{n}Arueshalae takes the chair.{/n}
"I came back for you. There are easier meals in Drezen."''', c("[Continue.]", "named")),
        terminal("named", "Camellia", '"Then we understand one another. Leave the bottles alone."', *DESIRE),
        terminal("declined", "Arueshalae", '"Company, then. She can keep her pretty excuses."',
                 "desire.seen", "desire.declined", "arc.declined"),
    ], fallen + (p("company.kept"),), delay=48, optional=True)
    contact = entry("choice", "No harmless invitation", [
        n("start", "Camellia", '''{n}At the Table, Camellia sets down the key to the workroom. Arueshalae traps it beneath one finger. Outside, soldiers are being called to their posts.{/n}
"We shall not be long. The march can spare us seven minutes."''',
          c('"Leave them alone."', "camellia_yes", requires=("arueshalae.ward_held",)),
          c('"Keep it friendship."', "declined"), later()),
        n("camellia_yes", "Camellia", '''"I said company. Do try to distinguish an invitation from a serving dish."
{n}Camellia looks directly at Arueshalae.{/n}
"Come with me. I want you there."''', c("[Continue.]", "arueshalae_yes")),
        n("arueshalae_yes", "Arueshalae", '''"You were very careful to make both sound alike."
{n}Arueshalae lifts her finger from the key.{/n}
"Yes, Cami. Tonight I want the woman who asked."''', c("[Continue.]", "ward_application")),
        n("ward_application", "Narrator", '''{n}The shrine chaplain unrolls the Scroll of Death Ward. Camellia stands before him while Arueshalae waits clear of her. The ward must be read over Camellia before they leave together.{/n}''',
          c("[Have the ward read over Camellia.]", "cut", requires=("arueshalae.ward_held",),
            remove_item=SCROLL, flags=(p("choice.ward_spent"), p("ward.applied_camellia"))),
          c('"Keep their company; leave the rest tonight."', "declined")),
        n("cut", "Narrator", '''{n}At the workbench, Camellia catches Arueshalae by the collar and kisses her. Arueshalae's hands close on her waist; she answers the kiss without taking the life beneath it. Camellia pulls her nearer. You leave them and shut the door.{/n}''',
          c("[Continue.]", SLOT)),
        n(SLOT, "Camellia", '{n}The lamp at the workbench burns down while they remain together.{/n}\n"You will not tell them I asked."',
          c("[Continue.]", "kept_warded")),
        terminal("kept_warded", "Arueshalae", '''{n}Camellia straightens her clothes and steps away before the ward expires. Arueshalae laughs from the other side of the bench.{/n}
"You did ask. And you enjoyed my answer. Call it desire if you like — I will still remember who turned the key."
{n}They leave separately for their own quarters.{/n}''',
                 "choice.seen", "choice.both_yes", "deed.a_chose", "deed.b_chose", "choice.ward_spent",
                 "ward.applied_camellia"),
        terminal("declined", "Camellia", '"Keep the wine, then. I shall keep the key."',
                 "choice.seen", "choice.declined", "arc.declined"),
    ], fallen + FRIENDS + tuple(p(x) for x in COMPANY[1:] + DESIRE[1:]), delay=48, optional=True)
    morning = entry("morning", "Who kept the key", [
        n("start", "Camellia", '''{n}Eight hours later, the two chairs at the Table stand apart. Camellia has a packed case beside her. Arueshalae's bow rests against the wall. The troops are assembling outside.{/n}
"I trust this morning will contain fewer impertinent questions."''',
          c('"Whose invitation was it?"', "cover"), later()),
        n("cover", "Camellia", '''"Mine. You may stop looking so pleased about it."
{n}Camellia snaps the case shut.{/n}
"And when the soldiers ask, we were preparing equipment for the march. That much is true."''', c("[Continue.]", "done")),
        terminal("done", "Arueshalae", '''"I will tell them you were very thorough."
{n}Arueshalae shoulders her bow without touching Camellia.{/n}
"Go on, Cami. Keep your respectable face. I know where to find the other one."
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
    existing = {s["Id"] for s in scenes}
    scenes.extend(s for s in additions if s["Id"] not in existing)
    household.CONSUMERS.update({s["Id"]: household.PAGE_TAKEN for s in additions})
