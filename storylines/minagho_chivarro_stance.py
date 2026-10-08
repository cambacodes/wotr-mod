"""Authored partner-stance additions for Minagho and Chivarro only.

Canon anchors: Chivarro_dialogue/Cue_0119 (7b8ff644c3d1e6848bef78edcab65193),
Cue_0097 (d8b51192f7ce23440bfb22b7d28e03d0), Cue_0091
(6098d97e435e0694493ebaf7de128c51). Their craving and violence survive the
Commander's invitation. These additions use existing mornings and arrivals;
they grant no return, presence, service release, or new eligibility.
"""
from copy import deepcopy

from story_format import c, n, p, scene

REL = "minagho_chivarro"
P = REL + ".trickster."
S = REL + ".partner_stance."
STATE = REL + ".partner_state."
SHARE, EXCLUSIVE, SECRET = S + "share", S + "exclusive", S + "secret"
EXPOSED, COOLED = S + "exposed", S + "cooled"
TARGET_M, TARGET_C = S + "minagho", S + "chivarro"
RET_M, RET_C = P + "returned_minagho", P + "returned_chivarro"
MIN_IN, CH_IN = P + "minagho_in", P + "chivarro_in"
SENT_BACK, DECL_M, DECL_C = P + "chivarro_sent_back", P + "declined_minagho", P + "chivarro_declined"
COMPLETE, CLOSED = "minachiv.complete", "minachiv.closed"

# Observers, not producers: historical returns do not themselves stage a body.
STATES = {
    STATE + "minagho.dead": [["minagho.dead", "!" + RET_M]],
    STATE + "minagho.present": [
        [MIN_IN, "!" + DECL_M, "!" + STATE + "minagho.dead"],
        ["minachiv.reunion_history", "!minagho.dead", "!" + DECL_M]],
    STATE + "minagho.distant": [
        ["minagho.spared.latched", "!" + STATE + "minagho.dead", "!" + STATE + "minagho.present"],
        [RET_M, "!" + STATE + "minagho.present"],
        [DECL_M, "!minagho.dead", "!" + STATE + "minagho.present"]],
    STATE + "minagho.unknown": [["!" + STATE + "minagho.dead", "!" + STATE + "minagho.present", "!" + STATE + "minagho.distant"]],
    STATE + "chivarro.dead": [["chivarro.dead_confirmed", "!" + RET_C, "!" + P + "chivarro_deposit"]],
    STATE + "chivarro.cellar": [["chivarro.dead_confirmed", P + "chivarro_deposit", "!" + RET_C]],
    STATE + "chivarro.present": [
        [CH_IN, "!" + SENT_BACK, "!chivarro.dead", "!" + STATE + "chivarro.dead", "!" + STATE + "chivarro.cellar"],
        [CH_IN, RET_C, "!" + SENT_BACK],
        ["minachiv.reunion_history", "!chivarro.dead", "!" + SENT_BACK]],
    STATE + "chivarro.distant": [
        [SENT_BACK, "!chivarro.dead", "!" + STATE + "chivarro.present"],
        [SENT_BACK, RET_C, "!" + STATE + "chivarro.present"],
        [DECL_C, "!chivarro.dead", "!" + STATE + "chivarro.present"],
        ["chivarro.searching", "!chivarro.dead", "!" + STATE + "chivarro.present"],
        ["chivarro.exiled", "!chivarro.dead", "!" + STATE + "chivarro.present"]],
    STATE + "chivarro.unknown": [["!" + STATE + "chivarro.dead", "!" + STATE + "chivarro.cellar", "!" + STATE + "chivarro.present", "!" + STATE + "chivarro.distant"]],
}
for woman in ("minagho", "chivarro"):
    STATES[STATE + woman + ".alive"] = [[STATE + woman + ".present"], [STATE + woman + ".distant"]]
STATES[STATE + "chivarro.alive"].append([STATE + "chivarro.cellar"])
for woman in ("minagho", "chivarro"):
    STATES[STATE + woman + ".possibly_alive"] = [[STATE + woman + ".alive"], [STATE + woman + ".unknown"]]

