"""Earned alternative private contact; native observation is supplied by the host.

Unreleased authoring candidate. No native appointment, dismissal or death is changed.
"""
from authoring.generation_errors import record
from copy import deepcopy
from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"
ACCESS = "konomi.missed_private_access"
OBSERVED = "konomi.missed_contact_available"
INVALIDATED = "konomi.missed_contact_invalidated"
SCENES = []


def s(id, title, nodes, requires=(), delay=24):
    for page in nodes:
        page["Portrait"] = "Konomi"
    entry = (OBSERVED,) if id == "the_unintroduced_letter" else ()
    SCENES.append(scene("konomi." + id, title, "Konomi", 3, "", nodes,
        Relationship="konomi", Remote=True, Areas=[DREZEN], Chapters=[3, 5],
        requires=(*entry, *requires),
        forbids=("konomi.present", "konomi.dismissed", "konomi.closed", "konomi.farewell", "inhuman", INVALIDATED),
        delay=delay, optional=True))


s("the_unintroduced_letter", "A name without an appointment", [
    n("start", "Narrator", '''{n}The inquiry comes back with the name intact and the destination crossed out. Lady Konomi. Beneath it, the clerk has written that this office cannot arrange a personal introduction.{/n}
{n}You turn the sheet over. On the blank side, another hand has added: NEITHER CAN THE OTHER SIDE.{/n}
{n}When you turn it back, the first side has acquired an indignant note asking why the second side was consulted. The two offices appear to occupy a single sheet of paper. Neither considers this a reason to cooperate.{/n}''',
      c('[Ask the paper which side handles a letter addressed to a person.]', "sides"),
      c('[Leave the unanswered inquiry for another day.]', abort=True)),
    n("sides", "Narrator", '''{n}A rectangular window opens in the sheet. Behind it, an ink-stained finger points to a notice: INTRODUCTIONS REQUIRE PRIOR ACQUAINTANCE.{/n}
{n}You point out that this makes introductions unnecessary. The finger taps the notice harder.{/n}
{n}The clerk, who has been watching from a prudent distance, sets a fresh envelope beside you. "Perhaps you could ask her yourself," she says.{/n}
{n}The finger retreats. You have discovered an alarming possibility: a letter may be delivered before its recipient has agreed to know its sender.{/n}''',
      c('[Write to Lady Konomi in your own name.]', "purpose"),
      c('[Ask whether the delivery would oblige her to answer.]', "answer")),
    n("answer", "Narrator", '''{n}The paper produces a receipt declaring that an answer is not included in the delivery fee. You ask about the fee. A new line appears: ONE LETTER.{/n}
{n}You offer the blank envelope. The finger pushes it back. For once, the office has a reasonable objection.{/n}''', c('[Find something worth putting inside it.]', "purpose")),
    n("purpose", "Narrator", '''{n}The inquiry has room for her name and almost nothing else. Your new page is more accommodating. You have to decide what you actually want her to read.{/n}''',
      c('[Ask for a personal afternoon, without claiming a previous friendship.]', "new", forbids=("konomi.margin", "konomi.lovers")),
      c('[Acknowledge the conversations you have already had.]', "known", requires=("konomi.margin",), forbids=("konomi.lovers",)),
      c('[Tell her that you miss her company.]', "lover", requires=("konomi.lovers",))),
    n("new", "Narrator", '''{n}"Lady Konomi, would you consider a private afternoon? I would like to know what you enjoy discussing when nobody has prepared an agenda. You may choose the place. I can offer my company, and a better question than the council has ever asked you."{/n}
{n}You add your name. The little window in the sheet waits while you reread the page.{/n}''', c('[Send the invitation.]', "send", flags=("konomi.missed_personal_invitation",))),
    n("known", "Narrator", '''{n}"Konomi, I would like to speak with you again. Privately, at a place you choose, with time to finish an answer. I have wondered what you are doing and caught myself composing the reply before hearing it. You would have something to say about that. I would like to hear it."{/n}
{n}You leave room below the invitation for a short refusal. She writes excellent ones, and you would rather not make her buy more paper.{/n}''', c('[Send the invitation.]', "send", flags=("konomi.missed_known_invitation",))),
    n("lover", "Narrator", '''{n}"Konomi, I miss you. Tell me how you are, and do not trim the parts you think will sting; you never did before. If you want to see me, name a place and a time. I am asking for an afternoon. I would ask for more, but you would only make me pay for it."{/n}
{n}For a moment you consider making the first sentence more elaborate. You leave it alone.{/n}''', c('[Send the invitation.]', "send", flags=("konomi.missed_lover_invitation",))),
    n("send", "Narrator", '''{n}The envelope passes through the window. Its edges do not fold. Instead, the window reluctantly becomes large enough to admit it, bumping into the inquiry's upper margin.{/n}
{n}The ink-stained finger returns your receipt. Beneath DELIVERY OFFERED, someone has written that future correspondence must use an address supplied by the recipient.{/n}
{n}The clerk lifts the now ordinary sheet by one corner. She examines the other side, then lays it down.{/n}
{n}"Shall I file that under introductions?"{/n}
{n}You suggest waiting for the answer.{/n}''', c('[Keep the receipt.]', flags=("konomi.missed_letter_sent",))),
], requires=("trickster",), delay=0)


