"""History-aware copies of the harbor visits after the earned Trickster bridge.

Unregistered author draft. Native parent, Gift and seen-cue bindings are read-only.
The hosted dreams are the bridge's authored mechanism, not a replacement Gift.
All romantic participants are unrelated adults; intimacy is graphic and explicit.
Root must exclude original harbor scenes when bridge readiness selects this family.
Original completion aliases preserve the existing progress and ending contracts.
"""
from copy import deepcopy

from story_format import c, n
from storylines import nocticula_continuation as original


HISTORIES = {
    "new": "noct.join.history_new",
    "refused": "noct.join.history_refused",
    "prior": "noct.join.history_prior",
}
BRIDGE = (
    "noct.join.harbor_variant_ready", "noct.join.recurring_dreams_accepted",
    "noct.join.exit_demonstrated", "noct.join.a_chosen_shore_done",
)
RELATIONSHIP = deepcopy(original.RELATIONSHIP)
RELATIONSHIP.update(
    Description="Nocticula has invited me to investigate a hidden harbor through the meetings we chose together.",
    Guidance="After completing the Trickster correspondence and accepting the hosted meetings, rest in Drezen to hear Nocticula's harbor proposal. Her invitation does not accept an earlier refused offer, restore a lost Gift or settle the Worldwound. Each undertaking and private invitation can still be declined.",
)


def replace(page, before, after):
    """Fail visibly if the donor prose changed underneath this adaptation."""
    assert page["Text"].count(before) == 1, (page["Id"], before)
    page["Text"] = page["Text"].replace(before, after)


