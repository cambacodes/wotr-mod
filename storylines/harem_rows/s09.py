"""S09, authored lower-town lookout operation; hs-B section S09, lore-check S09.

Canon voice anchors (not dialogue hooks): BarkBanter f2886a94768a1814fb409193d8e02dca,
enGB ae75bc3b-cb63-4009-b6e2-edcdd9a68571 / 11c8ae98-3684-410a-8544-267fd4893433;
BarkBanter d5728377ea1155d4ba33f96e66f7c082, enGB
3c852e2b-1f56-4f35-97a6-fad2a1e1474e / 1f4cd851-cd23-4c7d-bdc8-04e2443375a6.
Rechecked in /wrath/blueprints.zip and enGB.json. No native history is rewritten.
The Table is the actual hook. No return, partner stance, echo or new price.
Four optional completions, one arc start; protected primary plus one retry.
The sheet's unnamed second settlement tool is not invented here.
"""
from story_format import c, n
from storylines import household, arueshalae_trickster

PREFIX = "household.pair.wenduag_arueshalae."
PAIR = ("wenduag", "arueshalae")
WENDUAG = "ae766624c03058440a036de90a7f2009"
GOOD_ARUE = "a352873d37ec6c54c9fa8f6da3a6b3e1"
EVIL_ARUE = "e3bc95db7e2181d41847b3a1d858258d"
SCROLL = "89e10c3f21fa50c4b8719e004c7628d3"
LIVE = ("trickster.now", "wenduag.present_now", "arueshalae.present_now")
RESPECT = ("deed.wenduag_ground", "deed.arueshalae_height",
           "cost.wenduag_credit_shared", "cost.arueshalae_foot_plan_yielded")
FRIEND_W = ("friend_wenduag.done", "deed.wenduag_credit_kept", "cost.wenduag_solo_boast_yielded")
FRIEND_A = ("friend_arueshalae.done", "deed.arueshalae_cover_kept", "cost.arueshalae_easy_bait_yielded")


def p(suffix):
    return PREFIX + suffix


def flags(*suffixes):
    return tuple(p(s) for s in suffixes)


def page(node, speaker, text, *choices):
    return n(node, speaker, text, *choices, portrait=speaker if speaker != "Narrator" else "Wenduag")


def later():
    return c('"Later."', abort=True)


def terminal(node, speaker, text, writes):
    return page(node, speaker, text, c("Continue", flags=flags(*writes)))


def add(suffix, title, nodes, trigger, requires=(), forbids=(), delay=0, evil=False,
        protected=False, witness=None, arc_start=False):
    branch = "arueshalae.corrupted" if evil else "arueshalae.redeemed"
    body = p("body.arueshalae.evil" if evil else "body.arueshalae.good")
    return household.table_entry(
        p(suffix), title, '[Wenduag and Arueshalae: ' + title + ']', nodes, PAIR, p(trigger),
        requires=LIVE + (branch, p("body.wenduag"), body) + tuple(requires),
        forbids=tuple(forbids) + (() if evil else ("arueshalae.corrupted",)),
        delay=delay, chapters=(5,), RestAllowance="household.protected" if protected else "household.pair",
        HouseholdCategory="protected" if protected else "pair", HouseholdWitness=p(witness or suffix + ".seen"),
        HouseholdArc=PREFIX.rstrip("."), HouseholdArcStart=arc_start)


