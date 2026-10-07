"""Seelah x Wenduag (doc 16 §3 row 2, the worked pair of §8b): the §8c.6 prerequisites. DATA ONLY: no scene, no prose.

Source: Writer/handoffs/16-HOUSEHOLD-DYNAMICS.md §8b/§8c.6 and the reviewed build sheet
Writer/drafts/sol/review-harem-seelah-wenduag-prereqs/out.md (Sol second pass, Luna-corrected). This module freezes, for the
harem pass that writes the pair (memory rrt-harem-order: pair scenes come last):
- the conduct Seelah objects to and what she can live with (OBJECTS, TOLERATES);
- the consequential boundary Wenduag accepts for her own reasons (BOUNDARY);
- what the captive is worth to her, so the restraint costs something real (CAPTIVE);
- the lasting consequence of Seelah's intervention, recorded as flags (DEBT);
- the step sheet: scene ids, gates, delays, check DCs, choice indices and the outcome flags each terminal writes (STEPS);
- the verified canon evidence (EVIDENCE: enGB keys, blueprint paths and GUIDs, rechecked 2026-10-02).
Everything in OBJECTS..DEBT and every incident is AUTHORED (RRT), not canon; EVIDENCE is canon.

Ownership (ROUTE-BRIEF-R "Household hooks"; doc 16 §7): no producer here writes `*.harem.attitude.*`, strain, enmity,
tolerated, stance, closure or native romance state. The household integrator owns the ladder; LADDER only says which
witness flag it may read for each directional advance. validate() enforces this and is called from household.integrate.

Save safety: none of these ids is shipped (development/Story.json and package/Story.json hold no `household.pair.` id on
2026-10-02). Once a step ships, its scene id, node ids, flags and choice indices are frozen; new choices and wrapper scenes
are appended (AGENTS.md hard rules).
"""

PREFIX = "household.pair.seelah_wenduag."
PAIR = ("seelah", "wenduag")
CHAPTERS = (5,)          # Wenduag's courtship and commit are Ch5 (06 registry), and table_entry needs both eligible
STEP_DELAY = 48          # deed clocks; ER-H1 separately limits completion per successful rest
MORNING_DELAY = 8
STAGES = ("rival", "respect", "friend", "lover")
FORBIDDEN_TOKENS = (".harem.attitude.", ".strain.", ".enmity.", ".tolerated", ".stance.", ".closed", ".committed",
                    ".mend.", ".disappointed")


def P(x):
    return PREFIX + x


def att(a, b, stage):
    """Integrator-owned attitude flag (doc 16 §2.2). Read here, never written."""
    return "%s.harem.attitude.%s.%s" % (a, b, stage)


def _above(a, b, stage):
    return tuple(att(a, b, s) for s in STAGES[STAGES.index(stage) + 1:])


# 06 §1a (canonical household registry, 2026-10-02): both women list §3 row 2 as ally (R, F->R) and friction (start).
REGISTRY = dict(
    seelah=dict(temperament="possessive",
                terms="no lie told in Iomedae's name, and what she steals back is hers to keep"),
    wenduag=dict(temperament="competitive",
                 terms="she claims what strength wins; nobody feeds her with a leash hidden in it"),
)
# Consequences for this pair: Seelah's yes is never bought with a lie in the Lady's name (the restraint is a deed, not a
# sworn conversion); Wenduag's boundary is no leash because she sets it herself, before her hunters (BOUNDARY).

# --- §8c.6 (1): what Seelah objects to, and what she can live with (authored applications of the evidence) -------------
OBJECTS = (
    dict(conduct="breaking a bound prisoner's fingers to make him talk, prolonging his pain for amusement, or killing him "
                  "to display his head", response="intervenes physically; guilt does not make helplessness permission",
         evidence=("S1", "S2", "S3")),
    dict(conduct="hunting civilians, killing a subordinate for weakness, or settling jealousy with violence against another "
                  "partner", response="will not assist or stand aside", evidence=("W1", "W4")),
    dict(conduct="asking her to prove love by watching cruelty, or using her presence as a paladin's endorsement",
         response="refuses", evidence=("S2", "S5", "seelah_later.py:139 (RRT)")),
)
TOLERATES = (
    dict(conduct="force against an armed enemy still fighting; a dangerous rescue; a first-blood spar both women choose",
         response="participates", evidence=("S4", "P1")),
    dict(conduct="Wenduag's pride, coarse boasts, cunning, hunger for rank and a faith unlike hers",
         response="dislikes them, still shares a watch or desires her; never blesses the cruelty they produce",
         evidence=("W1", "W2", "S5")),
    dict(conduct="Wenduag's blunt sexual offer and chosen roughness between them",
         response="only after Seelah herself wants her, shown in her later actions; no source gives her that taste",
         evidence=("S6", "P1", "P2")),
)
NOT_REQUIRED = ("Wenduag converts", "Wenduag renounces ambition", "Wenduag becomes generally merciful",
                "Seelah is indifferent to what Wenduag does out of her sight")