def adapt(source, history, gift=None):
    current = deepcopy(source)
    original_id = source["Id"]
    current["Id"] = original_id + ".acquired." + history + ("." + gift if gift else "")
    current["Requires"] = [x for x in current["Requires"] if x not in (
        "noct.parent_active", "noct.parent_agreement_seen", "noct.gift")]
    current["Requires"] += [*BRIDGE, HISTORIES[history]]
    current["Forbids"] = [x for x in current["Forbids"] if x != "noct.parent_rejected"]
    current["Forbids"] += [original_id, *(v for k, v in HISTORIES.items() if k != history)]
    if source["Owner"] == "Memory":
        current["Requires"] += ["trickster", "noct.acq.renewed_agreement"]
        current["Forbids"] += ["noct.acq.council_fight", "noct.acq.closed", "noct.join.closed"]
    if gift == "renewed":
        current["Requires"].append("noct.acq.gift_renewed")
    elif gift == "original":
        current["Requires"].append("noct.gift")
        current["Forbids"].append("noct.acq.gift_renewed")
    elif gift == "absent":
        current["Forbids"] += ["noct.gift", "noct.acq.gift_renewed"]
    pages = {p["Id"]: p for p in current["Nodes"]}

    if original_id == "noct.unlit_quay":
        replace(pages["start"],
            "And this is not an improvement to the accommodation I promised you.",
            "And this is not a palace door hidden inside the invitation you accepted.")
        # The bridge's first question gets an answer before this new undertaking.
        first = pages["start"]["Choices"].pop(0)
        for name, flag, answer, text in (
            ("passengers", "noct.join.first_question_passengers",
             '"I asked you to bring the travelers\' accounts. Whose voice am I going to hear?"',
             '''"The returned passenger first. I kept the missing names too. You need not look so ready to accuse me of losing them."
{n}She takes a folded strip from beneath the sailcloth. Three names cross it in different hands. The last has been written twice; somebody disputed its spelling.
You touch that correction. Nocticula watches the movement.{/n}
"You can ask about him. I have not brought you enough to pretend I know where he is."
"And what do you want from the man doing the asking?"
{n}She draws the strip back slowly enough that her fingers pass over yours.{/n}'''),
            ("profit", "noct.join.first_question_profit",
             '"I asked who profits. Have you brought a price or a man who thinks he can name one?"',
             '''"A man. Prices become more informative when their owners have to explain them."
{n}She lays the sailcloth over your wrist, fitting the embroidered flower against your pulse as though considering a bracelet.{/n}
"He expects payment for his story. You expect a return for useful advice. I shall have an expensive evening if neither of you learns to be useful."
"You agreed to hear what I wanted."
"I am hearing it. I have not offered you a share of a road neither of us understands."
{n}She lifts the cloth away. Its light pressure remains in your attention longer than it did against your skin.{/n}
"Then tell me what sort of adviser you mean to purchase."'''),
        ):
            pages["start"]["Choices"].insert(0, c(answer, "first_" + name, requires=(flag,)))
            current["Nodes"].append(n("first_" + name, "Nocticula", text,
                c(first["Text"], first["Next"]), portrait="Nocticula"))
        pages["council"]["Choices"] = deepcopy(pages["start"]["Choices"][:2])
        if history != "prior":
            reply = ('''"Your refusal remains a refusal. I am not offering to make it disappear beneath an attractive evening. You would notice, and then I should have to listen to you explain why you noticed."
"A terrible price."
"One I have already paid. The letters are ours. The Worldwound is still a disagreement."'''
                if history == "refused" else
                '''"The letters continue. You have promised me neither the Worldwound nor obedience, and I have offered you no solution to either. Try to remember that when you find yourself enjoying my company."
"I might enjoy it more for remembering."
"Then you have discovered an inexpensive way to improve your evening."''')
            replace(pages["offer"],
                '"Continues. This is not a new price secretly added to it. The Worldwound remains the price we discussed, and you are still quite capable of disappointing me about that."', reply)
            replace(pages["decline_undertaking"],
                '"I will take this elsewhere. Our earlier agreement remains precisely what it was. You have declined an invitation, not renegotiated the Worldwound."',
                '"I will take this elsewhere. Send me a better subject in your next letter. You have declined this undertaking; you have not settled the much larger thing we still disagree about."')

    withdrawal = pages.get("withdraw_undertaking")
    if withdrawal and history != "prior":
        if '"And our earlier bargain?"' in withdrawal["Text"]:
            replace(withdrawal,
                '"And our earlier bargain?"\n"Was not about a harbor. I have not forgotten its terms because you have tired of these."',
                '"The letters?"\n"If you have something worth saying. Bore me and I shall stop reading, and you will never know which letter it was."')
        else:
            replace(withdrawal,
                '"Our earlier bargain still stands too."\n"I did not confuse it with an evening\'s company. Do me the courtesy of remembering that."',
                '"I would still write to you."\n"Then write. I shall decide how to answer when I have read something besides your departure."')
        withdrawal["Choices"][0]["Text"] = '[End these harbor meetings. Keep the personal correspondence without a new invitation.]'
    if withdrawal and original_id == "noct.counterseal":
        # The new creditor dispute is still work, despite the older late-exit text.
        for choice in pages["start"]["Choices"]:
            if choice.get("Next") == "withdraw_undertaking":
                choice["Text"] = '"I will not take on this new claim. I am ending the harbor meetings."'
        replace(withdrawal, '"I invited you because the business was settled. You need not explain the distinction to me."',
                '"A claimant arrives, and you discover that our business ought to have ended yesterday. How convenient."')

    if original_id == "noct.her_own_face":
        replace(pages["start"],
            '"You have used dreams to offer me things I wanted," {n}you say.{/n} "Does this room mean you know what I want tonight?"',
            '"You have arranged another room around a question," {n}you say.{/n} "Does that mean you know what I want tonight?"')
        pages["start"]["Choices"][0]["Text"] = '"I wanted an evening in which I could look at you without pretending to study the evidence."'
        replace(pages["face"],
            '"That is either a very good compliment or a remarkably provincial objection to variety."\n"You may choose the interpretation you like."\n"I usually do. It saves time."',
            '"You have been remarkably diligent about studying the wrong parts of the room."\n"I did not hear you complain."\n"I was enjoying your attempts to look industrious."')
        replace(pages["face"],
            'When she kisses you, she does not change her shape. The kiss lasts long enough for you to answer, then she draws back with a pleased, almost challenging glance.',
            'She catches your hand before you can turn it over and study hers. Her kiss gives you something else to attend to. It lasts long enough for you to answer, then she draws back with a pleased, almost challenging glance.')
        replace(pages["face"], 'There are disadvantages to recognizing me.',
            'There are disadvantages to knowing my habits.')
        if gift == "renewed":
            replace(pages["start"], 'Your gift has not gone away.', 'You have given me your power again. I have not forgotten what that permits.')
            replace(pages["start"], '"No," {n}she says.{/n} "It has not."', '"Nor have I," {n}she says.{/n} "You should be suspicious if I pretended otherwise."')
        elif gift == "absent":
            replace(pages["start"],
                '"You could make the invitation rather difficult to refuse. Your gift has not gone away."\n"No," {n}she says.{/n} "It has not."',
                '"There is no gift between us tonight. There is still a room which exists because you want me in it."\n"And a door you asked me to open. I opened it because I wanted you through it. Try not to make me regret the hinges."')
        if history != "prior":
            replace(pages["start"],
                '"You should remember it. Particularly if you begin imagining that a pleasant evening has altered our older bargain."',
                '"You should remember whom you are visiting. Particularly if you begin imagining that wanting you has made me safe."')
        elif gift == "absent":
            replace(pages["start"],
                '"You should remember it. Particularly if you begin imagining that a pleasant evening has altered our older bargain."',
                '"You should remember it. The loss of a privilege did not make me harmless, or erase the older bargain. Neither will a pleasant evening."')

    if original_id == "noct.second_door":
        if history != "prior":
            replace(pages["future"], 'Our original bargain still has its own terms.',
                'We have chosen company, and we have done useful work. You have not bought my agreement to your larger ambitions.')
            replace(pages["limited"], 'Our earlier arrangement remains what it was.',
                'Then the letters remain. The rooms I make are for guests who come to them.')
            pages["limited"]["Choices"][0]["Text"] = '[Keep the correspondence. Decline the larger invitation.]'
            pages["limited"]["Choices"][0]["Set"].append("noct.join.letters_after_harbor")
        replace(pages["power"],
            'A minor courtier has been selling introductions to me. I thought you might enjoy deciding what he ought to receive for his trouble.',
            'A minor courtier has sold the same balcony to three guests for an execution none of them arranged. After Salven, one might have hoped for a little imagination in choosing a fraud. I thought you might enjoy deciding who ought to receive the best view.')
        replace(pages["power"], 'Send him an introduction to his creditors.',
            'Seat his creditors on the balcony. Let him explain why the entertainment has been canceled.')

    if original_id == "noct.ending_alliance" and history != "prior":
        replace(pages["end"], 'The older Worldwound bargain still awaited its reckoning.',
            'They had made no Worldwound bargain in those rooms. The larger disagreement still awaited its answer.')
    if original_id == "noct.ending_limit" and history != "prior":
        replace(pages["end"], 'The Commander kept the earlier arrangement and declined to enlarge it.',
            'The Commander kept their personal correspondence and declined further private rooms or a larger alliance.')

    for page in current["Nodes"]:
        for choice in page["Choices"]:
            if not choice.get("Next") and not choice.get("Check") and not choice["Abort"]:
                choice["Set"].append(original_id)
    return current