def settlement(evil, retry=False):
    branch = "evil" if evil else "good"
    step = "retry" if retry else "settle"
    opening = ('{n}The unfinished approach lies across the corner table. Wenduag has scratched out the exposed alley.{/n}'
               if retry else '{n}Wenduag pins a lower-town map to the corner table with her knife. A cult lookout has been watching the gate patrols from a ruined roof. She marks the alley beneath it.{/n}')
    nodes = [page("start", "Wenduag", opening + ' "We take him before he sends another signal." {n}Arueshalae marks the roof overlooking the alley.{/n} "He sees your feet from there," {n}she says. Wenduag shifts her line beneath an overhanging wall.{/n} "Your wings won\'t lift my hunters. Turn his head. We reach cover here."',
                  c('[Replot the unfinished approach with both of them.]' if retry else '[Plot the ground approach with their aerial correction.]', "plotted"),
                  c('"Leave it."' if retry else '"Send everyone by the foot route."', "refused" if retry else "blind"),
                  *([] if retry else [c('"Leave this operation to another patrol."', "refused")]), later())]
    success = [step + ".seen", "settle.done", "settle." + branch + "_done", *RESPECT,
               "cost.commander_route_labour"] + (["retry.done"] if retry else [])
    answer = ('"Then put them where I can drive the quarry. I want him looking up when your claws reach his throat."'
              if evil else '"I will draw him out. Your hunters stay under that wall until he turns. And no bait tied beneath the roof, Wenduag."')
    nodes.extend([
        terminal("plotted", "Arueshalae", answer + ' {n}You work the patrol timings into both lines. Arueshalae scratches out her exposed landing point and uses Wenduag\'s cover. Wenduag calls over the scouts who have offered to join the hunt.{/n} "Ground is mine. Height is hers. Copy both." {n}She makes each scout follow both lines with a finger.{/n}', success),
        terminal("refused", "Wenduag", '"Then give it to somebody else. I won\'t lose hunters because you can\'t choose a road." {n}She takes back her knife. The lookout remains another patrol\'s problem.{/n}',
                 (step + ".seen", step + ".refused", "unsettled"))])
    if not retry:
        nodes.append(terminal("blind", "Arueshalae", '{n}The scouts test the alley and scramble back under the wall when a signal flare rises from the roof. The lookout has seen the approach. Arueshalae leaves her unused aerial line on the map.{/n} "There. Now he knows where to watch."',
                              ("settle.seen", "settle.failed", "failed." + branch, "cost.commander_lookout_uncovered")))
    return add(step + "." + branch, "The route nobody walks", nodes,
               "settle.failed" if retry else "ready." + branch,
               requires=flags("failed." + branch) if retry else (),
               forbids=flags("retry.seen", "unsettled", "settle.done") if retry else flags("settle.seen"),
               delay=48 if retry else 0, evil=evil, protected=True, witness=step + ".seen")


def friend_steps():
    add("friend_wenduag", "The flier's mark", [
        page("start", "Wenduag", '{n}Wenduag is copying the approach for her hunters. The roof line still bears Arueshalae\'s mark.{/n} "They asked if I drew that too. She thinks I\'ll say yes."',
             c('"Let her mark the approach."', "her"), c('"Keep this to the operation."', "refused"), later()),
        terminal("her", "Wenduag", '{n}She calls her hunters back and pushes the map toward Arueshalae.{/n} "The roof line is hers. Watch her hands. If you run before she turns him, I\'ll leave you up there for the crows." {n}Arueshalae marks the turn on each copy. Wenduag watches her mouth while the hunters follow her finger.{/n} "Come back when they\'ve learned it. I want to see what else those wings can do."',
                 ("friend_wenduag.seen", *FRIEND_W)),
        terminal("refused", "Wenduag", '"Fine. She gets the roof. I get my hunt." {n}She rolls up the map without calling Arueshalae over.{/n}',
                 ("friend_wenduag.seen", "friend_wenduag.refused", "arc.declined"))],
        "settle.done", requires=flags("settle.evil_done", *RESPECT),
        forbids=flags("friend_wenduag.seen", "arc.declined"), delay=48, evil=True, arc_start=True)
    add("friend_arueshalae", "Under the wall", [
        page("start", "Arueshalae", '{n}Arueshalae tests the turn with two fingers walking across the map.{/n} "A man running in the open looks wonderfully helpless. That would bring our lookout down, wouldn\'t it?" {n}Wenduag\'s knife stops the little march.{/n} "Try it with someone else\'s hunters."',
             c('"Let her answer the ground correction."', "her"), c('"Keep this to the hunt."', "refused"), later()),
        terminal("her", "Arueshalae", '{n}She moves her fingers beneath the wall, following Wenduag\'s line, then calls the waiting hunters over.{/n} "Stay here until he looks at me. I can show him something worth coming down for." {n}She draws her landing mark inside the cover, beside Wenduag\'s.{/n} "There. Your little pack stays out of sight, and I get to watch you tear his throat out." {n}Wenduag taps the two marks with a claw. Arueshalae leaves hers where it is.{/n}',
                 ("friend_arueshalae.seen", *FRIEND_A)),
        terminal("refused", "Arueshalae", '"Only the lookout, then. How industrious we are." {n}She lifts her fingers off the map.{/n}',
                 ("friend_arueshalae.seen", "friend_arueshalae.refused", "arc.declined"))],
        "friend_wenduag.done", forbids=flags("friend_arueshalae.seen", "arc.declined"), delay=48, evil=True)