# --- §8c.6 (2): the consequential boundary Wenduag accepts for her own reasons ----------------------------------------
BOUNDARY = dict(
    flag=P("boundary.prisoners_kept_alive"),
    scope="every enemy who surrenders or is captured on their SHARED operations",
    rule="goes alive and unmaimed to guarded crusade custody",
    gives_up=("torture", "private interrogation by injury", "maiming", "trophy killings", "having one of her hunters do either for her"),
    allows="force against active resistance; invented resistance or a staged escape is a breach",
    not_a="pardon, sentence, canon law, redemption, conversion, or obedience bought with sex",
    her_reason=("Seelah has proved a strong fighting partner (spar, watch); fighting her over every bound prisoner would "
                "turn each joint victory into someone else restraining Wenduag; she decides in front of her hunters and "
                "orders the handover herself, keeping command"),
)

# --- §8c.6 (3): the captive, and what he is worth to her -------------------------------------------------------------
CAPTIVE = dict(
    name="Rusk", kind="authored male cultist scout captain; no roster route, native NPC, Brask or Lann",
    history=("in `watch` Wenduag names him: his patrol trapped her on a reconnaissance run and nearly killed her; some of "
             "his scouts escaped the trap (the later extraction risk)"),
    worth=("revenge on the man who nearly killed her", "the pleasure of breaking him herself",
           "visible proof, before her hunters, that whoever hunts her ends as her trophy"),
    not_payment="his knowledge of cult patrol routes is the crusade's reason to hold him, not a prize for Wenduag",
    custody_flag=P("captive.rusk_in_custody"),
    hunters=("a few willing crusade scouts she recruits during `watch` for the false trail; never assume a living tribe "
             "under her command; say 'my hunters' only after that"),
    staging="narrated action inside the Table dialogue; no spawned unit, no tactical encounter, no native quest edit",
)

# --- §8c.6 (4): the lasting consequence of Seelah's intervention (a debt, not an injury) -----------------------------
DEBT = dict(
    owed=P("stood.debt_owed"),       # historical latch: stays set after repayment
    paid=P("stood.debt_paid"),
    cost=P("cost.hunt_forgone"),
    terms="one dangerous watch at Seelah's request; buys service, never affection or access to her body",
    called_in="Rusk's next overnight watch, against an extraction attempt, the night Wenduag had named for her own hunt",
    her_reason="pays a fighter's debt in full rather than concede weakness (W5); keeps command of her hunters and refuses a Commander gift with a hidden leash",
    outstanding_reader=dict(requires=(P("stood.debt_owed"),), forbids=(P("stood.debt_paid"),)),
)
COSTS = (P("cost.kill_yielded"), P("cost.seelah_first_watch"), P("cost.hunt_forgone"), P("cost.seelah_wounded"))

# --- The step sheet (doc 16 §8b, revised by §8c.6) ---------------------------------------------------------------------
# outcomes: {choice index: {"label", "next" or terminal flags}}; checks list success/failure flag sets. Every flag here is
# written by a terminal "Continue" AFTER the action is narrated; a "later" exit uses Abort=True and writes nothing.
_RESTRAINT = dict(
    seelah_from=att("seelah", "wenduag", "respect"),
    outcomes={0: dict(label='"Let her decide."',
                      flags=(P("restraint.seen"), P("restraint_witnessed"), BOUNDARY["flag"], CAPTIVE["custody_flag"],
                             P("cost.kill_yielded"), P("cost.seelah_first_watch"))),
              1: dict(label='"Hang him."',      # Seelah objects and refuses to assist; the account states the execution
                      flags=(P("restraint.seen"), P("restraint.execution_ordered")))},
)
_STOOD = dict(
    check=("SkillAthletics", 18),   # the Commander's covering move: decides rescue vs scramble, never whether Seelah tries
    success=(P("stood.seen"), P("stood_witnessed"), P("stood.debt_owed"), P("cost.seelah_wounded")),
    failure=(P("stood.seen"), P("stood.failed"), P("cost.seelah_wounded")),
)