SCENES = [adapt(source, history, gift)
          for source in original.SCENES
          for history in HISTORIES
          for gift in (("absent", "original", "renewed") if source["Id"] == "noct.her_own_face" else (None,))]


def validate():
    """Count selected played paths after an explicitly supplied bridge fixture."""
    import runpy
    from functools import cache
    from itertools import product
    from pathlib import Path
    from storylines.nocticula_trickster_acquisition import allowed
    from storylines.nocticula_trickster_concession import outcomes
    words = cache(runpy.run_path(str(Path(__file__).resolve().parents[1] / "tools/measure-story-content.py"))["words"])
    assert len({s["Id"] for s in SCENES}) == len(SCENES)
    donor_snapshot = deepcopy(original.SCENES)
    native = set(original.ETUDES) | set(original.SEEN_CUES)
    native |= {"noct.acq.gift_renewed", "noct.acq.original_gift_completed"}
    for s in SCENES:
        assert len({p["Id"] for p in s["Nodes"]}) == len(s["Nodes"])
        for p in s["Nodes"]:
            for choice in p["Choices"]:
                assert not native.intersection(choice["Set"])
                assert not (choice.get("Check") and choice.get("Next"))
    results = {}
    closure_count = 0
    ending_checks = 0
    for history in HISTORIES:
        base = {*BRIDGE, HISTORIES[history], "trickster", "noct.acq.renewed_agreement"}
        gift_states = (set(), {"noct.gift"}, {"noct.acq.gift_renewed"},
                       {"noct.gift", "noct.acq.gift_renewed"})
        faces = [s for s in SCENES if s["Id"].startswith("noct.her_own_face.acquired." + history)]
        for gift_state in gift_states:
            eligible = [s for s in faces if allowed(s, base | gift_state | {"noct.dessa_safe"})]
            assert len(eligible) == 1
            assert not any(allowed(s, base | gift_state | {"noct.dessa_safe", "noct.her_own_face"}) for s in faces)
            for chosen in ("company", "alliance", "limit"):
                for dead, changed, ascent, sacrifice in product((False, True), repeat=4):
                    state = base | gift_state | {"noct.complete", "noct.chosen_" + chosen}
                    for active, flag in ((dead, "noct.dead"), (changed, "inhuman"),
                                         (ascent, "ascended"), (sacrifice, "sacrifice")):
                        if active:
                            state.add(flag)
                    eligible = [s for s in SCENES if s["Owner"] == "Epilogue"
                                and s["Id"].endswith(".acquired." + history) and allowed(s, state)]
                    expected = "death" if dead else "changed" if changed else "ascent" if ascent else "sacrifice" if sacrifice else chosen
                    assert len(eligible) == 1 and eligible[0]["Id"].startswith("noct.ending_" + expected + ".")
                    ending_checks += 1
        aeon = next(s for s in SCENES if s["Id"] == "noct.ending_aeon.acquired." + history)
        assert allowed(aeon, base | {"noct.complete"})
        assert not allowed(aeon, base)
    for history in HISTORIES:
        for gift in ("absent", "original", "renewed"):
            # The acquired prior-pact opening concerns lost original patronage.
            if history == "prior" and gift == "original":
                continue
            for question, witnesses in product(("passengers", "profit"), ((),
                    ("noct.parent_ambition_heard",), ("noct.socoth_plan_exposed",),
                    ("noct.parent_ambition_heard", "noct.socoth_plan_exposed"))):
                base = {*BRIDGE, HISTORIES[history], "trickster", "noct.acq.renewed_agreement",
                        "noct.join.first_question_" + question, *witnesses}
                if history == "refused":
                    base.add("noct.parent_rejected")
                elif history == "prior":
                    base.update(("noct.parent_active", "noct.acq.original_gift_completed"))
                if gift != "absent":
                    base.add("noct.gift" if gift == "original" else "noct.acq.gift_renewed")
                family = [s for s in SCENES if ".acquired." + history in s["Id"] and (
                    not s["Id"].startswith("noct.her_own_face") or s["Id"].endswith("." + gift))]
                visits = [s for s in family if s["Owner"] == "Memory"]
                endings = [s for s in family if s["Owner"] == "Epilogue" and s["Id"].split(".")[1] in (
                    "ending_company", "ending_alliance", "ending_limit")]
                states = {frozenset(base): (0, 0)}
                assert len([s for s in SCENES if s["Id"].startswith("noct.unlit_quay.") and allowed(s, base)]) == 1
                for missing in BRIDGE:
                    assert not any(allowed(s, base - {missing}) for s in visits)
                for other in HISTORIES.values():
                    if other != HISTORIES[history]:
                        assert not any(allowed(s, base | {other}) for s in visits)
                for s in visits:
                    original_id = s["Id"].split(".acquired.")[0]
                    assert not allowed(s, base | {original_id})
                    for page in s["Nodes"]:
                        for choice in page["Choices"]:
                            if choice["Abort"]:
                                assert original_id not in choice["Set"]
                # Preserve only flags tested later, retaining min/max prefixes.
                for index, s in enumerate(visits):
                    later = visits[index + 1:] + endings
                    used = set()
                    for future in later:
                        for item in (future, *(c for p in future["Nodes"] for c in p["Choices"])):
                            used.update(item["Requires"] + item["Forbids"])
                    updated = {}
                    for state, (low, high) in states.items():
                        assert allowed(s, state), (s["Id"], state)
                        for final, count in outcomes(s, state, words):
                            if "noct.closed" in final:
                                closure_count += 1
                                assert not any(allowed(future, final) for future in visits[index + 1:])
                                continue
                            assert s["Id"].split(".acquired.")[0] in final
                            key = frozenset(final & used)
                            bounds = (low + count, high + count)
                            old = updated.get(key, bounds)
                            updated[key] = (min(old[0], bounds[0]), max(old[1], bounds[1]))
                    states = updated
                lows, highs = [], []
                for state, (low, high) in states.items():
                    eligible = [s for s in endings if allowed(s, state)]
                    assert len(eligible) == 1
                    for final, count in outcomes(eligible[0], state, words):
                        lows.append(low + count); highs.append(high + count)
                results[history + "/" + gift + "/" + question + "/" + str(len(witnesses)) + ":" + ",".join(witnesses)] = dict(minimum=min(lows), maximum=max(highs))
    assert original.SCENES == donor_snapshot
    return dict(delivery_scenes=len(SCENES), unique_visits=24, unique_recollections=8,
                fixtures=len(results), closure_paths=closure_count, ending_gate_checks=ending_checks, selected_words=results,
                minimum=min(x["minimum"] for x in results.values()),
                maximum=max(x["maximum"] for x in results.values()),
                status="author draft; unregistered; independent review and runtime verification required")


if __name__ == "__main__":
    import hashlib
    import json
    from pathlib import Path
    result = validate()
    result["sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper()
    print(json.dumps(result, indent=2))
