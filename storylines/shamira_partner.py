"""Round 2a: Shamira's choice of lovers, in her existing game and court.

AUTHORED additions: the private summons to Nocticula, her written reply while
in hiding, and her discovery at the third bell. The Harem is already where she
visits her chosen lover (Shamira_dialogue/Cue_0066 216d0445, Cue_0116 5df0033b).
Shamira wants her throne, not release from her service (Trickster/Nocticula/
Cue_0021 84df3b22). Nocticula's defeat is not proof of permanent death:
Epilogues/Cue_2 bc753cb0 explicitly has her lying low. A returned Nocticula
speaks as a projection; this module grants neither her return nor a body.

All new decisions live inside existing Shamira scenes. No native edits, new
rest deliveries, costs, romance eligibility or presence rules. The late page
keeps its existing eligibility, but its relationship terms are now chosen.
"""
import copy

from story_format import c, n, p

STANCE = "shamira.partner_stance."
SHARE, EXCLUSIVE, SECRET = (STANCE + s for s in ("share", "exclusive", "secret"))
DEMANDED = "shamira.partner.exclusivity_demanded"
EXPOSED = "shamira.partner.secret_exposed"
PAID = "shamira.partner.public_claim"
BROKEN = "shamira.partner.affair_ended"
KNOWN = "shamira.partner.nocticula_knows"
DEAD = "noct.dead"
HIDING = "noct.defeated_not_dead"
RETURNED = "nocticula.trickster.returned"
P = "shamira.trickster."
COMMITTED, CLOSED, ALLY = "shamira.committed", "shamira.closed", P + "ally"


def sh(id, text, *choices, **kw):
    return n(id, "Shamira", text, *choices, portrait="Shamira", **kw)


def noct(id, text, *choices):
    # A reply delivered in her own words, not a spawned romance-route actor.
    return n(id, "Narrator", text, *choices, portrait="Nocticula")


def state_choices(prefix):
    """Disjoint, exhaustive current-state dispatch, never a return producer."""
    return [c("Continue", prefix + "returned", requires=(RETURNED,)),
            c("Continue", prefix + "hiding", requires=(HIDING,), forbids=(RETURNED,)),
            c("Continue", prefix + "dead", requires=(DEAD,), forbids=(RETURNED, HIDING)),
            c("Continue", prefix + "alive", forbids=(DEAD, RETURNED, HIDING))]