STEPS = [
    dict(id=P("init"), kind="derived", requires=("seelah.harem.eligible", "wenduag.harem.eligible"), flags=(),
         note="Derived canon start (both rival); the integrator's producer, listed so the chain is complete"),
    dict(id=P("spar"), requires=(P("invited"), att("seelah", "wenduag", "rival"), att("wenduag", "seelah", "rival")),
         forbids=(att("seelah", "wenduag", "respect"), att("wenduag", "seelah", "respect"), P("spar.seen")), delay=0,
         check=("SkillAthletics", 20), choice=0,
         success=(P("spar.seen"), P("spar.held")), failure=(P("spar.seen"), P("spar.failed")),
         outcomes={0: dict(label='"First blood, my rules, my ring."'),
                   1: dict(label='"Not in my tavern."', flags=(P("spar.seen"), P("spar.declined")))}),
    dict(id=P("rematch"), any_groups=((P("spar.failed"), P("spar.declined")),),
         forbids=(att("seelah", "wenduag", "respect"), att("wenduag", "seelah", "respect"), P("rematch.seen")),
         delay=STEP_DELAY, check=("SkillPerception", 18),
         success=(P("rematch.seen"), P("rematch.held")),
         failure=(P("rematch.seen"), P("rematch.failed")),   # permanent player-caused outcome, stated in the Ledger
         outcomes={0: dict(label="Referee it"),
                   1: dict(label='"No more fighting in my tavern."', flags=(P("rematch.seen"), P("rematch.declined")))}),
    dict(id=P("watch"), any_groups=((P("spar.held"), P("rematch.held")),), requires=(att("seelah", "wenduag", "respect"), att("wenduag", "seelah", "respect")),
         forbids=(P("watch.seen"),), delay=STEP_DELAY,
         outcomes={0: dict(label="Continue", flags=(P("watch.seen"), P("watch.done")))},
         optional_reads=("wenduag.trickster.claim.given", "wenduag.trickster.claim.knelt", "wenduag.trickster.claim.struck"),
         note="names Rusk and the trap; recruits the scouts; Brask is admitted/condemned from the claim flags, never rewritten"),
    dict(id=P("restraint"), requires=(P("watch.done"), _RESTRAINT["seelah_from"]),
         forbids=(P("restraint.seen"), P("stood.seen")) + _above("seelah", "wenduag", "respect"),
         delay=STEP_DELAY, outcomes=_RESTRAINT["outcomes"], first_of="personal"),
    dict(id=P("restraint.after_stood"), requires=(P("watch.done"), P("stood.seen"), _RESTRAINT["seelah_from"]),
         forbids=(P("restraint.seen"),) + _above("seelah", "wenduag", "respect"),
         delay=STEP_DELAY, outcomes=_RESTRAINT["outcomes"], wrapper_of=P("restraint")),
    dict(id=P("stood"), requires=(P("watch.done"), att("wenduag", "seelah", "respect")),
         forbids=(P("stood.seen"), P("restraint.seen")) + _above("wenduag", "seelah", "respect"),
         delay=STEP_DELAY, check=_STOOD["check"], success=_STOOD["success"], failure=_STOOD["failure"], outcomes={},
         first_of="personal"),
    dict(id=P("stood.after_restraint"), requires=(P("watch.done"), P("restraint.seen"), att("wenduag", "seelah", "respect")),
         forbids=(P("stood.seen"),) + _above("wenduag", "seelah", "respect"),
         delay=STEP_DELAY, check=_STOOD["check"], success=_STOOD["success"], failure=_STOOD["failure"], outcomes={},
         wrapper_of=P("stood")),
    dict(id=P("debt_repayment"),
         requires=(P("restraint_witnessed"), P("stood_witnessed"), BOUNDARY["flag"], CAPTIVE["custody_flag"], DEBT["owed"]),
         forbids=(DEBT["paid"],), delay=STEP_DELAY,
         outcomes={0: dict(label="Continue", flags=(P("debt_repayment.seen"), DEBT["paid"], DEBT["cost"], P("boundary.kept"))),
                   1: dict(label='"He could die escaping. Nobody would ask."',
                           flags=(P("debt_repayment.seen"), DEBT["paid"], DEBT["cost"], P("boundary.kept"), P("boundary.trick_refused"))),
                   2: dict(label='"Then I will do it."',
                           flags=(P("debt_repayment.seen"), P("captive.rusk_dead"), P("debt.betrayed")))},
         note="appended; narrates the completed watch and the lost hunt; no attitude change, no erotic reward"),
    dict(id=P("choice"),
         requires=(att("seelah", "wenduag", "friend"), att("wenduag", "seelah", "friend"), P("restraint_witnessed"),
                   P("stood_witnessed"), BOUNDARY["flag"], CAPTIVE["custody_flag"], DEBT["owed"], DEBT["paid"], DEBT["cost"], P("boundary.kept")),
         forbids=(att("seelah", "wenduag", "lover"), att("wenduag", "seelah", "lover"), P("choice.seen"),
                  P("debt.betrayed"), P("captive.rusk_dead"), P("boundary.breached")),
         delay=STEP_DELAY,
         outcomes={0: dict(label="taking their shared watch until dawn",
                           flags=(P("choice.seen"), P("choice.watch_taken")),
                           mutual=P("choice.both_yes")),   # set only when BOTH women say yes inside [0]
                   1: dict(label="a household evening", flags=(P("choice.seen"), P("choice.household_evening")))},
         note="recalls the repayment without replaying it; Seelah's objection names the cruelty, the kept rule and her own "
              "desire, never a reformation"),
    dict(id=P("morning"), requires=(P("choice.both_yes"),), forbids=(P("morning.seen"),), delay=MORNING_DELAY,
         outcomes={0: dict(label="Continue", flags=(P("morning.seen"), P("morning.done")))},
         note="intimacy contract: Wenduag initiates at their shared lower-wall watch post; cut at the first explicit act, then this morning"),
]