s("the_answer_she_addressed", "The address she supplied", [
    n("start", "Narrator", '''{n}An ordinary carrier brings the answer. She checks your name, records the delivery in her book, and asks when she should return for a reply.{/n}
{n}Inside the envelope is a short note in a precise hand.{/n}
{n}"Your invitation interrupted a conversation with two carriers. The envelope appeared between their hands while they were arguing about a contract. Each initially accused the other of producing it. I explained that neither was likely to have gone to such trouble merely to interrupt me."{/n}
{n}"I am examining their proposed partnership. There are two wagons, six horses, and an uncertain quantity of agreement. I have accepted a fee to find out how much. They intend to travel to Nerosyan. I have arranged to accompany them once we settle the terms."{/n}''', c('[Read the second page.]', "invitation")),
    n("invitation", "Narrator", '''{n}"I can arrange an afternoon in Drezen while I finish that work. The house below lets its covered courtyard to travelers. Its owner has agreed to reserve it. Use the entrance beside the cooper's yard. The yard itself is not a shortcut; I have asked."{/n}
{n}"I shall be glad to have a conversation in which neither participant owns a disputed wagon. I expect you to find another subject on which we can disagree."{/n}
{n}The address follows. She has proposed two afternoons and left you to choose.{/n}''',
      c('[Choose an afternoon and send your acceptance through her carrier.]', "accept"),
      c('[Write that you have reconsidered and will not pursue the invitation.]', "decline"),
      c('[Set aside time to answer properly.]', abort=True)),
    n("accept", "Narrator", '''{n}You give the carrier your answer. She reads the address on the outside, tells you when it will be delivered, and goes. Nothing in the wall opens to assist her.{/n}
{n}Konomi's chosen afternoon remains ahead of you. You keep her directions where you will find them before leaving.{/n}''', c('[Keep the appointment.]', flags=("konomi.missed_appointment",))),
    n("decline", "Narrator", '''{n}You thank Konomi for the answer and tell her you will not take the afternoon she offered. The carrier accepts the sealed reply.{/n}
{n}The receipt from the impossible office does not produce another envelope. You put it away.{/n}''', c('[Let the invitation end here.]', flags=("konomi.closed", "konomi.missed_declined"))),
], requires=("konomi.missed_letter_sent",), delay=48)