# Preserve the existing generated eligibility exits before appending stance choices.
# These are the integration branch guards, not new requirements.
_SAVED_GUARDS = {('minachiv.before_the_last_road', 'minagho'): ({0: ('minagho_chivarro.outcome.eligible',),
                                                 1: ('minagho_chivarro.outcome.eligible',)},
                                                (('minagho_chivarro.outcome.eligible',),)),
 ('minachiv.before_the_last_road', 'together'): ({0: ('minagho_chivarro.outcome.eligible',)},
                                                 (('minagho_chivarro.outcome.eligible',),)),
 ('minachiv.before_the_last_road', 'friendship'): ({0: ('minagho_chivarro.outcome.eligible',),
                                                    1: ('minagho_chivarro.outcome.eligible',),
                                                    2: ('minagho_chivarro.outcome.eligible',)},
                                                   (('minagho_chivarro.outcome.eligible',),)),
 ('minachiv.before_the_last_road', 'open'): ({0: ('minagho_chivarro.outcome.eligible',)},
                                             (('minagho_chivarro.outcome.eligible',),)),
 ('minachiv.before_the_last_road', 'service'): ({0: ('minagho_chivarro.outcome.eligible',),
                                                 1: ('minagho_chivarro.outcome.eligible',)},
                                                (('minagho_chivarro.outcome.eligible',),)),
 ('minagho_chivarro.trickster.after.before_the_last_road', 'terms'): ({0: ('minagho_chivarro.outcome.eligible',
                                                                           'trickster.now')},
                                                                      (('minagho_chivarro.outcome.eligible',),
                                                                       ('trickster.now',))),
 ('minagho_chivarro.trickster.after.before_the_last_road_letter', 'start'): ({0: ('minagho_chivarro.outcome.eligible',
                                                                                  'trickster.now')},
                                                                             (('minagho_chivarro.outcome.eligible',),
                                                                              ('trickster.now',))),
 ('minagho_chivarro.trickster.alone.chivarro', 'terms'): ({0: ('minagho_chivarro.outcome.chivarro_open',),
                                                           2: ('minagho_chivarro.outcome.chivarro_open',)},
                                                          (('minagho_chivarro.outcome.chivarro_open',),)),
 ('minagho_chivarro.trickster.alone.chivarro_letter', 'start'): ({0: ('minagho_chivarro.outcome.chivarro_open',)},
                                                                 (('minagho_chivarro.outcome.chivarro_open',),)),
 ('minagho_chivarro.trickster.alone.minagho', 'terms'): ({0: ('minagho_chivarro.outcome.minagho_open',)},
                                                         (('minagho_chivarro.outcome.minagho_open',),)),
 ('minagho_chivarro.trickster.alone.minagho_spared', 'terms'): ({0: ('minagho_chivarro.outcome.minagho_open',)},
                                                                (('minagho_chivarro.outcome.minagho_open',),)),
 ('minagho_chivarro.trickster.alone.minagho_letter', 'start'): ({0: ('minagho_chivarro.outcome.minagho_open',),
                                                                 2: ('minagho_chivarro.outcome.minagho_open',),
                                                                 4: ('minagho_chivarro.outcome.minagho_open',),
                                                                 6: ('minagho_chivarro.outcome.minagho_open',)},
                                                                (('minagho_chivarro.outcome.minagho_open',),)),
 ('minagho_chivarro.trickster.after.when_it_scars', 'pair'): ({0: ('minagho_chivarro.outcome.eligible',
                                                                   'trickster.now')},
                                                              (('minagho_chivarro.outcome.eligible',),
                                                               ('trickster.now',))),
 ('minagho_chivarro.trickster.alone.minagho_when_it_scars', 'min'): ({0: ('minagho_chivarro.outcome.minagho_open',)},
                                                                     (('minagho_chivarro.outcome.minagho_open',),)),
 ('minagho_chivarro.trickster.alone.minagho_when_it_scars', 'killer_min'): ({0: ('minagho_chivarro.outcome.minagho_open',)},
                                                                            (('minagho_chivarro.outcome.minagho_open',),)),
 ('minagho_chivarro.trickster.alone.chivarro_when_it_scars', 'chv'): ({0: ('minagho_chivarro.outcome.chivarro_open',)},
                                                                      (('minagho_chivarro.outcome.chivarro_open',),)),
 ('minagho_chivarro.trickster.epilogue.commit', 'start'): ({0: ('minagho.life.house',
                                                                'minagho_chivarro.outcome.eligible'),
                                                            2: ('minagho.life.reunited',
                                                                'minagho_chivarro.outcome.eligible')},
                                                           (('minagho_chivarro.outcome.eligible',),)),
 ('minagho_chivarro.trickster.epilogue.commit', 'pair'): ({0: ('minagho_chivarro.outcome.eligible',)},
                                                          (('minagho_chivarro.outcome.eligible',),))}

def _saved_guards(pages):
    for page in pages:
        for node in page["Nodes"]:
            row = _SAVED_GUARDS.get((page["Id"], node["Id"]))
            if not row:
                continue
            requirements, exits = row
            for index, flags in requirements.items():
                node["Choices"][index]["Requires"].extend(f for f in flags if f not in node["Choices"][index]["Requires"])
            for flags in exits:
                node["Choices"].append(c("[Leave.]", forbids=flags, abort=True))