# A1-A10 approved amendments, DATA ONLY. Append the invitation without moving any existing step ID.
STEPS.append(dict(id=P("invite"), kind="invitation", remote=True, sender="Wenduag", delay=0,
                  requires=("seelah.harem.eligible", "wenduag.harem.eligible"),
                  forbids=(P("invite.seen"),),
                  outcomes={0: dict(label="Reply", flags=(P("invite.seen"), P("invited")))}))
for _entry in STEPS:
    if _entry.get("kind") == "derived":
        continue
    _entry.setdefault("kind", "morning" if _entry["id"] == P("morning") else "table")
    _entry["participants"] = PAIR
    _entry["rest_allowance"] = (None if _entry["kind"] == "invitation" else
                                "household.protected" if _entry["id"] in (P("spar"), P("rematch")) else "household.pair")
    _entry["seen"] = _entry.get("wrapper_of", _entry["id"]) + ".seen"
    # Abort is an appended exit. It writes no flags and never spends the allowance.
    if _entry["id"] != P("watch") and _entry["id"] != P("morning"):
        _index = len(_entry["outcomes"])
        if "check" in _entry and not _index:
            _entry["outcomes"][0] = dict(label="Continue")
            _index = 1
        _entry["outcomes"][_index] = dict(label="Later", abort=True, flags=())
del _entry, _index

# A10 reserves a future breach witness; this sheet does not fabricate its producer.
RESERVED_READS = (P("boundary.breached"),)
SEATING_NOTES = (dict(id="boundary_breached", requires=RESERVED_READS),)

# Which witness flag the integrator may read for each directional advance (§8b); it writes the stage, not this module.
LADDER = (
    dict(edge=("seelah", "wenduag"), to="respect", reads=(P("spar.held"), P("rematch.held"))),
    dict(edge=("wenduag", "seelah"), to="respect", reads=(P("spar.held"), P("rematch.held"))),
    dict(edge=("seelah", "wenduag"), to="friend", reads=(P("restraint_witnessed"),)),
    dict(edge=("wenduag", "seelah"), to="friend", reads=(P("stood_witnessed"),)),
    dict(edge=("seelah", "wenduag"), to="lover", reads=(P("choice.both_yes"),)),
    dict(edge=("wenduag", "seelah"), to="lover", reads=(P("choice.both_yes"),)),
)

