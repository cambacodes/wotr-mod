"""History-safe prose joins for existing Tirabade saves and late starts."""
from copy import deepcopy
from story_format import c, n

SCENES = []


def integrate(payload):
    books = {s["Id"]: s for s in payload["Scenes"]}
    reunion = books["return"]
    pages = {node["Id"]: node for node in reunion["Nodes"]}
    if "before_the_abyss" in pages:
        raise ValueError("Tirabade chronology overlay applied twice")
    pages["now"]["Text"] = '''"Some things are better. Some are not. I would rather tell you which than make you guess."
{n}Irabeth describes an evening when she took her papers to bed. Anevia supplies the detail she omitted: her wife had fallen asleep before reading them, leaving Anevia to rescue a page from beneath her elbow.{/n}
"You could have woken me."
"I wanted you asleep. Wanted the paper somewhere else. Managed both."
{n}Irabeth smiles, then looks at you.{/n}
"We are still learning which things need an argument and which need a little room on the bedside table. I would rather you knew that than thought we had settled everything before inviting you in."
"And you get to tell us when we're crowding your side of it," Anevia adds. "We can be very considerate about a question we haven't let you answer yet."'''
    pages["back"]["Text"] = '''"I miss how easy some of it felt, too."
{n}Anevia leans toward you.{/n}
"Not the hiding. Before that, when seeing you was a good part of the day and I hadn't started making excuses for it. I'd like more of the good part."
{n}Irabeth takes your hand.{/n}
"So would I. But I do not want to call a conversation finished because we enjoyed the way it began. We can keep what we want without pretending nothing has changed."'''
    # Departure is Chapter 3 only and requires the negotiated table scene.
    # Current Chapter 5 flags alone cannot date an older conversation.
    pages["start"]["Choices"].append(c(
        '"Before I left for the Abyss, you told me you would keep living. I want to hear about it."',
        "before_the_abyss", requires=("departure",)))
    reunion["Nodes"].append(n("before_the_abyss", "Irabeth", '''"You remembered."
{n}Irabeth looks at Anevia, who gives her a small nod.{/n}
"There were evenings when I wanted to tell you something and reached for paper before remembering how little chance it had of finding you. Eventually I told Anevia some of it instead."
"Some," Anevia says. "She saved a complaint about a recruit's boots for your personal attention."
"It was an impressive complaint."
{n}Anevia laughs, then reaches across the table for your hand.{/n}
"We missed you. We also had things to say to each other that weren't about waiting. I don't want to lose those now you're here."
"Nor do I," Irabeth says. "And I want to hear what you have to tell us, when you are ready. We need not fit all of it into this evening."''',
        c('"Then begin with something from your days here."', "now")))

    night = books["shared_night"]
    pages = {node["Id"]: node for node in night["Nodes"]}
    pages["close"]["Text"] = '''{n}Anevia says something irreverent against Irabeth's cheek. Irabeth laughs and draws her closer, then turns toward you without letting her wife go.{/n}
{n}You kiss her. Anevia's hand settles warmly against your back. When you shift to make room for her, she touches your face and waits until you meet her eyes before leaning in.{/n}
"Still all right?" Irabeth asks.
{n}You answer her. Anevia answers too, with a pleased little smile which becomes another kiss. The lamp is turned low, and the rest of the evening passes beyond the reach of reports and explanations.{/n}'''
    for sid, flag, text in (
        ("three_small_journeys", "three_small_journeys.night", '"I have been thinking about the night we stayed together after looking at the map."'),
        ("three_open_road", "three_open_road.night", '"I remember the night you wore the blue coat for us. I would like another night together."'),
        ("three_rooms_unlocked", "three_rooms_unlocked.night", '"I liked waking with you both in Tessa\'s room. I want another morning like that."'),
    ):
        # The choice flag can survive interruption before the night completes.
        pages["near"]["Choices"].append(c(text, "familiar", requires=(sid, flag)))
    night["Nodes"].append(n("familiar", "Anevia", '''"So have I. Though I was trying to concentrate on this evening."
{n}Anevia's teasing softens as Irabeth takes her hand. Her wife looks at you with a smile you have seen across a pillow before.{/n}
"I liked waking up and finding you still there," Irabeth says. "I would like that again."
"After we've enjoyed the bit before sleeping," Anevia adds.
{n}Irabeth laughs and draws her wife close enough to kiss her. Anevia answers without hurrying, then reaches toward you. There is pleasure in recognizing the invitation and being wanted all over again.{/n}''',
        c('[Join them for another night together.]', "close")))

    loss = books["ending_loss"]["Nodes"][0]
    loss["Text"] = '''{n}War had taken a future the three had wanted. The days they had shared were not made less real by losing the days still ahead. Private hopes remained in ordinary things: a book left open, a cup set out before its owner remembered, a place someone still turned to look.{/n}
{n}No promise made in tenderness overruled the loss. No intimacy changed the choices that had brought them to it. Those who remained were left with the difficult freedom of deciding what to do with love that could no longer be returned in the way they had wished.{/n}
{n}The crusade's histories preserved victories and sacrifices. They had little room for the smaller things that made the sacrifices unbearable.{/n}'''


