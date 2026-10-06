"""Authored round-2a terms for Nocticula and her canon lover Shamira.

Canon: Shamira_dialogue/Cue_0066, Cue_0116; Obj_3_ShamiraEssence.
The messages and court responses below are additions, not native history.
They use Nocticula's existing correspondence and Shamira's earned mental presence;
no meeting, resurrection, shell, native breakup or reconciliation is granted.
Only Nocticula entries are changed, including her Last Call template.
"""
from copy import deepcopy

from story_format import c, n, p, scene

P = "nocticula.partner_stance."
TERMS = "nocticula.partner_terms"
EXPOSED = "nocticula.partner_secret_exposed"
REFUSED = "nocticula.partner_exclusive_refused"
EARNED = "nocticula.partner.exclusive_earned"
CHOSEN = "nocticula.partner.exclusive_chosen"
CAREFUL = "nocticula.partner.letters_burned"
KILLED = "shamira.killed"
RETURNED = "shamira.trickster.returned"
BODY = "shamira.trickster.embodied"
CAPTIVE = "shamira.trickster.cost.kept_captive"
CAST = "shamira.trickster.cast_out"
DECLINED = "shamira.trickster.declined"

# Read CURRENT condition, rather than treating the historical returned receipt as a body.
STATES = (
    ("alive", (), (KILLED, RETURNED, CAST, DECLINED)),
    ("body", (RETURNED, BODY), (CAST, DECLINED)),
    ("mind", (RETURNED,), (BODY, CAPTIVE, CAST, DECLINED)),
    ("captive", (RETURNED, CAPTIVE), (BODY, CAST, DECLINED)),
    ("dead", (KILLED,), (RETURNED, CAST, DECLINED)),
    ("cast", (CAST,), ()),
    ("declined", (DECLINED,), (CAST,)),
)
LIVING = {"alive", "body", "mind", "captive"}
INTRO = {
    "alive": '"Years ago, Shamira was my chosen lover long before you came to Alushinyrra. She still is. Her place is in the Harem of Ardent Dream; she rules my city and would rather rule my islands. Do not mistake a place in my bed for a vacancy in hers."',
    "body": '"Years ago, Shamira was my lover. She coveted my throne. You killed her, then found her another body. She has her Harem again. I have not mistaken her return for renewed loyalty — or invited her back into my bed."',
    "mind": '"Years ago, Shamira was my lover. She wanted my throne; now she has the inside of your skull. No body, no place in my bed. But she can hear us. Shall we disappoint her by pretending otherwise?"',
    "captive": '"Years ago, Shamira was my lover. She wanted my throne. You have locked what survived her death inside your head. She cannot come to my bed, or answer an invitation. I have not forgotten whose voice you silenced."',
    "dead": '"Years ago, Shamira was my chosen lover, in the Harem of Ardent Dream. She coveted my throne. You killed her. That bed is empty now; do not congratulate yourself on having won an argument with a corpse."',
    "cast": '"Years ago, Shamira was my lover. She coveted my throne. You kept something of her after her death, then threw it back into the Abyss. Nothing remains to answer us. I remember her perfectly well."',
    "declined": '"Years ago, Shamira was my lover. She coveted my throne. What clung to you after her death went under. No reply will come from her Harem. Do not ask me to pretend she never occupied it."',
}


def nt(key, text, *choices):
    return n(key, "Nocticula", text, *choices, portrait="Nocticula")


def dispatch(prefix, destination):
    return [c("Continue", destination + state, requires=req, forbids=bad)
            for state, req, bad in STATES]