def intimacy():
    add("choice", "Their map", [
        page("start", "Wenduag", '{n}The copies are finished. Wenduag has kept the original beneath her hand. Arueshalae stays beside it while the scouts leave.{/n} "She keeps finding excuses to inspect my route."',
             c('[Leave them their map.]', "wenduag_answer"), c('"Keep this company at the Table."', "refused"), later()),
        page("wenduag_answer", "Wenduag", '{n}Arueshalae lifts the map out from under Wenduag\'s hand. A beat of her wings carries her beyond the hunter\'s reach. Wenduag rises, grinning.{/n} "Keep flying, pretty thing. I\'ll have armour against that mouth tonight. Then we\'ll hear what comes out of it when you aren\'t boasting."', c("Continue", "arueshalae_answer")),
        page("arueshalae_answer", "Arueshalae", '"Oh, I can boast with my mouth full." {n}She leans close enough for Wenduag to feel her breath and stops there, enjoying the hunter\'s fixed stare.{/n} "Get your armour. Then come after me. I want those claws on me."', c("Continue", "protection")),
        page("protection", "Narrator", '{n}The chapel can read a scroll over Wenduag. Until then, the map stays between them.{/n}',
             c('[Spend a Scroll of Death Ward: have the ward read over Wenduag and let them go.]', "threshold",
               requires=("arueshalae.ward_held",) + LIVE, remove_item=SCROLL,
               flags=flags("cost.ward_scroll", "ward.applied_wenduag")),
             c('"Keep the map; leave the rest tonight."', "no_contact")),
        page("threshold", "Wenduag", '{n}Wenduag returns with the ward cold on her skin. Arueshalae holds the map above her head, wings spreading. Wenduag steps inside their sweep and catches her by the belt. The succubus folds her wings around them and presses her mouth to Wenduag\'s.{/n} "Seven minutes. You spend one talking, I\'ll make you regret it." {n}Arueshalae laughs against her lips, then draws her toward the back stair. Wenduag pulls her through the door.{/n} {n}The map goes forgotten on the floor. Wenduag gets the succubus’s dress down off her shoulders with a hunter’s quick hands and her mouth follows, hard, down the throat to the breasts, claws raking light red lines along Arueshalae’s back that the demon arches into with a moan. \"Louder,\" Wenduag growls, and gets it. Arueshalae strips the hunter’s leathers away piece by piece, her wings spread wide round them both, grinning, hungry, her thighs already parting around Wenduag’s hip. Wenduag shoves her down on the narrow bed.{/n}',
             c("Continue", p("choice.explicit.1"))),
        page("after", "Arueshalae", '{n}They separate while the ward still holds. Arueshalae smooths her belt; Wenduag retrieves the map before the succubus can take it.{/n} "With my correction." {n}Wenduag bares her teeth and rolls up the map with both lines intact. They leave for separate sleeping places.{/n}',
             c("Continue", flags=flags("choice.seen", "choice.both_yes", "deed.wenduag_desire_answer", "deed.arueshalae_desire_answer"))),
        terminal("refused", "Wenduag", '"The map stays. The rest can wait." {n}She slides it out from under Arueshalae\'s hand.{/n}', ("choice.seen", "choice.declined", "arc.declined")),
        terminal("no_contact", "Arueshalae", '"A pity. I had something much better than a map to show her." {n}She straightens without touching Wenduag.{/n}', ("choice.seen", "choice.declined", "arc.declined")),
        # Appended slot: empty and filled forms both return to the same state producer.
        page(p("choice.explicit.1"), "Narrator", '{n}The lower-town map stays open while they take their argument elsewhere.{/n}', c("Continue", "after"))],
        "friend_arueshalae.done", requires=flags(*FRIEND_W, *FRIEND_A) + (
            "wenduag.harem.attitude.arueshalae.friend", "arueshalae.harem.attitude.wenduag.friend"),
        forbids=flags("choice.seen", "arc.declined"), delay=48, evil=True)
    add("morning", "The dawn route", [
        page("start", "Arueshalae", '{n}At opposite ends of the corner table, the two women check the map for the dawn patrol. Arueshalae adds an arrow over the ridge.{/n} "You left out the turn where I drive him toward you."',
             c('"Who owns the route now?"', "kept"), later()),
        terminal("kept", "Wenduag", '"Mine. She just can\'t keep her fingers off it." {n}Wenduag takes the map. Arueshalae lets her, leaving the aerial arrow plainly visible.{/n} "Bring it back tonight," {n}the succubus says. Wenduag bares her teeth and heads for her hunters; Arueshalae goes to inspect the roof.{/n}',
                 ("morning.seen", "morning.done"))], "choice.both_yes",
        requires=flags(*FRIEND_W, *FRIEND_A), forbids=flags("morning.seen"), delay=8, evil=True)