def continuity():
    return [
        p('{n}Minagho was dead. Chivarro kept her letters, every insult intact, and sold none of them.{/n}', requires=(STATE + "minagho.dead",)),
        p('{n}Minagho was alive. She kept her own keys, chose her own visitors, and gutted the ones she had not chosen.{/n}', requires=(STATE + "minagho.present",)),
        p('{n}Minagho kept her distance. The second chair still had her knife in it.{/n}', requires=(STATE + "minagho.distant",)),
        p('{n}Nobody knew where Minagho had gone. Chivarro kept her letters, and read every rumour of her out of every head that came down the stair.{/n}', requires=(STATE + "minagho.unknown",)),
        p('{n}Chivarro was dead. Minagho kept her old reply, insults and all, and corrected anyone who misquoted it.{/n}', requires=(STATE + "chivarro.dead",)),
        p('{n}Chivarro was still in Herrax\'s cellar, alive under a dead woman\'s name. The deposit had bought the substitution, not the key. Herrax still held it, and enjoyed holding it.{/n}', requires=(STATE + "chivarro.cellar",)),
        p('{n}Chivarro was alive. The place beside her was Minagho\'s, and anyone who forgot it was reminded.{/n}', requires=(STATE + "chivarro.present",)),
        p('{n}Chivarro stayed away from their table. Her last reply was mostly insults, and promised the Commander nothing.{/n}', requires=(STATE + "chivarro.distant",)),
        p('{n}There was no sure word of Chivarro: no body, no answer and no bill, which was the most alarming part.{/n}', requires=(STATE + "chivarro.unknown",)),
        p('{n}Minagho had been stolen back from Baphomet\'s brand, and never once said thank you for it.{/n}', requires=(RET_M, STATE + "minagho.alive")),
        p('{n}Chivarro had been bought out of Herrax\'s cellar. She still wanted the house that had sold her to suffer for it.{/n}', requires=(RET_C, STATE + "chivarro.alive")),
        p('{n}Minagho and Chivarro stayed lovers. Nothing the Commander did in either bed ever came between them, though the Commander was welcome to keep trying.{/n}', requires=(STATE + "minagho.alive", STATE + "chivarro.alive")),
        p('{n}Chivarro\'s service was still the Commander\'s on paper. Her bed was not. Minagho made sure the Commander understood the difference, once, with a knife.{/n}', requires=(COOLED, "minachiv.future_chivarro_service")),
        p('{n}Chivarro\'s service was still the Commander\'s. Refusing the Commander\'s demand had not bought her out of it, and she never let the Commander forget which of the two had been refused.{/n}', requires=(COOLED, P + "chivarro_owned"), forbids=(P + "bill_burned",)),
        p('{n}Chivarro\'s service was never released. Her bed was shut to the Commander; Minagho\'s place in it was not.{/n}', requires=(COOLED, P + "kept_in_service"), forbids=(P + "bill_burned", P + "chivarro_owned")),
        p('{n}The Commander had taken the terms on offer: a bed, an invitation, and the other woman\'s place kept on pain of disembowelment.{/n}', requires=(SHARE,)),
        p('{n}The Commander had demanded one of them alone. They answered together, and the invitations to bed ended there.{/n}', requires=(EXCLUSIVE,)),
        p('{n}At the last meeting the affair was still a secret, and the other woman had still not been told. Nobody ever asked her whether she already knew.{/n}', requires=(SECRET,), forbids=(EXPOSED,)),
        p('{n}When the affair came out, the Commander was thrown down the stair half-dressed. The invitations stopped.{/n}', requires=(SECRET, EXPOSED)),
    ]


def _node(id, speaker, text, *answers):
    return n(id, speaker, text, *answers, portrait=speaker if speaker in ("Minagho", "Chivarro") else "")


def _discovery(nodes, suffix="", target=None, returned=False, at_meeting=False):
    """Only called after an existing meeting/morning has established both bodies."""
    entry = "stance_discovery" + suffix
    added = [
        _node(entry, "Narrator", ('{n}They have barely finished speaking when the returned woman catches the familiar scent on your collar. She turns toward her lover. Neither of you answers quickly enough.{/n}' if returned else '{n}The other woman arrives as you finish speaking. She catches her lover\'s scent on your collar and looks at the hand still resting on your arm. Neither of you answers quickly enough.{/n}' if at_meeting else '{n}At dawn, the latch lifted before either of you could answer the knock. The woman at the door saw the discarded clothes, then the hand still resting on your bare waist.{/n}'),
              c("Continue", entry + "_chivarro", requires=(TARGET_M,)),
              c("Continue", entry + "_minagho", forbids=(TARGET_M,))),
        _node(entry + "_chivarro", "Chivarro", ('"You piece of shit. Both of you." {n}Chivarro holds out a hand for the room key.{/n} "You could have asked me. Instead you waited until I was out of the way to start fucking behind my back. Give me the key, honey. Your visits are over."' if returned or at_meeting else '"You piece of shit. Both of you." {n}Chivarro takes the room key off the table.{/n} "You could have asked me. Instead you made me the last woman in my own house to know who was fucking whom. Get dressed, honey. You are leaving."'),
              c('"Minagho?"', entry + "_minagho_answers")),
        _node(entry + "_minagho_answers", "Minagho", '{n}Minagho lets go of you.{/n} "I wanted the secret. I enjoyed it." {n}Her mouth twists.{/n} "But I am not giving her up to keep you. Find another bed, Golarian."',
              c("[Leave.]", flags=(EXPOSED, COOLED, CLOSED))),
        _node(entry + "_minagho", "Minagho", ('{n}Minagho draws your dagger from its sheath. She catches your belt and cuts it free, letting it fall with the scabbard.{/n} "Chivarro. Tell me you did not let this idiot think I would thank you for lying to me."' if returned or at_meeting else '{n}Minagho draws a dagger from the clothes on the floor. She drives it through your belt into the door.{/n} "Chivarro. Tell me you did not let this idiot think I would thank you for lying to me."'),
              c("Continue", entry + "_chivarro_answers")),
        _node(entry + "_chivarro_answers", "Chivarro", ('"I liked having something you did not know, honey." {n}Chivarro takes the fallen belt and presses it into your hand.{/n} "You have had your night, Commander. She stays. You go. And if Herrax asks about us, remember how much worse I could have made this."' if returned or at_meeting else '"I liked having something you did not know, honey." {n}Chivarro rises and throws your shirt at you.{/n} "You have had your night, Commander. She stays. You go. And if Herrax asks about us, remember how much worse I could have made this."'),
              c("[Leave.]", flags=(EXPOSED, COOLED, CLOSED))),
    ]
    if target:
        arriving = "chivarro" if target == "minagho" else "minagho"
        answering = "minagho" if target == "minagho" else "chivarro"
        added[0]["Choices"] = [c("Continue", entry + "_" + arriving)]
        added = [x for x in added if x["Id"] in {entry, entry + "_" + arriving, entry + "_" + answering + "_answers"}]
    nodes.extend(added)
    return entry