# Last Call may recall the repaid night only with both flags; the rescue witness or debt_owed alone proves nothing.
LAST_CALL = (
    dict(id="debt_repaid", requires=(DEBT["paid"], DEBT["cost"])),
    dict(id="morning", requires=(P("morning.seen"),)),
    dict(id="debt_betrayed", requires=(P("debt.betrayed"), P("captive.rusk_dead"))),
    dict(id="boundary_breached", requires=RESERVED_READS),
)

# Native/RRT state a later beat may read. Native outcomes only through SelectedAnswers/SeenCues, never Started-only etudes.
EXTERNAL_READS = dict(
    wenduag_eligible_native="wenduag.romance_finished.latched",      # household.EXTRA_ELIGIBLE; never require committed alone
    brask=("wenduag.trickster.claim.given", "wenduag.trickster.claim.knelt", "wenduag.trickster.claim.struck"),
    wenduag_redeemed=("52576309e24d8024fbc08c2ff7016c2f", "World/Etudes/Common/WrathOfTheRighteous/Companions/"
                      "WenduagCompanion/WenduagRedeemed.jbp"),
    wendu_good_now=("9ce50eac84ade7042872352b5d2622e7", "World/Etudes/Common/WrathOfTheRighteous/Companions/"
                    "WenduagCompanion/WenduagRomance/WenduagRomance_WenduGoodNow.jbp"),
)