def terms_nodes(late=False):
    yes = () if late else (COMMITTED,)
    next_yes = "partner_late_won" if late else "rise"
    no = "partner_late_no" if late else None
    return [
        n("partner_status", "Narrator", "{n}Shamira holds you at arm's length. Her attention has gone past you, toward the doors of her Harem.{/n}",
          *state_choices("partner_status_")),
        sh("partner_status_alive", '''"Nocticula's palace still sends orders to my city. My lady will hear that I am back, and whom I have brought home."''', c("Continue", "partner_start")),
        sh("partner_status_hiding", '''"Nocticula's disappearance has left her throne empty. My lady is in hiding, not dead. Do not mistake her absence for my freedom."''', c("Continue", "partner_start")),
        sh("partner_status_returned", '''"Nocticula's palace has sent an answer through a projection. I cannot hold my lady's shadow. I can still want her. She can still want things from me."''', c("Continue", "partner_start")),
        sh("partner_status_dead", '''"Nocticula is gone. Nothing has answered me since she was struck down. I will not swear she is gone for good, to make a mortal comfortable."''', c("Continue", "partner_start")),
        sh("partner_start", '''{n}Shamira catches your wrist before you touch her.{/n} "Nocticula's palace had a place for me: steward of her city, and her chosen lover. This is where she came when she had tired of governing the Midnight Isles and wanted my mouth instead. I have not given her place away. Your coat on my floor will not buy it."
"Do you mean to share, Golarian? To demand I leave her? Or to fuck behind her back and hope my court keeps its mouth shut?"''',
           c('"Let her hear it from us. I will share you; I will not be your excuse."', "partner_share"),
           c('"End it with your lady. I want you for myself."', "partner_demand", flags=(DEMANDED,)),
           c('"Keep us from her. This is between you and me."', "partner_secret")),
        sh("partner_demand", '''{n}She presses your wrist against the arm of her throne.{/n} "You want me to send my lady away? From the Harem she named for me? I ruled her city and warmed her bed before you had a name worth remembering. I want her throne. I have not stopped wanting her."
{n}Her thumb strokes your pulse.{/n} "No. Take your hand away, if that spoils your appetite."''',
           c('"Then we stop here."', no, flags=(EXCLUSIVE, CLOSED)),
           c('"Very well. Tell her I will share."', "partner_share"),
           c('"Then let her know nothing of us."', "partner_secret")),
        sh("partner_secret", '''"A secret in Alushinyrra." {n}She smiles against your knuckles.{/n} "My servants sell what they hear. My lady knew how I smelled when I had been enjoying myself. And you will have to stand in my Harem when the court comes back."
"I could send you away. Instead, I shall enjoy watching you try."''',
           c("[Draw her close.]", next_yes, flags=(SECRET, *yes))),
        sh("partner_share", '''{n}She rings the little bell beside her throne. A servant appears at the far door.{/n} "A message for my lady. Private. The Commander has a proposition concerning her lover. Bring the answer to me, not to the court."
{n}The servant bows. Shamira waits with your wrist still in her hand.{/n} "She will want something. She always does. Decide whether you can stomach hearing it."''',
           *state_choices("partner_share_")),
        noct("partner_share_alive", '''{n}The servant brings a black silk pillow and a note in Nocticula's handwriting. Shamira passes the note to you. It smells of night-blooming flowers.{/n} "My steward has acquired a new appetite. How industrious. Keep each other occupied. But at the third bell she will name you to her court, and name whose city this is. No conspirators whispering into my lover's pillow. If you want my seat as well, come and ask me for it."
{n}Shamira drives the pin into the throne's arm.{/n}''',
           c('"Your city. Her choice of lovers. Mine too."', "partner_share_answer", flags=(KNOWN,))),
        noct("partner_share_returned", '''{n}A message from Nocticula's palace arrives as a shadow. Her projection takes shape beside the dais; the fountain's spray passes through her gown.{/n} "A borrowed body for my steward, and none for me. How thoughtful of you."
"You may share her attention. At the third bell she will name you to her court, and name whose city this is. A shadow can hear a conspiracy quite as well as flesh."''',
           c('"Let the court hear us both. I am asking for her, not your throne."', "partner_share_answer", flags=(KNOWN,))),
        n("partner_share_hiding", "Narrator", '''{n}The servant returns with a black silk pillow. Pinned to it is a note in Nocticula's handwriting.{/n} "My dear Shamira. You ask for a second lover as though you ever asked for the first. Enjoy your mortal. At the third bell, name your lover and name whose city this is. I shall hear. Do not mistake an empty chair for an invitation."
{n}Shamira drives the pin into the throne's arm, deep enough to split the wood.{/n}''',
          c('"She knows. Let the court hear it."', "partner_share_answer", flags=(KNOWN,)), portrait="Nocticula"),
        sh("partner_share_dead", '''{n}The servant comes back alone. Shamira dismisses him with a flick of her fingers.{/n} "My lady is gone. No reply, no trace of her. I will not dress a servant in her voice to give you an answer."
"There is no arrangement to make with her now. If she comes back, she will answer for herself. Until then, I shall keep her place. If you mean to demand I give it up, my answer is no. You may decide whether that is enough."''',
           c('"Keep her place. I will share if she returns."', next_yes, flags=(SHARE, *yes)),
           c('"Then we stop here. I will have you for myself, or not at all."', no, flags=(DEMANDED, EXCLUSIVE, CLOSED))),
        sh("partner_share_answer", '''"Her city." {n}Shamira says it through her teeth. Then she draws you between her knees.{/n} "There. She has her announcement. You have your answer. I have two lovers and a court that will start counting which one I look at first."
{n}Her hand closes on the back of your neck.{/n} "Do not grow tedious about it. Either of you."''',
           c("[Kiss her.]", next_yes, flags=(SHARE, PAID, *yes))),
    ]