def terms_nodes(prefix, resume, closed):
    """Append-only menu. Accepted terms return to the original commitment answer.

    Exclusive is a demand she refuses, never an automatic breakup of another route.
    A dead partner needs acknowledgement, not a manufactured negotiation.
    """
    out = [nt(prefix, '"Before you promise me another evening, Commander: what do you intend to do about Shamira\'s name in this arrangement? The Worldwound has not made my bed a crusader\'s reward."',
              *dispatch(prefix, prefix + ".name."))]
    for state, _, _ in STATES:
        base = prefix + "." + state
        out.append(nt(prefix + ".name." + state, INTRO[state],
            c('"Let her know. I am offering company, not a claim on your throne."', base + ".share"),
            c('"End it with her. I want you to myself."', base + ".exclusive"),
            c('"Keep this between us. Let her believe what she likes."', base + ".secret")))
        if state in {"alive", "body"}:
            staging = ('{n}Nocticula lays out Shamira\'s old letter: terms for another lover, answered before she invited you. The hand is sharp, the seal scorched.{/n}'
                       if state == "alive" else
                       '{n}Nocticula lays out Shamira\'s old letter, written after her return to the Harem. It bears the Ardent Dream\'s seal, not an invitation back to Nocticula\'s bed.{/n}')
            answer = ('"Another amusement? Keep the mortal away from my throne. When you tire of crusade reports, you know where I am."'
                      if state == "alive" else
                      '"Your bed is yours. My Harem is mine. Send your mortal if you want an answer; I would enjoy finding out what else you have told them."')
            out.append(n(base + ".share", "Narrator", staging + "\n" + answer,
                         c('"And you, Nocticula?"', base + ".share_answer"), portrait="Shamira"))
            out.append(nt(base + ".share_answer", '"She may have your ear. She may try for rather more. Carry nothing from my pillow to her throne, and nothing from hers to mine. I shall enjoy watching which of us she thinks she can cheat first."',
                          c('[Accept their terms.]', resume, flags=(TERMS, P + "share"))))
        elif state == "mind":
            out.append(n(base + ".share", "Narrator", '{n}Inside your mind, the voice presses against the inside of your skull.{/n} "You have your throne, my dear. Now you want my Golarian too? Keep your secrets out of this head if you can."',
                         c('"You heard her."', base + ".share_answer"), portrait="Shamira"))
            out.append(nt(base + ".share_answer", '"I did. No promises on your behalf, Commander. She has your thoughts; I shall have what you choose to bring me. And if she whispers about my throne, I expect to hear it from you."',
                          c('[Keep that arrangement.]', resume, flags=(TERMS, P + "share"))))
        elif state == "captive":
            out.append(nt(base + ".share", '"Her answer is behind the lock you put on her. How considerate — my invitations have never been so quiet. Offer me your own company, Commander. Do not claim to speak for my former lover."',
                          c('[Acknowledge the captive; promise only your own company.]', resume, flags=(TERMS, P + "share"))))
        else:
            out.append(nt(base + ".share", '"There is nobody left to tell. You may share my company; you will not borrow a dead woman\'s approval."',
                          c('[Keep her name in the agreement.]', resume, flags=(TERMS, P + "share"))))
        if state in LIVING:
            out.append(nt(base + ".exclusive", '"End it? You speak as though I were dismissing a chambermaid. I choose who comes to my bed. Her treachery did not transfer that choice to you."\n{n}Her smile widens.{/n} "You may ask for me. You may not order me to erase her. Shall I show you the door?"',
                          c('"Then let her know about us."', base + ".share"),
                          c('"Keep me secret, then."', base + ".secret"),
                          c('"Yes. We are finished."', flags=(P + "exclusive", REFUSED, closed))))
        else:
            out.append(nt(base + ".exclusive", '"She is dead. There is no lover left to dismiss. If you mean that I must never take another, the answer is no. Take the evening I offer, or leave it."',
                          c('[Accept her refusal to promise exclusivity.]', resume, flags=(TERMS, P + "exclusive", REFUSED)),
                          c('"Then we are finished."', flags=(P + "exclusive", REFUSED, closed))))
        secret_text = ('"A secret, then. She knows my seals. She knows how I mark a lover. If she finds either on you, I shall not hide behind your lie."'
                       if state in {"alive", "body"} else
                       '"From the woman inside your head? Try. Your dreams will tell her more than your mouth does."'
                       if state == "mind" else
                       '"You have already arranged her silence. Her courtiers are rather harder to gag. Keep the affair quiet if it amuses you. I shall enjoy watching you decide which one sold us."'
                       if state == "captive" else
                       '"Shamira is dead. Keep it from her courtiers, then. They still sell what they learn about my bed. Keep your mouth shut if you intend to give them nothing."')
        out.append(nt(base + ".secret", secret_text,
                      c('[Keep the affair private.]', resume, flags=(TERMS, P + "secret"))))
    for state, _, _ in STATES:
        base = prefix + "." + state
        name = next(node for node in out if node["Id"] == prefix + ".name." + state)
        name["Choices"][1]["Next"] = base + ".answer"
        out.append(nt(base + ".answer", '"You have asked for a great deal. Let us see what you have brought me."',
            c("Continue", base + ".chosen", requires=(EARNED,)),
            c("Continue", base + ".exclusive", forbids=(EARNED,))))
        # Every response is delivered from her CURRENT form. The partner's body
        # is never conjured for a breakup, nor is its survival newly inferred.
        response = ('{n}Shamira\'s answer burns across the letter.{/n} "You dismiss me from your bed? Keep your mortal. You will still hear from my Harem when your city displeases me."'
                    if state in ("alive", "body") else
                    '{n}Shamira\'s voice strikes behind your eyes.{/n} "Very well, my lady. I have a place where your lover cannot shut the door on me."'
                    if state == "mind" else
                    '{n}The message to Shamira\'s court brings no answer from its mistress. Nocticula does not call the silence agreement.{/n}')
        out.append(nt(base + ".chosen", '''"You have brought me something worth keeping. My brother's schemes are tiresome; someone who can cost him an advantage is rather less so."
{n}Her answering mark cuts across Shamira's name.{/n}
"No invitations to my bed for her. Or for another lover while I keep this promise. My city remains my city. You remain the person who brings me what others would hide. That part will become inconvenient."
''' + response + '''
{n}Nocticula's smile bares the edge of a tooth.{/n} "Come here. I want to see how much pleasure you take in being wanted."''',
            c('[Accept her claim and the work already owed.]', resume, flags=(TERMS, P + "exclusive", CHOSEN)),
            c('"Let her keep her place. I will share."', base + ".share")))
        secret = next(node for node in out if node["Id"] == base + ".secret")
        if state != "mind":
            secret["Choices"].append(c('[Burn the private invitations before anyone else can read them. Take no marked gifts.]', resume,
                flags=(TERMS, P + "secret", CAREFUL), forbids=("nocticula.trickster.secret_known.shamira",)))
    return out


