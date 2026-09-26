"""History-safe prose joins for existing Tirabade saves and late starts."""
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