def register(payload, scenes, refs):
    """Called before household integration; queue entries without duplicating builds."""
    household.ENTRIES[:] = [s for s in household.ENTRIES if not s["Id"].startswith(PREFIX)]
    derived = payload.setdefault("Derived", {})
    negative = payload.setdefault("DerivedForbids", {})
    # The Table helper reads these controller-owned hooks. S09 adds no enmity
    # or reconciliation producer; declare its two edges like household.integrate.
    pending = payload.setdefault("PendingHooks", [])
    for a, b in (PAIR, tuple(reversed(PAIR))):
        for key in (household.enmity(a, b), a + ".harem.reconciled." + b):
            if key not in pending:
                pending.append(key)
    # Table entries cannot carry ContactUnit (Rules.Validate). Use the routes'
    # current companion/body placements, independently of romance eligibility.
    derived[p("body.wenduag")] = [["wenduag.in_party", "wenduag.present_now"],
        ["wenduag.trickster.returned", "wenduag.present_now", "trickster.now", p("body.wenduag.street")]]
    derived[p("body.wenduag.street")] = [["wenduag.presence.route_open"]]
    negative[p("body.wenduag.street")] = ["wenduag.presence.failed", "wenduag.trickster.echo.abyss.ready"]
    derived[p("body.arueshalae.good")] = [["arueshalae.recruited_drezen", "arueshalae.native_alive"],
                                         ["arueshalae.recruited_redoubt", "arueshalae.native_alive"]]
    derived[p("body.arueshalae.evil")] = [["arueshalae.evil_recruited", p("body.arueshalae.native_evil")]]
    derived[p("body.arueshalae.native_evil")] = [["arueshalae.present_now"]]
    negative[p("body.arueshalae.native_evil")] = ["arueshalae.evil_dead"]
    # The lair is not Drezen. Only the current arcade/awning placements can
    # supply a returned fallen body here; a failed placement supplies nothing.
    for key in (arueshalae_trickster.TAVERN_PRESENCE, arueshalae_trickster.YARD_PRESENCE):
        presence = arueshalae_trickster.PRESENCES[key]
        local = p("body." + key)
        derived[local] = [list(presence["Requires"]) + ["arueshalae.present_now", "arueshalae.presence.route_open"]]
        negative[local] = list(presence["Forbids"]) + [key + ".failed"]
        if presence.get("RequiresAnyGroups"):
            for index, group in enumerate(presence["RequiresAnyGroups"]):
                any_key = local + ".any." + str(index)
                derived[any_key] = [[flag] for flag in group]
                derived[local][0].append(any_key)
        derived[p("body.arueshalae.evil")].append([local])
    for branch, personality in (("good", "redeemed"), ("evil", "corrupted")):
        derived[p("ready." + branch)] = [["wenduag.harem.eligible", "arueshalae.harem.eligible", *LIVE, "arueshalae." + personality]]
    negative[p("ready.good")] = ["arueshalae.corrupted"]
    for a, b, friendship in (("wenduag", "arueshalae", FRIEND_W), ("arueshalae", "wenduag", FRIEND_A)):
        base = a + ".harem.attitude." + b + "."
        derived[base + "rival"] = [list(flags("settle.seen"))]
        derived[base + "respect"] = [list(flags(*RESPECT))]
        derived[base + "friend"] = [list(flags("settle.evil_done", *friendship)) + ["arueshalae.corrupted"]]
        derived[base + "lover"] = [list(flags("settle.evil_done", *FRIEND_W, *FRIEND_A, "choice.both_yes",
                                                 "deed.wenduag_desire_answer", "deed.arueshalae_desire_answer",
                                                 "cost.ward_scroll", "ward.applied_wenduag")) + ["arueshalae.corrupted"]]
        for stage in ("rival", "respect", "friend", "lover"):
            payload.setdefault("DerivedOpenRoutes", {})[base + stage] = list(PAIR)
        negative[base + "rival"] = [base + s for s in ("respect", "friend", "lover")]
        negative[base + "respect"] = [base + s for s in ("friend", "lover")]
    for evil in (False, True):
        settlement(evil)
        settlement(evil, retry=True)
    friend_steps()
    intimacy()