s("the_courtyard_introduction", "An afternoon by arrangement", [
    n("start", "Narrator", '''{n}The door beside the cooper's yard opens into a passage smelling of clean linen. Beyond it, Konomi waits in a covered courtyard. She has put a small stone beneath one leg of the second chair.{/n}
{n}"Try it before you settle," she says. "I have improved the argument, but I cannot promise I have won it."{/n}
{n}The chair stays level when you sit. She looks briefly satisfied.{/n}''',
      c('"Lady Konomi. Thank you for choosing the place."', "first", requires=("konomi.missed_personal_invitation",)),
      c('"I was glad to receive your answer."', "again", forbids=("konomi.missed_personal_invitation",)),
      c('[Explain that you must postpone the conversation.]', abort=True)),
    n("first", "Konomi", '''{n}She inclines her head.{/n}
"You have an unusual understanding of how invitations should be delivered. I have been trying to decide whether the letter would have reached me if I had remained silent until the carriers finished arguing."
{n}Her mouth tightens with amusement.{/n}
"We might still be waiting. I chose to read it."
{n}She settles into her own chair.{/n}
"What did you hope to discover?"''',
      c('"What you choose when nobody has given you an assignment."', "work"),
      c('"Whether you would enjoy an afternoon with me."', "company")),
    n("again", "Konomi", '''"I was pleased to write it. Once I had established that the carrier would not be expected to reproduce your method of delivery."
{n}She rests her hands on her knees.{/n}
"We have an afternoon. I would like us to use it without conducting every sentence as though somebody were going to ask us for an account afterward."''',
      c('"Then tell me about the work you chose."', "work"),
      c('"I would like to spend some of it simply enjoying your company."', "company")),
    n("work", "Konomi", '''"The carriers asked me to settle their terms. One has wagons. The other has introductions to customers. Each can describe the other's obligations with considerable precision. Her own are a more delicate subject."
{n}She picks a thread from the chair arm.{/n}
"The owner of the wagons is particularly interesting. She becomes angry when her partner exaggerates what they can carry, then immediately begins finding reasons to excuse her. There is something between them that has not reached the contract."
"You want to know what."
"Yes. And I would like to be paid before they decide that discussing it constitutes a personal favor."
{n}She smiles.{/n}
"I enjoy being useful. I also enjoy discovering that I have understood a difficult person correctly. Occasionally those ambitions help one another."''', c('[Ask what she would enjoy about this afternoon.]', "company")),
    n("company", "Konomi", '''"I would like to be asked a question whose answer you have not already prepared. I receive very few. People bring me prepared answers the way they bring me wine, to put me in a generous mood."
{n}She catches your expression.{/n}
"Yes, I am a hypocrite. You arrived, and I had already drafted three explanations of your invitation. Asking is cheaper than drafting."
{n}Her fingers move over the chair arm, then stop.{/n}
"So. What do you want, Commander?"''',
      c('"To see you privately and find out whether the attraction is mutual."', "interest", forbids=("konomi.lovers",)),
      c('"To have afternoons together again. I have missed them."', "lover", requires=("konomi.lovers",)),
      c('"Another conversation first. I want to see your terms before I name mine."', "slow")),
    n("interest", "Konomi", '''"It is sufficiently mutual for me to want another afternoon."
{n}She lets you see the smile this time.{/n}
"I am not yet prepared to make a more elaborate prediction. It would be unfortunate if the first thing you learned about me were that I become inaccurate when pleased."
{n}She moves her chair a little nearer. The stone beneath yours stays in place.{/n}''', c('[Arrange another visit.]', "arrange", flags=("konomi.private_interest", "konomi.attracted"))),
    n("lover", "Konomi", '''"So have I."
{n}She holds out her hand. When you take it, her fingers close around yours.{/n}
"I have thought of several things I wanted to tell you. Most seemed too small to begin a letter. I should probably have begun with one of them."
{n}She looks down at your joined hands.{/n}
"I would like another afternoon. Then we may discover whether I have remembered all the small things."''', c('[Stay near and make another plan.]', "arrange", flags=("konomi.private_interest",))),
    n("slow", "Konomi", '''"Sensible. Irritatingly so."
{n}She leans back and glances up at the light along the courtyard wall.{/n}
"I did not reserve this place merely to improve the comfort of our correspondence. But a bargain struck because the chairs were already arranged is a bargain somebody regrets by supper."
{n}A smile returns.{/n}
"They were a considerable undertaking. You have no idea how long I looked for that stone."''', c('[Promise another conversation.]', "arrange", flags=("konomi.private_unhurried",))),
    n("arrange", "Konomi", '''"The carriers will show me their wagons next. I would like you to come, if they agree. I shall ask them before sending you the time."
{n}She gives you the ordinary carrier's hours. Then she walks with you to the passage, leaving the chairs where they are.{/n}
"I have rooms here until the agreement is settled. After that I intend to go to Nerosyan with them. I wanted you to know before arranging the next visit."
{n}At the door, she pauses.{/n}
"I am pleased you came. Write to me at this address. I should prefer my next letter to arrive somewhere I have chosen to receive it."''',
      c('[Keep the address and arrange the next conversation.]', flags=(ACCESS, "konomi.reconnection_open"), requires=("konomi.disagreement",)),
      c('[Keep the address and arrange the next conversation.]', flags=(ACCESS, "konomi.reconnection_open", "konomi.private_history_ready"), forbids=("konomi.disagreement",))),
], requires=("konomi.missed_appointment",), delay=24)