def wrap_commit(scene_, page, index):
    """Retain the original answer/index; append its terms-first twin."""
    node = next(x for x in scene_["Nodes"] if x["Id"] == page)
    answer = deepcopy(node["Choices"][index])
    node["Choices"][index] = answer
    prefix = "partner_terms." + page + "." + str(index)
    if any(x["Id"] == prefix for x in scene_["Nodes"]):
        return
    twin = deepcopy(answer)
    twin.update(Next=prefix, Set=[], Abort=False)
    twin.pop("NativeNext", None)
    twin["Forbids"].append(TERMS)
    answer["Requires"].append(TERMS)
    node["Choices"].append(twin)
    closed = "noct.acq.closed" if scene_.get("Relationship") == "nocticula.acquisition" else "noct.closed"
    resume = prefix + ".accepted"
    scene_["Nodes"].extend(terms_nodes(prefix, resume, closed))
    scene_["Nodes"].append(nt(resume, '"Now. You were about to promise me something."', deepcopy(answer)))


def discovery(scene_, page, index):
    """Discover a secret at an EXISTING morning/letter receipt, keeping its old exit."""
    node = next(x for x in scene_["Nodes"] if x["Id"] == page)
    answer = deepcopy(node["Choices"][index])
    node["Choices"][index] = answer
    prefix = "partner_discovery." + page + "." + str(index)
    if any(x["Id"] == prefix for x in scene_["Nodes"]):
        return
    twin = deepcopy(answer)
    twin.update(Next=prefix, Set=[], Abort=False)
    twin["Requires"].append(P + "secret")
    twin["Forbids"].append(EXPOSED)
    twin["Forbids"].append(CAREFUL)
    node["Choices"].append(twin)
    # Two appended continuations replace the old exit only while a secret is unexposed.
    answer["Forbids"].append(P + "secret")
    seen = deepcopy(answer)
    seen["Forbids"].remove(P + "secret")
    seen["Requires"].extend((P + "secret", EXPOSED))
    node["Choices"].append(seen)
    private = deepcopy(seen)
    private["Requires"].remove(EXPOSED)
    private["Requires"].append(CAREFUL)
    private["Forbids"].append(EXPOSED)
    private["Next"] = prefix + ".hidden"
    private["Set"] = []
    private.pop("NativeNext", None)
    node["Choices"].append(private)
    node["Choices"].append(c('[Keep the signed invitation. Let the clerk carry the next one.]', prefix,
                             requires=(P + "secret", CAREFUL), forbids=(EXPOSED,)))
    hidden_exit = deepcopy(answer)
    hidden_exit["Forbids"].remove(P + "secret")
    hidden = nt(prefix + ".hidden", '''{n}The invitation curls in the lamp flame before the morning clerk arrives. No seal leaves the room; no marked gift goes to the Harem.{/n}
"You would have enjoyed keeping that," {n}Nocticula writes on the answering scrap.{/n} "Burn this too. You may come when I summon you. You may not keep a pretty collection for her servants to buy."
{n}You feed the last scrap to the flame. There is nothing for the courier to carry.{/n}''', hidden_exit)
    scene_["Nodes"].append(nt(prefix, '"Your private invitation has acquired an answer. Read it before you send another."',
                              *dispatch(prefix, prefix + ".")))
    for state, _, _ in STATES:
        if state in {"alive", "body"}:
            text = '{n}A scrap of Nocticula\'s invitation has come back with another seal burned across it.{/n} "I know that hand, mortal. I know what she writes when she wants someone in her bed. Let her keep you. My Harem is closed to her tonight. She may send an assassin if she wants an audience."'
        elif state == "mind":
            text = '{n}Inside your mind, the voice catches the memory of Nocticula\'s invitation as you wake. Her voice burns behind your eyes.{/n} "You hid her from me? In my own lodging? Keep your little affair. I shall remember every word she whispers here. Tell her that."'
        elif state == "captive":
            text = '{n}The answering message comes from Shamira\'s court, where her courtiers still trade in her name. The captive behind your eyes cannot answer it.{/n} "The Lady\'s invitations have found another bed. The court thanks you for the intelligence."'
        else:
            text = '{n}The answering message comes from Shamira\'s court. Her surviving courtiers have copied the private invitation; their mistress is dead.{/n} "The Lady\'s invitations have found another bed. The court thanks you for the intelligence."'
        scene_["Nodes"].append(n(prefix + "." + state, "Narrator", text,
                                   c('[Show Nocticula the answer.]', prefix + ".fallout", flags=(EXPOSED,)),
                                   portrait="Shamira"))
    finish = deepcopy(answer)
    finish["Forbids"].remove(P + "secret")
    scene_["Nodes"].append(nt(prefix + ".fallout", '"So much for discretion. No more letters beyond the business already agreed. When I want your company, I shall summon you. You may arrive, or let me wonder whose door you used instead."\n{n}She withdraws the invitation. The war dispatch beside it remains unanswered.{/n}', finish))
    scene_["Nodes"].append(hidden)