def discovery_nodes(late=False):
    resume = "partner_late_end" if late else "bell_end"
    return [
        sh("partner_discovery", '''{n}At the third bell a servant brings a black silk pillow to the dais. The music stops. Shamira tears the note from it and reads; her mouth hardens.{/n}
"My lady has heard who kept me occupied. Someone in this room has been selling our nights. I shall find them." {n}She lets the court see the pin between her fingers.{/n} "First, we answer her."''',
           *state_choices("partner_found_")),
        noct("partner_found_alive", '''{n}The note bears Nocticula's handwriting and seal. Shamira reads it aloud to her court.{/n} "No need to search for an informant, my dear. The whole city was watching your new lover arrive. Commander, you hid it because you feared my answer. Now you will hear it before her court. Name what you are to her, and whose city this is. Or leave her bed. I will not keep a conspiracy warm for you."
{n}Shamira has the servant take the pillow back. He remains at the door, waiting for her answer.{/n}''',
           c("Continue", "partner_price")),
        noct("partner_found_returned", '''{n}The gift from Nocticula's palace has brought a shadow with it. Her projection gathers beside the throne. Shamira's hand passes through it when she reaches for the pin.{/n} "Still trying to grasp what you cannot hold, my dear."
{n}The shadow looks at you.{/n} "You kept your affair from me. Now name it before her court, and name whose city this is. Or leave her bed. You have seen how far a shadow can reach. Shall I demonstrate again?"''',
           c("Continue", "partner_price")),
        n("partner_found_hiding", "Narrator", '''{n}Shamira reads the note aloud. Nocticula's handwriting fills only three lines.{/n} "Your court has been most informative. Name your mortal lover before them, and name whose city this is. Or send the mortal away. I shall know which you choose."
{n}The demons on the couches look everywhere except at one another. Shamira crumples the silk pillow in her fist.{/n}''',
          c("Continue", "partner_price"), portrait="Nocticula"),
        sh("partner_found_dead", '''{n}Shamira turns the note over.{/n} "No seal. No reply from my lady since she was struck down. Somebody is playing her with a borrowed hand."
{n}She has the servant dragged before the dais.{/n} "You will tell me whose. Slowly." {n}In your mind, her voice is colder.{/n} "The court knows. If she ever answers again, she will hear it from them. Our secret has bought us an enemy who knows what to sell."''',
           c("[Stay beside her.]", resume, flags=(EXPOSED,))),
        sh("partner_price", '''{n}Shamira looks over the silent court.{/n} "You wanted a secret. You have cost me the pleasure of announcing my own lover. Now she makes us do it under her seal."
{n}She holds out her hand to you, palm up.{/n} "I will say whose city it is. You will say what you came here for. Refuse, and get out. I will not have you skulking in my Harem while she holds this over me."''',
           c('"I am Shamira\'s lover. Her lady rules Alushinyrra."', "partner_paid", flags=(EXPOSED, PAID, KNOWN)),
           c('"I will not make our bed her business."', "partner_broken", flags=(EXPOSED, BROKEN, CLOSED))),
        sh("partner_paid", '''"My lady's city." {n}Shamira's voice carries to the doors. She draws you to her side, then waves the musicians back to work.{/n}
{n}In your mind:{/n} "Listen to them whisper. Every claim I make for the next century will be answered with those words. You will stand here and hear it with me."
{n}She turns the pin between her fingers.{/n} "And my lady will discover how much I still enjoy finding things she wants kept from her."''',
           c("[Remain at her side.]", resume)),
        sh("partner_broken", '''{n}She closes her empty hand.{/n} "Then take yourself out of it. No more nights on my dais. No more mouth against mine."
{n}She addresses the court without looking at you.{/n} "The Commander is leaving. See that nobody detains our guest."
{n}Inside your head, one last order:{/n} "I shall take the coal that keeps this body alive. Nothing else. Do not mistake that for an invitation."''',
           c("[Leave the Harem.]", "partner_late_no" if late else None)),
    ]