SCENES.append(scene("konomi.ending_missed_declined", "The afternoon declined", "Epilogue", 5, "", [
    n("start", "Narrator", '''{n}Konomi accepted the Commander's refusal of her invitation. She finished the carriers' agreement and went on toward Nerosyan when their work allowed. The proposed afternoon remained a line crossed out in her appointments.{/n}
{n}She occasionally wondered what she would have made of the conversation. There were other people to meet, and she continued to meet them.{/n}''', c(), portrait="Konomi"),
], Relationship="konomi", requires=("konomi.missed_declined", "konomi.closed"), forbids=(INVALIDATED,), last=99))


SCENES.append(scene("konomi.ending_missed_interrupted", "The letters already written", "Epilogue", 5, "", [
    n("start", "Narrator", '''{n}The copy of the invitation bore Lady Konomi's name. Below it were words intended for one reader, with no provision for an audience. They had not been included among the Commander's public declarations.{/n}''',
      c('[Recall the invitation in the light of ascension.]', "ascended", requires=("ascended",)),
      c('[Recall the invitation from before the transformation.]', "changed", requires=("inhuman",), forbids=("ascended",)),
      c('[Recall what actually followed the invitation.]', "history", forbids=("ascended", "inhuman")), portrait="Konomi"),
    n("ascended", "Narrator", '''{n}The names by which worshippers now invoked the Commander filled books. On this page, the signature was smaller. The sentence above it asked for an afternoon.{/n}''', c('[Turn to the earlier pages.]', "history"), portrait="Konomi"),
    n("changed", "Narrator", '''{n}The invitation still bore the old forms of address. They belonged to the days before the Commander's transformation. The change had left the ink untouched.{/n}''', c('[Turn to the earlier pages.]', "history"), portrait="Konomi"),
    n("history", "Narrator", '''{n}The pages had been folded to different sizes. Some corners were worn more than others.{/n}''',
      c('[Remember the life developed through the private visits.]', "developed", requires=("konomi.private_consequence_complete",)),
      c('[Remember the afternoons that were actually shared.]', "affection", requires=("konomi.lovers",), forbids=("konomi.private_consequence_complete",)),
      c('[Remember the meeting at which further visits were agreed.]', "meeting", requires=(ACCESS,), forbids=("konomi.lovers", "konomi.private_consequence_complete")),
      c('[Remember the earlier private meeting.]', "meeting", requires=("konomi.private_meeting",), forbids=(ACCESS, "konomi.lovers", "konomi.private_consequence_complete")),
      c('[Leave the invitation as an invitation.]', "invitation", forbids=(ACCESS, "konomi.private_meeting", "konomi.lovers", "konomi.private_consequence_complete")), portrait="Konomi"),
    n("developed", "Narrator", '''{n}There had been journeys between cities, a room made ready for an evening, and work that Konomi had chosen with its costs understood. The last farewell belonged to two people who had learned something of how the other kept an appointment.{/n}
{n}Beyond that part of the packet, an empty sheet had been folded to the same size. It bore no date.{/n}''', c(), portrait="Konomi"),
    n("affection", "Narrator", '''{n}There had been private afternoons and words neither had spoken for the council's benefit. Konomi's handwriting was familiar by then. A page could bring back the way she waited for an answer, the amusement she sometimes allowed into a correction.{/n}
{n}One correction had been underlined twice. Her voice seemed to belong to that small stroke of the pen. The last page ended well above its lower edge; the empty space had never been filled.{/n}''', c(), portrait="Konomi"),
    n("meeting", "Narrator", '''{n}An invitation had become a meeting. Konomi had given an address for another note and spoken about the work she intended to do. The afternoon had ended with something still to discover.{/n}
{n}The packet was tied with a short piece of thread. On its outside was only her name.{/n}''', c(), portrait="Konomi"),
    n("invitation", "Narrator", '''{n}The proposed afternoon had not taken place. The copy remained among the personal papers, with the words of the request still legible.{/n}''', c(), portrait="Konomi"),
], Relationship="konomi", requires=("konomi.missed_letter_sent", INVALIDATED), last=99))

SCENES.append(scene("konomi.ending_missed_interrupted_aeon", "An address in the erased years", "AeonEpilogue", 5, "", [
    n("start", "Narrator", '''{n}The letter belonged to a crusade that had never begun. Its impossible delivery found no address in the remade history. Whatever had followed it in the erased years remained there.{/n}''', c(), portrait="Konomi"),
], Relationship="konomi", requires=("konomi.missed_letter_sent", INVALIDATED), last=99))