def ending_paragraphs(nocticula_dead=False):
    out = []
    for state, req, bad in STATES:
        text = {
            "alive": '{n}Shamira\'s court remained in the Harem of Ardent Dream. Its mistress was still Nocticula\'s chosen lover and would-be rival. Her place in the Midnight Isles had not passed to the Commander.{/n}',
            "body": '{n}Shamira\'s court had its mistress back in the body the Commander earned for her. Survival had not restored her old place in Nocticula\'s bed or settled her claim on the throne.{/n}',
            "mind": '{n}Shamira\'s name was spoken inside the Commander\'s head. She remained bodiless there. Nocticula\'s former lover could listen there; she could neither occupy the royal bed nor sit beside its owner.{/n}',
            "captive": '{n}Shamira\'s name remained in the court\'s accounts. What survived of her remained captive inside the Commander. She had once shared Nocticula\'s bed and coveted her throne. No answer had come from the cage to the new invitation.{/n}',
            "dead": '{n}Shamira was dead. Nocticula\'s court still remembered the lover who had coveted the Lady in Shadow\'s throne. No guest could claim the Ardent Dream\'s agreement.{/n}',
            "cast": '{n}Shamira was dead; what had clung to the Commander had been cast back into the Abyss. The name of Nocticula\'s former lover remained in the court\'s accounts; no guest could speak for her.{/n}',
            "declined": '{n}Shamira was dead; her last remnant had gone under. Her Harem outlasted her. Its courtiers could not claim their mistress had willingly surrendered her place beside Nocticula.{/n}',
        }[state]
        if nocticula_dead and state == "alive":
            text = '{n}Shamira\'s court remained in the Harem of Ardent Dream. Its mistress had been Nocticula\'s chosen lover and would-be rival. After Nocticula\'s death, the Harem shut its doors to mourners. Its courtiers began buying reports from the other islands.{/n}'
        if state == "alive":
            out.append(p(text, requires=req, forbids=(*bad, EXPOSED, CHOSEN)))
            out.append(p('{n}Shamira remained in her Harem. Nocticula had ended her claim to the royal bed. The dismissal had cost Nocticula her favorite; Shamira had kept the Harem and answered the Lady in Shadow\'s orders with threats of her own.{/n}', requires=(*req, CHOSEN), forbids=bad))
            separated = ('{n}Shamira\'s court remained in the Harem of Ardent Dream. Before Nocticula\'s death, its mistress had closed her doors to her former lover over the exposed affair. The courtiers kept their copies of the invitations and began buying reports from the other islands.{/n}' if nocticula_dead else
                         '{n}Shamira\'s court remained in the Harem of Ardent Dream. Its mistress had closed her doors to Nocticula over the exposed affair. She was alive, separated from her former lover, and still buying intelligence about the Lady in Shadow\'s throne.{/n}')
            out.append(p(separated, requires=(*req, EXPOSED), forbids=bad))
            continue
        if state in {"body", "mind", "captive"}:
            bad = (*bad, "nocticula.partner_passenger_lost")
        out.append(p(text, requires=req, forbids=bad))
    out.append(p('{n}The Commander did not return from the sacrifice. Shamira died again without that mind\'s warmth. The Harem\'s courtiers found the cold shell in an Alushinyrra doorway. The Ardent Dream\'s old place beside Nocticula remained empty.{/n}',
                 requires=("nocticula.partner_passenger_lost", BODY)))
    out.append(p('{n}The Commander did not return from the sacrifice. The death of Shamira followed: she had still been bodiless, sheltered inside that mind. Nothing came back to her Harem. The Ardent Dream\'s old place beside Nocticula remained empty.{/n}',
                 requires=("nocticula.partner_passenger_lost",), forbids=(BODY,)))
    out.extend((
        p('{n}The Commander had chosen to share Nocticula\'s company. Shamira\'s name remained part of that bargain, with her answer where she could still give one; no claim on the Midnight Isles came with it.{/n}', requires=(P + "share",)),
        p("{n}Nocticula had chosen the Commander alone as her lover. She had bound that promise to the work the Commander already owed her, and dismissed Shamira from her bed. She had asked for the Commander's time and service, and given no claim on her throne.{/n}", requires=(P + "exclusive", CHOSEN)),
        p('{n}The Commander had demanded exclusivity. Nocticula refused the claim. Until her death, she had kept her own choice of lovers.{/n}' if nocticula_dead else
          '{n}The Commander had demanded exclusivity. Nocticula refused the claim. Her bed and her throne remained hers to dispose of.{/n}', requires=(P + "exclusive", REFUSED)),
        p('{n}The Commander had asked for a secret affair. Its private invitations were evidence in a court that sold pillow talk.{/n}', requires=(P + "secret",), forbids=(EXPOSED,)),
        p('{n}The secret affair had been exposed through Nocticula\'s invitations. She had withdrawn the private letters and summoned the Commander on her own terms. Her death ended those invitations too; copies of the old ones remained in the courtiers\' hands.{/n}' if nocticula_dead else
          '{n}The secret affair had been exposed through Nocticula\'s invitations. Nocticula withdrew the private letters. Future visits came at her summons, with the slight still remembered.{/n}', requires=(P + "secret", EXPOSED)),
        p('{n}No new arrangement concerning Shamira\'s name had been concluded. Nocticula\'s interest in the Commander did not erase her lover or settle their struggle for the throne.{/n}', forbids=(TERMS,)),
    ))
    for state, req, bad in STATES:
        if state == "alive":
            reaction = '{n}Shamira\'s old letter of refusal was nailed to the Harem\'s doors: "Let her keep the mortal. Nocticula comes here at my invitation now." The royal bed had lost its old favorite; the royal throne still had her attention.{/n}'
        elif state == "body":
            reaction = '{n}Shamira\'s old letter of refusal was nailed to the Harem\'s doors: "Let her keep the mortal. Nocticula comes here at my invitation now." Survival had not reconciled the two queens. The court no longer accepted Nocticula\'s private messages.{/n}'
        elif state == "mind":
            reaction = ('{n}Shamira\'s name preceded a threat heard inside the Commander\'s head: "I shall remember every word she whispers here." She had kept her threat while Nocticula lived. After the Lady\'s death, she still asked the Commander to recall the last invitation.{/n}' if nocticula_dead else
                        '{n}Shamira\'s name preceded a threat heard inside the Commander\'s head: "I shall remember every word she whispers here." She kept her threat. Nocticula had lost a lover and acquired a listener she could not dismiss.{/n}')
        else:
            reaction = '{n}The courtiers in Shamira\'s court sold copies of the exposed invitation. No answer came from the Ardent Dream herself.{/n}'
        if state in {"body", "mind", "captive"}:
            bad = (*bad, "nocticula.partner_passenger_lost")
        out.append(p(reaction, requires=(*req, P + "secret", EXPOSED), forbids=bad))
    return out