def partner_paragraphs(condition="body"):
    """Current partner position plus chosen terms, on every ending surface."""
    whereabouts = {
        "body": "Shamira had returned to her Harem in flesh. Nocticula still claimed her as her chosen lover; Shamira still coveted her throne.",
        "alive": "Shamira remained in the Harem of Ardent Dream, Nocticula's chosen lover and ambitious steward.",
        "mind": "Shamira had no body to bring to Nocticula's bed. What remained of the Ardent Dream was inside the Commander's mind; her old lover had no place there.",
        "gone": "Shamira was gone. Nocticula's chosen lover had left no body that could answer a summons to her bed.",
    }[condition]
    paragraphs = (
        p("{n}Nocticula's palace remained the seat of the Midnight Isles' ruler. Its mistress still held her throne. " + whereabouts.replace("Nocticula", "Her lady") + "{/n}", forbids=(DEAD, HIDING, RETURNED)),
        p("{n}Nocticula's disappearance after her defeat had left her throne empty. Its mistress lay low in the shadows, still alive. " +
          ("Shamira's tie to her old lover stretched across that absence; no summons brought her back to the Harem." if condition in ("body", "alive") else
           "Her bond with Shamira survived only in what each had once wanted of the other.") + "{/n}", requires=(HIDING,), forbids=(RETURNED,)),
        p("{n}Nocticula's disappearance after she was struck down had yielded no reply, no trace. There was no answer to Shamira's name from her old lover, and no certainty about what the shadows concealed.{/n}",
          requires=(DEAD,), forbids=(HIDING, RETURNED)),
        p("{n}Nocticula's palace had sent an answer through a projection. Her returned shadow carried her voice, without restoring her body. " +
          ("Shamira still wanted her old lover, and still wanted her throne, but there was no body to bring to her bed. Their messages carried invitations and threats in the same hand." if condition in ("body", "alive") else
           "Her former lover Shamira could offer no body in return. What had passed between them remained a claim without a bed.") + "{/n}", requires=(RETURNED, "trickster.now")),
        p("{n}Nocticula's palace had sent an answer through a projection while the Commander's tricks still had power. Her old lover's shadow had survived the loss of that power; no flesh had been restored to her.{/n}", requires=(RETURNED,), forbids=("trickster.now",)),
        p('''{n}The Commander had demanded Shamira give up her old lover. Shamira had refused. Their romance went no further; her old lover's place had never been the Commander's to give away.{/n}''', requires=(EXCLUSIVE,)),
        p('''{n}The Commander had chosen to share Shamira with her old lover. The bargain named the Commander's place in the Harem and her lady's rule over the city; Shamira had spoken the latter through her teeth. Neither woman surrendered her appetite or her ambitions.{/n}''', requires=(SHARE, PAID)),
        p('''{n}The Commander had agreed to keep her old lover's place if she returned. With no answer from her, there had been no bargain to claim she accepted.{/n}''', requires=(SHARE,), forbids=(PAID,)),
        p('''{n}The Commander had chosen a secret affair with Shamira. Her old lover had received no confession; the Harem's servants had something valuable to sell. Her claim remained, and the secret remained an unpaid risk.{/n}''', requires=(SECRET,), forbids=(EXPOSED,)),
        p('''{n}The affair had been exposed before Shamira's court. To keep her, the Commander had named their bed and her lady's rule over Alushinyrra in public. Shamira made the Commander stand beside her whenever the court repeated those words. The announcement had bought no forgiveness.{/n}''', requires=(SECRET, EXPOSED, PAID), forbids=(BROKEN,)),
        p('''{n}The secret had reached Shamira's court while her old lover remained unanswered. A forged message had brought an enemy to light; it had not settled her claim. Shamira kept the culprit alive long enough to learn who else knew.{/n}''', requires=(SECRET, EXPOSED), forbids=(PAID, BROKEN)),
        p('''{n}When the affair was exposed, the Commander refused to name it before the court. Shamira ended it herself. She took only the coal owed for her body, and left the Commander's bed cold.{/n}''', requires=(BROKEN,)),
        p('''{n}The Commander never settled a lover's claim against Shamira's lady. Shamira's old bond was no promise of a place for anyone else.{/n}''', forbids=(SHARE, EXCLUSIVE, SECRET)),
    )
    # Return receipts and the native defeat flag are separate inputs. Keep
    # both serializations covered, without claiming a second physical return.
    out = []
    for paragraph in paragraphs:
        if RETURNED in paragraph["Requires"]:
            without_death = copy.deepcopy(paragraph)
            paragraph["Requires"].append(DEAD)
            without_death["Forbids"].append(DEAD)
            out.extend([paragraph, without_death])
        else:
            out.append(paragraph)
    return tuple(out)