# Canon evidence (enGB key, blueprint GUID, archive path under World/Dialogs/), rechecked against blueprints.zip and
# enGB.json on 2026-10-02. W3 (Savamelekh search), W4 (Dyra) and W6 (native romance) need their own campaign evidence
# before any retrospective line; P2 is Ch4 Abyss banter and may not have played.
EVIDENCE = {
    "S1": ("Seelah", "Companions/CompanionDialogues/Seelah/Cue_0019.jbp", "ca24b7ef8a4dd4d41ad3a2f78bb16023",
           "dfe40638-3044-46af-8c24-84cd259b61cd", "penance and a debt unpaid"),
    "S2": ("Seelah", "Companions/CompanionDialogues/Seelah/Cue_0032.jbp", "c9147be053e0b0d47b7d0c18951beece",
           "c273d91c-5a9b-4da3-9596-6b6b4f8c7b26", "we're all accountable for our actions"),
    "S3": ("Seelah", "Companions/CompanionDialogues/Seelah/Cue_0069.jbp", "02a3368727fddcf4a97f6cd4dcf3a6e5",
           "6607c79a-3f42-46a5-b5ce-93d9b856842d", "a kind deed done by an unkind person is a hundred times more precious"),
    "S4": ("Seelah", "Companions/CompanionDialogues/Seelah/Cue_0139.jbp", "c4bd1640d9c1a294e823d135bab0ad9c",
           "c68487d9-7da9-43fb-8c8c-084f2386ccde", "I will never abandon a companion"),
    "S5": ("Seelah", "Barkobanters/Banter/VenduagSeelah/Banter_VenduagSeelah_banter3.jbp", "24782fad6649efe408c874574fde6134",
           "40ad8e48-5ea9-4257-9df5-160058c74f4f", "Being a paladin gives me a purpose and my soul peace."),
    "S6": ("Seelah", "Barkobanters/Banter/VenduagSeelah/Banter_VenduagSeelah_banter4_pack2.jbp",
           "6e57435ac3323ae43ba66b239b33e55c", "b9f8dc05-5b58-4bd2-a365-ab675a4fb5b0",
           "I don't like it when someone looks at me like I'm a piece of meat."),
    "S7": ("Seelah", "Barkobanters/Banter/VenduagSeelah/Banter_VenduagSeelah_banter5_pack2.jbp",
           "58d56e26d59b0eb488d3636cfaf774b9", "feac0e33-8ed3-4438-a1d0-d12a4428366e",
           "poison slipped into a drink vs medicine offered openly (faith, not sexual preference)"),
    "W1": ("Wenduag", "Companions/CompanionDialogues/Wenduag/Cue_0044.jbp", "9e0dae25d5d23cc4592fab33a46106e3",
           "a8dc8b07-c1ee-405b-a248-b813b480d514", "The weak must obey the strong"),
    "W2": ("Wenduag", "Companions/CompanionDialogues/Wenduag/Cue_0048.jbp", "fd5d2041a388288429e757c4fd31702e",
           "4543cdfe-1d4e-445a-ba3d-98dde3b8a540", "the best hunter in the tribe"),
    "W3": ("Wenduag", "Companions/CompanionDialogues/Wenduag/Cue_0106.jbp", "463a7b3f13fcf8e488d169142814e498",
           "0320437a-4f81-4efa-acd2-838c7fec14a6", "My hunters regularly bring me prisoners to interrogate"),
    "W4": ("Wenduag", "Companions/CompanionDialogues/Wenduag/Cue_0121.jbp", "76f06e4a3937dee409e3dd69e6acbcf5",
           "3f36fa98-137c-48ab-a489-0796b83a61d4", "Dyra kept meddling in my affairs, so I killed her."),
    "W5": ("Wenduag", "Companions/CompanionDialogues/Wenduag/Cue_0204.jbp", "20b8253ec52123d4abe79c8feb2fce14",
           "4068efb9-38bc-4ccc-a4b6-18e5a9225354", "people who are strong, determined, who don't hide behind others"),
    "W6": ("Wenduag", "Companions/CompanionRomances/Wenduag/ThatIsFinal/Cue_0051.jbp", "0dbf18c26dc933a4aa73cb09329d1b6a",
           "58494bc6-0a26-44d6-bd3e-1e6fccf78ba1", "the same wicked, lying, traitorous bitch that I was before"),
    "P1": ("Wenduag, then Seelah", "Barkobanters/Banter/VenduagSeelah/Banter_VenduagSeelah_banter2.jbp",
           "398cebd73ae9f5a48a2609eb33532e25", "28b3abfb-caf8-4d06-a470-8871ff576c0a d178b689-0733-4020-b4c1-341d85b0e230",
           "It will be a good fight, I promise. / It sounds like you're asking me out on a date."),
    "P2": ("Wenduag", "Barkobanters/Story/Seelah/Banter_Seelah_ch4_1.jbp", "35a940ae7d67acc4984b430d4d54c063",
           "566b41f5-e329-40ac-ba17-3544011c0c3c", "Which is more to your taste, paladin?"),
}
# The Ch5 Table door these entries use (household.KING_C5): FoolKing_Tavern AnswersList_0054 (6dccfd39...), listed by
# Cue_0053 (f5b33951...) which requires Chapter05 Playing (5b01aa69...); the `c3` folder is not a chapter gate.


def _produced(steps):
    out = set()
    for step in steps:
        out.update(step.get("flags", ()))
        out.update(step.get("success", ()))
        out.update(step.get("failure", ()))
        for o in step.get("outcomes", {}).values():
            out.update(o.get("flags", ()))
            if o.get("mutual"):
                out.add(o["mutual"])
    return out


def _producers_of(flag, steps):
    hits = []
    for step in steps:
        if flag in step.get("success", ()):
            hits.append((step["id"], "success"))
        if flag in step.get("failure", ()):
            hits.append((step["id"], "failure"))
        for i, o in step.get("outcomes", {}).items():
            if flag in o.get("flags", ()) or flag == o.get("mutual"):
                hits.append((step["id"], i))
    return hits


def validate(partners=None, steps=None):
    """Lint the sheet (doc 16 §8 and the reviewed handoff). Raises ValueError listing every problem."""
    return _validate(partners, STEPS if steps is None else steps)