# Exact, reviewed-source replacements apply only to the new provenance branch.
# Existing prose remains on its original page and every original answer index survives.
REPLACEMENTS = {
    ("private_history", "figures"): [(
        "I did not need my appointment to ask a correspondent whether a donation had arrived. It did take longer to obtain an answer addressed to me alone. People who replied promptly to the officer have discovered other demands on their time.",
        "I asked a correspondent whether the donation had arrived. It took longer to obtain an answer than I wanted. I sent a second inquiry, then found another person to ask.")],
    ("private_history", "frank"): [(
        "I am still angry about the dismissal. The petitioners did not dismiss me. Leaving their account unanswered would have been an exceedingly petty way to prove that my absence mattered.",
        "I disliked leaving the argument unfinished. Leaving their account unanswered would have given them a worse problem than ours.")],
    ("private_history", "delivered"): [("The receipt did not stop being real when you dismissed me.", "The receipt did not become less important because our own conversation was interrupted.")],
    ("private_history", "public"): [("Losing my appointment has not made me indifferent to that.", "I have not become indifferent to that.")],
    ("private_history", "discreet"): [("Dismissal has not improved my character nearly as much as some people might hope.", "An indiscreet person explaining exactly how clever he has been is excellent company.")],
    ("private_history", "source"): [("Losing my officer's appointment does not prevent me from being a client whose letter was sold.", "I am a client whose letter was sold. That is the complaint I have asked them to hear.")],
    ("private_history", "apology"): [("We have discussed the dismissal. This is another thing.", "We have discussed arranging these visits. I also need to discuss this."),
        ("the larger argument", "the argument about the shipment")],
    ("private_history", "repaired"): [("I am angry about losing my appointment. I can give you a lengthy account of why, if you have somehow misplaced the first one. But you did not disown that letter when we disagreed. I noticed.", "There are arguments between us that I still want to finish. But you did not disown that letter when we disagreed. I noticed.")],
    ("before_road", "lovers"): [("I am still angry about some of it. I had hoped the anger would cure me of wanting your company. It has proved a very poor physician.", "I kept postponing the letter until I had something weightier to put in it. Then I realised that wanting your company was the weightiest item I had, and I had been filing it under trivia.")],
    ("private_departure", "ready"): [("The capital will be less impressed by my arrival than I once imagined. That may be useful. I can find out who wants my judgment when I am no longer carrying an appointment from the council.", "I have written to people in the capital about the work I would like to do. Some have answered. I expect to spend the journey deciding which of the others to ask again.")],
    ("private_hearing", "start"): [("I have confirmed that leaving my appointment changes neither my complaint nor their authority to hear it.", "I have confirmed that they will hear the complaint as a dispute over their members' work.")],
    ("private_hearing_after", "start"): [("Nobody has attempted to deliver it to my former office.", "Nobody has attempted to forward it to Nerosyan after I expressly asked them not to.")],
    ("private_political_account", "start"): [(
        "An acquaintance thought leaving my appointment might have cured my interest in Mendev. She sent me an account of a supper instead of the news I asked for. I have replied with more precise questions.",
        "An acquaintance sent me an account of a supper instead of the news I asked for. I have replied with more precise questions. I already knew she disliked the hostess; I was hoping to discover something about Mendev."),
        ("I no longer advise you by virtue of that office. You may still ask what I think. I will probably tell you.", "This evening belongs to us. You may still ask what I think about the country. I will probably tell you.")],
    ("private_political_account", "concluded"): [(
        "Leaving the appointment has not made me indifferent to what becomes of my country. It has changed which letters I can expect people to answer.",
        "The work I have chosen has not made me indifferent to what becomes of my country. I still have letters to write and people I hope will answer."),
        ("I cannot call it a council instruction and expect a clerk to hurry because I have signed it.", "I have to give her a reason to answer rather than assume the next letter will be more effective simply because I have signed it.")],
}
for _scene in ("private_reunion", "private_absence_catchup"):
    REPLACEMENTS[(_scene, "absence_already")] = [(
        "We have also had the dismissal to discuss, and the business of deciding whether we wanted to meet without an office between us.",
        "We have also had the business of deciding how to arrange these visits and what we wanted from them.")]
    REPLACEMENTS[(_scene, "absence_now")] = [(
        "This is part of the life I am making after the dismissal.",
        "This is part of the life I am making between these journeys.")]