def _commit(page, node, answer, serial):
    """Keep the old answer and its state effects; append the two new moves."""
    future = next((f for f in answer["Set"] if f.startswith("minachiv.future_")), "")
    if future not in {"minachiv.future_two", "minachiv.future_together", "minachiv.future_minagho", "minachiv.future_chivarro", "minachiv.future_chivarro_service"}:
        return
    pair = future in {"minachiv.future_two", "minachiv.future_together"}
    women = ("minagho", "chivarro") if pair else (("minagho",) if future.endswith("minagho") else ("chivarro",))
    old = deepcopy(answer)
    remote = page.get("Remote", False)
    tag = "stance_" + str(serial)
    answer["Set"].append(SHARE)
    if page["Id"].startswith(P):
        answer["Next"] = tag + "_share"
    if pair:
        page["Nodes"].append(_node(tag + "_share", "Chivarro", ('{n}Chivarro answers above Minagho\'s signature.{/n} "Minagho keeps me, honey. You join us; you do not divide the takings."\n{n}Minagho adds a line beneath it.{/n} "And she keeps me. Knock before coming in, Golarian. If we do not answer, entertain yourself outside."' if remote else '"Minagho keeps me, honey. You join us; you do not divide the takings." {n}Minagho catches Chivarro\'s chin and kisses her.{/n} "And she keeps me. Knock before coming in, Golarian. If we do not answer, entertain yourself outside."'), c("Continue", old["Next"])))
    elif not page["Id"].startswith(P):
        woman = women[0]
        other = "Chivarro" if woman == "minagho" else "Minagho"
        page["Nodes"].append(_node(tag + "_share", other,
            ('"Keep her company, honey. Keep your hands off her bargains with me. She comes back to my bed when she chooses."' if other == "Chivarro" else '"She wants you. That does not make her yours. Hurt her and I will open you from throat to crotch."'), c("Continue", old["Next"])))
    else:
        woman = women[0]
        other = "chivarro" if woman == "minagho" else "minagho"
        speaker = woman.capitalize()
        page["Nodes"].append(_node(tag + "_share", speaker,
            ('"Chivarro\'s place beside me is not yours, Golarian. Understand that before you get into my bed."' if woman == "minagho" else '"Minagho\'s place is not yours, honey. I sold plenty of nights at the Delights. Never hers."'),
            c("Continue", tag + "_present", requires=(STATE + other + ".present",)),
            c("Continue", tag + "_letter", requires=(STATE + other + ".alive",), forbids=(STATE + other + ".present",)),
            c("Continue", tag + "_dead", requires=(STATE + other + ".dead",)),
            c("Continue", tag + "_absent", forbids=(STATE + other + ".alive", STATE + other + ".dead"))))
        reply = ('"Keep her company. Keep your hands off her bargains with me. And if you bring the Goat to her door, I shall send him to yours."' if other == "chivarro" else '"Chivarro wants you. That does not make her yours. Hurt her and I will open you from throat to crotch. She can charge for the mess."')
        page["Nodes"].extend([
            _node(tag + "_present", other.capitalize(), reply, c("Continue", old["Next"])),
            _node(tag + "_letter", other.capitalize(), '{n}She sends your terms with her next letter. The reply comes back in the other woman\'s hand, with your name underlined.{/n}\n' + reply, c("Continue", old["Next"])),
            _node(tag + "_dead", speaker, ('"Chivarro is dead. I have chosen to stay. Do not ever tell me what I should forget."' if woman == "minagho" else '"Minagho is dead. You have my answer, honey. Hers is not for sale."'), c("Continue", old["Next"])),
            _node(tag + "_absent", speaker, ('"I will not call silence permission. If Chivarro can answer, she will. Until then, you have what I offer tonight. Nothing of hers."' if woman == "minagho" else '"No answer from Minagho. If she comes back, we settle this with her. Until then, you have my room, honey. Not her place in it."'), c("Continue", old["Next"])),
        ])
    for woman in women:
        other = "chivarro" if woman == "minagho" else "minagho"
        end = tag + "_exclusive_" + woman
        exclusive = c('"' + woman.capitalize() + ', end it with ' + other.capitalize() + '. I want you to myself."', end,
                      requires=tuple(old["Requires"]) + ("trickster.now", STATE + other + ".possibly_alive"), forbids=tuple(old["Forbids"]))
        node["Choices"].append(exclusive)
        back = deepcopy(old)
        back["Text"] = '"Then I accept sharing. Your terms."'
        back["Set"].append(SHARE)
        back["Next"] = tag + "_share"
        routing = [c("Continue", end + "_present")]
        if page["Id"].startswith(P):
            routing = [c("Continue", end + "_present", requires=(STATE + other + ".present",)),
                       c("Continue", end + "_letter", requires=(STATE + other + ".alive",), forbids=(STATE + other + ".present",)),
                       c("Continue", end + "_unknown", requires=(STATE + other + ".unknown",))]
        page["Nodes"].append(_node(end, woman.capitalize(),
            (('{n}Minagho returns your demand with her refusal written across it.{/n} "You want Chivarro gone? I wanted her dead once. It did not take. I choose her. Swallow that, or leave."' if remote else '"You want Chivarro gone? I wanted her dead once. It did not take." {n}Minagho bares her teeth.{/n} "I choose her. Swallow that, or leave."') if woman == "minagho" else '"You want me to throw Minagho out? Honey, I lost the Delights. I will not lose her to furnish your bedroom. Share, or find someone cheaper."'), *routing))
        reaction = ('"Trying to evict me, honey? From a woman you never owned? Keep your little citadel. She has answered you."' if other == "chivarro" else '"You asked her to throw me away? I have gutted people for less. She has given you your answer. Try to hear it through that thick skull."')
        for kind in (("present", "letter") if page["Id"].startswith(P) else ("present",)):
            page["Nodes"].append(_node(end + "_" + kind, other.capitalize(),
                ('{n}The next letter comes back with the demand copied beneath her refusal.{/n}\n' if kind == "letter" or remote else '') + reaction,
                deepcopy(back), c('"Then we are finished."', flags=(EXCLUSIVE, COOLED, CLOSED))))
        if page["Id"].startswith(P):
            page["Nodes"].append(_node(end + "_unknown", woman.capitalize(),
                ('"No answer from Chivarro. I have given you mine. If she lives, she still has me. Leave, or accept it."' if woman == "minagho" else '"Minagho has not answered, honey. That does not make her place yours. I choose her. Take what I offer, or leave."'),
                deepcopy(back), c('"Then we are finished."', flags=(EXCLUSIVE, COOLED, CLOSED))))
        # No breakup or exclusive commitment is granted by a switch.
        secret = c('"' + woman.capitalize() + ', keep this between us. ' + other.capitalize() + ' need not know."', tag + "_secret_" + woman,
                   requires=tuple(old["Requires"]) + ("trickster.now", STATE + other + ".possibly_alive"), forbids=tuple(old["Forbids"]))
        node["Choices"].append(secret)
        flags = [f for f in old["Set"] if not f.startswith("minachiv.future_")]
        secret_future = future if future == "minachiv.future_chivarro_service" else "minachiv.future_" + woman
        flags += [secret_future, SECRET, TARGET_M if woman == "minagho" else TARGET_C]
        if page["Id"].startswith(P) and P + "cost.half_the_pair" not in flags:
            flags.append(P + "cost.half_the_pair")
        page["Nodes"].append(_node(tag + "_secret_" + woman, woman.capitalize(),
            (('{n}You address a second letter to Minagho alone. Her answer comes back sealed.{/n} "A secret from Chivarro? Oh, she will hate that. Lock your door tonight. And do not send her one of your earnest little letters."' if remote else '{n}You draw Minagho aside. Her fingers close inside your collar.{/n} "A secret from Chivarro? Oh, she will hate that. Lock your door tonight. And do not send her one of your earnest little letters."') if woman == "minagho" else ('{n}You address a second letter to Chivarro alone. She returns it folded shut over her answer.{/n} "You want to lie to Minagho, honey? Come after she leaves. If you blab, I shall tell her whose idea it was."' if remote else '{n}Chivarro lets you draw her aside, then rests a nail against your throat.{/n} "You want to lie to Minagho, honey? Come after she leaves. If you blab, I shall tell her whose idea it was."')),
            c('"Tonight, then."', tag + "_night_" + woman, flags=tuple(flags), requires=tuple(old["Requires"])), c('"Forget it. I will ask openly."', tag + "_share", flags=tuple(old["Set"]) + (SHARE,), requires=tuple(old["Requires"]))))
        # Solo threshold; existing physical mornings or narrated letter mornings
        # expose it. No sexual act is described past the threshold.
        nightflag = P + "night." + woman
        nxt = "morning" if any(x["Id"] == "morning" for x in page["Nodes"]) else None
        if not page["Id"].startswith(P):
            nxt = _discovery(page["Nodes"], "_" + str(serial) + "_" + woman, woman)
        page["Nodes"].append(_node(tag + "_night_" + woman, woman.capitalize(),
            ('{n}Minagho comes after the watch changes. She kicks the door shut, tears your shirt open and presses you against it. Her mouth catches yours; her fingers work the buckle at your waist.{/n}\n"Quiet, Golarian. I want her to wonder where I spent the night."\n{n}She draws you toward the bed by your open collar.{/n}' if woman == "minagho" else '{n}Chivarro comes without a lamp. She drops your belt beside the door and opens her gown, watching your hands as you catch her bare waist. Her kiss drives you back against the bed.{/n}\n"Keep that pretty mouth occupied, honey. I do not want Minagho hearing it."\n{n}She pushes you onto the mattress and follows.{/n}'),
            c("Continue", nxt, flags=(nightflag,) if page["Id"].startswith(P) else ())))