def late_discovery_paragraphs():
    """The existing late morning can tell its fallout, but epilogues cannot set flags."""
    out = []
    for state, req, bad in STATES:
        if state in {"alive", "body"}:
            text = '{n}The next invitation came back bearing another seal. Shamira\'s old letter of refusal was enclosed: "I know how she marks a lover. She may keep you. My Harem is closed to her." Nocticula withdrew the private letters. The Commander would come at her summons, with an insult waiting on either side of the royal bed.{/n}'
        elif state == "mind":
            text = '{n}Shamira\'s name preceded a voice heard inside the Commander\'s head at dawn: "You hid her from me? Here? I shall remember every word she whispers." Nocticula withdrew the private letters when the Commander repeated it. Their next meeting came at her summons; the listener never left.{/n}'
        else:
            text = '{n}Shamira\'s court sent back the next invitation with an offer to sell its copies. No answer came from the Ardent Dream herself. Nocticula withdrew the private letters. The Commander would come at her summons; the court kept the evidence.{/n}'
        out.append(p(text, requires=(*req, P + "secret"), forbids=(*bad, EXPOSED)))
    return out


def integrate(payload):
    payload.setdefault("Derived", {})[EARNED] = [
        ["trickster.now", "noct.acq.concession_delivered"],
        ["trickster.now", "noct.parent_active", "noct.socoth_plan_exposed"],
        ["trickster.now", "nocticula.trickster.cost.shade_paid"],
    ]
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    for s in list(payload["Scenes"]):
        if s["Id"] == "noct.second_door" or s["Id"].startswith("noct.second_door.acquired."):
            for i in range(3):
                wrap_commit(s, "future", i)
        elif s["Id"] == "nocticula.trickster.defeated.chair":
            for page in ("verdict_true", "verdict_joke"):
                for i in range(2):
                    wrap_commit(s, page, i)
            for page in ("morning_late_paid", "morning_late"):
                discovery(s, page, 0)
        elif s["Id"] == "noct.acq.an_answer_of_her_own":
            wrap_commit(s, "risk", 0)
            discovery(s, "accept", 0)
        elif s["Id"] == "nocticula.trickster.defeated.morning":
            for page in ("start", "note_paid_alone", "daeran"):
                # Read the price/Daeran first; replace terminal exits only.
                node = next(n for n in s["Nodes"] if n["Id"] == page)
                for i, answer in enumerate(list(node["Choices"])):
                    if not answer["Next"]:
                        discovery(s, page, i)
        if s["Id"] == "noct.second_door" or s["Id"].startswith("noct.second_door.acquired."):
            discovery(s, "end", 0)
            if ".acquired." in s["Id"]:
                # Retained harbor copies alias every terminal back to the donor scene.
                for node in s["Nodes"]:
                    if node["Id"].startswith("partner_"):
                        for choice in node["Choices"]:
                            if not choice["Next"] and not choice["Abort"] and "noct.second_door" not in choice["Set"]:
                                choice["Set"].append("noct.second_door")
        if s.get("Relationship") in ("nocticula", "nocticula.acquisition") and s["Owner"].endswith("Epilogue"):
            for node in s["Nodes"]:
                # Branching slides carry the account at each ending, rather than
                # repeating it while the Commander is still crossing the room.
                if not any(not choice["Next"] for choice in node["Choices"]):
                    continue
                if s["Owner"] == "AeonEpilogue":
                    node.setdefault("Paragraphs", []).append(p('{n}In the lost history, Shamira had been Nocticula\'s chosen lover in the Harem of Ardent Dream. The Commander\'s demands, bargains and secret invitations belonged to that erased court; none settled her place in the remade world.{/n}'))
                    for stance in ("share", "exclusive", "secret"):
                        node["Paragraphs"].append(p('{n}' + {
                            "share": 'The agreement to share Nocticula\'s company had been erased with those evenings.',
                            "exclusive": 'The demand that Nocticula abandon Shamira had never been spoken in this history.',
                            "secret": 'The secret invitations were gone. Shamira\'s court had no copies to sell.',
                        }[stance] + '{/n}', requires=(P + stance,)))
                else:
                    node.setdefault("Paragraphs", []).extend(deepcopy(ending_paragraphs(
                        nocticula_dead=s["Id"] == "noct.ending_death" or s["Id"].startswith("noct.ending_death.acquired."))))
                    if s["Id"] == "nocticula.trickster.epilogue.commit" and node["Id"] in ("after_paid", "after_refused"):
                        node["Paragraphs"].extend(late_discovery_paragraphs())

    # The existing read-only late epilogues cannot set a stance. Offer terms beforehand
    # on the same Threshold audience, with no changed return, price or presence gates.
    late = scene("nocticula.trickster.partner_terms.threshold", "The Ardent Dream's place", "Nocticula", 6,
                 '"Before another invitation: tell me about Shamira."',
                 terms_nodes("terms", "accepted", "noct.closed") + [
                     nt("accepted", '"Very well. Finish your war, Commander. I shall decide what I want from you when you survive it."', c())],
                 requires=("trickster.ever", "nocticula.trickster.returned"),
                 forbids=(TERMS, "noct.closed", "noct.complete"), last=6,
                 Relationship="nocticula", Chapters=[6],
                 AnswerLists=["765173e2a9e535e4cb66f0ec767c13af"],
                 NativeReturnCue=by_id["nocticula.trickster.defeated.call_in"]["NativeReturnCue"])
    # Reuse the verified return of the existing call-in instead of a guessed GUID.
    late["NativeReturnCue"] = by_id["nocticula.trickster.defeated.call_in"]["NativeReturnCue"]
    payload["Scenes"].append(late)
    for key in ("nocticula.trickster.epilogue.commit", "nocticula.trickster.epilogue.declined"):
        by_id[key]["Requires"].append(TERMS)

    payload.setdefault("Derived", {})["nocticula.partner_passenger_lost"] = [
        [RETURNED, "sacrifice"]]
    payload.setdefault("DerivedForbids", {})["nocticula.partner_passenger_lost"] = [
        "trickster.commander_back", CAST, DECLINED]

    # These pages are assembled later. Extend only Nocticula's named data entries;
    # shared Last Call code, other partners and their conditions are untouched.
    from storylines import lastcall_partners, nm1_nocticula
    ep = nm1_nocticula.EPILOGUE["Nodes"][0]
    if not any(P + "share" in x["Requires"] for x in ep.get("Paragraphs", [])):
        ep.setdefault("Paragraphs", []).extend(deepcopy(ending_paragraphs()))
    partner = next(x for x in lastcall_partners.PARTNERS if x["key"] == "nocticula")
    if not any(P + "share" in x["Requires"] for x in partner["paragraphs"]):
        partner["paragraphs"] = (*partner["paragraphs"], *ending_paragraphs())