# Apply new variants after the established overlay, preserving its saved answer indices.
REPLACEMENTS.update({
    ("before_road", "new"): [(
        "At court I would have dressed this up as a farewell call and let you guess the rest. I have lost the court, so I may as well lose the costume.",
        "At court I would have called this a farewell visit and left you to guess the rest. I arranged this journey myself. I can manage the invitation too.")],
    ("chosen_evening", "pleasure"): [(
        "When I lost the office I assumed I would have to pick: a smaller life with you in it, or the capital without. I dislike choosing between two poor offers. I have spent my career refusing to.",
        "I expected Nerosyan to offer me work and Drezen to offer me you. Two cities, each keeping the thing I wanted in the other. I have arranged better terms."),
        ("I am glad I did not.", "I am glad I did.")],
    ("private_last_visit", "business"): [(
        "There. That is done, and I did not have to be dismissed for it this time. There will always be another applicant. I refuse to spend tonight on any of them.",
        "There. Signed, paid, and settled on the terms we chose. There will always be another applicant. I refuse to spend tonight on any of them.")],
})


def _variant(book, node_id, replacements):
    original = next(page for page in book["Nodes"] if page["Id"] == node_id)
    variant = deepcopy(original)
    variant["Id"] = "missed_" + node_id
    for old, new in replacements:
        if variant["Text"].count(old) != 1:
            record("overlay.swap_snippet", scene=book["Id"], node=node_id, detail=old[:70])
            continue
        variant["Text"] = variant["Text"].replace(old, new)
    if book["Nodes"][0] is original:
        # Blueprint identity uses scene/page ID and answer index, never list position.
        book["Nodes"].insert(0, n("missed_entry", "Narrator",
            "{n}You make time for Konomi's invitation.{/n}",
            c('[Keep the appointment.]', node_id, forbids=(ACCESS,)),
            c('[Keep the appointment.]', variant["Id"], requires=(ACCESS,), forbids=("konomi.dismissed",)),
            c('[Keep the appointment.]', node_id, requires=(ACCESS, "konomi.dismissed")), portrait="Konomi"))
    else:
        for page in list(book["Nodes"]):
            for choice in list(page["Choices"]):
                targets = ([choice["Check"]["Success"], choice["Check"]["Failure"]]
                           if choice.get("Check") else [choice.get("Next")])
                if node_id not in targets:
                    continue
                added = deepcopy(choice)
                native_again = deepcopy(choice)
                native_again["Requires"].extend([ACCESS, "konomi.dismissed"])
                added["Requires"].append(ACCESS)
                added["Forbids"].append("konomi.dismissed")
                if added.get("Check"):
                    for outcome in ("Success", "Failure"):
                        if added["Check"][outcome] == node_id:
                            added["Check"][outcome] = variant["Id"]
                else:
                    added["Next"] = variant["Id"]
                choice["Forbids"].append(ACCESS)
                page["Choices"].extend([added, native_again])
    book["Nodes"].append(variant)


def integrate(payload):
    """Apply atomically to copies; explicit groups preserve the original conjunction."""
    if any(s["Id"] == SCENES[0]["Id"] for s in payload["Scenes"]):
        raise ValueError("Konomi missed-contact overlay applied twice")
    scenes = deepcopy(payload["Scenes"])
    books = {s["Id"].removeprefix("konomi."): s for s in scenes if s.get("Relationship") == "konomi"}
    acquisition = {"fate_post", "fate_reply", "private_meeting"}
    for key in acquisition:
        books[key]["Forbids"].append(ACCESS)
    targets = [s for key, s in books.items() if key not in acquisition and "konomi.dismissed" in s["Requires"]]
    if len(targets) != 19:
        raise ValueError("Konomi private access target set changed")
    for book in targets:
        if "konomi.office_completed" not in book["Requires"]:
            raise ValueError("Konomi legacy private conjunction changed")
        book["Requires"] = [f for f in book["Requires"] if f not in ("konomi.dismissed", "konomi.office_completed")]
        groups = book.setdefault("RequiresAnyGroups", [])
        groups.extend([["konomi.dismissed", ACCESS], ["konomi.office_completed", ACCESS]])
        book["Forbids"].append(INVALIDATED)
        if "konomi.private_meeting" in book["Requires"]:
            book["Requires"].remove("konomi.private_meeting")
            groups.append(["konomi.private_meeting", "konomi.the_courtyard_introduction"])
    for (scene_id, page_id), replacements in REPLACEMENTS.items():
        _variant(books[scene_id], page_id, replacements)
    for book in books.values():
        if book["Owner"].endswith("Epilogue"):
            book["Forbids"].append(INVALIDATED)
    scenes.extend(deepcopy(SCENES))
    payload["Scenes"] = scenes