def _morning(page):
    if not page["Id"].startswith(P):
        return
    nodes = page["Nodes"]
    entry = next((x for x in nodes if x["Id"] == "morning"), None)
    if entry is None and ".alone." in page["Id"] and page["Id"].endswith("morning"):
        entry = nodes[0]
    if entry is None:
        return
    target = "minagho" if ".alone.minagho" in page["Id"] else ("chivarro" if ".alone.chivarro" in page["Id"] else None)
    discovery = _discovery(nodes, target=target, at_meeting=entry["Id"] != "morning")
    letter_entry = "stance_discovery_letter"
    nodes.extend([
        _node(letter_entry, "Narrator", '{n}The night has found its way into a letter. The reply is folded over the offending lines, with your name cut through the paper.{/n}',
              c("Continue", letter_entry + "_chivarro", requires=(TARGET_M,)),
              c("Continue", letter_entry + "_minagho", forbids=(TARGET_M,))),
        _node(letter_entry + "_chivarro", "Chivarro", '{n}Minagho has sent Chivarro a description of the night, ending with a question: did she miss anything? Chivarro\'s reply is short.{/n}\n"You piece of shit. Both of you. Ask me next time you want me angry, honey. Commander, find another bed. She has already agreed."', c("Continue", letter_entry + "_minagho_answers")),
        _node(letter_entry + "_minagho_answers", "Minagho", '"I wanted to hear her angry. You wanted a secret. One of us got what we wanted." {n}Minagho folds the reply and keeps it.{/n} "Chivarro stays mine, Golarian. Your night is over."', c("[Leave.]", flags=(EXPOSED, COOLED, CLOSED))),
        _node(letter_entry + "_minagho", "Minagho", '{n}Chivarro copied the night\'s receipt into her next letter. Minagho has returned it with a knife slit through the total.{/n}\n"Chivarro. Send me that bill again and I will collect it from your lover\'s throat. You wanted me to know. Now we both know."', c("Continue", letter_entry + "_chivarro_answers")),
        _node(letter_entry + "_chivarro_answers", "Chivarro", '"I wanted her answer, honey. And I have it." {n}Chivarro keeps the slashed receipt and takes back your key.{/n} "You have paid for one night. Minagho has had me for much longer. Your visits end here."', c("[Leave.]", flags=(EXPOSED, COOLED, CLOSED))),
    ])
    if target:
        other = "chivarro" if target == "minagho" else "minagho"
        entry_node = next(x for x in nodes if x["Id"] == letter_entry)
        entry_node["Choices"] = [c("Continue", letter_entry + "_" + other)]
        unused = {letter_entry + "_" + target, letter_entry + "_" + other + "_answers"}
        nodes[:] = [x for x in nodes if x["Id"] not in unused]
    # Each original answer retains its position. Pending secrets route through
    # the same morning only when both women are currently at hand.
    guard = S + "discovery_due"
    by_letter = S + "letter_due"
    for answer in entry["Choices"]:
        answer["Forbids"].extend((guard, by_letter))
    entry["Choices"].append(c("Continue", discovery, requires=(guard,), flags=(P + "cost.morning_after",)))
    entry["Choices"].append(c("Continue", letter_entry, requires=(by_letter,), flags=(P + "cost.morning_after",)))
    # Secret nights must reach discovery before the original shared dawn.
    # Keep that saved morning node and its honest paths in place.
    secret_nights = [x for x in nodes if x["Id"].startswith("stance_") and "_night_" in x["Id"]]
    if entry["Id"] == "morning" and secret_nights:
        nodes.append(_node("stance_morning_route", "Narrator", "{n}Dawn.{/n}",
            c("Continue", discovery, requires=(guard,), flags=(P + "cost.morning_after",)),
            c("Continue", letter_entry, requires=(by_letter,), flags=(P + "cost.morning_after",)),
            c("Continue", "morning", forbids=(guard, by_letter))))
        for night in secret_nights:
            for answer in night["Choices"]:
                if answer["Next"] == "morning":
                    answer["Next"] = "stance_morning_route"