def late_current_paragraphs(node):
    """Brief context on each book page, including the pages between decisions."""
    alive = {
        "partner_status": "Nocticula's palace still had its mistress. Shamira's old lover ruled the city beyond these doors.",
        "partner_start": "Nocticula's court still served the ruler whose lover was offering the Commander her hand.",
        "partner_demand": "Nocticula's palace remained hers. Shamira wanted its mistress as well as her throne.",
        "partner_secret": "Nocticula's court had ears throughout the city. Its living mistress still had a claim on this room.",
        "partner_share": "Nocticula's palace received the summons. Shamira was asking her living lover to answer it.",
        "partner_share_answer": "Nocticula's court would hear the bargain. Its mistress kept her old lover, and her sovereignty.",
        "partner_late_won": "Nocticula's palace stood elsewhere in the city. Its mistress remained Shamira's lover; this night had not dismissed her.",
        "partner_late_court": "Nocticula's court still watched the Harem. Its mistress had not surrendered her claim on Shamira.",
        "partner_discovery": "Nocticula's handwriting carried the authority of a living ruler, and the anger of Shamira's old lover.",
        "partner_price": "Nocticula's court waited for the answer. Its mistress remained Shamira's lover whichever way the Commander chose.",
        "partner_paid": "Nocticula's court would repeat that announcement. Its mistress kept her place as Shamira's lover and ruler.",
        "partner_broken": "Nocticula's palace still had its mistress. Shamira had refused to give up her old lover; now she had sent the Commander away.",
    }.get(node, "Nocticula's palace remained hers. Its mistress was still Shamira's chosen lover, and the city's ruler.")
    paragraphs = copy.deepcopy(list(partner_paragraphs()[:7]))
    for paragraph in paragraphs:
        if RETURNED in paragraph["Requires"]:
            text = "Nocticula's palace had answered through a projection. Shamira's old lover had survived, without flesh to bring to her bed."
        elif HIDING in paragraph["Requires"]:
            text = "Nocticula's disappearance had left the throne empty. Shamira's old lover was alive in hiding; the distance had not released her claim."
        elif DEAD in paragraph["Requires"]:
            text = "Nocticula's disappearance remained unanswered. Shamira kept her old lover's place without knowing whether anything would ever claim it again."
        else:
            text = alive
        paragraph["Text"] = "{n}" + text + "{/n}"
    return paragraphs


