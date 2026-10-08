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
    "alive": '"Shamira is my chosen lover. She rules Alushinyrra for me and would rather rule my islands. She knows I have invited you. Shall we read her answer?"',
    "body": '"You found Shamira a body. She has her Harem again; she has not recovered my bed. Survival is a poor apology for wanting my throne."',
    "mind": '"My former lover is listening inside your skull. No body, no place in my bed. She can hear us discuss hers. How attentive of her."',
    "captive": '"You have caged my former lover inside your head. She cannot answer this invitation. Her courtiers can still sell it. I know which silence you bought."',
    "dead": '"Shamira was my chosen lover. You killed her. Do not congratulate yourself on having won an argument with a corpse."',
    "cast": '"You threw what remained of my former lover into the Abyss. Nothing answers from there. Her court still remembers who coveted my throne."',
    "declined": '"What remained of my former lover went under. Her courtiers outlived her. They have not forgotten her old claim on my bed."',
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
    scene_["Nodes"].append(nt(resume, '"Now. You were about to give me an answer."', deepcopy(answer)))


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
    hidden = nt(prefix + ".hidden", '''{n}A hand knocks at the door. The clerk asks for the next dispatch; its corner lies beneath the private invitation. You draw the dispatch free and hold the invitation to the lamp. It curls in the flame before the clerk enters. No seal leaves the room; no marked gift goes to the Harem.{/n}
"You would have enjoyed keeping that," {n}Nocticula writes on the answering scrap.{/n} "Burn this too. You may come when I summon you. You may not keep a pretty collection for her servants to buy."
{n}You feed the last scrap to the flame. There is nothing for the courier to carry.{/n}''', hidden_exit)
    scene_["Nodes"].append(nt(prefix, '''{n}The clerk has put the morning dispatch on top of your private packet. Beneath it, Nocticula's seal carries a second impression, burned deep into the wax. Her answering mark stops when your fingers uncover it.{/n} "Your private invitation has acquired an answer. Read it before you send another."''',
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
    scene_["Nodes"].append(nt(prefix + ".fallout", '''"So much for discretion. No more letters beyond the business already agreed. When I want your company, I shall summon you. You may arrive, or let me wonder whose door you used instead."
{n}Her mark strikes out the invitation, then moves onto the war dispatch beside it. She corrects the broker's demand in three strokes.{/n}
"That business proceeds. The next private letter does not."''', finish))
    scene_["Nodes"].append(hidden)


def ending_paragraphs(nocticula_dead=False):
    out = []
    for state, req, bad in STATES:
        text = {
            "alive": '{n}Shamira\'s court remained in the Harem of Ardent Dreams. Its mistress was still Nocticula\'s chosen lover and would-be rival. Her place in the Midnight Isles had not passed to the Commander.{/n}',
            "body": '{n}Shamira\'s court had its mistress back in the body the Commander earned for her. Survival had not restored her old place in Nocticula\'s bed or settled her claim on the throne.{/n}',
            "mind": '{n}Shamira\'s name was spoken inside the Commander\'s head. She remained bodiless there. Nocticula\'s former lover could listen there; she could neither occupy the royal bed nor sit beside its owner.{/n}',
            "captive": '{n}Shamira\'s name remained in the court\'s accounts. What survived of her remained captive inside the Commander. She had once shared Nocticula\'s bed and coveted her throne. No answer had come from the cage to the new invitation.{/n}',
            "dead": '{n}Shamira was dead. Nocticula\'s court still remembered the lover who had coveted the Lady in Shadow\'s throne. No guest could claim the Ardent Dream\'s agreement.{/n}',
            "cast": '{n}Shamira was dead; what had clung to the Commander had been cast back into the Abyss. The name of Nocticula\'s former lover remained in the court\'s accounts; no guest could speak for her.{/n}',
            "declined": '{n}Shamira was dead; her last remnant had gone under. Her Harem outlasted her. Its courtiers could not claim their mistress had willingly surrendered her place beside Nocticula.{/n}',
        }[state]
        if nocticula_dead and state == "alive":
            text = '{n}Shamira\'s court remained in the Harem of Ardent Dreams. Its mistress had been Nocticula\'s chosen lover and would-be rival. After Nocticula\'s death, the Harem shut its doors to mourners. Its courtiers began buying reports from the other islands.{/n}'
        if state == "alive":
            out.append(p(text, requires=req, forbids=(*bad, EXPOSED, CHOSEN)))
            out.append(p('{n}Shamira remained in her Harem. Nocticula had ended her claim to the royal bed. The dismissal had cost Nocticula her favorite; Shamira had kept the Harem and answered the Lady in Shadow\'s orders with threats of her own.{/n}', requires=(*req, CHOSEN), forbids=bad))
            separated = ('{n}Shamira\'s court remained in the Harem of Ardent Dreams. Before Nocticula\'s death, its mistress had closed her doors to her former lover over the exposed affair. The courtiers kept their copies of the invitations and began buying reports from the other islands.{/n}' if nocticula_dead else
                         '{n}Shamira\'s court remained in the Harem of Ardent Dreams. Its mistress had closed her doors to Nocticula over the exposed affair. She was alive, separated from her former lover, and still buying intelligence about the Lady in Shadow\'s throne.{/n}')
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
    # R2: the existing arrangement is heard before the first physical approach.
    # The commitment wrappers below reuse its receipt rather than charging twice.
    for s in payload["Scenes"]:
        if ".acquired." in s["Id"]:
            continue  # N1 frozen baseline, restored below
        donor = s["Id"].split(".acquired.")[0]
        if donor == "noct.unlit_quay":
            wrap_commit(s, "offer", 1)
        elif donor == "noct.her_own_face":
            for i in (0, 1):
                wrap_commit(s, "start", i)
        elif donor == "noct.another_place":
            for i in (0, 1):
                wrap_commit(s, "start", i)
        elif donor == "noct.unborrowed_evening":
            wrap_commit(s, "start", 0)
        elif donor == "noct.what_she_keeps":
            for i in range(3):
                wrap_commit(s, "ambition", i)

    for s in list(payload["Scenes"]):
        if ".acquired." in s["Id"]:
            continue  # do not re-match or re-voice frozen clones
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
        polish_situation(s)
        appended_accounts = take_new_accounts(s)
        if s.get("Relationship") in ("nocticula", "nocticula.acquisition") and s["Owner"].endswith("Epilogue"):
            for node in s["Nodes"]:
                # Branching slides carry the account at each ending, rather than
                # repeating it while the Commander is still crossing the room.
                if not any(not choice["Next"] for choice in node["Choices"]):
                    continue
                if s["Owner"] == "AeonEpilogue":
                    node.setdefault("Paragraphs", []).append(p('{n}In the lost history, Shamira had been Nocticula\'s chosen lover in the Harem of Ardent Dreams. The Commander\'s demands, bargains and secret invitations belonged to that erased court; none settled her place in the remade world.{/n}'))
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
        # The engine's payoff ledger addresses existing paragraphs by index.
        # New accounts follow the old partner blocks, preserving those addresses.
        for host, blocks in appended_accounts:
            target = next(x for x in s["Nodes"] if x["Id"] == host)
            target.setdefault("Paragraphs", []).extend(blocks)

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
    add_correspondence_visit(nm1_nocticula.EPILOGUE)
    partner = next(x for x in lastcall_partners.PARTNERS if x["key"] == "nocticula")
    if not any(P + "share" in x["Requires"] for x in partner["paragraphs"]):
        partner["paragraphs"] = (*partner["paragraphs"], *ending_paragraphs())

    # Acquisition has its own open-route guard; a closed parent road cannot
    # suppress an independently earned correspondence coda. No shared entry changes.
    add_acquisition_coda(payload, lastcall_partners, partner)

    from storylines.nocticula_acquired_harbor import frozen_integrated
    frozen = {s["Id"]: s for s in frozen_integrated()}
    for i, s in enumerate(payload["Scenes"]):
        if s["Id"] in frozen:
            payload["Scenes"][i] = frozen[s["Id"]]
    from storylines.nocticula_n1 import finish_partners
    finish_partners(payload)


def node(scene_, key):
    return next(x for x in scene_["Nodes"] if x["Id"] == key)


def take_new_accounts(s):
    sid = s["Id"]
    donor = sid.split(".acquired.")[0]
    hosts = {}
    if donor in {"noct.ending_company", "noct.ending_alliance", "noct.ending_limit", "noct.ending_ascent"}:
        hosts["end"] = 0
    elif sid == "nocticula.trickster.defeated.epilogue":
        hosts["end"] = 1  # the original paid-chair paragraph stays at index zero
    elif sid == "nocticula.trickster.defeated.epilogue.unanswered":
        hosts["end"] = 0
    elif sid == "nocticula.trickster.epilogue.commit":
        hosts.update(refused_page=0, inn=0)
    out = []
    for key, keep in hosts.items():
        page = node(s, key)
        blocks = page.get("Paragraphs", [])
        out.append((key, blocks[keep:]))
        page["Paragraphs"] = blocks[:keep]
    return out


def slot(scene_, host, number, cut, *, split=None):
    """An appended fill node; old node/answer indices and old targets survive.

    The empty fill is a heated cut. Its answers carry the original aftermath
    mechanics. No desire, rescue, payment or arrival receipt is invented here.
    """
    key = scene_["Id"] + ".explicit." + str(number)
    if any(x["Id"] == key for x in scene_["Nodes"]):
        return
    original = node(scene_, host)
    # Authoring tuples can share answer dictionaries between sibling nodes.
    # Split that alias before changing a destination for this host alone.
    original["Choices"] = deepcopy(original["Choices"])
    text = original["Text"]
    after = ""
    if split:
        before, after = text.split(split, 1)
        # The harbor text keeps narration open across the old cut.
        original["Text"] = before.rstrip() + "{/n}"
        after = "{n}" + split + after
        after = after.replace("Later, the lamp burns beside the couch. ", "")
        after = after.replace("The book has fallen open on the floor. ", "")
        after = after.replace("The curtains close across the window. Much later, she asks", "She asks")
    old_choices = deepcopy(original["Choices"])
    for answer in original["Choices"]:
        answer.update(Next=key, Set=[], Abort=False)
        answer.pop("NativeNext", None)
    # Explicit content brief: see tools/route_packs/explicit_slots/nocticula/<id>.json.
    if after:
        aftermath = scene_["Id"] + ".aftermath." + str(number)
        scene_["Nodes"].append(n(key, "Narrator", cut,
                                  c("Continue", aftermath), portrait="Nocticula"))
        scene_["Nodes"].append(n(aftermath, "Narrator", after,
                                  *old_choices, portrait="Nocticula"))
    else:
        scene_["Nodes"].append(n(key, "Narrator", cut,
                                  *old_choices, portrait="Nocticula"))


def polish_situation(s):
    """Situation receipts, sensory staging and slots for this route only."""
    sid = s["Id"]
    donor = sid.split(".acquired.")[0]
    if donor in {"noct.ending_company", "noct.ending_alliance", "noct.ending_limit", "noct.ending_ascent"}:
        # These are accounts of the actual harbor history, not prices added
        # to romance. Contradictory rescue/chart/lodge choices remain distinct.
        s["Nodes"][0].setdefault("Paragraphs", []).extend(harbor_receipts())
    if donor == "noct.unlit_quay":
        slot(s, "later", 1,
             "{n}She pulls you close on the balcony cushions. Beyond the rail, the city's lights burn until morning.{/n}",
             split="Later, the flower")
    elif donor == "noct.her_own_face":
        node(s, "start")["Text"] = '''{n}Nocticula sweeps the harbor accounts away. Their voices stop. A single lamp lights the couch, a bowl of pale fruit, and the book open on her knee. She closes it as you approach. The face she turns toward you is her own.{/n}
"The captains can wait. I have heard enough about their appetites."
{n}She eats one piece of fruit and holds the next at your mouth. Her thumb lingers against your lower lip, then withdraws. She shifts the book to leave a place beside her.{/n}
"I know what obedience sounds like. It grows dull. Tonight I want your company. Well?"'''
        node(s, "face")["Text"] = '''"My own face? You have developed an expensive preference."
{n}She turns your hand palm upward. Her fingertip follows a line across it, stopping at your wrist. When you look up she is already close enough to kiss you. You meet her; she stays, then draws back just far enough to see your mouth.{/n}
"There. No mask to blame when you come looking for it again."
{n}She catches the fastening at your collar but leaves it closed. Her hand rests there while she waits for you to sit.{/n}'''
        slot(s, "night", 1,
             "{n}She draws you down beside her, leaving the lamp where you can see her face. Later, the book lies open on the floor.{/n}",
             split="Later she lies beside you")
        # She dismisses the work herself; no reconstructed witness is in the bed.
        node(s, "start")["Text"] = node(s, "start")["Text"].replace(
            "This time there is no harbor.", "Nocticula sweeps the harbor accounts away with one hand. No voices remain in the chamber.")
    elif donor == "noct.second_door":
        node(s, "end")["Text"] = '''{n}At the door, Nocticula catches your sleeve. She straightens the fold she has gripped, then draws you back for a last kiss.{/n}
"I shall send for you. Keep the questions I disliked. I intend to win those arguments."
{n}You wake with the pull of her hand still in your shoulder. The lamp in Drezen has gone cold. A clerk knocks again: the morning dispatch is late. You reach for it before dressing, and find yourself looking for another invitation beneath the papers.{/n}'''
        slot(s, "yes", 1, "{n}She draws you close by the wrist. Later, the lamp still burns beside the couch.{/n}",
             split="Later, the lamp burns")
        slot(s, "power", 2, "{n}She pulls you down beside her. Much later, she remembers the courtier.{/n}",
             split="The curtains close")
    elif donor == "noct.unborrowed_evening":
        node(s, "want")["Text"] = '''"Nobody in that street knew what I intended to do next."
{n}She points the knife toward the perfume seller's shutters. The borrowed view sharpens for a moment: a stair, a torn garment, a woman watching the upstairs window.{/n}
"That woman thought I was somebody's expensive mistake. She told me to buy the room in my own name. I already owned the building."
{n}Nocticula sets the knife down beside the pear, then takes your plate away before you have finished with it.{/n}
"I wanted you here. I still do. Tell me what you want while the lodge can do nothing about it."'''
        node(s, "honest")["Text"] = '''{n}She cuts another slice of pear and holds it against your lower lip. When you reach for it, she draws it back and eats it herself.{/n}
"You have spent the evening confessing appetites. I had hoped to occupy one."
{n}Her foot finds your ankle beneath the couch. The knife stays on the plate; she watches your hand leave it there.{/n}
"Stay. The next report can wait until morning. Istrava is learning to wait for my answer. You may keep her company."'''
    elif sid == "noct.acq.the_retained_copy":
        node(s, "end")["Text"] = '''{n}Nocticula has written a time across the top of the clean sheet: after tomorrow's reports. Beneath it she has copied one line from your last question, changing nothing. You start a business reply. Her mark crosses the first figure before you finish it.{/n}
"Not that page. The other one."
{n}You put the ledger aside. Her next instruction arrives against the empty space where it rested.{/n}
"Finish your dispatches before then. I have no intention of sharing the whole evening with a quartermaster."
{n}You leave the clean sheet beside the half-seal and return to the remaining work.{/n}'''
    elif sid == "noct.acq.an_answer_of_her_own":
        node(s, "start")["Text"] = '''{n}The supply report is still under your hand when the mark moves. Nocticula has put her question across the blank margin.{/n}
"Did you choose a sentence, or spend the whole evening admiring your paper?"
{n}You turn the report over and ask whether she wanted this evening. Her reply cuts across the word wanted.{/n}
"Yes. You remain troublesome after I put down the report. I want to hear what else you will ask me for."
{n}The next stroke arrives smaller, crowded against the place where your fingers rest.{/n}
"Move your hand. I am not finished with you."'''
        slot(s, "accept", 1,
             "{n}You bring the sheet closer. Her next line arrives before the ink beneath your answer has dried. At dawn, the dispatch still waits.{/n}",
             split="At dawn, a last line")
    elif sid == "nocticula.trickster.defeated.chair":
        slot(s, "threshold", 1,
             "{n}Her cold hand closes over yours. Beyond the darkness, Threshold's fires burn through the night.{/n}")
        node(s, "threshold")["Text"] = node(s, "threshold")["Text"].replace(
            "The dark around her widens and closes over the two of you like a drawn curtain.",
            "A sentry's footsteps halt nearby. Nocticula turns her head toward the sound. Her shadow shuts out the campfires; the footsteps recede. She returns her attention to you.")
    elif sid == "nocticula.trickster.epilogue.commit":
        for host, number, cut in (
            ("kissed", 1, "She kept the Commander close in the royal chair. The last lamp burned low before morning."),
            ("knelt", 2, "She caught the Commander's hand and drew them nearer. The palace lamps burned low before morning."),
            ("walked", 3, "She drew the Commander down beside her. The last lamp burned low before morning."),
        ):
            slot(s, host, number, "{n}" + cut + "{/n}")
        collection = p("{n}The next spring a sealed note found the Commander: \"My favour. A chair at your right hand, wherever you eat. I did not ask for your bed.\" The Commander set it there. Nocticula came to dinner, looked once at the empty place beside her debtor, and sat down. She returned the following month without asking whether the refusal had changed.{/n}",
                       requires=("nocticula.trickster.cost.shade_paid",))
        # The legacy inert Continue exits stay exactly inert. Collection is
        # paid-only epilogue narration, independent of any romantic yes.
        for host in ("refused_page", "inn"):
            node(s, host).setdefault("Paragraphs", []).append(deepcopy(collection))
        node(s, "yes_page")["Text"] += "\n{n}A servant appears with a tray. Nocticula waves her out before she has crossed the threshold. The door shuts; the queen lays a hand on the chair's arm.{/n}"


def add_correspondence_visit(ep):
    """One authored postwar invitation. A letter is never bodily arrival."""
    if any(x["Id"] == "invitation" for x in ep["Nodes"]):
        return
    first = ep["Nodes"][0]
    first["Text"] = first["Text"].replace("in ink, in person, at whatever hour the wax chose", "in ink, at whatever hour the wax chose")
    # Preserve the old .continue suffix AND its inert mechanics.
    first["Choices"][0]["Id"] = "continue"
    first["Choices"].append(c("[Read her invitation.]", "invitation"))
    ep["Nodes"].extend([
        nt("invitation", '''"You have spent enough nights imagining my room. Come and inspect the error. One visit. Leave the undertaking where I can find it."
{n}The half-seal carried a date and the name of an Alushinyrra landing court. The Commander obtained a conjurer's price for passage and return, and set the offer beside Nocticula's invitation.{/n}''',
           c("[Make the journey.]", "arrival"),
           c("[Decline the visit. Keep answering by letter.]", "letters")),
        nt("arrival", '''{n}The Commander paid the conjurer for passage and return before leaving Golarion. The spell delivered them to the named court. A doorkeeper took the invitation inside. The Commander waited while the return papers grew damp in the night air. At last the doors opened. Nocticula stood beyond them, with the retained signature in her hand.{/n}
"I considered leaving you outside. Come in. I want to hear how you would have described the wait."''',
           c("[Enter at her invitation.]", "admitted"),
           c("[Use the paid return passage.]", "letters")),
        nt("admitted", '{n}Nocticula sent the attendants away. The old undertaking lay beside her glass. She had not torn it up.{/n}\n\"You wanted my company. Yes. Tonight I want yours.\"\n{n}She caught the Commander by the coat and drew them close. Her other hand stayed on the door until the Commander reached for her; then she closed it. Her mouth found theirs; she pulled the coat free of their shoulders and let it fall. The Commander caught her wrist as she reached for the next fastening. She smiled, guided that hand to her waist, and resumed.{/n}',
           c("[Stay with her.]", ep["Id"] + ".explicit.1"),
           c("[Keep the visit to conversation.]", "conversation")),
        n(ep["Id"] + ".explicit.1", "Narrator", "{n}Nocticula took the Commander's hand and closed the chamber door. At dawn, the half-seal rested beside the travel papers.{/n}",
          c("Continue", "morning"), portrait="Nocticula"),
        n("morning", "Narrator", "{n}At dawn she was still there, reading a broker's appeal over the Commander's shoulder. She crossed out his proposed fee, kissed the bare shoulder beneath her hand, and returned the travel papers.{/n}\n\"Go. Ask for the next visit through the mark. I may make you wait longer.\"",
          c(), portrait="Nocticula", paragraphs=visit_paragraphs()),
        n("conversation", "Narrator", "{n}Nocticula kept the Commander beside her until the landing court's bells sounded. When the return spell was due she rose, touched their mouth with one finger, and withdrew it smiling. The next letter arrived three nights later, with a correction to the last argument.{/n}",
          c(), portrait="Nocticula", paragraphs=visit_paragraphs()),
        n("letters", "Narrator", "{n}The Commander kept the letters. Nocticula answered the refusal with a single line: \"Then keep imagining it. I shall enjoy your mistakes.\" The next business report received her corrections. Later she sent another private question; the Commander answered in ink.{/n}",
          c(), portrait="Nocticula", paragraphs=visit_paragraphs()),
    ])
    for host in ("morning", "conversation", "letters"):
        node(ep, host)["Paragraphs"].extend(deepcopy(ending_paragraphs()))
    node(ep, "morning")["Paragraphs"].extend(late_discovery_paragraphs())


def visit_paragraphs():
    return (
        p("{n}Her renewed Gift remained a separate bargain. The half-seal still carried requests; it did not open the palace doors. She kept the signed undertaking beside the next unanswered letter.{/n}", requires=("noct.acq.gift_renewed",)),
        p("{n}The earlier Gift remained what it had been. Their correspondence had paid none of its debts. She retained the undertaking and answered the next request through the narrow mark.{/n}", requires=("noct.gift",), forbids=("noct.acq.gift_renewed",)),
        p("{n}No Gift came through the correspondence. The half-seal cooled without joining its missing half. The Commander still had to ask, and Nocticula still kept the signed undertaking.{/n}", forbids=("noct.gift", "noct.acq.gift_renewed")),
        p("{n}She had kept the surrendered sketch out of the correspondence. None of the subsequent invitations carried another copy of the exposed aperture.{/n}", requires=("noct.acq.sketch_surrendered",)),
    )


def add_acquisition_coda(payload, lastcall, partner):
    key = "nocticula.acquisition.lastcall.page"
    if any(x["Id"] == key for x in payload["Scenes"]):
        return
    guard = "nocticula.acquisition.lastcall.route_open"
    payload.setdefault("Derived", {})[guard] = [["trickster.ever"]]
    payload.setdefault("DerivedOpenRoutes", {})[guard] = ["nocticula.acquisition", "nocticula"]
    payload["Scenes"].append(scene(key, "The answering mark", "Epilogue", 1, "", [
        n("page", "Narrator", "{n}After the war, the half-seal moved while the Commander was putting away the travel accounts. \"Alive, then. Send me something worth my evening.\" The Commander wrote back. By midnight Nocticula had corrected one figure and left a second page for a private answer. The dispatch waited until morning.{/n}",
          c(), portrait="Nocticula", paragraphs=(*visit_paragraphs(), *ending_paragraphs())),
    ], requires=("trickster.ever", lastcall.ACTIVE, guard, "noct.acq.renewed_agreement"),
       forbids=("noct.complete", "noct.closed", "noct.acq.closed", "noct.dead", "sacrifice"), last=99,
       Relationship="lastcall", Partner="nocticula.acquisition",
       EpilogueAfter="scene:noct.acq.epilogue.correspondence",
       ForbidOverrides={"sacrifice": "trickster.commander_back"}))
    # Original coda has the same exit and earns a concrete subsequent return.
    if not any(x.get("Text", "").startswith("{n}The next visit") for x in partner["paragraphs"]):
        partner["paragraphs"] = (*partner["paragraphs"], p("{n}The next visit came at her summons. Nocticula found the Commander waiting, laid her hand over the latch, and opened the door herself. She had brought an argument about the Midnight Isles and kept the evening after losing it.{/n}"))


def harbor_receipts():
    from storylines.nocticula_n1 import placeholder
    return [
        p("{n}They named conflicts before turning them into bargains. Nocticula brought the next offer against one of the Commander's lovers to the quay herself. She watched the answer closely, then tore up the buyer's copy.{/n}", requires=("noct.conflicts_named",)),
        p("{n}The room stayed private. Nocticula sent back a broker's question about another lover unopened, with one cut made through its seal. The Commander's other rooms remained beyond that door.{/n}", requires=("noct.privacy_named",)),
        p("{n}Ilvara had seen the strengthened road. Nocticula kept the intact chart locked away and watched for a captain who had learned too much. The passengers' names stayed beside the price of the stronger crossing.{/n}", requires=("noct.door_reinforced", "noct.chart_intact")),
        p("{n}Vessa's damaged hand never vanished from the account of the narrower crossing. The crushed bell went back to her; Nocticula kept the broken instrument and sent away buyers who mistook it for a working road.{/n}", requires=("noct.door_unreinforced", "noct.vessa_injured", "noct.chart_lost")),
        p("{n}The allotted crossings were spent. Nocticula kept the final token beside the chart, and made the next petitioner explain why she should spend another.{/n}", requires=("noct.door_limited", "noct.chart_limited")),
        p("{n}The attendants received their canceled entries. Nocticula retained the purchased guarantor's signature; the next collector found her name where he had expected a frightened servant's.{/n}", requires=("noct.lodge_debt_purchased",)),
        p("{n}Tazren kept his original claim. Nocticula paid for the names of anyone still willing to buy it, and sent each buyer the published denial before asking how much he had lost.{/n}", requires=("noct.lodge_debt_denied",)),
        p("{n}Nocticula kept the lodge's guest list and position. The old attendants left with their possessions; a new chamberlain answered the door in her name.{/n}", requires=("noct.lodge_kept_house",), forbids=("noct.lodge_given_rhez",)),
        p("{n}The lodge stayed closed. Nocticula sent away an offer to reopen its hunting rooms, then brought the letter to the quay to complain about the profit the Commander had denied her.{/n}", requires=("noct.lodge_closed_house",)),
    ] + [p(placeholder("noct.harbor_receipts"), requires=("noct." + flag,))
         for flag in ("orren_hand_taken", "orren_lamp", "orren_given", "orren_run",
                      "captain_sold", "threat_sent", "returned_sold", "returned_harem",
                      "returned_released", "ilvara_executed", "sentence_overruled",
                      "quarry_istrava", "quarry_suth", "quarry_guests", "lodge_given_rhez",
                      "wager_lost", "laulieh_rewarded", "work_named")]