def _arrival(page):
    if page["Id"] not in {P + "reunion.wardrobe", P + "chivarro_dead.bought", P + "minagho_dead.brand", P + "minagho_dead.brand_letter", P + "minagho_dead.collateral", P + "spared.brand", P + "spared.brand_letter"}:
        return
    target = TARGET_M if page["Id"] in {P + "reunion.wardrobe", P + "chivarro_dead.bought"} else TARGET_C
    candidates = [(node, answer) for node in page["Nodes"] for answer in node["Choices"] if P + "reunited" in answer["Set"] and answer["Next"] is None]
    if not candidates:
        return
    discovery = _discovery(page["Nodes"], "_return", "minagho" if target == TARGET_M else "chivarro", returned=True)
    page["Nodes"].append(_node("stance_share_return", "Chivarro" if target == TARGET_M else "Minagho",
        ('"You made terms while I was away, honey?" {n}Chivarro catches Minagho\'s wrist.{/n} "Let us finish them. She still comes to my bed. When I want her alone, your invitation waits."\n"Her terms," {n}Minagho tells you.{/n} "You heard mine. Answer her."' if target == TARGET_M else '"Chivarro tells me she has been keeping your bed warm." {n}Minagho catches Chivarro\'s hand.{/n} "She still comes to mine. When I ask for her alone, you leave us to it."\n"You have my answer, honey," {n}Chivarro tells you.{/n} "Now she gets hers."'),
        c('"Agreed. Your terms, too."'), c('"Then keep each other. I am leaving."', flags=(COOLED, CLOSED))))
    for node, answer in candidates:
        clone = deepcopy(answer)
        answer["Forbids"].extend((SECRET, SHARE))
        shared = deepcopy(clone)
        shared["Requires"].append(SHARE)
        shared["Forbids"].append(SECRET)
        shared["Next"] = "stance_share_return"
        node["Choices"].append(shared)
        clone["Requires"].extend((SECRET, target))
        clone["Next"] = discovery
        node["Choices"].append(clone)
        # A secret with the arriving woman herself cannot be exposed to an
        # absent partner by this arrival; preserve that original route too.
        quiet = deepcopy(clone)
        quiet["Requires"].remove(target)
        quiet["Forbids"].append(target)
        quiet["Next"] = None
        node["Choices"].append(quiet)