def integrate(payload):
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    # Sweep sibling claims that put Nocticula on her throne after defeat.
    for suffix in ("", "_awning"):
        city = scenes[P + "after.city" + suffix]
        for node in city["Nodes"]:
            old = [choice for choice in node["Choices"] if choice.get("Next") in ("lady", "lady_unsure", "hiding")]
            if not old:
                continue
            common = (P + "cost.ramisa_story",) if node["Id"] in ("talk", "cruel") else ()
            for choice in old:
                choice["Forbids"].append(RETURNED)
                if choice.get("Next") != "hiding":
                    choice["Forbids"].append(DEAD)
            node["Choices"].extend([
                c("Continue", "partner_city_returned", requires=(RETURNED,), forbids=common),
                c("Continue", "partner_city_unanswered", requires=(DEAD,), forbids=(RETURNED, HIDING, *common))])
        city["Nodes"].extend([
            sh("partner_city_returned", '''"My lady has answered through a projection. A shadow instead of the woman who came for me across the black water." {n}Shamira turns her cup.{/n} "I have come back in flesh. She has not. I wonder how much she will enjoy that."''', c("Continue", "cold")),
            sh("partner_city_unanswered", '''"Nothing from my lady since she was struck down. No pillow, no knife, no word." {n}Shamira watches the street.{/n} "I shall not take her silence for an invitation. Or a grave."''', c("Continue", "cold")),
        ])
        throne = scenes[P + "after.throne" + suffix]
        chair = next(node for node in throne["Nodes"] if node["Id"] == "chair")
        for choice in chair["Choices"]:
            choice["Forbids"].append(RETURNED)
            if choice.get("Next") != "hiding":
                choice["Forbids"].append(DEAD)
        chair["Choices"].extend([
            c("Continue", "partner_throne_returned", requires=(RETURNED,)),
            c("Continue", "partner_throne_unanswered", requires=(DEAD,), forbids=(RETURNED, HIDING))])
        throne["Nodes"].extend([
            sh("partner_throne_returned", '''"She answers through a projection. I can sit in a chair, take a cup, kiss a mouth. She cannot do those things in flesh." {n}Shamira smiles into her wine.{/n} "It does not make the Midnight Isles mine. I intend to enjoy the distinction while it lasts."''', c("Continue", "ask")),
            sh("partner_throne_unanswered", '''"She was struck down. I have heard nothing since. Everyone has an opinion about where she is. Nobody will put their neck behind it." {n}Shamira sets down her cup.{/n} "I want her throne. I would rather know whether its mistress is still waiting behind it."''', c("Continue", "ask")),
        ])
    for id in (P + "harem", P + "harem_awning"):
        s = scenes[id]
        nodes = {n["Id"]: n for n in s["Nodes"]}
        # The original yes still loses the game. Commitment follows her answer
        # about Nocticula, so neither the exclusive demand nor her refusal grants it.
        nodes["search"]["Choices"][0]["Set"].remove(COMMITTED)
        # The original exported yes already required current Trickster power.
        # Moving its commit setter must not remove that existing entry guard.
        nodes["search"]["Choices"][0]["Requires"].append("trickster.now")
        # That setter also used to produce this exported off-path fallback.
        # Preserve its original answer index even though it is now explicit.
        nodes["search"]["Choices"].append(c("[Leave.]", forbids=("trickster.now",), abort=True))
        nodes["lost"]["Choices"][0]["Next"] = "partner_status"
        nodes["steps"]["Text"] = nodes["steps"]["Text"].replace(
            "she says aloud, and it is the only word spoken in the Harem that night.", "she says against your mouth.")
        s["Nodes"].extend(terms_nodes())
        # Use the existing third-bell court, before any departure through the arch.
        for source in ("fool", "guest", "equal", "steward"):
            for choice in nodes[source]["Choices"]:
                if choice.get("Next") == "bell_end":
                    choice["Forbids"].append(SECRET)
                    new = copy.deepcopy(choice)
                    new["Forbids"].remove(SECRET)
                    new["Requires"].append(SECRET)
                    new["Next"] = "partner_discovery"
                    nodes[source]["Choices"].append(new)
                    break
        s["Nodes"].extend(discovery_nodes())
        # Share pays with the same court announcement, regardless of court role.
        nodes["bell_silence"]["Text"] += ('\n{n}Before the court can choose a name for you, Shamira gives them one: '
            '"My lover." She makes them wait, then adds, "In my lady\'s city."{/n}')
        # The secret branches use a different opening: secrecy is not proclaimed
        # until discovery forces the declaration.
        # Route every incoming edge through a flag dispatch; preserve all old nodes.
        shared = copy.deepcopy(nodes["bell_silence"])
        shared["Id"] = "partner_public_court"
        nodes["bell_silence"]["Text"] = nodes["bell_silence"]["Text"].split("\n{n}Before the court", 1)[0]
        for node in s["Nodes"]:
            for choice in node["Choices"]:
                if choice.get("Next") == "bell_silence":
                    choice["Next"] = "partner_court"
        s["Nodes"].extend([n("partner_court", "Narrator", "{n}The court waits for Shamira to speak.{/n}",
                             c("Continue", "partner_public_court", requires=(SHARE, PAID)),
                             c("Continue", "bell_silence", requires=(SHARE,), forbids=(PAID,)),
                             c("Continue", "bell_silence", forbids=(SHARE,))), shared])

    late = scenes[P + "epilogue.late"]
    late["Nodes"][0]["Text"] = '''{n}The war ended before Shamira could finish her game. A month after Threshold she came to the Commander's window, her red hair smelling of the Abyss. She said she had come for the round she was owed, and took the Commander through the wardrobe to her Harem. Before she reached into the Commander's thoughts, she held out one hand and waited.{/n}'''
    late["Nodes"][0]["Choices"][0]["Next"] = "partner_status"
    late["Nodes"][0]["Choices"][0]["Id"] = "continue"  # saves reference the legacy .continue answer
    late["Nodes"].extend(terms_nodes(late=True))
    late["Nodes"].extend([
        n("partner_late_won", "Narrator", '''{n}Shamira went through the Commander's thoughts and found herself in every room. The Commander did not try to hide her. She slipped the pins from her hair and let her gown fall among them, then drew the Commander down onto the warm steps of her throne. Her mouth opened against the Commander's; her hand pulled at the coat between them. The fountains drowned the sound of the first fastening breaking.{/n}''',
          c("Continue", "partner_late_court")),
        n("partner_late_court", "Narrator", '''{n}At the third bell she led the Commander before her court. The demons on the couches had already heard who had kept her away from them.{/n}''',
          c("Continue", "partner_discovery", requires=(SECRET,)),
          c("Continue", "partner_late_end", forbids=(SECRET,)),
          paragraphs=(p('''{n}Shamira put her hand on the Commander's shoulder. "My lover," she told the court. She waited until the whispering stopped. "In my lady's city." Her fingers dug into the Commander's coat; she held them there until the musicians began to play.{/n}''', requires=(SHARE, PAID)),)),
        n("partner_late_end", "Narrator", '''{n}Shamira kept the Commander's place beside her throne. In the Commander's room, a chair faced the wardrobe. Neither invitation concealed who else still had a claim.{/n}''', paragraphs=partner_paragraphs()),
        n("partner_late_no", "Narrator", '''{n}Shamira returned to her Harem. The Commander had a debt to her body, and no welcome in her bed.{/n}''', paragraphs=partner_paragraphs()),
    ])
    late["Nodes"].extend(discovery_nodes(late=True))

    door = scenes[P + "epilogue.closed_door"]
    door.setdefault("ForbidOverrides", {})[COMMITTED] = BROKEN
    door["Nodes"][0]["Text"] = '''{n}Shamira returned to the Harem of Ardent Dream. She took the coal that kept her stolen body alive from the edge of the Commander's sleep, without a word. The Commander never mistook that silence for company.{/n}'''
    door["Nodes"][0].setdefault("Paragraphs", []).append(p(
        '''{n}The Commander had thrown her out of her own trade, in her own Harem. She never spoke the Commander's name again.{/n}''', forbids=(BROKEN, EXCLUSIVE)))
    for id, s in scenes.items():
        if id.startswith(P + "epilogue."):
            suffix = id.rsplit(".", 1)[-1]
            condition = ("alive" if suffix == "never" else "mind" if suffix in ("captive", "unhoused")
                         else "gone" if suffix in ("cast_out", "drowned", "mourned") else "body")
            node = s["Nodes"][0]
            node.setdefault("Paragraphs", []).extend(partner_paragraphs(condition))
            # Retained historical knowledge is not a current living audience.
            for para in node["Paragraphs"]:
                if P + "court.guest" in para.get("Requires", []):
                    # A public lover can still enter court as her guest. The
                    # old "never came near the truth" claim cannot survive it.
                    para["Text"] = '''{n}In the Harem of Ardent Dream the Commander was always her guest, who drank her wine without asking, and whom she had not yet killed. Every visit started another quarrel over how much her invitation was worth.{/n}'''
                if "nocticula.trickster.secret_known.shamira" in para.get("Requires", []):
                    para["Forbids"].extend([DEAD, HIDING, RETURNED, SHARE, EXPOSED])
    for node in late["Nodes"][1:]:
        if node["Id"] not in ("partner_late_end", "partner_late_no"):
            node.setdefault("Paragraphs", []).extend(late_current_paragraphs(node["Id"]))

    # Last Call builds its coda after this route. Change only Shamira's entry,
    # through the route integration, without editing the shared Last Call file.
    from storylines import lastcall_partners
    part = next(part for part in lastcall_partners.PARTNERS if part["key"] == "shamira")
    if not any(SHARE in para.get("Requires", []) for para in part["paragraphs"]):
        part["paragraphs"] = (*part["paragraphs"], *partner_paragraphs())