def _validate(partners, steps):
    errors = []
    if partners is not None:
        for rel in PAIR:
            if rel not in partners:
                errors.append("unknown household partner " + rel)
    if set(PAIR) & {"ember", "aivu"}:
        errors.append("Ember and Aivu are friendship-only")
    ids = [s["id"] for s in steps]
    if len(ids) != len(set(ids)):
        errors.append("duplicate step id")
    produced = _produced(steps)
    for step in steps:
        sid = step["id"]
        if not sid.startswith(PREFIX):
            errors.append("%s: id outside %s" % (sid, PREFIX))
        if step.get("kind") == "derived":
            continue
        for f in _produced_by(step):
            if not f.startswith(PREFIX) or any(t in f[len(PREFIX) - 1:] for t in FORBIDDEN_TOKENS):
                errors.append("%s writes %s: only pair outcome/cost flags are allowed" % (sid, f))
        reads = tuple(step.get("requires", ())) + tuple(f for g in step.get("any_groups", ()) for f in g)
        for f in reads:
            if f.startswith(PREFIX) and f not in produced:
                errors.append("%s requires %s, which no step produces" % (sid, f))
        kind = step.get("kind")
        if kind not in ("table", "morning", "invitation"):
            errors.append("%s: invalid step kind" % sid)
        want = 0 if kind == "invitation" or sid == P("spar") else MORNING_DELAY if kind == "morning" else STEP_DELAY
        if step.get("delay", 0) < want or kind == "invitation" and step.get("delay") != 0:
            errors.append("%s: delay %s < %s or invalid invitation delay" % (sid, step.get("delay", 0), want))
        if tuple(step.get("participants", ())) != PAIR:
            errors.append("%s: every step needs both participants" % sid)
        allowance = None if kind == "invitation" else "household.protected" if sid in (P("spar"), P("rematch")) else "household.pair"
        if step.get("rest_allowance") != allowance:
            errors.append("%s: wrong rest allowance category" % sid)
        if kind == "invitation" and (not step.get("remote") or step.get("sender") != "Wenduag"):
            errors.append("%s: invitation must be Wenduag's remote letter" % sid)
        terminals = [step[key] for key in ("success", "failure") if key in step]
        for index, outcome in step.get("outcomes", {}).items():
            if outcome.get("abort"):
                if outcome.get("flags") or outcome.get("mutual"):
                    errors.append("%s: Abort writes nothing" % sid)
            elif "flags" in outcome:
                terminals.append(outcome["flags"])
            elif "check" not in step or index != step.get("choice", 0):
                errors.append("%s: terminal needs seen and an outcome" % sid)
        for flags in terminals:
            if step.get("seen") not in flags or len(set(flags) - {step.get("seen")}) < 1:
                errors.append("%s: terminal needs seen and an outcome" % sid)
        if "check" in step:
            skill, dc = step["check"]
            if skill not in ("SkillAthletics", "SkillPerception") or not step.get("success") or not step.get("failure"):
                errors.append("%s: a check needs a valid skill and both success and failure outcomes" % sid)
            bad = [f for f in step.get("failure", ()) if f.endswith(("_witnessed", ".held", ".debt_owed"))]
            if bad:
                errors.append("%s: failure writes a success witness %s" % (sid, bad))
        idx = sorted(step.get("outcomes", {}))
        if idx != list(range(len(idx))):
            errors.append("%s: choice indices must be 0..n-1 (append-only)" % sid)
    # the personal beats: base + wrapper pairs, mutually exclusive, either order
    for base, other in ((P("restraint"), P("stood")), (P("stood"), P("restraint"))):
        b = _step(base, steps)
        w = _step(base + (".after_stood" if base == P("restraint") else ".after_restraint"), steps)
        if not b or not w:
            errors.append("%s needs its base scene and its wrapper" % base)
            continue
        if other + ".seen" not in b.get("forbids", ()):
            errors.append("%s must forbid %s.seen (the wrapper covers that order)" % (base, other))
        if other + ".seen" not in w.get("requires", ()):
            errors.append("%s must require %s.seen" % (w["id"], other))
        for s in (b, w):
            if base + ".seen" not in s.get("forbids", ()):
                errors.append("%s must forbid %s.seen" % (s["id"], base))
            if P("watch.done") not in s.get("requires", ()):
                errors.append("%s must require watch.done" % s["id"])
        if _produced_by(b) != _produced_by(w):
            errors.append("%s and its wrapper must write the same outcomes" % base)
    # the debt
    owed = {sid for sid, _ in _producers_of(DEBT["owed"], steps)}
    if owed != {P("stood"), P("stood.after_restraint")}:
        errors.append("debt_owed may be written only by stood success: %s" % sorted(owed))
    for sid, how in _producers_of(DEBT["owed"], steps):
        if how != "success":
            errors.append("debt_owed written on %s %s" % (sid, how))
    if {sid for sid, _ in _producers_of(DEBT["paid"], steps)} != {P("debt_repayment")}:
        errors.append("debt_paid may be written only by debt_repayment")
    if {sid for sid, _ in _producers_of(DEBT["cost"], steps)} != {P("debt_repayment")}:
        errors.append("hunt_forgone may be written only by debt_repayment")
    choice = _step(P("choice"), steps)
    if choice:
        for f in (DEBT["owed"], DEBT["paid"], DEBT["cost"], BOUNDARY["flag"], CAPTIVE["custody_flag"], P("boundary.kept")):
            if f not in choice.get("requires", ()):
                errors.append("choice must require " + f)
        for f in (P("debt.betrayed"), P("captive.rusk_dead"), P("boundary.breached")):
            if f not in choice.get("forbids", ()):
                errors.append("choice must forbid " + f)
    watch = _step(P("watch"), steps)
    if watch and watch.get("any_groups") != ((P("spar.held"), P("rematch.held")),):
        errors.append("watch needs both alternative respect clocks")
    for sid in (P("stood"), P("stood.after_restraint")):
        for terminal in ("success", "failure"):
            if P("cost.seelah_wounded") not in (_step(sid, steps) or {}).get(terminal, ()):
                errors.append("%s: %s must record Seelah wounded" % (sid, terminal))
    for sid in (P("restraint"), P("restraint.after_stood")):
        hang = (_step(sid, steps) or {}).get("outcomes", {}).get(1, {}).get("flags", ())
        if set(hang) & {P("restraint_witnessed"), BOUNDARY["flag"], CAPTIVE["custody_flag"], P("cost.kill_yielded")}:
            errors.append('%s "Hang him" must not record restraint, boundary, custody or a mercy cost' % sid)
    debt = _step(P("debt_repayment"), steps)
    if debt:
        outcomes = debt.get("outcomes", {})
        kept = {P("debt_repayment.seen"), DEBT["paid"], DEBT["cost"], P("boundary.kept")}
        if not kept <= set(outcomes.get(0, {}).get("flags", ())):
            errors.append("debt_repayment must record the kept boundary and complete cost")
        if not kept | {P("boundary.trick_refused")} <= set(outcomes.get(1, {}).get("flags", ())):
            errors.append("trick refusal must keep the boundary and pay the debt")
        betrayed = set(outcomes.get(2, {}).get("flags", ()))
        if betrayed != {P("debt_repayment.seen"), P("captive.rusk_dead"), P("debt.betrayed")}:
            errors.append("betrayal must record death, never a paid debt or kept boundary")
    if choice and (P("choice.watch_taken") not in choice.get("outcomes", {}).get(0, {}).get("flags", ())
                   or choice.get("outcomes", {}).get(0, {}).get("mutual") != P("choice.both_yes")):
        errors.append("choice needs the watch deed and both women's answers")
    for line in LAST_CALL:
        if line["id"] == "debt_repaid" and set(line["requires"]) != {DEBT["paid"], DEBT["cost"]}:
            errors.append("Last Call's repaid-debt recall requires debt_paid and hunt_forgone")
    for rung in LADDER:
        if rung["to"] not in STAGES or tuple(rung["edge"]) not in (PAIR, PAIR[::-1]):
            errors.append("bad ladder rung %s" % (rung,))
        for f in rung["reads"]:
            if f not in produced:
                errors.append("ladder reads %s, which no step produces" % f)
    for step in steps:
        if step.get("chapters", CHAPTERS) != CHAPTERS:
            errors.append("%s: the pair runs in Ch5 only" % step["id"])
    if errors:
        raise ValueError("Seelah x Wenduag sheet: " + "; ".join(errors))
    return True


def _step(sid, steps):
    for s in steps:
        if s["id"] == sid:
            return s
    return None


def _produced_by(step):
    out = set(step.get("flags", ())) | set(step.get("success", ())) | set(step.get("failure", ()))
    for o in step.get("outcomes", {}).values():
        out.update(o.get("flags", ()))
        if o.get("mutual"):
            out.add(o["mutual"])
    return out