def _late(page):
    if page["Id"] != P + "epilogue.commit":
        return
    pair = next(x for x in page["Nodes"] if x["Id"] == "pair")
    pair["Text"] += '\n"Minagho stays with me," {n}Chivarro says.{/n} "Come to our house, honey, and you take us as we are."\n"And you leave when we want the bed to ourselves," {n}Minagho adds, pulling Chivarro close.{/n} "Agreed?"'
    pair["Choices"][0]["Text"] = '[Go.] "Your terms. Both of you."'
    pair["Choices"][0]["Set"].append(SHARE)
    waiting = next(x for x in page["Nodes"] if x["Id"] == "waiting")
    waiting["Text"] += '\n"Minagho\'s place stays hers," {n}Chivarro says.{/n} "If she comes back, she answers for herself. You have my invitation, honey. Read it properly."'
    waiting["Choices"][0]["Set"].append(SHARE)
    waiting["Choices"].extend([
        c('"Leave Minagho. I want you to myself."', "late_waiting_exclusive", flags=(EXCLUSIVE,),
          requires=("trickster.now", STATE + "chivarro.present", STATE + "minagho.possibly_alive"), forbids=(STATE + "minagho.present",)),
        c('"Keep my visits from Minagho."', "late_waiting_secret", flags=(SECRET, TARGET_C),
          requires=("trickster.now", STATE + "chivarro.present", STATE + "minagho.possibly_alive"), forbids=(STATE + "minagho.present",)),
    ])
    page["Nodes"].extend([
        _node("late_waiting_exclusive", "Chivarro", '"No, honey. Minagho has not come back. That does not give you her place." {n}Chivarro takes back the key.{/n} "If she can answer, she will. You have my answer. Leave."', c("Continue", flags=(COOLED, CLOSED))),
        _node("late_waiting_secret", "Chivarro", '{n}Chivarro comes late, without a lamp. She opens her gown and catches your hands against her bare waist. Her kiss drives you back against the bed.{/n}\n"You want a secret, honey? Lock the door. And remember whose place you asked for."\n{n}She pushes you onto the mattress and follows.{/n}',
              c("Continue", "late_waiting_reply", requires=(STATE + "minagho.distant",), flags=(EXPOSED,)),
              c("Continue", requires=(STATE + "minagho.unknown",))),
        _node("late_waiting_reply", "Chivarro", '{n}Chivarro copied the night\'s receipt into her next letter. Minagho returned it with a knife slit through the total.{/n}\n"Send me that bill again, Chivarro, and I will collect it from your lover\'s throat."\n{n}Chivarro folds the reply and takes back your key.{/n} "I wanted her answer, honey. She stays. You go."', c("Continue", flags=(COOLED, CLOSED))),
    ])
    for woman in ("minagho", "chivarro"):
        other = "chivarro" if woman == "minagho" else "minagho"
        exclusive = "late_exclusive_" + woman
        secret = "late_secret_" + woman
        pair["Choices"].extend([
            c('"' + woman.capitalize() + ', leave ' + other.capitalize() + '. I want only you."', exclusive, flags=(EXCLUSIVE,),
              requires=("trickster.now", STATE + "minagho.present", STATE + "chivarro.present")),
            c('"' + woman.capitalize() + ', meet me alone. Do not tell ' + other.capitalize() + '."', secret, flags=(SECRET, TARGET_M if woman == "minagho" else TARGET_C),
              requires=("trickster.now", STATE + "minagho.present", STATE + "chivarro.present")),
        ])
        page["Nodes"].extend([
            _node(exclusive, woman.capitalize(),
                ('"Chivarro stays. You can fuck off." {n}Minagho tears the invitation in half. Chivarro takes the pieces and drops them in the fire.{/n} "A pity, honey. I had already priced your breakfast."' if woman == "minagho" else '"Minagho stays, honey. You can leave." {n}Chivarro takes back the key. Minagho smiles at you over her shoulder.{/n} "You heard her. Find another house."'), c("Continue", flags=(COOLED, CLOSED))),
            _node(secret, woman.capitalize(),
                ('{n}Minagho comes late, still wearing Chivarro\'s scent. She kisses you against the locked door, pulls your shirt open and draws you to the bed.{/n} "Quiet, Golarian. Let her wonder."' if woman == "minagho" else '{n}Chivarro comes late, without a lamp. She opens her gown, catches your hands against her bare waist, and pushes you back onto the bed.{/n} "Quiet, honey. This night is ours."'), c("Continue", secret + "_dawn", flags=(EXPOSED,))),
            _node(secret + "_dawn", other.capitalize(),
                ('{n}At dawn Chivarro lets herself in. She looks at the clothes, then at Minagho\'s hand on your bare waist.{/n} "You piece of shit. You could have asked me. Get dressed."\n{n}Minagho releases you.{/n} "I enjoyed the secret. But I choose her, Golarian. Go."\n{n}The invitations stopped. The two women kept their house, and each other.{/n}' if other == "chivarro" else '{n}At dawn Minagho lets herself in. She drives a dagger through your discarded belt into the door.{/n} "Chivarro. Tell this idiot where to go before I carve directions into that pretty skin."\n"You have had your night, honey. She stays. You leave." {n}Chivarro throws your shirt at you. No further invitation came; Minagho and Chivarro kept each other.{/n}'), c("Continue", flags=(COOLED, CLOSED))),
        ])