def integrate_morale(payload):
    # Append after negotiated joins to preserve existing answer GUIDs.
    books = {scene["Id"]: scene for scene in payload["Scenes"]}
    reunion = books["return"]
    pages = {node["Id"]: node for node in reunion["Nodes"]}
    pages["now"]["Choices"].append(c(
        '"And the days when you cannot find much confidence in yourself?"',
        "morale", requires=("broken",)))
    reunion["Nodes"].append(n("morale", "Irabeth", '''"I still have them."
{n}Irabeth turns her cup once, aligning its handle with the edge of the table.{/n}
"A report arrives and I know what I would have told another officer to do. Then I sit there looking for the mistake I must have missed. Sometimes I find one. That does not help me trust the next answer."
"She still gives it," Anevia says.
"Yes. I do."
{n}Irabeth looks up before her wife can add anything.{/n}
"I would like to come to supper without having to give you a better account of myself first. I may have very little to say."
"I can provide enough conversation for three," Anevia offers.
"That was not in doubt."
{n}The reply brings a brief smile. Irabeth leaves the cup where it is.{/n}
"And I want to hear about your day. Even a bad one. I am tired of everyone deciding what news I can bear."''',
        c('"Then I will tell you about mine, and leave you to tell me what you wish."', "future")))

    pages["now"]["Choices"].extend([
        c('"There is also the scar I gave you. I have not forgotten it."', "scar", requires=("irabeth.scar_known",)),
        c('"I remember what you told me about the Queen at Iz."', "queen", requires=("irabeth.queen_loss_known",)),
    ])
    reunion["Nodes"].extend([
        n("scar", "Irabeth", '''{n}Irabeth's fingers stop against the cup.{/n}
"I would rather not discuss it again."
{n}Anevia looks at you. Her expression has lost its warmth.{/n}
"Then don't make her explain it for you. If you've got something to say about what you did, say that."
{n}Irabeth turns toward her wife, but Anevia holds her gaze.{/n}
"I heard what you said, Beth. I haven't agreed with it."
{n}For a moment neither woman looks at you. Then Irabeth sets the cup down.{/n}
"Well?"''',
            c('"I will not ask either of you to call it a kindness."', "scar_quiet"),
            c('"I still believe it was necessary."', "scar_disputed"),
            c('[Respect her request and leave the subject.]', "scar_quiet")),
        n("scar_quiet", "Narrator", '''{n}Irabeth nods once. She does not touch her face or offer an explanation.{/n}
{n}Anevia draws the lamp away from the edge of the table. For a while, its small scraping sound is the only answer she gives you.{/n}
"I'd like some air," she says at last.
{n}Irabeth rises with her. At the door she pauses, one hand resting on the latch.{/n}
"We will speak another evening."
{n}She leaves with her wife. The cups remain on the table.{/n}''',
            c('[Let the evening end here.]', flags=("tirabade.scar_left_unsettled",))),
        n("scar_disputed", "Anevia", '''"I know what you believe. I was hoping you had something else to say."
"Anevia."
"No, Beth. You can think it helped you. I watched you keeping the mark because you thought you deserved it. I don't have to be pleased."
{n}Irabeth looks down at her hands, then back at you.{/n}
"I do not want to spend this evening defending my answer to either of you."
{n}Anevia's reply comes more quietly.{/n}
"All right."
{n}She collects her wife's cloak. When Irabeth stands, Anevia hands it to her without looking at you.{/n}
"I'm going with her. We can leave the rest for another day."
{n}Irabeth waits by the door until her wife joins her.{/n}''',
            c('[Let them leave without demanding agreement.]', flags=("tirabade.scar_left_unsettled", "tirabade.scar_defended"))),
        n("queen", "Irabeth", '''"Then you remember what I said about relying on me."
{n}Anevia opens her mouth, then shuts it. Irabeth notices.{/n}
"You need not agree. Neither of you. But I was there, and she did not come back."
{n}She pulls the unused saucer toward her. There is a chip in its rim; she turns it out of sight.{/n}
"I have begun three letters to people who will want to know what happened. I keep finding a way to write about the battle without saying that I came home."
"Who are they for?" Anevia asks.
{n}Irabeth gives her the names. This time her wife listens without trying to finish the answer.{/n}''',
            c('"We can sit with you while you write, if you want."', "queen_letters"),
            c('"You need not finish them tonight. I would still like to hear what you want next."', "future")),
        n("queen_letters", "Narrator", '''{n}Irabeth fetches the unfinished pages. Anevia clears a place beside the lamp and sits down again.{/n}
"I want to write it myself," Irabeth says.
{n}She reads the first line under her breath. Crosses out a word. Leaves the next sentence alone.{/n}
{n}Anevia catches your eye when you move to speak. You let the silence stand. After a while Irabeth asks for fresh ink, and her wife goes to find it.{/n}
{n}You remain beside her. By the time Anevia returns, Irabeth has reached the sentence she could not write before. She does not read it aloud.{/n}''',
            c('[Stay while she writes, without offering words for her.]', flags=("tirabade.queen_letters_shared",))),
    ])

    watch = books["last_watch"]
    for page in watch["Nodes"]:
        for choice in list(page["Choices"]):
            if choice.get("Next") == "life":
                # Keep existing answer positions and GUIDs; append the conditional alternative.
                alternate = deepcopy(choice)
                alternate["Next"] = "life_broken"
                alternate["Requires"].append("broken")
                page["Choices"].append(alternate)
                choice["Forbids"].append("broken")
    watch["Nodes"].append(n("life_broken", "Irabeth", '''"I have kept the list. The places we spoke about."
{n}Irabeth takes a folded sheet from her pocket. One corner has worn through.{/n}
"There are days when I think I should hand everything over to someone better and be grateful if they let me go. Then I look at this and find myself planning the road as though I had already earned the journey."
"You can plan a road without putting yourself on trial," Anevia says.
{n}Irabeth presses the fold flat with her thumb. She does not answer at once.{/n}
"I know what you mean. I cannot always believe it."
{n}Anevia sits closer. She reads the first place on the sheet, then the second.{/n}
"That one's three days out of our way."
"Four. The shorter road floods."
"Then we'd better hope the view's worth it."
{n}Irabeth almost smiles. When she offers you the page, her hand is steady.{/n}
"Will you keep a copy? I would like someone else to know the way, on the days when I cannot see much beyond the next duty."''',
        c('"Yes. We can choose the first road together when there is time."', "end")))

    watch_start = next(node for node in watch["Nodes"] if node["Id"] == "start")
    watch_start["Choices"].extend([
        c('"We left a difficult evening unfinished. I have not forgotten that either."', "scar_unsettled",
          requires=("tirabade.scar_left_unsettled",)),
        c('"Did you send the letters you wrote while we sat together?"', "queen_letters",
          requires=("tirabade.queen_letters_shared",)),
    ])
    watch["Nodes"].extend([
        n("scar_unsettled", "Anevia", '''"Good."
{n}Anevia's answer is short. Irabeth looks between you.{/n}
"I don't want to spend tonight on it," she says.
"Neither do I. But I don't want a grand farewell to do the arguing for us."
{n}Anevia reaches for her wife's hand. When she looks back at you, the anger has not vanished from her face.{/n}
"I want us to come back. Then we'll still have things to say."
{n}Irabeth's thumb moves across her wife's knuckles.{/n}
"I would rather have the time for an argument than have everything left unsaid."''',
            c('"Then let us speak about coming home."', "life", forbids=("broken",)),
            c('"Then let us speak about coming home."', "life_broken", requires=("broken",))),
        n("queen_letters", "Irabeth", '''"Yes. I read them once more in the morning, then sent them."
{n}Irabeth smooths a crease in her sleeve.{/n}
"I nearly asked to have them brought back. Anevia had already given them to the courier."
"You told me to."
"I know. Thank you."
{n}She turns toward you.{/n}
"I remember that you stayed. You cannot promise me that nobody will need to write another letter after the next battle. I would like to know what you hope to do if you return."''',
            c('"I want the life we planned. I will fight for the chance to live it."', "life", forbids=("broken",)),
            c('"I want the life we planned. I will fight for the chance to live it."', "life_broken", requires=("broken",))),
    ])