def integrate(payload):
    definitions = deepcopy(STATES)
    definitions[S + "discovery_due"] = [[SECRET, "!" + EXPOSED, STATE + "minagho.present", STATE + "chivarro.present"]]
    definitions[S + "letter_due"] = [
        [SECRET, "!" + EXPOSED, TARGET_M, STATE + "minagho.present", STATE + "chivarro.distant"],
        [SECRET, "!" + EXPOSED, TARGET_C, STATE + "chivarro.present", STATE + "minagho.distant"],
    ]
    derived = payload.setdefault("Derived", {})
    forbids = payload.setdefault("DerivedForbids", {})
    for key, groups in definitions.items():
        compiled = []
        for group in groups:
            inputs = []
            for member in group:
                if member.startswith("!"):
                    flag = member[1:]
                    member = STATE + "not." + flag
                    derived[member] = [["chapter_one"], ["chapter_later"]]
                    forbids[member] = [flag]
                inputs.append(member)
            compiled.append(inputs)
        derived[key] = compiled
    pages = [x for x in payload["Scenes"] if x.get("Relationship") == REL]
    _saved_guards(pages)
    for page in pages:
        # Late invitations never produce the earlier commitment. Their own
        # answers record only the stance and the consequences staged below.
        producers = [(node, answer) for node in page["Nodes"] for answer in node["Choices"] if COMPLETE in answer["Set"]]
        for serial, (node, answer) in enumerate(producers):
            _commit(page, node, answer, serial)
        if page["Id"] == "minachiv.before_the_last_road":
            for node in page["Nodes"]:
                if node["Id"] == "minagho":
                    node["Text"] += '\n"She comes back to me, honey," {n}Chivarro tells you.{/n} "You may keep her company. You do not buy my place beside her."'
                elif node["Id"] in {"friendship", "service"}:
                    node["Text"] += '\n"Chivarro wants you," {n}Minagho says.{/n} "She still comes back to me. Hurt her and I will open you from throat to crotch."'
        _morning(page)
        _arrival(page)
        _late(page)
        if page["Id"] == P + "epilogue.chivarro":
            for para in page["Nodes"][0].get("Paragraphs", []):
                if para["Requires"] == ["minagho.dead"]:
                    para["Requires"] = [STATE + "minagho.dead"]
                    para["Forbids"] = []
                elif para["Requires"] == [MIN_IN]:
                    para["Requires"] = [STATE + "minagho.present"]
                elif para["Forbids"] == [MIN_IN, "minagho.dead"]:
                    para["Requires"] = [STATE + "minagho.distant"]
                    para["Forbids"] = []
        if page["Id"] == P + "epilogue.minagho":
            for para in page["Nodes"][0].get("Paragraphs", []):
                if para["Requires"] == [RET_C]:
                    para["Text"] = '{n}Chivarro read the terms signed in her absence and added her own demands. Minagho kept the sheet, with every insult in the margin.{/n}'
        if page["Owner"].endswith("Epilogue"):
            page["Forbids"].append(COOLED)
            if page["Owner"] != "AeonEpilogue":
                for node in page["Nodes"]:
                    node.setdefault("Paragraphs", []).extend(continuity())
    payload["Scenes"].append(scene(P + "epilogue.partner_refused", "The door they shut", "Epilogue", 1, "", [
        n("end", "Narrator", '{n}At their last meeting, the Commander had been told to leave. The door shut. No invitation followed.{/n}', paragraphs=continuity())],
        requires=("trickster.ever", COOLED), forbids=("sacrifice",), last=99, Relationship=REL,
        ForbidOverrides={"sacrifice": "trickster.commander_back"}))
    # Own Last Call entry only: the shared module remains byte-exact. Install
    # before lastcall builds its copied pages; keep repeat exports idempotent.
    from storylines import lastcall_partners
    part = next(x for x in lastcall_partners.PARTNERS if x["rel"] == REL)
    paras = [deepcopy(x) for x in part["paragraphs"] if not any(k.startswith((S, STATE)) for k in x.get("Requires", []))]
    for para in paras:
        if para["Requires"] == ["minachiv.future_minagho"]:
            para["Text"] = '{n}Minagho kept her own hours, with a dagger by the door. Chivarro\'s place was hers to answer for, never the Commander\'s to give away.{/n}'
        if para["Requires"] == ["minachiv.future_chivarro"]:
            para["Text"] = '{n}Chivarro held the lease, the rent and the key. A visit from the Commander bought nothing of Minagho.{/n}'
    part["paragraphs"] = tuple(paras + continuity())
    part["page_forbids"] = tuple(dict.fromkeys((*part["page_forbids"], COOLED)))
